"""
Graphical abstract (required by Applied Soft Computing, optional for Neurocomputing): one landscape panel,
aspect about 2.5:1 (Elsevier minimum 1328 x 531 px), readable at 13 x 5 cm. Same draw.io-like style as Fig. 1,
following the figures of S-Mamba (pastel fills with darker edges, shadows, dashed containers, Times text).

    python -m scripts.paper_graphical_abstract  ->  paper/graphical_abstract.{pdf,tif}
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt                                             # noqa: E402

from scripts.paper_figures import EDGE, SURFACE, arrow, container, dbox, tensor   # noqa: E402

OUT = Path("paper/graphical_abstract")


def main():
    fig, ax = plt.subplots(figsize=(8.0, 3.25))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 41)
    ax.axis("off")
    for x, label in ((10.75, "Study"), (40.0, "Three-axis protocol (pre-registered)"), (79.5, "Findings")):
        ax.text(x, 39.8, label, fontsize=9.5, fontweight="bold", ha="center", va="top")

    # study: input windows into four forecasters
    container(ax, 0.5, 0.5, 20.5, 35.5)
    tensor(ax, 4.6, 28.3, cw=1.45, ch=1.15, cols=6, dx=0.8, dy=0.7)
    for k, (name, color) in enumerate((("PlainMamba (time)", "purple"), ("S-Mamba (variates)", "purple"),
                                       ("TimeMachine (channels)", "purple"), ("iTransformer (attention)", "grey"))):
        dbox(ax, 1.8, 20.6 - k * 4.4, 18.0, 3.5, color, name, size=6.7)
    arrow(ax, (10.75, 27.6), (10.75, 24.1))
    ax.text(10.75, 3.6, "14 attribution methods\n192 trained models", fontsize=7.6, ha="center", va="center",
            fontstyle="italic", linespacing=1.35)

    # three axes
    container(ax, 24.5, 0.5, 31.0, 35.5, edge=EDGE["green"], fill="#eef6ec", lw=0.9)
    dbox(ax, 26.3, 24.6, 27.4, 9.6, "blue", "Axis 1: ground truth", ["sparse cells · blocks ·", "feature Shapley values"],
         size=7.6)
    dbox(ax, 26.3, 13.3, 27.4, 9.6, "orange", "Axis 2: resolution", ["cell → 16 → 8 → 4", "segments → channel"],
         size=7.6)
    dbox(ax, 26.3, 2.0, 27.4, 9.6, "teal", "Axis 3: masker", ["deletion under mean and", "interpolation maskers"],
         size=7.6)
    arrow(ax, (21.0, 18.0), (24.5, 18.0))

    # findings
    for y, title, lines in ((24.6, "Mamba-specific methods: no gain",
                             ["MambaLRP vs. Integrated Gradients:", "better in 1, worse in 8 of 15 cells"]),
                            (13.3, "Resolution outweighs the estimator",
                             ["accuracy spread 0.28 across resolutions", "vs. 0.04 between estimators"]),
                            (2.0, "The masker decides the winner",
                             ["best method changed in 39 of 40 cells;", "replicated on new data and horizons"])):
        dbox(ax, 59.5, y, 40.0, 9.6, "white", title, lines, size=7.6)
        arrow(ax, (55.5, y + 4.8), (59.5, y + 4.8))
    for ext in ("pdf", "tif"):
        fig.savefig(OUT.with_suffix(f".{ext}"), dpi=300, facecolor=SURFACE, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    print("written", OUT.with_suffix(".pdf"), OUT.with_suffix(".tif"))


if __name__ == "__main__":
    main()
