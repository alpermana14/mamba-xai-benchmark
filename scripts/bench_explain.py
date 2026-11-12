"""
Benchmark v2 (plan §12): run every pre-registered explainer on one trained run and
score it against the task's ground truth and by deletion/insertion faithfulness.

  model-agnostic   Random, GxI (Gradient x Input), IG (32 steps, baseline 0 = train mean),
                   IG-U{4,8,16} (IG summed inside the uniform segments: resolution-matched),
                   SHAP-C (players = channels), SHAP-U{4,8,16} (channel x uniform segment),
                   SHAP-MMD8 (channel x per-channel MMD segments, v1), GS-SHAP (official code)
  Mamba-specific   MambaLRP (every Mamba model), SHAP-Δ8 (Δ-mass segments; models that scan time)

  G1, G2   AP, P@k, mass in GT over the scored cells; G2 also GS-SHAP's player metrics
  G3       per-channel attribution vs ground-truth SHAP value: Spearman of |.|, Pearson
           (signed), share of |attribution| on the two noise channels
  all      deletion / insertion AOPC with the mean and interp maskers; parameter-
           randomisation sanity (Spearman of |attr| trained vs randomly initialised model)

    python -m scripts.bench_explain --run results/bench/g2a/smamba_s0
    -> <run>/xai/{per_window.csv, sanity.csv, summary.md}
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from scipy.stats import pearsonr, spearmanr

from src.bench.tasks import GSSHAP_DIR, _gsshap_module, build_task
from src.models.zoo import SCAN_AXIS, build_model
from src.xai.baselines import integrated_gradients, random_attr
from src.xai.faithfulness import deletion_insertion, gt_metrics, rank_similarity
from src.xai.mamba_lrp import grad_x_input, mamba_lrp
from src.xai.sg_shap import (SegmentShap, delta_profile, player_map_per_channel, player_map_shared,
                             segments_mass, segments_mmd, segments_uniform)

sys.path.insert(0, str(GSSHAP_DIR))
from gsshap.deletion import player_phi_to_cell_scores                      # noqa: E402
from gsshap.explainers import build_group_segment_players, segment_groups_by_mmd  # noqa: E402
from gsshap.hsic import cluster_features_hsic                              # noqa: E402
from gsshap.shapley import shapley_for_one_sample                          # noqa: E402


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--run", required=True)
    p.add_argument("--n_explain", type=int, default=50)
    p.add_argument("--n_sanity", type=int, default=8)
    p.add_argument("--tag", default="xai", help="output folder inside the run (v2.2 budget runs use xai_budget)")
    p.add_argument("--shap_mult", type=float, default=1.0, help="KernelSHAP sample multiplier (sampled cases only)")
    p.add_argument("--ig_steps", type=int, default=32)
    p.add_argument("--shap_batch", type=int, default=512)
    p.add_argument("--gsshap_budget", type=int, default=1500, help="model calls, as in GS-SHAP's synthetic study")
    p.add_argument("--methods", nargs="*", default=None, help="subset (default: all applicable)")
    p.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    return p.parse_args()


def aggregate_to_map(attr: np.ndarray, pm: np.ndarray) -> np.ndarray:
    P = pm.max() + 1
    return (np.bincount(pm.ravel(), weights=attr.ravel(), minlength=P) / np.bincount(pm.ravel(), minlength=P))[pm]


class Explainers:
    def __init__(self, model, f, task, groups, seed, a):
        self.model, self.f, self.task, self.groups, self.seed, self.a = model, f, task, groups, seed, a
        C, L = len(task.channels), task.L
        self.C, self.L = C, L
        self.uniform = {M: player_map_shared(segments_uniform(L, M), C) for M in (4, 8, 16)}

    def shap(self, x, pm):
        P = int(pm.max()) + 1
        n = 2 ** P if P <= 13 else int(max(2048, 16 * P) * self.a.shap_mult)  # P <= 13: all coalitions (exact)
        res = SegmentShap(self.f, masker="mean", nsamples=n, batch_size=self.a.shap_batch,
                          seed=self.seed).explain_map(x, pm)
        return res["cell"], res["n_evals"], res["efficiency_gap"]

    def gsshap(self, x):
        """As evaluate_method_on_sample in GS-SHAP's synthetic_recovery_experiment.py (10 segments, budget calls)."""
        x_np = x.T.cpu().numpy()                                           # GS-SHAP layout [T, D]
        dev = x.device

        def predict_fn(xb):
            with torch.no_grad():
                return self.f(torch.as_tensor(xb, device=dev).transpose(1, 2)).cpu().numpy()

        segs = segment_groups_by_mmd(x_np, self.groups, min_seg_len=max(2, self.L // 10), max_segments=10,
                                     mmd_threshold=None, threshold_alpha=0.05, threshold_permutations=30,
                                     candidate_stride=1, seed=self.seed)
        players = build_group_segment_players(self.groups, segs)
        n_perm = max(1, self.a.gsshap_budget // len(players))
        phi = shapley_for_one_sample(x_np, players, np.zeros(self.C, np.float32), predict_fn,
                                     num_permutations=n_perm, rng=np.random.default_rng(self.seed))
        return player_phi_to_cell_scores(phi, players, self.L, self.C).T, n_perm * len(players) + 1, None

    def run(self, name, x, model=None, f=None):
        """-> (attr [C, L], n_evals, efficiency_gap) for one method; model/f override for the sanity check."""
        model, f = model or self.model, f or self.f
        if name == "Random":
            return random_attr(x, seed=self.seed)[0], 0, None
        if name == "GxI":
            return grad_x_input(f, x)[0], 1, None
        if name == "IG":
            return integrated_gradients(f, x, steps=self.a.ig_steps)[0], self.a.ig_steps, None
        if name.startswith("IG-U"):
            return (aggregate_to_map(integrated_gradients(f, x, steps=self.a.ig_steps)[0], self.uniform[int(name[4:])]),
                    self.a.ig_steps, None)
        if name == "MambaLRP":
            return mamba_lrp(f, model, x)[0], 1, None
        saved, self.f, self.model = (self.f, self.model), f, model
        try:
            if name == "SHAP-C":
                return self.shap(x, np.repeat(np.arange(self.C)[:, None], self.L, 1))
            if name.startswith("SHAP-U"):
                return self.shap(x, self.uniform[int(name[6:])])
            if name == "SHAP-MMD8":
                x_np = x.cpu().numpy()
                return self.shap(x, player_map_per_channel([segments_mmd(x_np[c], 8) for c in range(self.C)]))
            if name == "SHAP-Δ8":
                return self.shap(x, player_map_shared(segments_mass(delta_profile(model, x.unsqueeze(0))[0], 8), self.C))
            if name == "GS-SHAP":
                return self.gsshap(x)
        finally:
            self.f, self.model = saved
        raise ValueError(name)


def applicable_methods(model_name: str) -> list:
    m = ["Random", "GxI", "IG", "IG-U4", "IG-U8", "IG-U16", "SHAP-C", "SHAP-U4", "SHAP-U8", "SHAP-U16",
         "SHAP-MMD8", "GS-SHAP"]
    if SCAN_AXIS[model_name] != "none (attention)":
        m.append("MambaLRP")
    if SCAN_AXIS[model_name] == "time":
        m.append("SHAP-Δ8")
    return m


def hsic_groups(task, seed, cache: Path) -> list:
    """GS-SHAP feature groups from the training data (cached per task and seed: they do not depend on the model)."""
    if cache.exists():
        return json.loads(cache.read_text())
    C = len(task.channels)
    Xtr = task.X["train"].transpose(0, 2, 1).reshape(-1, C)
    var = np.flatnonzero(Xtr.std(0) > 1e-6)                                 # constant channels get their own group
    groups = cluster_features_hsic(Xtr[:, var], max_samples=3000, seed=seed)
    groups = [[int(var[j]) for j in g] for g in groups] + [[c] for c in range(C) if c not in var]
    tmp = cache.with_suffix(f".{os.getpid()}.tmp")                          # atomic: parallel queues share the cache
    tmp.write_text(json.dumps(groups))
    os.replace(tmp, cache)
    return groups


def feature_metrics(attr, g, score_mask, channels):
    a = np.array([attr[c][score_mask[c]].sum() for c in range(len(channels))])
    noise = [i for i, c in enumerate(channels) if c.startswith("noise")]
    return {"feat_spearman": float(spearmanr(np.abs(a), np.abs(g)).statistic),
            "feat_pearson": float(pearsonr(a, g).statistic) if a.std() > 0 else np.nan,
            "noise_share": float(np.abs(a[noise]).sum() / max(np.abs(a).sum(), 1e-12))}


def main():
    a = parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    run = Path(a.run)
    summ = json.loads((run / "summary.json").read_text(encoding="utf-8"))
    ra = summ["args"]
    seed, dev = ra["seed"], a.device
    task = build_task(ra["task"], seed)
    C, L, tgt = len(task.channels), task.L, task.target
    model = build_model(ra["model"], C, L, task.H, norm=task.norm).to(dev)
    model.load_state_dict(torch.load(run / "model.pt", map_location=dev))
    model.eval()
    f = lambda xs: model(xs)[:, tgt].mean(-1)
    torch.manual_seed(seed + 999)
    rmodel = build_model(ra["model"], C, L, task.H, norm=task.norm).to(dev).eval()
    f_r = lambda xs: rmodel(xs)[:, tgt].mean(-1)

    Xe = task.X[task.explain_split]
    idx = np.linspace(0, len(Xe) - 1, a.n_explain).astype(int)
    xs = torch.as_tensor(Xe[idx], device=dev)
    groups = hsic_groups(task, seed, run.parent / f"hsic_groups_s{seed}.json")
    methods = [m for m in applicable_methods(ra["model"]) if a.methods is None or m in a.methods]
    ex = Explainers(model, f, task, groups, seed, a)
    gs = _gsshap_module() if task.name.startswith("g2") else None
    out = run / a.tag
    out.mkdir(exist_ok=True)
    print(f"{run}: {len(idx)} windows, methods {methods}, HSIC groups {groups}", flush=True)

    rows, sanity = [], []
    for w, (i, x) in enumerate(zip(idx, xs)):
        if task.explain_steps is not None:                                  # G3: one horizon step per window
            st = torch.as_tensor(task.explain_steps(i), device=dev)
            f = ex.f = lambda xs, st=st: model(xs)[:, tgt][:, st].mean(-1)
            f_r = lambda xs, st=st: rmodel(xs)[:, tgt][:, st].mean(-1)
        with torch.no_grad():
            fx = f(x.unsqueeze(0)).item()
        for name in methods:
            t0 = time.time()
            attr, n_ev, eff = ex.run(name, x)
            sec = time.time() - t0
            row = {"window": w, "index": int(i), "method": name, "seconds": sec, "n_evals": n_ev,
                   "efficiency_gap": eff, "fx": fx, "sum_attr": float(attr.sum())}
            if task.gt_cells is not None:
                gt = task.gt_cells(i)
                row.update(gt_metrics(attr, gt, task.score_mask))
                row["n_gt"] = int((gt & task.score_mask).sum())
            if gs is not None:
                scores = gs.aggregate_cell_scores_to_players(attr[:tgt].T, task.meta["groups"], task.meta["segments"])
                row.update(gs.player_metrics(scores, task.meta["gt_players"][i]))
            if task.gt_feat is not None:
                row.update(feature_metrics(attr, task.gt_feat(i), task.score_mask, task.channels))
            for mk in ("mean", "interp"):
                row.update({f"{k}_{mk}": v for k, v in deletion_insertion(f, x, attr, masker=mk).items()})
            rows.append(row)
            if w < a.n_sanity and name != "Random":
                attr_r = ex.run(name, x, model=rmodel, f=f_r)[0]
                sanity.append({"window": w, "method": name, "spearman": rank_similarity(attr, attr_r)})
        print(f"window {w + 1}/{len(idx)}", flush=True)

    df, sd = pd.DataFrame(rows), pd.DataFrame(sanity)
    df.to_csv(out / "per_window.csv", index=False)
    sd.to_csv(out / "sanity.csv", index=False)
    cols = [c for c in ["ap", "prec_at_k", "mass_in_gt", "player_iou", "player_top1_hit", "feat_spearman",
                        "feat_pearson", "noise_share", "del_aopc_mean", "ins_aopc_mean", "del_aopc_interp",
                        "ins_aopc_interp", "n_evals", "seconds"] if c in df]
    agg = df.groupby("method", sort=False)[cols].mean()
    agg["sanity_spearman"] = sd.groupby("method", sort=False)["spearman"].mean() if len(sd) else np.nan
    fc = summ["forecast"][task.explain_split]
    lines = [f"# {task.name} · {ra['model']} (scan axis: {SCAN_AXIS[ra['model']]}) · seed {seed}", "",
             f"Forecast on the explained split: MSE {fc['mse']:.4f}, trivial {fc['trivial_mse']:.4f}, "
             f"skill {fc['skill']:.3f}" + (f", oracle {fc['oracle_mse']:.4f}" if fc.get("oracle_mse") else ""),
             f"{len(idx)} windows; sanity on {min(a.n_sanity, len(idx))} windows (lower = passes)", "",
             "| method | " + " | ".join(agg.columns) + " |", "|---|" + "---|" * len(agg.columns)]
    for m, r in agg.iterrows():
        lines.append(f"| {m} | " + " | ".join(f"{v:.3f}" if abs(v) < 1000 else f"{v:.0f}" for v in r.values) + " |")
    (out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
