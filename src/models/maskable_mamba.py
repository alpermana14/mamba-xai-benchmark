"""
PlainMamba that can be run on a subset of time steps (Exp B / H2, plan §12):
removed steps get a learned mask token, and in "skip" mode every Mamba layer also
gets delta = 0 there, so the state passes through the removed steps unchanged (the
Mamba analogue of SHAPformer's attention -inf). Trained with random masks, the model
sees removed inputs in-distribution, so model(x, keep) is a native value function
for Shapley values over time segments.

    model = MaskablePlainMamba(..., mask_mode="skip")
    y = model(x)                 # ordinary forecast
    y = model(x, keep)           # keep [B, L] bool, False = removed time step
"""

import torch
import torch.nn as nn

from src.models.mamba_ext import scan_mask
from src.models.plain_mamba import PlainMamba


class MaskablePlainMamba(PlainMamba):
    def __init__(self, *args, mask_mode: str = "skip", **kw):
        super().__init__(*args, **kw)
        if mask_mode not in ("skip", "token"):
            raise ValueError(f"unknown mask_mode {mask_mode!r}")
        if self.revin is not None:
            raise ValueError("RevIN statistics would see the removed steps")
        self.mask_mode = mask_mode
        self.mask_token = nn.Parameter(torch.zeros(self.embed.out_features))

    def forward(self, x: torch.Tensor, keep: torch.Tensor | None = None) -> torch.Tensor:
        if keep is None:
            return super().forward(x)
        h = self.embed(x.transpose(1, 2))                                   # [B, L, d_model]
        h = torch.where(keep.unsqueeze(-1), h, self.mask_token).unsqueeze(1)
        if self.mask_mode == "skip":
            with scan_mask(self, keep):
                for blk in self.blocks:
                    h = blk(h)
        else:
            for blk in self.blocks:
                h = blk(h)
        return self._readout(self.norm(h.squeeze(1)))

    def _readout(self, h):
        out = self.head(self.reduce(h).flatten(1)) if self.head_type == "flatten" else self.head(h[:, -1])
        return out.view(-1, self.n_channels, self.pred_len)


def random_time_keep(batch: int, L: int, device, p_clean: float = 0.5, M_choices=(4, 8, 16),
                     generator: torch.Generator | None = None) -> torch.Tensor:
    """
    Training masks: a fraction p_clean of samples is left whole; for the rest the window
    is cut into M equal segments (M drawn from M_choices), q ~ U(0, 1) is drawn per sample
    and each segment is removed with probability 1 - q, so every coalition size occurs.
    """
    g = dict(generator=generator, device=device)
    M = torch.as_tensor(M_choices, device=device)[torch.randint(len(M_choices), (batch,), **g)]
    seg = (torch.arange(L, device=device).unsqueeze(0) * M.unsqueeze(1)) // L          # [B, L]
    q = torch.rand(batch, 1, **g)
    drop = torch.rand(batch, max(M_choices), **g) >= q                                 # [B, M_max]
    keep = ~drop.gather(1, seg)
    clean = torch.rand(batch, **g) < p_clean
    keep[clean] = True
    return keep
