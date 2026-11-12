"""
Aggregate several runs of scripts/run_sgshap_synthetic_v1.py (e.g. seeds): each
metric is first averaged over windows inside a run, then mean ± sd over runs.

    python -m scripts.aggregate_v1 results/sgshap_v1_flatten results/sgshap_v1_flatten_s1 \
        results/sgshap_v1_flatten_s2 --out results/sgshap_v1_flatten_seeds.md
"""

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

METRICS = [("ap", "AP"), ("prec_at_k", "P@k"), ("del_aopc_mean", "Del mean ↑"), ("ins_aopc_mean", "Ins mean ↓"),
           ("del_aopc_interp", "Del interp ↑"), ("n_evals", "evals")]
DIAG = [("delta_ratio_x_evt", "Δ at x_evt spikes / elsewhere"), ("delta_ratio_dis_evt", "Δ at dis_evt spikes / elsewhere"),
        ("delta_cv", "Δ CV"), ("ha_mass_in_gt_time", "HA mass on GT steps"), ("gt_time_frac", "GT fraction of lookback")]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("runs", nargs="+")
    p.add_argument("--out", required=True)
    a = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    per_run, diag, fc = [], [], []
    for r in a.runs:
        r = Path(r)
        s = json.loads((r / "summary.json").read_text(encoding="utf-8"))
        df = pd.read_csv(r / "per_window.csv")
        m = df.groupby("method", sort=False)[[k for k, _ in METRICS]].mean()
        m["run"] = r.name
        per_run.append(m.reset_index())
        diag.append({**s["diagnostics"], "run": r.name})
        fc.append({"run": r.name, "seed": s["args"]["seed"], **s["forecast"]})
    allm = pd.concat(per_run)
    order = list(dict.fromkeys(allm.method))
    g = allm.groupby("method", sort=False)
    mean, sd = g[[k for k, _ in METRICS]].mean().loc[order], g[[k for k, _ in METRICS]].std().loc[order]

    lines = [f"# SG-SHAP v1 — aggregate over {len(a.runs)} runs", "",
             "Runs: " + ", ".join(f"{f['run']} (seed {f['seed']}, test MSE y {f['test_mse_y']:.4f}, oracle {f['oracle_y']:.4f})"
                                   for f in fc), "",
             "Window-averaged metric per run, then mean ± sd over runs.", "",
             "| Method | " + " | ".join(n for _, n in METRICS) + " |", "|---|" + "---|" * len(METRICS)]
    for mth in order:
        cells = [f"{mean.loc[mth, k]:.3f}±{sd.loc[mth, k]:.3f}" if k != "n_evals" else f"{mean.loc[mth, k]:.0f}"
                 for k, _ in METRICS]
        lines.append(f"| {mth} | " + " | ".join(cells) + " |")
    d = pd.DataFrame(diag)
    lines += ["", "| Diagnostic | " + " | ".join(d.run) + " |", "|---|" + "---|" * len(d)]
    for k, n in DIAG:
        lines.append(f"| {n} | " + " | ".join(f"{v:.3f}" for v in d[k]) + " |")
    text = "\n".join(lines) + "\n"
    Path(a.out).write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
