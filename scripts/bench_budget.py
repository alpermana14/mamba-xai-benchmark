"""
v2.2 B (plan §12, pre-registered 2026-11-08): is KernelSHAP's lack of advantage at matched resolution a sampling
artefact? The G1/G2 models were re-explained with 4x KernelSHAP samples and 128 IG steps (<run>/xai_budget/).

  B1  with 4x samples, SHAP-U8 is not better than IG-U8 (32 steps, v2 run) by the locked rule on AP
      (paired Wilcoxon over windows pooled across seeds, same sign in all seeds) in >= 14 of 16 cells
  descriptive: mean AP change per method; map convergence (Spearman between default and high-budget maps) for
      SHAP-U8 and IG-U8, recomputed on seed 0 and the first 10 explained windows of each cell (the benchmark
      stores metrics, not maps)

    python -m scripts.bench_budget  ->  results/bench/budget.md
"""

import sys
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pandas as pd
import torch
from scipy.stats import spearmanr, wilcoxon

from scripts.bench_explain import Explainers, hsic_groups
from src.bench.tasks import build_task
from src.models.zoo import build_model

ROOT = Path("results/bench")
TASKS, MODELS, SEEDS = ["g1", "g2a", "g2b", "g2c"], ["plain", "smamba", "timemachine", "itransformer"], [0, 1, 2]
METHODS = ["IG", "IG-U4", "IG-U8", "IG-U16", "SHAP-U4", "SHAP-U8", "SHAP-U16"]


def load() -> pd.DataFrame:
    rows = []
    for t in TASKS:
        for m in MODELS:
            for s in SEEDS:
                run = ROOT / t / f"{m}_s{s}"
                if not (run / "xai_budget" / "per_window.csv").exists():
                    continue
                base = pd.read_csv(run / "xai" / "per_window.csv")[["window", "method", "ap"]]
                high = pd.read_csv(run / "xai_budget" / "per_window.csv")[["window", "method", "ap"]]
                d = base.merge(high, on=["window", "method"], suffixes=("_default", "_budget"))
                d["task"], d["model"], d["seed"] = t, m, s
                rows.append(d)
    return pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()


def verdict(cell: pd.DataFrame) -> dict:
    """SHAP-U8 at 4x samples vs IG-U8 at 32 steps, locked rule on AP."""
    a = cell[cell.method == "SHAP-U8"].set_index(["seed", "window"]).ap_budget
    b = cell[cell.method == "IG-U8"].set_index(["seed", "window"]).ap_default
    d = (a - b).dropna()
    per_seed = d.groupby(level="seed").mean()
    p = wilcoxon(d).pvalue if np.any(d != 0) else 1.0
    same = bool((per_seed > 0).all() or (per_seed < 0).all())
    v = ("A better" if d.mean() > 0 else "B better") if p < 0.05 and same else "no difference"
    return {"n": len(d), "diff": float(d.mean()), "p": float(p), "verdict": v}


def convergence(n_windows: int = 10) -> pd.DataFrame:
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    rows = []
    for t in TASKS:
        task = build_task(t, 0)
        Xe = task.X[task.explain_split]
        idx = np.linspace(0, len(Xe) - 1, 50).astype(int)[:n_windows]
        for m in MODELS:
            run = ROOT / t / f"{m}_s0"
            model = build_model(m, len(task.channels), task.L, task.H, norm=task.norm).to(dev)
            model.load_state_dict(torch.load(run / "model.pt", map_location=dev))
            model.eval()
            f = lambda xs: model(xs)[:, task.target].mean(-1)
            groups = hsic_groups(task, 0, ROOT / t / "hsic_groups_s0.json")
            lo = Explainers(model, f, task, groups, 0, SimpleNamespace(shap_batch=512, gsshap_budget=1500,
                                                                       shap_mult=1.0, ig_steps=32))
            hi = Explainers(model, f, task, groups, 0, SimpleNamespace(shap_batch=512, gsshap_budget=1500,
                                                                       shap_mult=4.0, ig_steps=128))
            for i in idx:
                x = torch.as_tensor(Xe[i], device=dev)
                for meth in ("SHAP-U8", "IG-U8"):
                    a, b = lo.run(meth, x)[0], hi.run(meth, x)[0]
                    rows.append({"task": t, "model": m, "method": meth,
                                 "spearman": spearmanr(a.ravel(), b.ravel()).statistic})
    return pd.DataFrame(rows)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    df = load()
    lines = ["# v2.2 B: estimator budget (pre-registered 2026-11-08)", ""]
    cells = [verdict(g) | {"task": t, "model": m} for (t, m), g in df.groupby(["task", "model"])]
    v = pd.DataFrame(cells)
    not_better = int((v.verdict != "A better").sum())
    lines += [f"B1: SHAP-U8 (4x samples) not better than IG-U8 (32 steps) in {not_better}/{len(v)} cells "
              f"(pass if >= 14 of 16): {'PASS' if len(v) == 16 and not_better >= 14 else 'FAIL' if len(v) == 16 else 'incomplete'}",
              f"verdicts: {v.verdict.value_counts().to_dict()}", "",
              "| task | model | n | mean(SHAP-U8 x4 − IG-U8) | p | verdict |", "|---|---|---|---|---|---|"]
    lines += [f"| {r.task} | {r.model} | {r.n} | {r.diff:+.3f} | {r.p:.1e} | {r.verdict} |" for r in v.itertuples()]
    df["delta"] = df.ap_budget - df.ap_default
    ch = df.groupby(["method", "task"]).delta.mean().unstack().reindex(METHODS)
    lines += ["", "Mean AP change (high budget − default), windows pooled over models and seeds", "",
              "| method | " + " | ".join(ch.columns) + " |", "|---|" + "---|" * len(ch.columns)]
    lines += [f"| {meth} | " + " | ".join(f"{x:+.4f}" for x in r) + " |" for meth, r in ch.iterrows()]
    if "--no-convergence" not in sys.argv:
        cv = convergence()
        cv.to_csv(ROOT / "budget_convergence.csv", index=False)
        s = cv.groupby(["method", "task"]).spearman.median().unstack()
        lines += ["", "Map convergence: median Spearman between default and high-budget maps "
                      "(seed 0, first 10 explained windows per cell)", "",
                  "| method | " + " | ".join(s.columns) + " |", "|---|" + "---|" * len(s.columns)]
        lines += [f"| {meth} | " + " | ".join(f"{x:.3f}" for x in r) + " |" for meth, r in s.iterrows()]
    (ROOT / "budget.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
