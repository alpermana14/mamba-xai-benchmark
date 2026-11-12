"""
v2.2 A (plan §12): example attribution maps against the ground truth, for the paper.

PlainMamba seed 0 (the only forecaster on which every method is defined). Windows are fixed by rule, not chosen
by eye: on G1 the first explained window with at least one ground-truth cell, on G2a the first explained window.

    python -m scripts.paper_examples  ->  paper/figures/fig2_examples.{pdf,png}
"""

from pathlib import Path
from types import SimpleNamespace

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt                                             # noqa: E402
import numpy as np                                                          # noqa: E402
import torch                                                                # noqa: E402
from matplotlib.colors import LinearSegmentedColormap                       # noqa: E402

from scripts.bench_explain import Explainers, hsic_groups                   # noqa: E402
from scripts.paper_figures import INK, INK2, RED, SURFACE, save             # noqa: E402
from src.bench.tasks import build_task                                      # noqa: E402
from src.models.zoo import build_model                                      # noqa: E402
from src.xai.faithfulness import gt_metrics                                 # noqa: E402

METHODS = ["IG", "MambaLRP", "SHAP-U8", "SHAP-Δ8", "GS-SHAP"]
N_EXPLAIN = 50                                                              # as in the benchmark runs
BLUES = LinearSegmentedColormap.from_list("blues", ["#ffffff", "#b7cff2", "#86ace3", "#5585cc", "#3563a8", "#1d3d70"])
UNSCORED = "#e6e6e6"                                                         # validated ramp; 0 = white surface


def explain_window(task_name: str, rule: str):
    run = Path(f"results/bench/{task_name}/plain_s0")
    task = build_task(task_name, 0)
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    model = build_model("plain", len(task.channels), task.L, task.H, norm=task.norm).to(dev)
    model.load_state_dict(torch.load(run / "model.pt", map_location=dev))
    model.eval()
    f = lambda xs: model(xs)[:, task.target].mean(-1)
    Xe = task.X[task.explain_split]
    idx = np.linspace(0, len(Xe) - 1, N_EXPLAIN).astype(int)
    if rule == "first_with_gt":
        w = next(k for k, i in enumerate(idx) if (task.gt_cells(i) & task.score_mask).any())
    else:
        w = 0
    i = idx[w]
    x = torch.as_tensor(Xe[i], device=dev)
    a = SimpleNamespace(shap_batch=512, gsshap_budget=1500, shap_mult=1.0, ig_steps=32)
    ex = Explainers(model, f, task, hsic_groups(task, 0, run.parent / "hsic_groups_s0.json"), 0, a)
    gt = task.gt_cells(i)
    maps = {m: ex.run(m, x)[0] for m in METHODS}
    aps = {m: gt_metrics(maps[m], gt, task.score_mask)["ap"] for m in METHODS}
    return task, w, gt, maps, aps


def gt_blocks(gt):
    """Ground-truth cells as rectangles: consecutive true cells of a channel, merged across identical channels."""
    runs = []
    for c, row in enumerate(gt):
        edges = np.flatnonzero(np.diff(np.r_[0, row.astype(int), 0]))
        runs += [(c, s, e) for s, e in zip(edges[::2], edges[1::2])]
    blocks = []
    for c, s, e in runs:
        if blocks and blocks[-1][1] == c - 1 and blocks[-1][2:] == (s, e):
            blocks[-1] = (blocks[-1][0], c, s, e)
        else:
            blocks.append((c, c, s, e))
    return blocks


def draw(ax, values, gt, mask, ticks, title):
    v = np.abs(values) * mask
    ax.imshow(v / max(v.max(), 1e-12), cmap=BLUES, vmin=0, vmax=1, aspect="auto", interpolation="nearest")
    ax.imshow(np.where(mask, np.nan, 1.0), cmap=LinearSegmentedColormap.from_list("g", [UNSCORED] * 2),
              aspect="auto", interpolation="nearest")                      # unscored channels in grey
    for c0, c1, s, e in gt_blocks(gt):
        ax.add_patch(plt.Rectangle((s - 0.5, c0 - 0.5), e - s, c1 - c0 + 1, fill=False, ec=RED, lw=1.1))
    ax.set_yticks(*ticks, fontsize=5.5)
    ax.tick_params(axis="x", labelsize=5.5, length=2)
    ax.tick_params(axis="y", length=0)
    ax.set_title(title, fontsize=7.2, color=INK, loc="left", pad=2, fontweight="normal")
    for s in ax.spines.values():
        s.set_color(INK)
        s.set_linewidth(0.5)


def main():
    cols = [explain_window("g1", "first_with_gt"), explain_window("g2a", "first")]
    fig, axes = plt.subplots(len(METHODS) + 1, 2, figsize=(7.2, 5.7), gridspec_kw={"hspace": 0.62, "wspace": 0.16})
    for j, (task, w, gt, maps, aps) in enumerate(cols):
        names = {"g1": "G1 (sparse cells)", "g2a": "G2a (group-segment block)"}[task.name]
        if task.name == "g1":
            ticks = (range(len(task.channels)), [c.replace("dis_", "d_") for c in task.channels])
        else:                                                               # 12 features in 4 groups of 3, then y
            groups = task.meta["groups"]
            ticks = ([np.mean(g) for g in groups] + [len(task.channels) - 1],
                     [f"f{g[0]}–f{g[-1]}" for g in groups] + ["y"])
        draw(axes[0, j], gt.astype(float), gt, task.score_mask, ticks, f"{names}, window {w + 1}: ground truth")
        for r, m in enumerate(METHODS, 1):
            draw(axes[r, j], maps[m], gt, task.score_mask, ticks, f"{m}  (AP {aps[m]:.2f})")
        axes[-1, j].set_xlabel("Time step in the input window", fontsize=6.5, color=INK)
        print(task.name, "window", w + 1, {m: round(v, 3) for m, v in aps.items()})
    fig.text(0.5, 0.035, "Shading: |attribution| scaled to the maximum of each map (darker = larger).  "
             "Red outlines: ground-truth cells.  Grey rows: channels excluded from scoring.",
             ha="center", fontsize=6.3, color=INK2, fontstyle="italic")
    fig.patch.set_facecolor(SURFACE)
    save(fig, "fig2_examples")


if __name__ == "__main__":
    main()
