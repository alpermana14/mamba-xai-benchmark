"""
Figures for the paper, from the benchmark results (run bench_analyze first):

    python -m scripts.paper_figures  ->  paper/figures/fig1_protocol, fig3_verdicts, fig4_resolution, fig5_masker (.pdf, .png)

Visual style follows the figures of S-Mamba (Wang et al., Neurocomputing 619 (2025) 129178), our target journal:
Times serif text with bold panel titles, fully framed axes with outward ticks, dotted grid lines, legends in a
dashed box, and diagrams in the draw.io manner (pastel fills with a darker edge of the same hue, soft shadow,
dashed containers, thin black arrows). The pastel fills come from the S-Mamba figures; data marks use darker
steps of the same hues, checked with the dataviz validator (light surface, all pairs): series blue/orange/pink
pass every check, and the blue/red polarity pair passes. Every colour is paired with a letter or a marker shape.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mp                                             # noqa: E402
import matplotlib.pyplot as plt                                             # noqa: E402
import numpy as np                                                          # noqa: E402
import pandas as pd                                                         # noqa: E402

from scripts.bench_analyze import GT_METRICS, PRIMARY, REPLICATION, ROOT, load   # noqa: E402

OUT = Path("paper/figures")
SURFACE, INK, INK2, GRID, SHADOW = "#ffffff", "#000000", "#404040", "#808080", "#cfcfcf"
BLUE, ORANGE, PINK, RED = "#4a7cc4", "#c08300", "#c2457a", "#b85450"     # validated data colours
FILL = {"blue": "#dae8fc", "orange": "#ffe6cc", "pink": "#fbdbe7", "red": "#f8cecc", "green": "#d5e8d4",
        "yellow": "#fff2cc", "purple": "#e1d5e7", "grey": "#f5f5f5", "teal": "#d4eff1", "white": "#ffffff"}
EDGE = {"blue": "#6c8ebf", "orange": "#d79b00", "pink": "#c2457a", "red": "#b85450", "green": "#82b366",
        "yellow": "#d6b656", "purple": "#9673a6", "grey": "#666666", "teal": "#0e8088", "white": "#000000"}
DOTTED = (0, (1.2, 0.8))
TASKS = ["g1", "g2a", "g2b", "g2c", "g3", "etth1", "weather"]
TASK_NAMES = {"g1": "G1", "g2a": "G2a", "g2b": "G2b", "g2c": "G2c", "g3": "G3", "etth1": "ETTh1",
              "weather": "Weather", "etth2": "ETTh2", "ettm1": "ETTm1", "exchange": "Exchange"}
MODELS = ["plain", "smamba", "timemachine", "itransformer"]
MODEL_ABBR = {"plain": "PM", "smamba": "SM", "timemachine": "TM", "itransformer": "iT"}
COMPARISONS = [("MambaLRP", "IG"), ("MambaLRP", "GxI"), ("SHAP-Δ8", "SHAP-U8"), ("SHAP-Δ8", "SHAP-MMD8"),
               ("GS-SHAP", "SHAP-U8"), ("GS-SHAP", "SHAP-MMD8"), ("SHAP-U8", "IG-U8")]

plt.rcParams.update({
    "font.family": "serif", "font.serif": ["Times New Roman", "Times", "DejaVu Serif"], "mathtext.fontset": "stix",
    "font.size": 8, "axes.titlesize": 8.5, "axes.titleweight": "bold", "axes.labelsize": 8,
    "axes.edgecolor": INK, "axes.linewidth": 0.6, "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK, "xtick.labelsize": 7, "ytick.labelsize": 7,
    "xtick.direction": "out", "ytick.direction": "out", "xtick.major.width": 0.6, "ytick.major.width": 0.6,
    "xtick.major.size": 2.5, "ytick.major.size": 2.5, "legend.fontsize": 7,
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE, "pdf.fonttype": 42})


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"{name}.{ext}", dpi=300, bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)


def dashed_legend(leg):
    """S-Mamba legends: dashed grey frame, bold serif labels."""
    fr = leg.get_frame()
    fr.set_linestyle((0, (3, 2)))
    fr.set_edgecolor(GRID)
    fr.set_linewidth(0.6)
    fr.set_boxstyle("square", pad=0.3)
    for t in leg.get_texts():
        t.set_fontweight("bold")
    return leg


# ---------------------------------------------------------------- draw.io-style diagram parts
def dbox(ax, x, y, w, h, color, title=None, lines=(), size=6.8, shadow=True, italic_lines=False):
    """Pastel box with a darker edge of the same hue and a soft shadow; centred bold title and lines."""
    if shadow:
        ax.add_patch(mp.Rectangle((x + 0.45, y - 0.55), w, h, fc=SHADOW, ec="none", zorder=2))
    ax.add_patch(mp.Rectangle((x, y), w, h, fc=FILL[color], ec=EDGE[color], lw=0.7, zorder=3))
    rows = ([(title, "bold")] if title else []) + [(s, "italic" if italic_lines else "normal") for s in lines]
    step = size * 0.29
    top = y + h / 2 + step * (len(rows) - 1) / 2
    for k, (s, style) in enumerate(rows):
        ax.text(x + w / 2, top - k * step, s, ha="center", va="center", fontsize=size + (0.3 if style == "bold" else 0),
                fontweight="bold" if style == "bold" else "normal", fontstyle="italic" if style == "italic" else "normal",
                color=INK, zorder=4)


def container(ax, x, y, w, h, edge=INK, fill="none", lw=1.0, dash=(0, (5, 3)), z=0):
    ax.add_patch(mp.Rectangle((x, y), w, h, fc=fill, ec=edge, lw=lw, ls=dash, zorder=z))


def arrow(ax, *pts, lw=0.75):
    """Orthogonal black arrow through the given points; the head sits on the last point."""
    xs, ys = zip(*pts)
    if len(pts) > 2:
        ax.plot(xs[:-1], ys[:-1], color=INK, lw=lw, zorder=5, solid_capstyle="butt")
    ax.annotate("", pts[-1], pts[-2], zorder=5,
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=lw, mutation_scale=7, shrinkA=0, shrinkB=0))


def tensor(ax, x, y, cw=1.5, ch=1.25, cols=6, colors=("blue", "green", "yellow"), layers=3, dx=0.9, dy=0.8):
    """Stacked windows drawn as channel × time grids (rows = channels), back layers offset up-right."""
    for k in reversed(range(layers)):
        ox, oy = x + k * dx, y + k * dy
        for r, c in enumerate(colors):
            for j in range(cols):
                ax.add_patch(mp.Rectangle((ox + j * cw, oy + (len(colors) - 1 - r) * ch), cw, ch, fc=FILL[c],
                                          ec=EDGE[c], lw=0.45, zorder=6 - k))


# ---------------------------------------------------------------- Fig. 1
def fig_protocol():
    """Fig. 1: overview of the protocol, in the layout of the graphical abstract (four columns, short labels)."""
    fig, ax = plt.subplots(figsize=(7.2, 3.0))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 41)
    ax.axis("off")
    for x, label in ((11.5, "Study design"), (36.25, "Attribution methods"), (63.0, "Three-axis evaluation"),
                     (89.0, "Decision rules")):
        ax.text(x, 40.6, label, fontsize=8.6, fontweight="bold", ha="center", va="top")

    # study design: input windows into four forecasters
    container(ax, 0.5, 0.5, 22.0, 35.5)
    tensor(ax, 5.4, 28.8, cw=1.4, ch=1.1, cols=6, dx=0.8, dy=0.7)
    for k, (name, color) in enumerate((("PlainMamba (time)", "purple"), ("S-Mamba (variates)", "purple"),
                                       ("TimeMachine (channels)", "purple"), ("iTransformer (attention)", "grey"))):
        dbox(ax, 1.8, 21.9 - k * 4.4, 19.4, 3.6, color, name, size=6.3)
    arrow(ax, (11.5, 28.1), (11.5, 25.5))
    ax.text(11.5, 4.4, "5 ground-truth tasks\n5 public datasets\n192 trained models", fontsize=6.4, ha="center",
            va="center", fontstyle="italic", linespacing=1.3)

    # attribution methods
    container(ax, 25.0, 0.5, 22.5, 35.5, edge=EDGE["yellow"], fill="#fffbef", lw=0.9)
    dbox(ax, 26.25, 18.5, 20.0, 15.5, "yellow", "Generic (12)", ["GxI, IG", "IG at 3 resolutions", "Kernel SHAP at 4",
                                                                  "SHAP-MMD8, GS-SHAP", "Random"], size=6.7)
    dbox(ax, 26.25, 3.0, 20.0, 12.0, "red", "Mamba-specific (2)", ["MambaLRP", "step-size-guided", "segments"],
         size=6.7)
    arrow(ax, (22.5, 18.0), (25.0, 18.0))

    # three axes
    container(ax, 50.5, 0.5, 25.0, 35.5, edge=EDGE["green"], fill="#eef6ec", lw=0.9)
    dbox(ax, 51.75, 24.6, 22.5, 9.6, "blue", "Axis 1: ground truth", ["sparse cells, blocks,", "feature Shapley values"],
         size=6.7)
    dbox(ax, 51.75, 13.3, 22.5, 9.6, "orange", "Axis 2: resolution", ["cell, 16, 8 and 4", "segments, channel"],
         size=6.7)
    dbox(ax, 51.75, 2.0, 22.5, 9.6, "teal", "Axis 3: masker", ["deletion under mean and", "interpolation maskers"],
         size=6.7)
    arrow(ax, (47.5, 18.0), (50.5, 18.0))

    # decision rules
    for y, title, lines in ((24.6, "Paired test", ["Wilcoxon signed-rank", "with Holm correction"]),
                            (13.3, "Seed agreement", ["same sign of the effect", "in all three seeds"]),
                            (2.0, "Replication", ["held-out datasets", "and longer horizons"])):
        dbox(ax, 78.5, y, 21.0, 9.6, "white", title, lines, size=6.7)
        arrow(ax, (75.5, y + 4.8), (78.5, y + 4.8))
    save(fig, "fig1_protocol")


# ---------------------------------------------------------------- Fig. 3
def fig_verdicts(comp: pd.DataFrame):
    """Locked verdict per comparison (rows) and task x model cell (columns), one panel per metric kind."""
    cells = [(t, m) for t in TASKS for m in MODELS]
    panels = [("Ground truth (AP; G3: feature Spearman)", lambda t: PRIMARY.get(t, "ap") if PRIMARY.get(t, "ap") in GT_METRICS else None),
              ("Deletion AOPC, mean masker", lambda t: "del_aopc_mean"),
              ("Deletion AOPC, interpolation masker", lambda t: "del_aopc_interp")]
    look = comp.set_index(["task", "model", "a", "b", "metric"]).verdict
    style = {"A better": ("#c6dbf5", BLUE, "A"), "B better": ("#f4c7c5", RED, "B"),
             "no difference": (FILL["grey"], "#9a9a9a", "=")}
    fig, axes = plt.subplots(3, 1, figsize=(7.2, 5.7), gridspec_kw={"hspace": 0.62})
    for ax, (title, metric_of) in zip(axes, panels):
        for i, (a, b) in enumerate(COMPARISONS):
            for j, (t, m) in enumerate(cells):
                met = metric_of(t)
                v = look.get((t, m, a, b, met)) if met else None
                x = j + TASKS.index(t) * 0.6                                # gap between task groups
                if v is None:
                    continue
                fc, ec, txt = style[v]
                ax.add_patch(mp.Rectangle((x + 0.08, i + 0.08), 0.84, 0.84, fc=fc, ec=ec, lw=0.6))
                ax.text(x + 0.5, i + 0.53, txt, ha="center", va="center", fontsize=6.3, color=INK,
                        fontweight="bold" if txt != "=" else "normal")
        width = len(cells) + (len(TASKS) - 1) * 0.6
        ax.set_xlim(0, width)
        ax.set_ylim(len(COMPARISONS), 0)
        ax.set_yticks(np.arange(len(COMPARISONS)) + 0.5, [f"{a} vs {b}" for a, b in COMPARISONS])
        ax.set_xticks([j + TASKS.index(t) * 0.6 + 0.5 for j, (t, m) in enumerate(cells)],
                      [MODEL_ABBR[m] for t, m in cells], fontsize=6)
        for k, t in enumerate(TASKS):
            ax.text(k * (len(MODELS) + 0.6) + len(MODELS) / 2, -0.35, TASK_NAMES[t], ha="center", va="bottom",
                    fontsize=7.5, fontweight="bold")
        ax.tick_params(length=0)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_title(title, loc="left", pad=15)
    handles = [mp.Rectangle((0, 0), 1, 1, fc=fc, ec=ec, lw=0.6) for fc, ec, _ in style.values()]
    dashed_legend(fig.legend(handles, ["A better (A)", "B better (B)", "no difference (=)"], loc="lower center",
                             ncol=3, bbox_to_anchor=(0.5, 0.03), handlelength=1.2, columnspacing=2.0))
    fig.text(0.5, 0.005, "PM PlainMamba · SM S-Mamba · TM TimeMachine · iT iTransformer · blank = not applicable",
             fontsize=6.5, color=INK2, ha="center", fontstyle="italic")
    save(fig, "fig3_verdicts")


# ---------------------------------------------------------------- Fig. 5
def fig_masker(tau: pd.DataFrame):
    """Kendall tau between method rankings: mean vs interp masker, and each masker vs ground truth."""
    tasks = [t for t in TASKS + REPLICATION if t in set(tau.task)]
    series = [("tau(del_mean, del_interp)", "mean vs. interpolation masker", BLUE, "o"),
              ("tau(GT, del_mean)", "ground truth vs. mean masker", ORANGE, "s"),
              ("tau(GT, del_interp)", "ground truth vs. interpolation masker", PINK, "^")]
    fig, ax = plt.subplots(figsize=(5.2, 0.27 * len(tasks) + 0.95))
    ax.axvline(0, color=INK, lw=0.6, zorder=1)
    for x in (-0.75, -0.5, -0.25, 0.25, 0.5, 0.75):
        ax.axvline(x, color=GRID, lw=0.5, ls=DOTTED, zorder=0)
    for k, (col, label, c, mk) in enumerate(series):
        for r, t in enumerate(tasks):
            v = tau[tau.task == t][col].dropna()
            ax.scatter(v, np.full(len(v), r + (k - 1) * 0.22), s=20, marker=mk, color=c, edgecolor=SURFACE,
                       linewidth=0.5, zorder=3, label=label if r == 0 else None)
    ax.set_yticks(range(len(tasks)), [TASK_NAMES[t] + (" (rep.)" if t in REPLICATION else "") for t in tasks])
    ax.set_ylim(len(tasks) - 0.5, -0.5)
    ax.set_xlim(-1, 1)
    ax.set_xlabel("Kendall τ between method rankings (one point per forecaster)")
    dashed_legend(ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=3, fontsize=6.3, handletextpad=0.2,
                            columnspacing=0.9, borderaxespad=0))
    save(fig, "fig5_masker")


# ---------------------------------------------------------------- Fig. 4
def fig_resolution(df: pd.DataFrame):
    """AP against resolution for IG and KernelSHAP; mean over the Mamba forecasters, range as a band."""
    xs = ["cell", "16 seg.", "8 seg.", "4 seg.", "channel"]
    fam = {"IG": (["IG", "IG-U16", "IG-U8", "IG-U4"], [0, 1, 2, 3], BLUE, FILL["blue"], "o"),
           "Kernel SHAP": (["SHAP-U16", "SHAP-U8", "SHAP-U4", "SHAP-C"], [1, 2, 3, 4], ORANGE, FILL["orange"], "s")}
    tasks = ["g1", "g2a", "g2b", "g2c"]
    d = df[df.task.isin(tasks) & df.model.isin(MODELS[:3])]
    per_model = d.groupby(["task", "model", "method"]).ap.mean()
    fig, axes = plt.subplots(1, 4, figsize=(7.2, 2.15), sharey=True, gridspec_kw={"wspace": 0.12})
    for ax, t in zip(axes, tasks):
        for name, (meths, pos, c, fc, mk) in fam.items():
            v = np.array([[per_model[(t, m, meth)] for meth in meths] for m in MODELS[:3]])
            ax.fill_between(pos, v.min(0), v.max(0), color=fc, alpha=0.75, lw=0)
            ax.plot(pos, v.mean(0), color=c, lw=1.2, marker=mk, ms=4.2, mfc=fc, mec=c, mew=0.9, label=name,
                    zorder=4 if name == "IG" else 3)
            if t == tasks[0]:                                               # direct labels in the first panel
                end, off, ha, va = (0, (6, 2), "left", "bottom") if name == "IG" else (-1, (-4, -8), "right", "top")
                ax.annotate(name, (pos[end], v.mean(0)[end]), xytext=off, textcoords="offset points",
                            fontsize=6.8, color=INK, ha=ha, va=va)
        ax.set_title(TASK_NAMES[t])
        ax.set_xticks(range(5), xs, rotation=35, ha="right", fontsize=6.6)
        ax.set_xlim(-0.35, 4.35)
        ax.set_ylim(0, 1)
        ax.grid(axis="x", color=GRID, lw=0.5, ls=DOTTED)
    axes[0].set_ylabel("Average precision")
    handles, labels = axes[0].get_legend_handles_labels()
    dashed_legend(fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, -0.07), ncol=2,
                             columnspacing=2.5, handlelength=2.2))
    save(fig, "fig4_resolution")


def main():
    df, fc = load()
    gate = fc.set_index(["task", "model", "seed"]).gate
    df = df[[bool(gate.get((t, m, s), False)) for t, m, s in zip(df.task, df.model, df.seed)]]
    fig_protocol()
    fig_verdicts(pd.read_csv(ROOT / "comparisons.csv"))
    fig_masker(pd.read_csv(ROOT / "masker_dependence.csv"))
    fig_resolution(df)
    print("figures in", OUT)


if __name__ == "__main__":
    main()
