"""
Paired comparison of two explanation methods pooled over runs (plan §12 pre-registration):
per-window difference A - B, its mean per run, and a two-sided Wilcoxon signed-rank test
over all windows with a defined metric.

    python -m scripts.paired_test --csv per_window.csv --a "Δ-mass (M=8)" --b "Uniform (M=8)" \
        --metrics ap --runs results/sgshap_v1_last results/sgshap_v1_last_s1 results/sgshap_v1_last_s2
"""

import argparse
import sys
from pathlib import Path

import pandas as pd
from scipy.stats import wilcoxon


def paired(runs, csv, a, b, metric, key="window", method_col="method"):
    diffs = []
    for r in runs:
        df = pd.read_csv(Path(r) / csv)
        va = df[df[method_col] == a].set_index(key)[metric]
        vb = df[df[method_col] == b].set_index(key)[metric]
        if va.empty or vb.empty:
            raise KeyError(f"{r}/{csv}: method {a!r} or {b!r} not found")
        d = (va - vb).dropna()
        diffs.append(pd.DataFrame({"run": Path(r).name, "diff": d.values}))
    d = pd.concat(diffs)
    per_run = d.groupby("run", sort=False)["diff"].mean()
    p = wilcoxon(d["diff"]).pvalue if (d["diff"] != 0).any() else 1.0
    return {"metric": metric, "A": a, "B": b, "n": len(d), "mean_diff": d["diff"].mean(),
            "wilcoxon_p": p, "per_run": per_run.round(4).to_dict(),
            "same_sign_all_runs": bool((per_run > 0).all() or (per_run < 0).all())}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--runs", nargs="+", required=True)
    p.add_argument("--csv", default="per_window.csv")
    p.add_argument("--a", required=True)
    p.add_argument("--b", required=True)
    p.add_argument("--metrics", nargs="+", default=["ap"])
    p.add_argument("--key", default="window")
    p.add_argument("--method_col", default="method")
    args = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    for m in args.metrics:
        r = paired(args.runs, args.csv, args.a, args.b, m, args.key, args.method_col)
        print(f"{r['A']} − {r['B']} [{m}]: mean {r['mean_diff']:+.4f}, n {r['n']}, Wilcoxon p {r['wilcoxon_p']:.3g}, "
              f"per run {r['per_run']}, same sign in all runs: {r['same_sign_all_runs']}")


if __name__ == "__main__":
    main()
