"""
Tables for the paper draft, generated from the benchmark results (run bench_analyze first):

    python -m scripts.paper_tables  ->  paper/tables/{forecast,gt_accuracy,faithfulness_public}.md
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

from scripts.bench_analyze import HORIZON, PRIMARY, REPLICATION, load
from src.bench.tasks import build_task

OUT = Path("paper/tables")
MODELS = ["plain", "smamba", "timemachine", "itransformer"]
MAMBA = MODELS[:3]
MODEL_NAMES = {"plain": "PlainMamba", "smamba": "S-Mamba", "timemachine": "TimeMachine", "itransformer": "iTransformer"}
GT_TASKS = ["g1", "g2a", "g2b", "g2c", "g3"]
METHODS = ["GxI", "IG", "MambaLRP", "IG-U4", "IG-U8", "IG-U16", "SHAP-C", "SHAP-U4", "SHAP-U8", "SHAP-U16",
           "SHAP-MMD8", "SHAP-Δ8", "GS-SHAP", "Random"]


def persistence_mse(task: str) -> float:
    t = build_task(task, 0)
    return float(((t.X["test"][:, -1, -1:] - t.Y["test"]) ** 2).mean())


def forecast_table(fc: pd.DataFrame) -> str:
    tasks = [t for t in GT_TASKS + ["etth1", "weather", *REPLICATION, *HORIZON] if t in set(fc.task)]
    rows = ["| task | " + " | ".join(MODEL_NAMES[m] for m in MODELS) + " | mean forecast | oracle | persistence |",
            "|---" * (len(MODELS) + 4) + "|"]
    for t in tasks:
        g = fc[fc.task == t]
        cells = []
        for m in MODELS:
            h = g[g.model == m]
            cells.append(f"{h.mse.mean():.4f} ± {h.mse.std():.4f}" if len(h) else "–")
        orc = g.oracle.dropna()
        pers = f"{persistence_mse(t):.3f}" if t not in GT_TASKS else "–"
        rows.append(f"| {t} | " + " | ".join(cells) + f" | {g.trivial.mean():.3f} | "
                    + (f"{orc.mean():.4f}" if len(orc) else "–") + f" | {pers} |")
    return "\n".join(rows)


def method_table(df: pd.DataFrame, tasks: list, metric_of) -> str:
    """
    Mean over the three Mamba forecasters (each: windows pooled over seeds) of each task's metric, so that
    MambaLRP is compared on the same models as the other methods; SHAP-Δ8 exists for PlainMamba only.
    """
    df = df[df.model.isin(MAMBA)]
    cols = [t for t in tasks if t in set(df.task)]
    rows = ["| method | " + " | ".join(f"{t} ({metric_of(t)})" for t in cols) + " |", "|---" * (len(cols) + 1) + "|"]
    for meth in METHODS:
        vals = []
        for t in cols:
            d = df[(df.task == t) & (df.method == meth)]
            vals.append(f"{d.groupby('model')[metric_of(t)].mean().mean():.3f}" if len(d) else "–")
        rows.append(f"| {meth}{' (PlainMamba only)' if meth == 'SHAP-Δ8' else ''} | " + " | ".join(vals) + " |")
    return "\n".join(rows)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)
    df, fc = load()
    gate = fc.set_index(["task", "model", "seed"]).gate
    df = df[[bool(gate.get((t, m, s), False)) for t, m, s in zip(df.task, df.model, df.seed)]]
    tables = {
        "forecast": forecast_table(fc),
        "gt_accuracy": method_table(df, GT_TASKS, lambda t: PRIMARY.get(t, "ap")),
        "faithfulness_public": "\n\n".join(
            f"**{mk}**\n\n" + method_table(df, ["etth1", "weather", *REPLICATION], lambda t, mk=mk: mk)
            for mk in ("del_aopc_mean", "del_aopc_interp")),
    }
    for k, v in tables.items():
        (OUT / f"{k}.md").write_text(v + "\n", encoding="utf-8")
        print(f"## {k}\n\n{v}\n")


if __name__ == "__main__":
    main()
