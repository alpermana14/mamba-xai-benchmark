"""
Exp C (plan §12, pre-registered H3): MambaLRP vs Gradient x Input vs IG on a model
trained by scripts/run_sgshap_synthetic_v1.py, on the same 40 test windows and with
the same metrics (GT AP / P@k / mass, deletion-insertion AOPC, randomisation sanity).

    python -m scripts.run_lrp_eval --run results/sgshap_v1_flatten
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch

from scripts.run_sgshap_synthetic import windows
from src.models.plain_mamba import PlainMamba
from src.synthetic.gt_generator import CHANNELS, EVT, LAG, TARGET, GTConfig, GTSeries
from src.xai.baselines import integrated_gradients, random_attr
from src.xai.faithfulness import deletion_insertion, gt_metrics, rank_similarity
from src.xai.mamba_lrp import grad_x_input, mamba_lrp

METRICS = ["ap", "prec_at_k", "mass_in_gt", "del_aopc_mean", "ins_aopc_mean", "del_aopc_interp", "ins_aopc_interp"]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--run", required=True)
    p.add_argument("--n_sanity", type=int, default=8)
    p.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    run, dev = Path(args.run), args.device
    a = json.loads((run / "summary.json").read_text(encoding="utf-8"))["args"]
    L, H, C = a["seq_len"], a["pred_len"], len(CHANNELS)

    gen = GTSeries(GTConfig(length=a["length"], seed=a["seed"]))       # same data and windows as the run
    raw = gen.data
    n_tr, n_va = int(0.7 * len(raw)), int(0.1 * len(raw))
    mu, sd = raw[:n_tr].mean(0), raw[:n_tr].std(0)
    data = torch.as_tensor((raw - mu) / sd, device=dev)
    te = np.arange(n_tr + n_va - L, len(raw) - L - H + 1)
    starts = te[np.linspace(0, len(te) - 1, a["n_explain"]).astype(int)]
    x_ex, _ = windows(data, starts, L, H)
    score_mask = gen.score_mask(L)

    def build():
        return PlainMamba(C, L, H, d_model=a["d_model"], n_layers=a["n_layers"], d_state=a.get("d_state", 16),
                          head=a["head"], revin=a["revin"]).to(dev).eval()

    model = build()
    model.load_state_dict(torch.load(run / "model.pt", map_location=dev))
    f = lambda xs: model(xs)[:, TARGET].mean(-1)

    rows, kept = [], {}
    for w, (s, x) in enumerate(zip(starts, x_ex)):
        gt = gen.gt_mask(int(s), L, H)
        fx = f(x.unsqueeze(0)).item()
        attrs = {"MambaLRP": mamba_lrp(f, model, x)[0], "Grad×Input": grad_x_input(f, x)[0],
                 "IG": integrated_gradients(f, x)[0], "Random": random_attr(x, seed=a["seed"] + w)[0]}
        for name, attr in attrs.items():
            row = {"window": w, "start": int(s), "method": name, "regime_on": bool(gt[LAG].any()),
                   "n_gt_evt": int(gt[EVT].sum()), "fx": fx, "sum_attr": float(attr.sum()),
                   **gt_metrics(attr, gt, score_mask)}
            for mk in ("mean", "interp"):
                row.update({f"{k}_{mk}": v for k, v in deletion_insertion(f, x, attr, masker=mk).items()})
            rows.append(row)
            if w < args.n_sanity:
                kept[(w, name)] = attr
        print(f"window {w + 1}/{len(starts)}", flush=True)

    torch.manual_seed(a["seed"] + 999)                                   # same randomised model as the v1 run
    rmodel = build()
    f_r = lambda xs: rmodel(xs)[:, TARGET].mean(-1)
    sanity = {"MambaLRP": [], "Grad×Input": [], "IG": []}
    for w in range(min(args.n_sanity, len(starts))):
        x = x_ex[w]
        r = {"MambaLRP": mamba_lrp(f_r, rmodel, x)[0], "Grad×Input": grad_x_input(f_r, x)[0],
             "IG": integrated_gradients(f_r, x)[0]}
        for k in sanity:
            sanity[k].append(rank_similarity(kept[(w, k)], r[k]))

    df = pd.DataFrame(rows)
    df.to_csv(run / "lrp_eval.csv", index=False)
    agg = df.groupby("method", sort=False)[METRICS].agg(["mean", "std"])
    cons = df.assign(gap=(df.sum_attr - df.fx).abs()).groupby("method", sort=False)["gap"].median()
    lines = [f"# Exp C — MambaLRP vs gradients, head={a['head']}, seed {a['seed']}", "",
             f"{len(starts)} test windows, same as `per_window.csv` of this run.", "",
             "| Method | " + " | ".join(METRICS) + " | median abs(Σattr − f(x)) | sanity Spearman ↓ |",
             "|---|" + "---|" * (len(METRICS) + 2)]
    for m in agg.index:
        san = f"{np.mean(sanity[m]):.3f}" if m in sanity else "—"
        lines.append(f"| {m} | " + " | ".join(f"{agg.loc[m, (k, 'mean')]:.3f}±{agg.loc[m, (k, 'std')]:.3f}"
                                             for k in METRICS) + f" | {cons[m]:.3f} | {san} |")
    text = "\n".join(lines) + "\n"
    (run / "lrp_eval.md").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
