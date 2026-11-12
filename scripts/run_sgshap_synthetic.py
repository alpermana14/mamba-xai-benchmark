"""
SG-SHAP prototype: plain Mamba on the planted-dependency series (plan §3.2-3.3).

Trains PlainMamba, then explains the mean forecast of y over the horizon on
test windows with SG-SHAP (mass / peaks), fixed-window segment SHAP,
GradientSHAP, Integrated Gradients and random, and scores them against the
planted ground truth, deletion/insertion AOPC, cost and a randomisation check.

    python -m scripts.run_sgshap_synthetic --head last --out results/sgshap_synth_last
"""

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn

from src.models.plain_mamba import PlainMamba
from src.synthetic.gt_generator import CHANNELS, EVT, LAG, TARGET, GTConfig, GTSeries
from src.xai.baselines import gradient_shap, integrated_gradients, random_attr
from src.xai.faithfulness import deletion_insertion, gt_metrics, rank_similarity
from src.xai.sg_shap import SegmentShap, delta_profile, segments_mass, segments_peaks, segments_uniform

DIS_EVT = CHANNELS.index("dis_evt")


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--head", default="last", choices=["flatten", "last"])
    p.add_argument("--seq_len", type=int, default=96)
    p.add_argument("--pred_len", type=int, default=24)
    p.add_argument("--d_model", type=int, default=32)
    p.add_argument("--n_layers", type=int, default=2)
    p.add_argument("--revin", action="store_true")
    p.add_argument("--epochs", type=int, default=30)
    p.add_argument("--patience", type=int, default=5)
    p.add_argument("--batch_size", type=int, default=128)
    p.add_argument("--lr", type=float, default=2e-3)
    p.add_argument("--train_stride", type=int, default=1)
    p.add_argument("--length", type=int, default=20000)
    p.add_argument("--n_explain", type=int, default=40)
    p.add_argument("--segments", type=int, default=8)
    p.add_argument("--nsamples", type=int, default=1024)
    p.add_argument("--masker", default="mean", choices=["mean", "interp"])
    p.add_argument("--n_sanity", type=int, default=8)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--threads", type=int, default=0)
    p.add_argument("--out", default="results/sgshap_synth")
    return p.parse_args()


def log(msg, fh):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    fh.write(line + "\n")
    fh.flush()


def windows(data: torch.Tensor, starts: np.ndarray, L: int, H: int):
    idx = torch.as_tensor(starts, device=data.device)[:, None] + torch.arange(L + H, device=data.device)
    w = data[idx].transpose(1, 2)                       # [n, C, L+H]
    return w[:, :, :L].contiguous(), w[:, :, L:].contiguous()


@torch.no_grad()
def evaluate(model, data, starts, L, H, bs=512):
    model.eval()
    se_all = se_tgt = n = 0.0
    for i in range(0, len(starts), bs):
        x, y = windows(data, starts[i:i + bs], L, H)
        err = (model(x) - y) ** 2
        se_all += err.mean(dim=(1, 2)).sum().item()
        se_tgt += err[:, TARGET].mean(-1).sum().item()
        n += len(x)
    return se_all / n, se_tgt / n


def train(model, data, tr, va, a, fh):
    opt = torch.optim.Adam(model.parameters(), lr=a.lr)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=a.epochs)
    loss_fn = nn.MSELoss()
    best, best_state, bad = float("inf"), None, 0
    rng = np.random.default_rng(a.seed)
    for ep in range(a.epochs):
        model.train()
        t0, tot = time.time(), 0.0
        perm = rng.permutation(tr)
        for i in range(0, len(perm), a.batch_size):
            x, y = windows(data, perm[i:i + a.batch_size], a.seq_len, a.pred_len)
            loss = loss_fn(model(x), y)
            opt.zero_grad()
            loss.backward()
            opt.step()
            tot += loss.item() * len(x)
        sched.step()
        va_all, va_tgt = evaluate(model, data, va, a.seq_len, a.pred_len)
        log(f"epoch {ep + 1:02d} train {tot / len(perm):.4f} val {va_all:.4f} val_y {va_tgt:.4f} "
            f"({time.time() - t0:.0f}s)", fh)
        if va_all < best - 1e-5:
            best, bad = va_all, 0
            best_state = {k: v.clone() for k, v in model.state_dict().items()}
        else:
            bad += 1
            if bad >= a.patience:
                log("early stop", fh)
                break
    model.load_state_dict(best_state)
    return model


def delta_event_ratio(prof, spikes, width=4):
    """Mean delta in the `width` steps starting at a spike / mean delta elsewhere."""
    L = len(prof)
    near = np.zeros(L, dtype=bool)
    for s in np.flatnonzero(spikes):
        near[s:s + width] = True
    if not near.any() or near.all():
        return np.nan
    return float(prof[near].mean() / prof[~near].mean())


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
    L, H, M = a.seq_len, a.pred_len, a.segments

    # ---------------- data ----------------
    gen = GTSeries(GTConfig(length=a.length, seed=a.seed))
    raw = gen.data
    n_tr, n_va = int(0.7 * len(raw)), int(0.1 * len(raw))
    mu, sd = raw[:n_tr].mean(0), raw[:n_tr].std(0)
    data = torch.as_tensor((raw - mu) / sd)
    last = len(raw) - L - H
    tr = np.arange(0, n_tr - L - H + 1, a.train_stride)
    va = np.arange(n_tr - L, n_tr + n_va - L - H + 1)
    te = np.arange(n_tr + n_va - L, last + 1)
    log(f"windows train {len(tr)} val {len(va)} test {len(te)}", fh)

    # ---------------- model ----------------
    def build():
        return PlainMamba(len(CHANNELS), L, H, d_model=a.d_model, n_layers=a.n_layers,
                          head=a.head, revin=a.revin)

    model = build()
    log(f"params {sum(p.numel() for p in model.parameters())}", fh)
    model = train(model, data, tr, va, a, fh).eval()
    torch.save(model.state_dict(), out / "model.pt")
    te_all, te_tgt = evaluate(model, data, te, L, H)
    _, y_te = windows(data, te, L, H)
    zero_tgt = float((y_te[:, TARGET] ** 2).mean())
    floor_tgt = float((gen.cfg.noise_y / sd[TARGET]) ** 2)
    log(f"test MSE all {te_all:.4f} | y {te_tgt:.4f} (zero-forecast {zero_tgt:.4f}, noise floor {floor_tgt:.4f})", fh)

    # ---------------- explanations ----------------
    f = lambda xs: model(xs)[:, TARGET].mean(-1)
    starts = te[np.linspace(0, len(te) - 1, a.n_explain).astype(int)]
    x_ex, _ = windows(data, starts, L, H)
    bg_starts = np.random.default_rng(a.seed).choice(tr, 64, replace=False)
    background, _ = windows(data, bg_starts, L, H)
    score_mask = gen.score_mask(L)
    shap_kw = dict(masker=a.masker, nsamples=a.nsamples, seed=a.seed)

    methods = {
        "SG-SHAP (mass)":   ("seg", lambda prof: segments_mass(prof, M)),
        "SG-SHAP (peaks)":  ("seg", lambda prof: segments_peaks(prof, M)),
        f"Fixed-SHAP (M={M})":     ("seg", lambda prof: segments_uniform(L, M)),
        f"Fixed-SHAP (M={2 * M})": ("seg", lambda prof: segments_uniform(L, 2 * M)),
        "GradientSHAP":     ("grad", None),
        "IG":               ("ig", None),
        "Random":           ("rand", None),
    }
    rows, keep_for_fig, trained_attr = [], [], {}
    for w, (s, x) in enumerate(zip(starts, x_ex)):
        gt = gen.gt_mask(int(s), L, H)
        prof = delta_profile(model, x.unsqueeze(0))[0]
        diag = {"window": w, "start": int(s), "regime_on": bool(gt[LAG].any()),
                "n_gt_lag": int(gt[LAG].sum()), "n_gt_evt": int(gt[EVT].sum()),
                "delta_ratio_x_evt": delta_event_ratio(prof, gen.is_spike[s:s + L]),
                "delta_ratio_dis_evt": delta_event_ratio(prof, raw[s:s + L, DIS_EVT] != 0),
                "delta_cv": float(prof.std() / prof.mean())}
        fig_item = {"x": x.numpy(), "gt": gt, "prof": prof, "attr": {}, "bounds": {}}
        for name, (kind, seg) in methods.items():
            t0 = time.time()
            extra = {}
            if kind == "seg":
                b = seg(prof)
                res = SegmentShap(f, **shap_kw).explain(x, b)
                attr, n_ev = res["cell"], res["n_evals"]
                extra = {"efficiency_gap": res["efficiency_gap"],
                         "seg_len_cv": float(np.diff(b).std() / np.diff(b).mean())}
                fig_item["bounds"][name] = b
            elif kind == "grad":
                attr, n_ev = gradient_shap(f, model, x, background, seed=a.seed)
            elif kind == "ig":
                attr, n_ev = integrated_gradients(f, x)
            else:
                attr, n_ev = random_attr(x, seed=a.seed + w)
            sec = time.time() - t0
            row = {**diag, "method": name, "seconds": sec, "n_evals": n_ev, **extra,
                   **gt_metrics(attr, gt, score_mask)}
            for mk in ("mean", "interp"):
                row.update({f"{k}_{mk}": v for k, v in deletion_insertion(f, x, attr, masker=mk).items()})
            rows.append(row)
            fig_item["attr"][name] = attr
            if w < a.n_sanity:
                trained_attr[(w, name)] = attr
        if w < 3:
            keep_for_fig.append(fig_item)
        log(f"window {w + 1}/{len(starts)} done (regime_on={diag['regime_on']}, evt_gt={diag['n_gt_evt']})", fh)

    # ---------------- sanity: parameter randomisation ----------------
    torch.manual_seed(a.seed + 999)
    rand_model = build().eval()
    f_rand = lambda xs: rand_model(xs)[:, TARGET].mean(-1)
    sanity = []
    for w in range(min(a.n_sanity, len(starts))):
        x = x_ex[w]
        prof_r = delta_profile(rand_model, x.unsqueeze(0))[0]
        r_mass = SegmentShap(f_rand, **shap_kw).explain(x, segments_mass(prof_r, M))["cell"]
        r_fixed = SegmentShap(f_rand, **shap_kw).explain(x, segments_uniform(L, M))["cell"]
        r_ig, _ = integrated_gradients(f_rand, x)
        sanity.append({"window": w,
                       "SG-SHAP (mass)": rank_similarity(trained_attr[(w, "SG-SHAP (mass)")], r_mass),
                       f"Fixed-SHAP (M={M})": rank_similarity(trained_attr[(w, f"Fixed-SHAP (M={M})")], r_fixed),
                       "IG": rank_similarity(trained_attr[(w, "IG")], r_ig)})

    # ---------------- save ----------------
    import pandas as pd
    df = pd.DataFrame(rows)
    df.to_csv(out / "per_window.csv", index=False)
    metrics = ["prec_at_k", "ap", "mass_in_gt", "del_aopc_mean", "ins_aopc_mean",
               "del_aopc_interp", "ins_aopc_interp", "n_evals", "seconds"]
    agg = df.groupby("method", sort=False)[metrics].agg(["mean", "std"])
    evt_only = df[df.n_gt_evt > 0].groupby("method", sort=False)["ap"].mean()
    lag_rows = df[df.regime_on].groupby("method", sort=False)["ap"].mean()
    sanity_df = pd.DataFrame(sanity)
    diag_df = df.drop_duplicates("window")
    summary = {
        "args": vars(a), "gt_config": gen.config_dict(),
        "forecast": {"test_mse_all": te_all, "test_mse_y": te_tgt, "zero_forecast_y": zero_tgt,
                     "noise_floor_y": floor_tgt},
        "delta_diagnostics": {k: float(diag_df[k].mean()) for k in
                              ("delta_ratio_x_evt", "delta_ratio_dis_evt", "delta_cv")},
        "n_windows": int(len(starts)), "n_regime_on": int(diag_df.regime_on.sum()),
        "n_with_evt_gt": int((diag_df.n_gt_evt > 0).sum()),
        "max_efficiency_gap": float(df["efficiency_gap"].max()),
        "sanity_spearman_mean": sanity_df.drop(columns="window").mean().to_dict(),
        "methods": {m: {k: {"mean": float(agg.loc[m, (k, "mean")]), "std": float(agg.loc[m, (k, "std")])}
                        for k in metrics} for m in agg.index},
        "ap_windows_with_evt_gt": evt_only.to_dict(),
        "ap_windows_regime_on": lag_rows.to_dict(),
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2, default=float))

    lines = [f"# SG-SHAP synthetic prototype — head={a.head}", "",
             f"Test MSE y = {te_tgt:.4f} (zero-forecast {zero_tgt:.4f}, noise floor {floor_tgt:.4f}); "
             f"{len(starts)} windows, {summary['n_regime_on']} regime-on, {summary['n_with_evt_gt']} with event GT.",
             f"Delta at x_evt spikes / elsewhere = {summary['delta_diagnostics']['delta_ratio_x_evt']:.3f}; "
             f"at dis_evt spikes = {summary['delta_diagnostics']['delta_ratio_dis_evt']:.3f}; "
             f"delta CV over lookback = {summary['delta_diagnostics']['delta_cv']:.3f}.", "",
             "| Method | P@k | AP | AP (evt windows) | mass in GT | Del-AOPC mean ↑ | Ins-AOPC mean ↓ | Del-AOPC interp ↑ | Ins-AOPC interp ↓ | evals | s |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for m in agg.index:
        g = lambda k: f"{agg.loc[m, (k, 'mean')]:.3f}±{agg.loc[m, (k, 'std')]:.3f}"
        lines.append(f"| {m} | {g('prec_at_k')} | {g('ap')} | {evt_only.get(m, np.nan):.3f} | {g('mass_in_gt')} | "
                     f"{g('del_aopc_mean')} | {g('ins_aopc_mean')} | {g('del_aopc_interp')} | {g('ins_aopc_interp')} | "
                     f"{agg.loc[m, ('n_evals', 'mean')]:.0f} | {agg.loc[m, ('seconds', 'mean')]:.2f} |")
    lines += ["", "Sanity (Spearman |attr| trained vs randomised model, lower = passes): " +
              ", ".join(f"{k} {v:.3f}" for k, v in summary["sanity_spearman_mean"].items()),
              f"Max KernelSHAP efficiency gap |Σφ − (f(x) − f(∅))| = {summary['max_efficiency_gap']:.2e}"]
    (out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    log("\n".join(lines), fh)
    plot(keep_for_fig, out, M)
    fh.close()


def plot(items, out: Path, M: int):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    show = ["SG-SHAP (mass)", f"Fixed-SHAP (M={M})", "GradientSHAP", "IG"]
    for i, it in enumerate(items):
        fig, axes = plt.subplots(2 + len(show), 1, figsize=(10, 2 + 1.6 * (2 + len(show))), sharex=True)
        ax = axes[0]
        ax.plot(it["x"][LAG], lw=0.8, label="x_lag")
        ax.plot(it["x"][EVT], lw=0.8, label="x_evt")
        for ch, c in ((LAG, "C0"), (EVT, "C1")):
            for t in np.flatnonzero(it["gt"][ch]):
                ax.axvspan(t - 0.5, t + 0.5, color=c, alpha=0.15, lw=0)
        ax.legend(loc="upper left", fontsize=7)
        ax.set_title("inputs (shaded = ground truth)", fontsize=9)
        ax = axes[1]
        ax.plot(it["prof"], color="k", lw=1)
        for name, ls in (("SG-SHAP (mass)", "-"), ("SG-SHAP (peaks)", ":")):
            for b in it["bounds"].get(name, [])[1:-1]:
                ax.axvline(b - 0.5, ls=ls, color="C3", lw=0.8)
        ax.set_title("Δ profile; red = SG-SHAP boundaries (solid mass, dotted peaks)", fontsize=9)
        for ax, name in zip(axes[2:], show):
            a = np.abs(it["attr"][name])
            ax.imshow(a / (a.max() + 1e-12), aspect="auto", cmap="viridis", interpolation="nearest")
            ax.set_yticks(range(len(CHANNELS)), CHANNELS, fontsize=7)
            ax.set_title(name, fontsize=9)
        axes[-1].set_xlabel("lookback position")
        fig.tight_layout()
        fig.savefig(out / f"window_{i}.png", dpi=120)
        plt.close(fig)


if __name__ == "__main__":
    main()
