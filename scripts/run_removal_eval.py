"""
Exp B (plan §12, pre-registered H2): exact Shapley values over M uniform time segments
under different removal operators, scored against time-level ground truth.

  replacement removals  mean, interp       on every model
  native removal        model(x, keep)     on MaskablePlainMamba models (mask token, + delta = 0 in "skip")

All models must come from the same seed (same data and test windows).

    python -m scripts.run_removal_eval --seed 0 --out results/removal/eval_s0 \
        --runs F1=results/sgshap_v1_flatten Fskip=results/removal/F_skip_s0 Ftoken=results/removal/F_token_s0
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import average_precision_score

from scripts.run_sgshap_synthetic import windows
from src.models.maskable_mamba import MaskablePlainMamba
from src.models.plain_mamba import PlainMamba
from src.synthetic.gt_generator import CHANNELS, LAG, TARGET, GTConfig, GTSeries
from src.xai.maskers import MASKERS
from src.xai.sg_shap import SegmentShap, player_map_shared, segments_uniform


def load_model(run: Path, dev):
    a = json.loads((run / "summary.json").read_text(encoding="utf-8"))["args"]
    kw = dict(d_model=a["d_model"], n_layers=a["n_layers"], d_state=a.get("d_state", 16), head=a["head"],
              revin=a["revin"])
    C, L, H = len(CHANNELS), a["seq_len"], a["pred_len"]
    mode = a.get("mask_train", "none")
    m = MaskablePlainMamba(C, L, H, mask_mode=mode, **kw) if mode != "none" else PlainMamba(C, L, H, **kw)
    m.load_state_dict(torch.load(run / "model.pt", map_location="cpu"))
    return m.to(dev).eval(), a


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--runs", nargs="+", required=True, help="name=run_dir")
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--n_windows", type=int, default=40)
    p.add_argument("--M", type=int, default=8)
    p.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    dev, out = args.device, Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    models, first = {}, None
    for spec in args.runs:
        name, run = spec.split("=", 1)
        models[name] = load_model(Path(run), dev)
        first = first or models[name][1]
        if any(models[name][1][k] != first[k] for k in ("length", "seq_len", "pred_len")) or models[name][1]["seed"] != args.seed:
            raise ValueError(f"{run}: data args differ from the first run or seed != {args.seed}")
    a = next(iter(models.values()))[1]
    L, H, C, M = a["seq_len"], a["pred_len"], len(CHANNELS), args.M

    gen = GTSeries(GTConfig(length=a["length"], seed=args.seed))
    raw = gen.data
    n_tr, n_va = int(0.7 * len(raw)), int(0.1 * len(raw))
    mu, sd = raw[:n_tr].mean(0), raw[:n_tr].std(0)
    data = torch.as_tensor((raw - mu) / sd, device=dev)
    te = np.arange(n_tr + n_va - L, len(raw) - L - H + 1)
    starts = te[np.linspace(0, len(te) - 1, args.n_windows).astype(int)]
    x_ex, _ = windows(data, starts, L, H)
    other, _ = windows(data, np.random.default_rng(0).choice(te, args.n_windows), L, H)
    b = segments_uniform(L, M)
    seg_of_t = np.repeat(np.arange(M), np.diff(b))
    pm = player_map_shared(b, C) % M                                   # time-only players
    score_mask = gen.score_mask(L)

    fc_rows, value_fns = [], {}
    for name, (model, ma) in models.items():
        f = (lambda mdl: lambda xs, keep=None: (mdl(xs) if keep is None else mdl(xs, keep))[:, TARGET].mean(-1))(model)
        with torch.no_grad():
            preds = torch.cat([model(windows(data, te[i:i + 512], L, H)[0]) for i in range(0, len(te), 512)])
            _, y_te = windows(data, te, L, H)
            mse = float(((preds - y_te)[:, TARGET] ** 2).mean())
        fc_rows.append({"model": name, "run_mask_train": ma.get("mask_train", "none"), "test_mse_y": mse,
                        "f_test_mean": float(preds[:, TARGET].mean(-1).mean()),
                        "f_test_sd": float(preds[:, TARGET].mean(-1).std())})
        for rm in ("mean", "interp"):
            value_fns[f"{name}·{rm}"] = (lambda f, rm: lambda x, keep: f(MASKERS[rm](x, keep)))(f, rm)
        if isinstance(model, MaskablePlainMamba):
            value_fns[f"{name}·native"] = (lambda f: lambda x, keep: f(x.unsqueeze(0).expand(len(keep), -1, -1),
                                                                        keep[:, 0, :]))(f)
            value_fns[f"_leak_{name}"] = f
    fc = pd.DataFrame(fc_rows).set_index("model")

    rows, leak = [], []
    for w, (s, x, xo) in enumerate(zip(starts, x_ex, other)):
        gt = gen.gt_mask(int(s), L, H)
        gt_time = (gt & score_mask).any(0)
        for meth, vf in value_fns.items():
            if meth.startswith("_leak_"):                             # native removal must erase the segment
                with torch.no_grad():
                    for k in range(M):
                        x2 = x.clone()
                        x2[:, b[k]:b[k + 1]] = xo[:, b[k]:b[k + 1]]
                        keep = torch.ones(1, L, dtype=torch.bool, device=dev)
                        keep[:, b[k]:b[k + 1]] = False
                        leak.append({"model": meth[6:], "window": w, "segment": k,
                                     "abs_diff": abs(vf(x.unsqueeze(0), keep) - vf(x2.unsqueeze(0), keep)).item()})
                continue
            res = SegmentShap(None, value_fn=vf, nsamples=2 ** M, seed=0).explain_map(x, pm)
            score_t = (np.abs(res["phi"]) / np.diff(b))[seg_of_t]
            rows.append({"window": w, "start": int(s), "method": meth, "model": meth.split("·")[0],
                         "removal": meth.split("·")[1], "regime_on": bool(gt[LAG].any()),
                         "ap_time": average_precision_score(gt_time, score_t) if gt_time.any() else np.nan,
                         "f_empty": res["base"], "fx": res["fx"], "efficiency_gap": res["efficiency_gap"]})
        print(f"window {w + 1}/{len(starts)}", flush=True)

    df = pd.DataFrame(rows)
    df.to_csv(out / "removal_eval.csv", index=False)
    lk = pd.DataFrame(leak)
    summ = df.groupby("method", sort=False).agg(ap_time=("ap_time", "mean"), ap_sd=("ap_time", "std"),
                                                f_empty=("f_empty", "mean"))
    lines = [f"# Exp B — removal operators, seed {args.seed}, exact Shapley over {M} time segments ({2 ** M} coalitions)",
             "", "| model | mask training | test MSE y | f on test: mean ± sd |", "|---|---|---|---|"]
    for name, r in fc.iterrows():
        lines.append(f"| {name} | {r.run_mask_train} | {r.test_mse_y:.4f} | {r.f_test_mean:.3f} ± {r.f_test_sd:.3f} |")
    lines += ["", "| model · removal | AP time-level GT | f(∅) | z of f(∅) |", "|---|---|---|---|"]
    for meth, r in summ.iterrows():
        m = fc.loc[meth.split("·")[0]]
        lines.append(f"| {meth} | {r.ap_time:.3f} ± {r.ap_sd:.3f} | {r.f_empty:.3f} | "
                     f"{(r.f_empty - m.f_test_mean) / m.f_test_sd:+.2f} |")
    if not lk.empty:
        lines += ["", "Native removal leak (max |f(x) − f(x')| when only the removed segment differs): " +
                  ", ".join(f"{k} {v:.2e}" for k, v in lk.groupby("model")["abs_diff"].max().items())]
    lines.append(f"Max efficiency gap = {df['efficiency_gap'].max():.2e}")
    text = "\n".join(lines) + "\n"
    (out / "removal_eval.md").write_text(text, encoding="utf-8")
    fc.to_csv(out / "forecast.csv")
    print(text)


if __name__ == "__main__":
    main()
