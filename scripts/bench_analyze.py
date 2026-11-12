"""
Benchmark v2 analysis with the statistics fixed in the protocol (plan §12):

  - forecast quality per (task, model), quality gate: MSE below the trivial forecast
  - per cell (task x model): method means, windows pooled over seeds
  - pre-registered comparisons (RQ1): "A better than B" only if the paired Wilcoxon
    p < 0.05 after Holm correction over all comparisons x metrics of that cell AND the
    mean difference has the same sign in every seed
  - average ranks over cells + Friedman test (RQ1/RQ3)
  - masker dependence (RQ2): Kendall tau between method rankings by deletion AOPC with
    the mean vs the interp masker, and between each and the ground-truth ranking
  - resolution vs estimator (RQ4): IG-U{M} vs SHAP-U{M}

    python -m scripts.bench_analyze  ->  results/bench/analysis.md (+ csv)
"""

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import friedmanchisquare, kendalltau, wilcoxon

ROOT = Path("results/bench")
REPLICATION = ["etth2", "ettm1", "exchange"]                                    # v2.1 (plan §12)
HORIZON = [f"{d}_h{h}" for d in ("etth1", "weather") for h in (192, 336, 720)]  # v2.2 (plan §12)
PRIMARY = {"g3": "feat_spearman", **dict.fromkeys(["etth1", "weather", *REPLICATION, *HORIZON], "del_aopc_interp")}  # else ap
HIGHER_BETTER = {"ap": True, "prec_at_k": True, "mass_in_gt": True, "player_iou": True, "feat_spearman": True,
                 "feat_pearson": True, "noise_share": False, "del_aopc_mean": True, "del_aopc_interp": True,
                 "ins_aopc_mean": False, "ins_aopc_interp": False}
GT_METRICS = {"ap", "prec_at_k", "mass_in_gt", "player_iou", "feat_spearman", "feat_pearson", "noise_share"}
COMPARISONS = [("MambaLRP", "IG"), ("MambaLRP", "GxI"), ("SHAP-Δ8", "SHAP-U8"), ("SHAP-Δ8", "SHAP-MMD8"),
               ("GS-SHAP", "SHAP-MMD8"), ("GS-SHAP", "SHAP-U8"), ("SHAP-U8", "IG-U8")]
GENERAL = ["GxI", "IG", "IG-U4", "IG-U8", "IG-U16", "SHAP-C", "SHAP-U4", "SHAP-U8", "SHAP-U16", "SHAP-MMD8",
           "GS-SHAP", "Random"]


def md(df: pd.DataFrame) -> str:
    fmt = lambda v: f"{v:.3f}" if isinstance(v, (float, np.floating)) else str(v)
    rows = ["| " + " | ".join(df.columns) + " |", "|---" * len(df.columns) + "|"]
    return "\n".join(rows + ["| " + " | ".join(fmt(v) for v in r) + " |" for r in df.itertuples(index=False)])


def holm(p: np.ndarray) -> np.ndarray:
    p = np.asarray(p, float)
    out = np.full_like(p, np.nan)
    ok = np.flatnonzero(~np.isnan(p))
    order = ok[np.argsort(p[ok])]
    m, running = len(order), 0.0
    for k, i in enumerate(order):
        running = max(running, min(1.0, (m - k) * p[i]))
        out[i] = running
    return out


def load():
    rows, fc = [], []
    for s in sorted(ROOT.glob("*/*_s*/summary.json")):
        run = s.parent
        summ = json.loads(s.read_text(encoding="utf-8"))
        task, model, seed = summ["task"], summ["args"]["model"], summ["args"]["seed"]
        f = summ["forecast"]
        split = "gt" if "gt" in f else "test"
        fc.append({"task": task, "model": model, "seed": seed, "mse": f[split]["mse"], "trivial": f[split]["trivial_mse"],
                   "skill": f[split]["skill"], "oracle": f[split].get("oracle_mse"), "gate": f["passes_quality_gate"],
                   "best_epoch": summ["training"]["best_epoch"], "verdict": summ["training"]["verdict"][:40],
                   "s_per_epoch": summ["training"].get("seconds_per_epoch")})
        pw = run / "xai" / "per_window.csv"
        if pw.exists():
            d = pd.read_csv(pw)
            d["task"], d["model"], d["seed"] = task, model, seed
            rows.append(d)
    return (pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()), pd.DataFrame(fc)


def compare(cell: pd.DataFrame, a: str, b: str, metric: str) -> dict | None:
    pv = cell.pivot_table(index=["seed", "window"], columns="method", values=metric)
    if a not in pv or b not in pv:
        return None
    d = (pv[a] - pv[b]).dropna()
    if len(d) < 5:
        return None
    sign = 1 if HIGHER_BETTER[metric] else -1
    per_seed = d.groupby(level="seed").mean() * sign
    p = wilcoxon(d).pvalue if np.any(d != 0) else 1.0
    return {"a": a, "b": b, "metric": metric, "n": len(d), "diff": float(d.mean()), "p": float(p),
            "same_sign_all_seeds": bool((per_seed > 0).all() or (per_seed < 0).all()),
            "a_better_in_seeds": int((per_seed > 0).sum()), "n_seeds": len(per_seed)}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    df, fc = load()
    lines = ["# Benchmark v2 — analysis", "", "## Forecast quality (mean over seeds)", "",
             "| task | model | seeds | MSE | trivial | skill | oracle | gate passed | s/epoch |", "|---|---|---|---|---|---|---|---|---|"]
    for (t, m), g in fc.groupby(["task", "model"]):
        orc = g.oracle.dropna()
        lines.append(f"| {t} | {m} | {len(g)} | {g.mse.mean():.4f} ± {g.mse.std():.4f} | {g.trivial.mean():.3f} | "
                     f"{g.skill.mean():.3f} | {orc.mean():.4f} | {int(g.gate.sum())}/{len(g)} | {g.s_per_epoch.mean():.1f} |"
                     if len(orc) else
                     f"| {t} | {m} | {len(g)} | {g.mse.mean():.4f} ± {g.mse.std():.4f} | {g.trivial.mean():.3f} | "
                     f"{g.skill.mean():.3f} | – | {int(g.gate.sum())}/{len(g)} | {g.s_per_epoch.mean():.1f} |")
    if df.empty:
        (ROOT / "analysis.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("\n".join(lines))
        return
    gate = fc.set_index(["task", "model", "seed"]).gate
    df = df[[bool(gate.get((t, m, s), False)) for t, m, s in zip(df.task, df.model, df.seed)]]

    comp_rows, rank_rows, tau_rows = [], [], []
    for (t, m), cell in df.groupby(["task", "model"]):
        prim = PRIMARY.get(t, "ap")
        metrics = list(dict.fromkeys([prim, "del_aopc_mean", "del_aopc_interp"]))     # public: prim is del_aopc_interp
        means = cell.groupby("method")[[c for c in HIGHER_BETTER if c in cell] + ["n_evals"]].mean()
        lines += ["", f"## {t} · {m} ({cell.seed.nunique()} seeds, {cell.groupby('seed').window.nunique().sum()} windows)",
                  "", "| method | " + " | ".join(means.columns) + " |", "|---|" + "---|" * len(means.columns)]
        for meth, r in means.sort_values(prim, ascending=not HIGHER_BETTER[prim]).iterrows():
            lines.append(f"| {meth} | " + " | ".join(f"{v:.3f}" if abs(v) < 100 else f"{v:.0f}" for v in r.values) + " |")
        res = [c for a_, b_ in COMPARISONS for met in metrics if (c := compare(cell, a_, b_, met))]
        for c, ph in zip(res, holm([c["p"] for c in res])):
            c.update(task=t, model=m, p_holm=ph,
                     verdict=("A better" if c["diff"] * (1 if HIGHER_BETTER[c["metric"]] else -1) > 0 else "B better")
                     if ph < 0.05 and c["same_sign_all_seeds"] else "no difference")
            comp_rows.append(c)
        r = means[prim].rank(ascending=not HIGHER_BETTER[prim])
        rank_rows.append(pd.Series(r, name=(t, m)))
        if {"del_aopc_mean", "del_aopc_interp"} <= set(means):
            mm = means.drop(index="Random", errors="ignore")
            tau_rows.append({"task": t, "model": m, "GT metric": prim if prim in GT_METRICS else "–",
                             "tau(del_mean, del_interp)": kendalltau(mm.del_aopc_mean, mm.del_aopc_interp).statistic,
                             "tau(GT, del_mean)": kendalltau(mm[prim], mm.del_aopc_mean).statistic
                             if prim in GT_METRICS else np.nan,
                             "tau(GT, del_interp)": kendalltau(mm[prim], mm.del_aopc_interp).statistic
                             if prim in GT_METRICS else np.nan,
                             "best by GT": (mm[prim].idxmax() if HIGHER_BETTER[prim] else mm[prim].idxmin())
                             if prim in GT_METRICS else "–",
                             "best by del_mean": mm.del_aopc_mean.idxmax(), "best by del_interp": mm.del_aopc_interp.idxmax()})

    comp = pd.DataFrame(comp_rows)
    comp.to_csv(ROOT / "comparisons.csv", index=False)
    lines += ["", "## Pre-registered comparisons (Holm within cell; verdict needs p_holm < 0.05 and same sign in all seeds)", "",
              "| task | model | A | B | metric | n | mean(A−B) | p_holm | A better in seeds | verdict |", "|---|---|---|---|---|---|---|---|---|---|"]
    for _, c in comp.iterrows():
        lines.append(f"| {c.task} | {c.model} | {c.a} | {c.b} | {c.metric} | {c.n} | {c['diff']:+.3f} | {c.p_holm:.1e} | "
                     f"{c.a_better_in_seeds}/{c.n_seeds} | {c.verdict} |")

    # descriptive tallies of the verdicts above (no new tests)
    comp["data"] = comp.task.map(lambda t: "G2" if t.startswith("g2") else t.upper() if t.startswith("g")
                                else "public v2.1" if t in REPLICATION else "public v2.2 horizon" if t in HORIZON
                                else "public")
    comp["kind"] = np.where(comp.metric.isin(GT_METRICS), "GT", comp.metric)
    short = ["A better", "no difference", "B better"]
    lines +=["", "## Verdict tally (A / = / B cells)", "", "| A vs B | data | GT | del_aopc_mean | del_aopc_interp | "
              "A under both maskers |", "|---|---|---|---|---|---|"]
    for (a_, b_), g in comp.groupby(["a", "b"], sort=False):
        for dat, h in g.groupby("data"):
            tally = {k: "/".join(str(int((h[h.kind == k].verdict == v).sum())) for v in short) if (h.kind == k).any() else "–"
                     for k in ("GT", "del_aopc_mean", "del_aopc_interp")}
            both = h[h.kind != "GT"].pivot_table(index=["task", "model"], columns="kind", values="verdict", aggfunc="first")
            n_both = int((both == "A better").all(axis=1).sum()) if len(both) else 0
            lines.append(f"| {a_} vs {b_} | {dat} | {tally['GT']} | {tally['del_aopc_mean']} | {tally['del_aopc_interp']} | "
                         f"{n_both}/{len(both)} |")
    dm = comp[comp.kind != "GT"].pivot_table(index=["task", "model", "a", "b"], columns="kind", values="verdict",
                                             aggfunc="first").dropna()
    tasks_of = dm.index.get_level_values("task")
    for label, sel in (("v2", ~tasks_of.isin(REPLICATION + HORIZON)), ("v2.1 replication", tasks_of.isin(REPLICATION)),
                       ("v2.2 horizon", tasks_of.isin(HORIZON))):
        d_ = dm[sel]
        flips = int((d_.del_aopc_mean != d_.del_aopc_interp).sum())
        opposite = int((d_.isin(["A better"]).any(axis=1) & d_.isin(["B better"]).any(axis=1)).sum())
        lines.append(f"\n{label}: deletion verdict differs between maskers in {flips}/{len(d_)} comparisons; "
                     f"opposite significant verdicts (A under one masker, B under the other) in {opposite}/{len(d_)}.")

    all_ranks = pd.DataFrame(rank_rows)
    all_ranks.to_csv(ROOT / "ranks.csv")
    main_cells = [i for i in all_ranks.index if i[0] not in REPLICATION + HORIZON]  # the pre-registered v2 scope
    v21_cells = [i for i in all_ranks.index if i[0] not in HORIZON]
    for scope, ranks in (("v2 cells", all_ranks.loc[main_cells]), ("cells (v2 + v2.1 replication)", all_ranks.loc[v21_cells])):
        if scope != "v2 cells" and len(ranks) == len(main_cells):
            continue
        gen = [m for m in GENERAL if m in ranks and ranks[m].notna().all()]
        lines += ["", f"## Average rank over {len(ranks)} {scope} (primary metric; 1 = best)", "",
                  "| method | mean rank | cells |", "|---|---|---|"]
        for meth, v in ranks.mean().sort_values().items():
            lines.append(f"| {meth} | {v:.2f} | {int(ranks[meth].notna().sum())} |")
        if len(ranks) >= 3 and len(gen) >= 3:
            sub = ranks[gen]
            lines.append(f"\nFriedman over the {len(gen)} general methods present in every cell: "
                         f"p = {friedmanchisquare(*[sub[c] for c in gen]).pvalue:.2e}")
        lrp = ranks.dropna(subset=["MambaLRP"]) if "MambaLRP" in ranks else None
        if lrp is not None and len(lrp):
            lines.append(f"MambaLRP rank in Mamba cells: mean {lrp.MambaLRP.mean():.2f} vs IG {lrp.IG.mean():.2f} "
                         f"({len(lrp)} cells)")

    tau = pd.DataFrame(tau_rows)
    tau.to_csv(ROOT / "masker_dependence.csv", index=False)
    lines += ["", "## Masker dependence (RQ2): Kendall tau between method rankings", "", md(tau)]

    rq4 = []
    for (t, m), cell in df.groupby(["task", "model"]):
        prim = PRIMARY.get(t, "ap")
        mm = cell.groupby("method")[prim].mean()
        rq4.append({"task": t, "model": m, **{k: mm.get(k, np.nan) for k in
                                              ["IG", "IG-U4", "SHAP-U4", "IG-U8", "SHAP-U8", "IG-U16", "SHAP-U16", "SHAP-C"]}})
    lines += ["", "## Resolution vs estimator (RQ4): primary metric", "", md(pd.DataFrame(rq4))]
    (ROOT / "analysis.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
