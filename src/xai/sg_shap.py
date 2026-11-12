"""
SG-SHAP: Selectivity-Guided Segment SHAP (plan §3.2).

1. One forward pass records the selective-scan internals of every Mamba layer.
2. A guide profile p_t over the lookback is built from them:
     delta_profile            - delta_t averaged over d_inner, each layer scaled to mean 1
     hidden_attention_profile - |alpha_{t,s} u_s| (Ali et al., 2024) rolled out over layers
                                with the residual (Abnar & Zuidema, 2020), read out at the
                                positions the head uses
3. The lookback is cut into M segments from p_t:
     "mass"  - equal mass of p_t. For delta, sum(delta) is the model's own clock;
               high-p stretches get shorter segments (finer resolution).
     "peaks" - boundaries at the M-1 largest local maxima of p_t.
   Baselines: "uniform" (fixed windows) and "mmd" (data-driven change points per
   channel, the segmentation step of GroupSegment-SHAP, Kim & Park 2026).
4. Players = channel x segment; Shapley values by KernelSHAP with a masker.
"""

import numpy as np
import shap
import torch

from src.models.mamba_ext import capture_internals, hidden_attention_row
from src.xai.maskers import MASKERS


@torch.no_grad()
def delta_profile(model, x: torch.Tensor) -> np.ndarray:
    """x [B, C, L] -> per-sample delta profile [B, L] (each layer scaled to mean 1)."""
    with capture_internals(model) as internals:
        model(x)
    profs = []
    for li in internals.layers:
        p = li.delta.mean(-1)                         # [B, L]
        profs.append(p / p.mean(-1, keepdim=True))
    return torch.stack(profs).mean(0).cpu().numpy()


@torch.no_grad()
def hidden_attention_profile(model, x: torch.Tensor, readout: np.ndarray | None = None) -> np.ndarray:
    """
    x [C, L] (one window) -> influence of each input step on the read-out [L].

    Per layer M[t, s] = sum_d |alpha[t, s, d] * u_s[d]|, row-normalised; layers are
    composed as R <- (I + M) / 2 @ R so the residual path counts. `readout` [L] weights
    the output positions the head looks at (one-hot last step for a last-state head,
    head-weight norms for a flatten head); default uniform.
    """
    L, dev = x.shape[-1], x.device
    with capture_internals(model) as internals:
        model(x.unsqueeze(0))
    eye = torch.eye(L, device=dev)
    R = eye.clone()
    for li in internals.layers:
        M = torch.zeros(L, L, device=dev)
        for t in range(L):
            a = hidden_attention_row(li, t)[0]                     # [t+1, d_inner]
            M[t, :t + 1] = (a * li.u[0, :t + 1]).abs().sum(-1)
        M = M / M.sum(1, keepdim=True).clamp_min(1e-12)
        R = (0.5 * eye + 0.5 * M) @ R
    w = (torch.full((L,), 1.0 / L, device=dev) if readout is None
         else torch.as_tensor(readout, dtype=torch.float32, device=dev))
    return (w @ R).cpu().numpy()


def _enforce_min_len(b: np.ndarray, L: int, min_len: int) -> np.ndarray:
    b = np.asarray(b, dtype=int).copy()
    b[0], b[-1] = 0, L
    for i in range(1, len(b) - 1):
        b[i] = max(b[i], b[i - 1] + min_len)
    for i in range(len(b) - 2, 0, -1):
        b[i] = min(b[i], b[i + 1] - min_len)
    return b


def segments_uniform(L: int, M: int) -> np.ndarray:
    return np.round(np.linspace(0, L, M + 1)).astype(int)


def segments_mass(profile: np.ndarray, M: int, min_len: int = 1) -> np.ndarray:
    L = len(profile)
    c = np.concatenate([[0.0], np.cumsum(profile)])
    b = np.searchsorted(c, np.linspace(0, c[-1], M + 1))
    return _enforce_min_len(b, L, min_len)


def segments_peaks(profile: np.ndarray, M: int, min_len: int = 2, smooth: int = 3) -> np.ndarray:
    L = len(profile)
    p = np.convolve(profile, np.ones(smooth) / smooth, mode="same") if smooth > 1 else profile
    is_max = np.r_[False, (p[1:-1] >= p[:-2]) & (p[1:-1] >= p[2:]), False]
    chosen = []
    for t in np.argsort(-p):
        if len(chosen) == M - 1:
            break
        if not is_max[t] or t < min_len or t > L - min_len:
            continue
        if all(abs(t - s) >= min_len for s in chosen):
            chosen.append(int(t))
    b = sorted([0, L] + chosen)
    while len(b) < M + 1:                             # too few peaks: split the longest segment
        i = int(np.argmax(np.diff(b)))
        b.insert(i + 1, (b[i] + b[i + 1]) // 2)
    return _enforce_min_len(np.array(b), L, 1)


def segments_mmd(series: np.ndarray, M: int, min_len: int = 4) -> np.ndarray:
    """
    Greedy binary segmentation of one channel by kernel MMD (RBF, median heuristic)
    on (value, first difference): split the segment/point with the largest
    n1*n2/n * MMD^2 until M segments. Simplified re-implementation of the
    segmentation step of GroupSegment-SHAP; it uses a fixed segment budget instead
    of the paper's significance threshold so that all methods get the same M.
    """
    L = len(series)
    z = (series - series.mean()) / (series.std() + 1e-8)
    feats = np.stack([z, np.diff(z, prepend=z[0])], 1)
    d2 = ((feats[:, None] - feats[None]) ** 2).sum(-1)
    med = np.median(d2[d2 > 0]) if np.any(d2 > 0) else 1.0
    K = np.exp(-d2 / med)

    def best_split(a, b):
        best = (-np.inf, None)
        for t in range(a + min_len, b - min_len + 1):
            n1, n2 = t - a, b - t
            mmd = K[a:t, a:t].mean() + K[t:b, t:b].mean() - 2 * K[a:t, t:b].mean()
            score = mmd * n1 * n2 / (n1 + n2)
            if score > best[0]:
                best = (score, t)
        return best

    segs = {(0, L): best_split(0, L)}
    while len(segs) < M:
        (a, b), (score, t) = max(segs.items(), key=lambda kv: kv[1][0])
        if t is None:
            break
        del segs[(a, b)]
        segs[(a, t)] = best_split(a, t)
        segs[(t, b)] = best_split(t, b)
    return np.array(sorted({0, L} | {s for s, _ in segs}))


def player_map_shared(boundaries: np.ndarray, C: int) -> np.ndarray:
    """Same time segments for every channel: player = c * M + segment."""
    M = len(boundaries) - 1
    seg = np.repeat(np.arange(M), np.diff(boundaries))
    return np.arange(C)[:, None] * M + seg[None]


def player_map_per_channel(boundaries: list) -> np.ndarray:
    """Different segments per channel: consecutive player ids channel after channel."""
    rows, offset = [], 0
    for b in boundaries:
        rows.append(offset + np.repeat(np.arange(len(b) - 1), np.diff(b)))
        offset += len(b) - 1
    return np.stack(rows)


class SegmentShap:
    """
    KernelSHAP over arbitrary groups of (channel, time) cells for a scalar forecast.

    By default a coalition is evaluated as f(masker(x, keep)). Pass value_fn(x, keep)
    -> tensor [n] to remove players some other way (e.g. selective-scan masking).
    """

    def __init__(self, f, masker: str = "mean", baseline: torch.Tensor | None = None,
                 nsamples: int = 1024, batch_size: int = 512, seed: int = 0, value_fn=None):
        mask_fn = MASKERS[masker]
        self.value_fn = value_fn or (lambda x, keep: f(mask_fn(x, keep, baseline)))
        self.nsamples = nsamples
        self.batch_size = batch_size
        self.seed = seed

    def explain_map(self, x: torch.Tensor, player_map: np.ndarray) -> dict:
        """x [C, L]; player_map [C, L] ints in 0..P-1."""
        P = int(player_map.max()) + 1
        pm = torch.as_tensor(player_map, device=x.device)
        n_evals = [0]

        @torch.no_grad()
        def g(Z: np.ndarray) -> np.ndarray:
            keep = torch.as_tensor(Z, dtype=torch.bool, device=x.device)[:, pm]   # [n, C, L]
            n_evals[0] += len(Z)
            return torch.cat([self.value_fn(x, keep[i:i + self.batch_size])
                              for i in range(0, len(keep), self.batch_size)]).cpu().numpy()

        np.random.seed(self.seed)
        explainer = shap.KernelExplainer(g, np.zeros((1, P)))
        phi = np.asarray(explainer.shap_values(np.ones((1, P)), nsamples=self.nsamples,
                                               l1_reg=False, silent=True)).reshape(P)
        base = float(np.asarray(explainer.expected_value).ravel()[0])
        fx = float(g(np.ones((1, P)))[0])
        counts = np.bincount(player_map.ravel(), minlength=P)
        cell = (phi / counts)[player_map]                                  # spread evenly over each group
        return {"phi": phi, "cell": cell, "player_map": player_map, "base": base, "fx": fx,
                "efficiency_gap": abs(phi.sum() - (fx - base)), "n_evals": n_evals[0]}

    def explain(self, x: torch.Tensor, boundaries: np.ndarray) -> dict:
        """Shared time segments for all channels; boundaries [M+1] with b[0]=0, b[-1]=L."""
        C = x.shape[0]
        res = self.explain_map(x, player_map_shared(boundaries, C))
        res["phi"] = res["phi"].reshape(C, len(boundaries) - 1)
        res["boundaries"] = np.asarray(boundaries)
        return res
