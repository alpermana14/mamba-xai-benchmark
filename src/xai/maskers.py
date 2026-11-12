"""
Maskers: replace "absent" cells of one input window with uninformative values.

All functions take x [C, L] and keep [n, C, L] (True = cell present) and return
[n, C, L]. In standardised space the channel mean is 0, which is the default
baseline for "mean".
"""

import torch


def mask_mean(x: torch.Tensor, keep: torch.Tensor, baseline: torch.Tensor | None = None) -> torch.Tensor:
    if baseline is None:
        baseline = torch.zeros(x.shape[0], 1, dtype=x.dtype, device=x.device)
    return torch.where(keep, x.unsqueeze(0), baseline.view(1, -1, 1).expand_as(keep).to(x.dtype))


def mask_interp(x: torch.Tensor, keep: torch.Tensor, baseline: torch.Tensor | None = None) -> torch.Tensor:
    """Linear interpolation across each masked run between its nearest kept neighbours.

    A run touching the window edge is held at the one neighbour it has; a channel
    with no kept cell falls back to the baseline.
    """
    n, C, L = keep.shape
    xb = x.unsqueeze(0).expand(n, C, L)
    idx = torch.arange(L, device=x.device).view(1, 1, L).expand(n, C, L)
    prev = torch.where(keep, idx, torch.full_like(idx, -1)).cummax(-1).values
    nxt = torch.where(keep, idx, torch.full_like(idx, L)).flip(-1).cummin(-1).values.flip(-1)
    x_prev = xb.gather(-1, prev.clamp(min=0))
    x_next = xb.gather(-1, nxt.clamp(max=L - 1))
    span = (nxt - prev).clamp(min=1).to(x.dtype)
    w = (idx - prev).to(x.dtype) / span
    out = x_prev + w * (x_next - x_prev)
    out = torch.where(prev < 0, x_next, out)
    out = torch.where(nxt >= L, x_prev, out)
    fallback = mask_mean(x, torch.zeros_like(keep), baseline)
    out = torch.where((prev < 0) & (nxt >= L), fallback, out)
    return torch.where(keep, xb, out)


MASKERS = {"mean": mask_mean, "interp": mask_interp}
