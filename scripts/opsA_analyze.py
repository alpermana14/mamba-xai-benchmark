"""
Opsi A analysis (plan §12, 2026-11-11): HA1-HA3 on the OFFICIAL S-Mamba and TimeMachine checkpoints,
side by side with the zoo cells of the paper. Written before any explanation result existed.
    python -m scripts.opsA_analyze
Reads  results/opsA/<model>_<dataset>_s<seed>/{summary.json, xai/per_window.csv}
Writes results/opsA/analysis.md and results/opsA/comparisons.csv

Operationalisation fixed here (before results):
- a seed-run that fails the inclusion criterion (test MSE > 1.10 x paper) is dropped; a cell stays
  confirmatory when >= 2 seeds remain, otherwise it is descriptive only;
- HA1: MambaLRP - IG on del_aopc_mean per cell, Wilcoxon over pooled windows, Holm over the HA1 tests of
  the confirmatory cells, pass = p_holm < 0.05, diff > 0 and the same sign in every remaining seed;
  HA1 passes overall in >= 3/4 cells. del_aopc_interp is secondary (own Holm family, descriptive);
- HA2: per cell, method means over pooled windows; Kendall tau between del_aopc_mean and del_aopc_interp;
  pass = best method differs in >= 3/4 cells and median tau < 0.5;
- HA3: per cell, rank of SHAP-C (1 = best) under each masker; pass = better under interp in 4/4 cells.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import kendalltau, wilcoxon

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.bench_analyze import holm                                                  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "opsA"
ZOO = ROOT / "results" / "bench"
CELLS = [("etth1", "smamba"), ("etth1", "timemachine"), ("weather", "smamba"), ("weather", "timemachine")]
NAMES = {"smamba": "S-Mamba", "timemachine": "TimeMachine"}


def load():
    rows, runs = [], []
    for s in sorted(OUT.glob("*_s*/summary.json")):
        summ = json.loads(s.read_text(encoding="utf-8"))
        a = summ["args"]
        runs.append({"task": a["task"], "model": a["model"], "seed": a["seed"], "mse": summ["test_mse"],
                     "paper": summ["paper_mse"], "ratio": summ["ratio_to_paper"], "included": summ["passes_inclusion"],
                     "n_params": summ["n_params"]})
        pw = s.parent / "xai" / "per_window.csv"
        if pw.exists():
            d = pd.read_csv(pw)
            d["task"], d["model"], d["seed"] = a["task"], a["model"], a["seed"]
            rows.append(d)
    return (pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()), pd.DataFrame(runs)


def compare(cell, a, b, metric):
    pv = cell.pivot_table(index=["seed", "window"], columns="method", values=metric)
    d = (pv[a] - pv[b]).dropna()
    per_seed = d.groupby(level="seed").mean()
    p = wilcoxon(d).pvalue if np.any(d != 0) else 1.0
    return {"a": a, "b": b, "metric": metric, "n": len(d), "diff": float(d.mean()), "p": float(p),
            "per_seed": per_seed.round(4).to_dict(),
            "same_sign_all_seeds": bool((per_seed > 0).all() or (per_seed < 0).all())}


def zoo_reference():
    comp = pd.read_csv(ZOO / "comparisons.csv")
    comp = comp[(comp.a == "MambaLRP") & (comp.b == "IG")]
    md = pd.read_csv(ZOO / "masker_dependence.csv")
    ref = {}
    for t, m in CELLS:
        c = comp[(comp.task == t) & (comp.model == m)]
        r = md[(md.task == t) & (md.model == m)].iloc[0]
        ref[(t, m)] = {"diff_mean": float(c[c.metric == "del_aopc_mean"]["diff"].iloc[0]),
                       "verdict_mean": c[c.metric == "del_aopc_mean"]["verdict"].iloc[0],
                       "diff_interp": float(c[c.metric == "del_aopc_interp"]["diff"].iloc[0]),
                       "verdict_interp": c[c.metric == "del_aopc_interp"]["verdict"].iloc[0],
                       "tau": float(r["tau(del_mean, del_interp)"]), "best_mean": r["best by del_mean"],
                       "best_interp": r["best by del_interp"]}
    return ref


def main():
    df, runs = load()
    ref = zoo_reference()
    L = ["# Opsi A: RQ1 and RQ2 on the official S-Mamba and TimeMachine (H = 96)", "",
         "Pre-registered 2026-11-11 (plan §12). Operationalisation in the docstring of `scripts/opsA_analyze.py`.", "",
         "## Runs and inclusion", "", "| task | model | seed | test MSE | paper | ratio | included | params |",
         "|---|---|---|---|---|---|---|---|"]
    for r in runs.sort_values(["task", "model", "seed"]).itertuples():
        L.append(f"| {r.task} | {NAMES[r.model]} | {r.seed} | {r.mse:.4f} | {r.paper} | "
                 f"{'' if r.ratio is None or pd.isna(r.ratio) else f'{r.ratio:.3f}'} | {r.included} | {r.n_params:,} |")
    if df.empty:
        (OUT / "analysis.md").write_text("\n".join(L) + "\n\n(no explanation results yet)\n", encoding="utf-8")
        print("no per_window.csv yet"); return

    keep = runs[runs.included.fillna(True).astype(bool)][["task", "model", "seed"]]
    dfi = df.merge(keep, on=["task", "model", "seed"])
    n_seeds = dfi.groupby(["task", "model"]).seed.nunique()
    confirmatory = {c for c in CELLS if n_seeds.get(c, 0) >= 2}

    # ---- HA1
    comps = []
    for t, m in CELLS:
        cell = dfi[(dfi.task == t) & (dfi.model == m)]
        if cell.empty:
            continue
        for metric in ("del_aopc_mean", "del_aopc_interp"):
            c = compare(cell, "MambaLRP", "IG", metric)
            c.update(task=t, model=m, confirmatory=(t, m) in confirmatory)
            comps.append(c)
    comps = pd.DataFrame(comps)
    for metric in ("del_aopc_mean", "del_aopc_interp"):
        sel = (comps.metric == metric) & comps.confirmatory
        comps.loc[sel, "p_holm"] = holm(comps.loc[sel, "p"].to_numpy())
    comps["passes"] = (comps.p_holm < 0.05) & (comps["diff"] > 0) & comps.same_sign_all_seeds
    comps.to_csv(OUT / "comparisons.csv", index=False)
    ha1 = comps[(comps.metric == "del_aopc_mean") & comps.confirmatory]
    L += ["", "## HA1: MambaLRP − IG, deletion AOPC (higher = more faithful)", "",
          "| task | model | masker | n | mean diff (official) | per seed | p_holm | passes | zoo diff | zoo verdict |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for c in comps.itertuples():
        mk = "mean" if c.metric == "del_aopc_mean" else "interp"
        z = ref[(c.task, c.model)]
        L.append(f"| {c.task} | {NAMES[c.model]} | {mk} | {c.n} | {c.diff:+.4f} | {c.per_seed} | "
                 f"{'' if pd.isna(c.p_holm) else f'{c.p_holm:.1e}'} | {c.passes if c.confirmatory else 'descriptive'} | "
                 f"{z['diff_' + mk]:+.4f} | {z['verdict_' + mk]} |")
    ha1_pass = int(ha1.passes.sum())
    L.append(f"\n**HA1 verdict: {ha1_pass}/{len(ha1)} confirmatory cells pass "
             f"({'PASS' if ha1_pass >= 3 and len(ha1) >= 3 else 'FAIL'}; criterion >= 3/4).**")

    # ---- HA2 and HA3
    L += ["", "## HA2 (rankings differ between maskers) and HA3 (SHAP-C gains under interpolation)", "",
          "| task | model | tau(mean, interp) | best mean | best interp | SHAP-C rank mean → interp | zoo tau | zoo best mean → interp |",
          "|---|---|---|---|---|---|---|---|"]
    taus, differs, ha3 = [], 0, 0
    for t, m in CELLS:
        cell = dfi[(dfi.task == t) & (dfi.model == m)]
        if cell.empty or (t, m) not in confirmatory:
            continue
        mm = cell.groupby("method")[["del_aopc_mean", "del_aopc_interp"]].mean()
        tau = kendalltau(mm.del_aopc_mean, mm.del_aopc_interp).statistic
        bm, bi = mm.del_aopc_mean.idxmax(), mm.del_aopc_interp.idxmax()
        rk_m = int(mm.del_aopc_mean.rank(ascending=False)["SHAP-C"])
        rk_i = int(mm.del_aopc_interp.rank(ascending=False)["SHAP-C"])
        taus.append(tau); differs += bm != bi; ha3 += rk_i < rk_m
        z = ref[(t, m)]
        L.append(f"| {t} | {NAMES[m]} | {tau:+.3f} | {bm} | {bi} | {rk_m} → {rk_i} | {z['tau']:+.3f} | "
                 f"{z['best_mean']} → {z['best_interp']} |")
    n = len(taus)
    L.append(f"\n**HA2 verdict: best differs in {differs}/{n}, median tau {np.median(taus):+.3f} "
             f"({'PASS' if n and differs >= 3 and np.median(taus) < 0.5 else 'FAIL'}; criterion >= 3/4 and median tau < 0.5).**")
    L.append(f"\n**HA3 verdict: SHAP-C better under interp in {ha3}/{n} "
             f"({'PASS' if n == 4 and ha3 == 4 else 'FAIL'}; criterion 4/4).**")

    # ---- descriptive tables
    L += ["", "## Method means per cell (3 seeds pooled)", ""]
    for t, m in CELLS:
        cell = df[(df.task == t) & (df.model == m)]
        if cell.empty:
            continue
        mm = cell.groupby("method", sort=False)[["del_aopc_mean", "del_aopc_interp", "ins_aopc_mean",
                                                   "ins_aopc_interp", "n_evals", "seconds"]].mean()
        L += [f"### {t} · {NAMES[m]}", "", mm.to_markdown(floatfmt=".3f"), ""]
    (OUT / "analysis.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(l for l in L if l.startswith("**")))


if __name__ == "__main__":
    main()
