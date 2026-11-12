"""
SG-SHAP prototype v1 (plan §12): plain Mamba on the planted-dependency series.

Changes from v0 (scripts/run_sgshap_synthetic.py, left unchanged):
  - training: loss on the target channel only ("MS" setting), model selection on
    val MSE of y, AdamW with weight decay, longer series, d_model 64
  - guides: delta profile and Mamba hidden attention (rolled out over layers)
  - baseline: MMD change-point segmentation per channel (GroupSegment-SHAP style)
  - segment budget sweep M in {4, 8, 16}
  - resolution-matched IG (IG summed inside the same segments)

    python -m scripts.run_sgshap_synthetic_v1 --head last --out results/sgshap_v1_last
"""

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn

from scripts.run_sgshap_synthetic import delta_event_ratio, log, windows
from src.models.maskable_mamba import MaskablePlainMamba, random_time_keep
from src.models.plain_mamba import PlainMamba
from src.synthetic.gt_generator import CHANNELS, EVT, LAG, TARGET, GTConfig, GTSeries
from src.xai.baselines import gradient_shap, integrated_gradients, random_attr
from src.xai.faithfulness import deletion_insertion, gt_metrics, rank_similarity
from src.xai.sg_shap import (SegmentShap, delta_profile, hidden_attention_profile, player_map_per_channel,
                             player_map_shared, segments_mass, segments_mmd, segments_peaks, segments_uniform)

DIS_EVT = CHANNELS.index("dis_evt")
SEGMENTERS = ["Uniform", "Δ-mass", "HA-mass", "MMD"]


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--head", default="last", choices=["flatten", "last"])
    p.add_argument("--seq_len", type=int, default=96)
    p.add_argument("--pred_len", type=int, default=24)
    p.add_argument("--d_model", type=int, default=64)
    p.add_argument("--n_layers", type=int, default=2)
    p.add_argument("--d_state", type=int, default=16)
    p.add_argument("--revin", action="store_true")
    p.add_argument("--load", default=None, help="model.pt of a run with the same model/data args; skips training")
    p.add_argument("--resume", default=None,
                   help="ckpt.pt of an unfinished/stopped run with the same args; continues up to --epochs")
    p.add_argument("--init", default=None,
                   help="warm start: load model.pt weights, then train with a fresh optimizer at --lr")
    p.add_argument("--loss", default="target", choices=["target", "all"])
    p.add_argument("--epochs", type=int, default=100)
    p.add_argument("--patience", type=int, default=10,
                   help="stop after this many epochs without val improvement")
    p.add_argument("--sched", default="plateau", choices=["plateau", "cosine"])
    p.add_argument("--lr_patience", type=int, default=3,
                   help="plateau: halve LR after this many epochs without improvement")
    p.add_argument("--batch_size", type=int, default=128)
    p.add_argument("--lr", type=float, default=2e-3)
    p.add_argument("--weight_decay", type=float, default=1e-2)
    p.add_argument("--grad_clip", type=float, default=0.0, help="max grad norm; 0 = off")
    p.add_argument("--train_stride", type=int, default=2)
    p.add_argument("--mask_train", default="none", choices=["none", "skip", "token"],
                   help="train a MaskablePlainMamba on random time-segment removals (Exp B)")
    p.add_argument("--mask_p_clean", type=float, default=0.5, help="fraction of unmasked training samples")
    p.add_argument("--length", type=int, default=30000)
    p.add_argument("--n_explain", type=int, default=40)
    p.add_argument("--M_list", type=int, nargs="+", default=[4, 8, 16])
    p.add_argument("--nsamples", type=int, default=1024)
    p.add_argument("--masker", default="mean", choices=["mean", "interp"])
    p.add_argument("--n_sanity", type=int, default=8)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--threads", type=int, default=0)
    p.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    p.add_argument("--shap_batch", type=int, default=512)
    p.add_argument("--out", default="results/sgshap_v1")
    return p.parse_args()


@torch.no_grad()
def evaluate_y(model, data, starts, L, H, bs=512):
    model.eval()
    se_tgt = se_all = 0.0
    for i in range(0, len(starts), bs):
        x, y = windows(data, starts[i:i + bs], L, H)
        err = (model(x) - y) ** 2
        se_tgt += err[:, TARGET].mean(-1).sum().item()
        se_all += err.mean(dim=(1, 2)).sum().item()
    return se_tgt / len(starts), se_all / len(starts)


def train(model, data, tr, va, a, fh, oracle_va: float, ckpt_path: Path):
    """
    AdamW + ReduceLROnPlateau (default) or cosine. With "plateau" the LR is halved
    after lr_patience flat epochs and training stops only after `patience` flat
    epochs, so every run passes through several lower-LR phases before stopping.
    The full training state is written to ckpt_path after every epoch (--resume).
    Returns the best-val model and the per-epoch history.
    """
    decay, no_decay = [], []
    for name, p in model.named_parameters():
        (no_decay if p.ndim < 2 or name.endswith("A_log") else decay).append(p)
    opt = torch.optim.AdamW([{"params": decay, "weight_decay": a.weight_decay},
                             {"params": no_decay, "weight_decay": 0.0}], lr=a.lr)
    if a.sched == "plateau":
        sched = torch.optim.lr_scheduler.ReduceLROnPlateau(opt, factor=0.5, patience=a.lr_patience,
                                                           min_lr=a.lr / 64)
    else:
        sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=a.epochs)
    best, best_state, bad, hist, start = float("inf"), None, 0, [], 0
    rng = np.random.default_rng(a.seed)
    mask_gen = torch.Generator(device=a.device).manual_seed(a.seed)
    if a.resume:
        ck = torch.load(a.resume, map_location=a.device, weights_only=False)
        model.load_state_dict(ck["model"])
        opt.load_state_dict(ck["opt"])
        sched.load_state_dict(ck["sched"])
        best, best_state, bad, hist, start = ck["best"], ck["best_state"], ck["bad"], ck["hist"], ck["epoch"]
        rng.bit_generator.state = ck["rng"]
        if "mask_gen" in ck:
            mask_gen.set_state(ck["mask_gen"].cpu())
        log(f"resumed {a.resume} after epoch {start} (best {best:.4f}, {bad} flat epochs)", fh)
    stop = "max_epochs"
    for ep in range(start, a.epochs):
        model.train()
        t0, tot = time.time(), 0.0
        perm = rng.permutation(tr)
        for i in range(0, len(perm), a.batch_size):
            x, y = windows(data, perm[i:i + a.batch_size], a.seq_len, a.pred_len)
            if a.mask_train == "none":
                out = model(x)
            else:
                out = model(x, random_time_keep(len(x), a.seq_len, x.device, a.mask_p_clean, generator=mask_gen))
            loss = ((out[:, TARGET] - y[:, TARGET]) ** 2).mean() if a.loss == "target" else nn.functional.mse_loss(out, y)
            opt.zero_grad()
            loss.backward()
            if a.grad_clip > 0:
                torch.nn.utils.clip_grad_norm_(model.parameters(), a.grad_clip)
            opt.step()
            tot += loss.item() * len(x)
        va_y, va_all = evaluate_y(model, data, va, a.seq_len, a.pred_len)
        crit = va_y if a.loss == "target" else va_all
        lr = opt.param_groups[0]["lr"]
        sched.step(crit) if a.sched == "plateau" else sched.step()
        hist.append({"epoch": ep + 1, "train": tot / len(perm), "val_y": va_y, "val_all": va_all, "lr": lr})
        log(f"epoch {ep + 1:03d} lr {lr:.1e} train {tot / len(perm):.4f} val_y {va_y:.4f} "
            f"(oracle {oracle_va:.4f}, x{va_y / oracle_va:.2f}) val_all {va_all:.4f} ({time.time() - t0:.0f}s)", fh)
        if crit < best - 1e-5:
            best, bad = crit, 0
            best_state = {k: v.clone() for k, v in model.state_dict().items()}
        else:
            bad += 1
        torch.save({"model": model.state_dict(), "opt": opt.state_dict(), "sched": sched.state_dict(),
                    "epoch": ep + 1, "best": best, "best_state": best_state, "bad": bad, "hist": hist,
                    "rng": rng.bit_generator.state, "mask_gen": mask_gen.get_state()}, ckpt_path)
        if bad >= a.patience:
            stop = "early_stop"
            break
    model.load_state_dict(best_state)
    return model, hist, stop


def diagnose_training(hist: list, stop: str, oracle_va: float, patience: int) -> dict:
    """Why training ended and whether more epochs could still help."""
    h = pd.DataFrame(hist)
    b = int(h.val_y.idxmin())
    best_ep, last_ep = int(h.epoch[b]), int(h.epoch.iloc[-1])
    tail = h.iloc[b:]
    train_drop = float(h.train[b] - h.train.iloc[-1])                  # train kept improving after best val?
    val_rise = float(h.val_y.iloc[-1] - h.val_y[b])
    spikes = [int(e) for e, t, m in zip(h.epoch, h.train, h.train.cummin()) if t > 1.5 * m]
    if stop == "max_epochs" and last_ep - best_ep < patience:
        verdict = "STILL IMPROVING at max epochs: increase --epochs"
    elif train_drop > 0.05 * h.train[b] and val_rise > 0.02 * h.val_y[b]:
        verdict = "overfitting (train fell, val rose after best epoch): more epochs will not help; regularise/more data"
    else:
        verdict = "plateau after LR reductions: capacity/optimisation limit, not too few epochs"
    return {"stop": stop, "best_epoch": best_ep, "last_epoch": last_ep, "best_val_y": float(h.val_y[b]),
            "oracle_val_y": oracle_va, "gap_to_oracle": float(h.val_y[b] / oracle_va),
            "train_at_best": float(h.train[b]), "lr_at_end": float(tail.lr.iloc[-1]),
            "n_lr_reductions": int((h.lr.diff() < 0).sum()), "loss_spike_epochs": spikes,
            "verdict": verdict + ("; UNSTABLE: train loss spiked (>1.5x its minimum), consider --grad_clip" if spikes else "")}


def plot_training(hist: list, oracle_va: float, out: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    h = pd.DataFrame(hist)
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.plot(h.epoch, h.train, label="train (y)")
    ax.plot(h.epoch, h.val_y, label="val (y)")
    ax.axhline(oracle_va, color="k", ls="--", lw=0.8, label="oracle (val)")
    ax.set_yscale("log")
    ax.set_xlabel("epoch")
    ax.set_ylabel("MSE")
    ax2 = ax.twinx()
    ax2.step(h.epoch, h.lr, color="gray", lw=0.8, where="post")
    ax2.set_yscale("log")
    ax2.set_ylabel("lr", color="gray")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(out / "training_curve.png", dpi=120)
    plt.close(fig)


def readout_weights(model, head: str, L: int) -> np.ndarray:
    """Which output positions feed the y forecast: last step, or flatten-head weight norms."""
    if head == "last":
        return np.eye(L)[-1]
    H, d_head = model.pred_len, model.reduce.out_features
    W = model.head.weight.detach()[TARGET * H:(TARGET + 1) * H]       # [H, L*d_head]
    w = W.view(H, L, d_head).norm(dim=(0, 2)).cpu().numpy()
    return w / w.sum()


def md_table(df: pd.DataFrame, fmt: str = "{:.3f}") -> str:
    head = "| " + " | ".join([str(df.index.name or "")] + [f"M={c}" for c in df.columns]) + " |"
    sep = "|" + "---|" * (len(df.columns) + 1)
    body = ["| " + " | ".join([str(i)] + [fmt.format(v) for v in r]) + " |" for i, r in zip(df.index, df.values)]
    return "\n".join([head, sep] + body)


def aggregate_to_map(attr: np.ndarray, pm: np.ndarray) -> np.ndarray:
    """Sum a cell attribution inside each player group and spread it evenly again."""
    P = pm.max() + 1
    sums = np.bincount(pm.ravel(), weights=attr.ravel(), minlength=P)
    counts = np.bincount(pm.ravel(), minlength=P)
    return (sums / counts)[pm]


def player_maps(x_np, prof_d, prof_ha, M, C, L):
    return {
        "Uniform": player_map_shared(segments_uniform(L, M), C),
        "Δ-mass": player_map_shared(segments_mass(prof_d, M), C),
        "HA-mass": player_map_shared(segments_mass(prof_ha, M, min_len=2), C),
        "MMD": player_map_per_channel([segments_mmd(x_np[c], M) for c in range(C)]),
    }


def main():
    a = parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if a.threads:
        torch.set_num_threads(a.threads)
    torch.manual_seed(a.seed)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    fh = open(out / "log.txt", "w", encoding="utf-8")
    log(f"args {vars(a)}", fh)
    L, H, C = a.seq_len, a.pred_len, len(CHANNELS)

    # ---------------- data ----------------
    gen = GTSeries(GTConfig(length=a.length, seed=a.seed))
    raw = gen.data
    n_tr, n_va = int(0.7 * len(raw)), int(0.1 * len(raw))
    mu, sd = raw[:n_tr].mean(0), raw[:n_tr].std(0)
    data = torch.as_tensor((raw - mu) / sd, device=a.device)
    tr = np.arange(0, n_tr - L - H + 1, a.train_stride)
    va = np.arange(n_tr - L, n_tr + n_va - L - H + 1)
    te = np.arange(n_tr + n_va - L, len(raw) - L - H + 1)
    log(f"windows train {len(tr)} val {len(va)} test {len(te)}", fh)

    def oracle_mse(starts):
        yhat = (gen.oracle_forecast(starts, L, H) - mu[TARGET]) / sd[TARGET]
        ytrue = (raw[starts[:, None] + L + np.arange(H), TARGET] - mu[TARGET]) / sd[TARGET]
        return float(((yhat - ytrue) ** 2).mean())

    oracle_va, oracle_te = oracle_mse(va), oracle_mse(te)
    log(f"oracle MSE y: val {oracle_va:.4f} test {oracle_te:.4f}", fh)

    # ---------------- model ----------------
    def build():
        kw = dict(d_model=a.d_model, n_layers=a.n_layers, d_state=a.d_state, head=a.head, revin=a.revin)
        if a.mask_train != "none":
            return MaskablePlainMamba(C, L, H, mask_mode=a.mask_train, **kw).to(a.device)
        return PlainMamba(C, L, H, **kw).to(a.device)

    model = build()
    log(f"params {sum(p.numel() for p in model.parameters())}", fh)
    train_diag = None
    if a.load:
        model.load_state_dict(torch.load(a.load, map_location=a.device))
        model.eval()
        log(f"loaded {a.load}", fh)
    else:
        if a.init:
            model.load_state_dict(torch.load(a.init, map_location=a.device))
            log(f"warm start from {a.init}", fh)
        t_train = time.time()
        model, hist, stop = train(model, data, tr, va, a, fh, oracle_va, out / "ckpt.pt")
        model.eval()
        train_diag = diagnose_training(hist, stop, oracle_va, a.patience)
        train_diag["seconds"] = time.time() - t_train
        pd.DataFrame(hist).to_csv(out / "training_history.csv", index=False)
        plot_training(hist, oracle_va, out)
        log(f"training {train_diag['seconds']:.0f}s on {a.device}: {train_diag}", fh)
    torch.save(model.state_dict(), out / "model.pt")
    te_y, _ = evaluate_y(model, data, te, L, H)
    _, y_te = windows(data, te, L, H)
    zero_y = float((y_te[:, TARGET] ** 2).mean())
    floor_y = float((gen.cfg.noise_y / sd[TARGET]) ** 2)
    log(f"test MSE y {te_y:.4f} (oracle {oracle_te:.4f}, zero-forecast {zero_y:.4f}, noise floor {floor_y:.4f})", fh)
    if a.n_explain == 0:
        (out / "summary.json").write_text(json.dumps(
            {"args": vars(a), "training": train_diag,
             "forecast": {"test_mse_y": te_y, "oracle_y": oracle_te, "zero_forecast_y": zero_y}},
            indent=2, default=float), encoding="utf-8")
        fh.close()
        return

    # ---------------- explanations ----------------
    f = lambda xs: model(xs)[:, TARGET].mean(-1)
    starts = te[np.linspace(0, len(te) - 1, a.n_explain).astype(int)]
    x_ex, _ = windows(data, starts, L, H)
    background, _ = windows(data, np.random.default_rng(a.seed).choice(tr, 64, replace=False), L, H)
    score_mask = gen.score_mask(L)
    w_read = readout_weights(model, a.head, L)

    def shap_for(x, pm):
        P = int(pm.max()) + 1
        return SegmentShap(f, masker=a.masker, nsamples=max(a.nsamples, 16 * P), batch_size=a.shap_batch,
                           seed=a.seed).explain_map(x, pm)

    rows, figs, kept = [], [], {}
    for w, (s, x) in enumerate(zip(starts, x_ex)):
        gt = gen.gt_mask(int(s), L, H)
        x_np = x.cpu().numpy()
        prof_d = delta_profile(model, x.unsqueeze(0))[0]
        prof_ha = hidden_attention_profile(model, x, w_read)
        gt_time = gt[score_mask.any(1)].any(0) if gt.any() else np.zeros(L, bool)
        diag = {"window": w, "start": int(s), "regime_on": bool(gt[LAG].any()),
                "n_gt_lag": int(gt[LAG].sum()), "n_gt_evt": int(gt[EVT].sum()),
                "delta_ratio_x_evt": delta_event_ratio(prof_d, gen.is_spike[s:s + L]),
                "delta_ratio_dis_evt": delta_event_ratio(prof_d, raw[s:s + L, DIS_EVT] != 0),
                "delta_cv": float(prof_d.std() / prof_d.mean()),
                "ha_mass_in_gt_time": float(prof_ha[gt_time].sum() / prof_ha.sum()) if gt_time.any() else np.nan,
                "gt_time_frac": float(gt_time.mean())}
        attrs, maps8 = {}, {}

        t0 = time.time()
        ig, ig_ev = integrated_gradients(f, x)
        ig_sec = time.time() - t0
        runs = []                                                           # (name, segmenter, M, attr, evals, secs, extra)
        for M in a.M_list:
            for seg_name, pm in player_maps(x_np, prof_d, prof_ha, M, C, L).items():
                t0 = time.time()
                res = shap_for(x, pm)
                runs.append((f"{seg_name} (M={M})", seg_name, M, res["cell"], res["n_evals"], time.time() - t0,
                             {"efficiency_gap": res["efficiency_gap"]}))
                if M == 8:
                    maps8[seg_name] = pm
        t0 = time.time()
        res = shap_for(x, player_map_shared(segments_peaks(prof_d, 8), C))
        runs.append(("Δ-peaks (M=8)", "Δ-peaks", 8, res["cell"], res["n_evals"], time.time() - t0,
                     {"efficiency_gap": res["efficiency_gap"]}))
        t0 = time.time()
        gs, gs_ev = gradient_shap(f, model, x, background, seed=a.seed)
        runs.append(("GradientSHAP", "-", 0, gs, gs_ev, time.time() - t0, {}))
        runs.append(("IG", "-", 0, ig, ig_ev, ig_sec, {}))
        for seg_name in ("Uniform", "HA-mass"):
            runs.append((f"IG@{seg_name} (M=8)", seg_name, 8, aggregate_to_map(ig, maps8[seg_name]), ig_ev, ig_sec, {}))
        rnd, _ = random_attr(x, seed=a.seed + w)
        runs.append(("Random", "-", 0, rnd, 0, 0.0, {}))

        for name, seg_name, M, attr, n_ev, sec, extra in runs:
            row = {**diag, "method": name, "segmenter": seg_name, "M": M, "seconds": sec, "n_evals": n_ev,
                   **extra, **gt_metrics(attr, gt, score_mask)}
            for mk in ("mean", "interp"):
                row.update({f"{k}_{mk}": v for k, v in deletion_insertion(f, x, attr, masker=mk).items()})
            rows.append(row)
            attrs[name] = attr
            if w < a.n_sanity:
                kept[(w, name)] = attr
        if w < 3:
            figs.append({"x": x_np, "gt": gt, "prof_d": prof_d, "prof_ha": prof_ha, "maps": maps8, "attr": attrs})
        log(f"window {w + 1}/{len(starts)} (regime_on={diag['regime_on']}, evt_gt={diag['n_gt_evt']}, "
            f"HA mass in GT time {diag['ha_mass_in_gt_time']:.2f} vs frac {diag['gt_time_frac']:.2f})", fh)

    # ---------------- sanity: parameter randomisation ----------------
    torch.manual_seed(a.seed + 999)
    rmodel = build().eval()
    f_r = lambda xs: rmodel(xs)[:, TARGET].mean(-1)
    sanity = []
    for w in range(min(a.n_sanity, len(starts))):
        x = x_ex[w]
        pd_r = delta_profile(rmodel, x.unsqueeze(0))[0]
        pha_r = hidden_attention_profile(rmodel, x, readout_weights(rmodel, a.head, L))
        maps = player_maps(x.cpu().numpy(), pd_r, pha_r, 8, C, L)
        row = {"window": w}
        for seg_name in ("Uniform", "Δ-mass", "HA-mass"):
            r = SegmentShap(f_r, masker=a.masker, nsamples=a.nsamples, batch_size=a.shap_batch,
                            seed=a.seed).explain_map(x, maps[seg_name])
            row[f"{seg_name} (M=8)"] = rank_similarity(kept[(w, f"{seg_name} (M=8)")], r["cell"])
        row["IG"] = rank_similarity(kept[(w, "IG")], integrated_gradients(f_r, x)[0])
        sanity.append(row)

    # ---------------- save ----------------
    df = pd.DataFrame(rows)
    df.to_csv(out / "per_window.csv", index=False)
    metrics = ["prec_at_k", "ap", "mass_in_gt", "del_aopc_mean", "ins_aopc_mean",
               "del_aopc_interp", "ins_aopc_interp", "n_evals", "seconds"]
    agg = df.groupby("method", sort=False)[metrics].agg(["mean", "std"])
    ap_evt = df[df.n_gt_evt > 0].groupby("method", sort=False)["ap"].mean()
    ap_lag = df[df.regime_on].groupby("method", sort=False)["ap"].mean()
    diag_df = df.drop_duplicates("window")
    sanity_df = pd.DataFrame(sanity)
    summary = {
        "args": vars(a), "gt_config": gen.config_dict(), "training": train_diag,
        "forecast": {"test_mse_y": te_y, "oracle_y": oracle_te, "zero_forecast_y": zero_y, "noise_floor_y": floor_y},
        "diagnostics": {k: float(diag_df[k].mean()) for k in
                        ("delta_ratio_x_evt", "delta_ratio_dis_evt", "delta_cv", "ha_mass_in_gt_time", "gt_time_frac")},
        "n_windows": int(len(starts)), "n_regime_on": int(diag_df.regime_on.sum()),
        "n_with_evt_gt": int((diag_df.n_gt_evt > 0).sum()),
        "max_efficiency_gap": float(df["efficiency_gap"].max()),
        "sanity_spearman_mean": sanity_df.drop(columns="window").mean().to_dict(),
        "methods": {m: {k: {"mean": float(agg.loc[m, (k, "mean")]), "std": float(agg.loc[m, (k, "std")])}
                        for k in metrics} for m in agg.index},
        "ap_windows_with_evt_gt": ap_evt.to_dict(), "ap_windows_regime_on": ap_lag.to_dict(),
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2, default=float), encoding="utf-8")

    dg = summary["diagnostics"]
    lines = [f"# SG-SHAP synthetic v1 — head={a.head}", "",
             f"Test MSE y = {te_y:.4f} (oracle {oracle_te:.4f}, zero-forecast {zero_y:.4f}, noise floor {floor_y:.4f}); "
             f"{len(starts)} windows, {summary['n_regime_on']} regime-on, {summary['n_with_evt_gt']} with event GT.",
             f"Δ at x_evt spikes / elsewhere = {dg['delta_ratio_x_evt']:.3f} (dis_evt {dg['delta_ratio_dis_evt']:.3f}); "
             f"Δ CV = {dg['delta_cv']:.3f}; hidden-attention mass on GT time steps = {dg['ha_mass_in_gt_time']:.3f} "
             f"(GT covers {dg['gt_time_frac']:.3f} of the lookback).", "",
             "| Method | P@k | AP | AP evt-win | AP regime-on | mass in GT | Del mean ↑ | Ins mean ↓ | Del interp ↑ | Ins interp ↓ | evals | s |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for m in agg.index:
        g = lambda k: f"{agg.loc[m, (k, 'mean')]:.3f}±{agg.loc[m, (k, 'std')]:.3f}"
        lines.append(f"| {m} | {g('prec_at_k')} | {g('ap')} | {ap_evt.get(m, np.nan):.3f} | {ap_lag.get(m, np.nan):.3f} | "
                     f"{g('mass_in_gt')} | {g('del_aopc_mean')} | {g('ins_aopc_mean')} | {g('del_aopc_interp')} | "
                     f"{g('ins_aopc_interp')} | {agg.loc[m, ('n_evals', 'mean')]:.0f} | {agg.loc[m, ('seconds', 'mean')]:.2f} |")
    sweep = df[df.segmenter.isin(SEGMENTERS) & ~df.method.str.startswith("IG")]
    piv = sweep.pivot_table(index="segmenter", columns="M", values="ap", aggfunc="mean").reindex(SEGMENTERS)
    piv_del = sweep.pivot_table(index="segmenter", columns="M", values="del_aopc_mean", aggfunc="mean").reindex(SEGMENTERS)
    lines += ["", "AP vs segment budget M:", "", md_table(piv),
              "", "Deletion AOPC (mean masker) vs M:", "", md_table(piv_del),
              "", "Sanity (Spearman |attr| trained vs randomised, lower = passes): " +
              ", ".join(f"{k} {v:.3f}" for k, v in summary["sanity_spearman_mean"].items()),
              f"Max KernelSHAP efficiency gap = {summary['max_efficiency_gap']:.2e}"]
    (out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    log("\n".join(lines), fh)
    plot_windows(figs, out)
    plot_sweep(piv, df, out)
    fh.close()


def plot_windows(items, out: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    show = ["Uniform (M=8)", "Δ-mass (M=8)", "HA-mass (M=8)", "MMD (M=8)", "IG"]
    for i, it in enumerate(items):
        fig, axes = plt.subplots(2 + len(show), 1, figsize=(10, 2 + 1.5 * (2 + len(show))), sharex=True)
        ax = axes[0]
        ax.plot(it["x"][LAG], lw=0.8, label="x_lag")
        ax.plot(it["x"][EVT], lw=0.8, label="x_evt")
        for ch, c in ((LAG, "C0"), (EVT, "C1")):
            for t in np.flatnonzero(it["gt"][ch]):
                ax.axvspan(t - 0.5, t + 0.5, color=c, alpha=0.15, lw=0)
        ax.legend(loc="upper left", fontsize=7)
        ax.set_title("inputs (shaded = ground truth)", fontsize=9)
        ax = axes[1]
        ax.plot(it["prof_d"] / it["prof_d"].mean(), color="k", lw=1, label="Δ (scaled)")
        ax.plot(it["prof_ha"] / it["prof_ha"].mean(), color="C3", lw=1, label="hidden attention (scaled)")
        ax.set_yscale("log")
        ax.legend(loc="upper left", fontsize=7)
        ax.set_title("guide profiles", fontsize=9)
        for ax, name in zip(axes[2:], show):
            a = np.abs(it["attr"][name])
            ax.imshow(a / (a.max() + 1e-12), aspect="auto", cmap="viridis", interpolation="nearest")
            ax.set_yticks(range(len(CHANNELS)), CHANNELS, fontsize=7)
            ax.set_title(name, fontsize=9)
        axes[-1].set_xlabel("lookback position")
        fig.tight_layout()
        fig.savefig(out / f"window_{i}.png", dpi=110)
        plt.close(fig)


def plot_sweep(piv, df, out: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(5, 3.5))
    for seg in piv.index:
        ax.plot(piv.columns, piv.loc[seg], marker="o", label=seg)
    for name, ls in (("IG", "--"), ("GradientSHAP", ":")):
        ax.axhline(df[df.method == name].ap.mean(), color="gray", ls=ls, label=name)
    ax.set_xlabel("segments per channel M")
    ax.set_ylabel("AP vs ground truth")
    ax.set_xticks(list(piv.columns))
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(out / "ap_vs_M.png", dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    main()
