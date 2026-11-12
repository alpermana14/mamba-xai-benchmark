"""
v2.1 replication of the masker-dependence finding (plan §12, pre-registered 2026-11-04 before any run):

  M1  method rankings are unstable across maskers: median Kendall tau(del_mean, del_interp) < 0.5
      AND the best method differs in >= 6/12 new cells
  M2  deletion-interp favours coarse attributions: SHAP-C ranks better under del_interp than under
      del_mean in >= 10/12 new cells (one-sided sign test p < 0.05; ties count as failures)
  M3  deletion-mean favours mean-masker SHAP: mean AOPC SHAP-U8 > IG-U8 under del_mean in >= 10/12
      new cells AND under del_interp in <= 6/12
  secondary (descriptive): MambaLRP vs IG, cells with "A better" under both maskers (locked rule)

Cell means pool windows over seeds; Random is excluded; rank 1 = highest AOPC. The original public
cells (etth1, weather) are reported alongside as the discovery set, not as evidence.

    python -m scripts.bench_analyze && python -m scripts.bench_replication  ->  results/bench/replication.md

v2.2 horizon robustness (plan §12, pre-registered 2026-11-08): the same statistics per horizon H in {192, 336, 720}
on ETTh1 and Weather (8 cells each): M1-H passes if median tau < 0.5 and the best method differs in >= 4/8 cells,
M2-H if SHAP-C ranks better under interp in >= 7/8 (the thresholds below at n = 8); M3 was closed and is descriptive.

    python -m scripts.bench_replication --set horizon  ->  results/bench/replication_horizon.md
"""

import sys

import numpy as np
import pandas as pd
from scipy.stats import binomtest, kendalltau

from scripts.bench_analyze import HORIZON, REPLICATION, ROOT, load

NEW, DISCOVERY = REPLICATION, ["etth1", "weather"]


def cell_stats(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (t, m), cell in df.groupby(["task", "model"]):
        mm = cell[cell.method != "Random"].groupby("method")[["del_aopc_mean", "del_aopc_interp"]].mean()
        rk = mm.rank(ascending=False)
        rows.append({"task": t, "model": m, "tau": kendalltau(mm.del_aopc_mean, mm.del_aopc_interp).statistic,
                     "best_mean": mm.del_aopc_mean.idxmax(), "best_interp": mm.del_aopc_interp.idxmax(),
                     "shapc_rank_mean": rk.loc["SHAP-C", "del_aopc_mean"],
                     "shapc_rank_interp": rk.loc["SHAP-C", "del_aopc_interp"],
                     "u8_beats_ig_mean": mm.loc["SHAP-U8", "del_aopc_mean"] > mm.loc["IG-U8", "del_aopc_mean"],
                     "u8_beats_ig_interp": mm.loc["SHAP-U8", "del_aopc_interp"] > mm.loc["IG-U8", "del_aopc_interp"]})
    return pd.DataFrame(rows)


def verdicts(st: pd.DataFrame, comp: pd.DataFrame) -> list:
    n = len(st)
    differs = int((st.best_mean != st.best_interp).sum())
    m2 = int((st.shapc_rank_interp < st.shapc_rank_mean).sum())
    u8m, u8i = int(st.u8_beats_ig_mean.sum()), int(st.u8_beats_ig_interp.sum())
    lrp = comp[(comp.a == "MambaLRP") & (comp.b == "IG") & comp.task.isin(st.task.unique())]
    both = lrp.pivot_table(index=["task", "model"], columns="metric", values="verdict", aggfunc="first")
    n_both = int((both[["del_aopc_mean", "del_aopc_interp"]] == "A better").all(axis=1).sum()) if len(both) else 0
    return [
        ("M1", f"median tau {st.tau.median():.3f}; best differs {differs}/{n}",
         st.tau.median() < 0.5 and differs >= n / 2),
        ("M2", f"SHAP-C ranks better under interp in {m2}/{n} (sign test p = "
               f"{binomtest(m2, n, 0.5, alternative='greater').pvalue:.1e})", m2 >= np.ceil(n * 10 / 12)),
        ("M3", f"SHAP-U8 > IG-U8: under mean {u8m}/{n}, under interp {u8i}/{n}",
         u8m >= np.ceil(n * 10 / 12) and u8i <= n / 2),
        ("secondary", f"MambaLRP better than IG under both maskers in {n_both}/{len(both)} cells", None),
    ]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    df, fc = load()
    gate = fc.set_index(["task", "model", "seed"]).gate
    df = df[[bool(gate.get((t, m, s), False)) for t, m, s in zip(df.task, df.model, df.seed)]]
    comp = pd.read_csv(ROOT / "comparisons.csv")
    horizon = "--set" in sys.argv and sys.argv[sys.argv.index("--set") + 1] == "horizon"
    if horizon:
        title, out = "# v2.2 horizon robustness: masker dependence (pre-registered 2026-11-08)", "replication_horizon.md"
        groups = [(f"H = {h} (ETTh1, Weather)", [t for t in HORIZON if t.endswith(f"_h{h}")]) for h in (192, 336, 720)]
    else:
        title, out = "# v2.1 replication: masker dependence (pre-registered 2026-11-04)", "replication.md"
        groups = [("Confirmatory: new cells", NEW), ("Discovery: original public cells (not evidence)", DISCOVERY)]
    lines = [title, ""]
    for name, tasks in groups:
        st = cell_stats(df[df.task.isin(tasks)])
        if st.empty:
            lines += [f"## {name}", "", "no runs yet", ""]
            continue
        lines += [f"## {name} ({len(st)} cells)", "", "| hypothesis | result | passes |", "|---|---|---|"]
        for h, txt, ok in verdicts(st, comp):
            if horizon and h == "M3":
                h, ok = "M3 (closed, descriptive)", None
            elif horizon and h in ("M1", "M2"):
                h += "-H"
            lines.append(f"| {h} | {txt} | {'–' if ok is None else 'yes' if ok else 'no'} |")
        lines += ["", "| task | model | tau | best (mean) | best (interp) | SHAP-C rank mean → interp | "
                      "SHAP-U8 > IG-U8 (mean / interp) |", "|---|---|---|---|---|---|---|"]
        for r in st.itertuples():
            lines.append(f"| {r.task} | {r.model} | {r.tau:.3f} | {r.best_mean} | {r.best_interp} | "
                         f"{r.shapc_rank_mean:.0f} → {r.shapc_rank_interp:.0f} | "
                         f"{'yes' if r.u8_beats_ig_mean else 'no'} / {'yes' if r.u8_beats_ig_interp else 'no'} |")
        lines.append("")
    (ROOT / out).write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
