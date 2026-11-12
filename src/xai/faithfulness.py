"""
Explanation metrics (plan §3.3): ground-truth recovery, deletion/insertion AOPC,
parameter-randomisation sanity check.
"""

import numpy as np
import torch
from scipy.stats import spearmanr
from sklearn.metrics import average_precision_score

from src.xai.maskers import MASKERS


def gt_metrics(attr: np.ndarray, gt: np.ndarray, score_mask: np.ndarray) -> dict:
    """|attr| ranked against binary ground truth over the scored cells."""
    a, y = np.abs(attr)[score_mask], gt[score_mask]
    if y.sum() == 0:
        return {"prec_at_k": np.nan, "ap": np.nan, "mass_in_gt": np.nan}
    k = int(y.sum())
    top = np.argsort(-a, kind="stable")[:k]
    return {"prec_at_k": float(y[top].mean()),
            "ap": float(average_precision_score(y, a)),
            "mass_in_gt": float(a[y].sum() / max(a.sum(), 1e-12))}


@torch.no_grad()
def deletion_insertion(f, x: torch.Tensor, attr: np.ndarray, masker: str = "mean",
                       fracs=(0.02, 0.05, 0.1, 0.2, 0.3), seed: int = 0) -> dict:
    """
    Deletion AOPC  = mean_q |f(x) - f(x without top-q cells)|   (higher = more faithful)
    Insertion AOPC = mean_q |f(x) - f(only top-q cells kept)|    (lower  = more faithful)
    Ties (segment-level attributions) are broken at random.
    """
    C, L = x.shape
    rng = np.random.default_rng(seed)
    score = np.abs(attr).ravel() + 1e-9 * rng.random(C * L)
    order = torch.as_tensor(np.argsort(-score))
    keeps_del, keeps_ins = [], []
    for q in fracs:
        top = torch.zeros(C * L, dtype=torch.bool)
        top[order[:max(1, int(round(q * C * L)))]] = True
        keeps_del.append(~top.view(C, L))
        keeps_ins.append(top.view(C, L))
    keep = torch.stack(keeps_del + keeps_ins).to(x.device)
    out = f(torch.cat([x.unsqueeze(0), MASKERS[masker](x, keep)])).cpu().numpy()
    fx, rest = out[0], out[1:]
    n = len(fracs)
    return {"del_aopc": float(np.abs(fx - rest[:n]).mean()),
            "ins_aopc": float(np.abs(fx - rest[n:]).mean())}


def rank_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return float(spearmanr(np.abs(a).ravel(), np.abs(b).ravel()).statistic)
