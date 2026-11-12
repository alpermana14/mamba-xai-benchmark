"""
Plain Mamba forecaster used to prototype SG-SHAP before HyMamba-X exists.

    x [B, C, L] -> (RevIN) -> Linear(C -> d_model) per time step
                -> N x MMambaBlock (unidirectional, pre-norm, FFN)
                -> head -> y [B, C, H]

Tokens are single time steps (no patching) so delta_t is defined per step, and
the channel-mixing embedding lets the model learn cross-channel lags.

head="flatten": PatchTST-style linear read-out over all L hidden states.
head="last":    read-out from the final hidden state only, which forces the SSM
                state (and therefore delta) to carry the information.
"""

import torch
import torch.nn as nn

from third_party.priorcast.mamba_block import MMambaBlock


class RevIN(nn.Module):
    """Instance normalisation over time, per channel (Kim et al., 2022)."""

    def __init__(self, n_channels: int, eps: float = 1e-5):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(n_channels, 1))
        self.bias = nn.Parameter(torch.zeros(n_channels, 1))

    def norm(self, x):
        self._mean = x.mean(-1, keepdim=True)
        self._std = (x.var(-1, keepdim=True, unbiased=False) + self.eps).sqrt()
        return (x - self._mean) / self._std * self.weight + self.bias

    def denorm(self, y):
        return (y - self.bias) / (self.weight + self.eps) * self._std + self._mean


class PlainMamba(nn.Module):
    def __init__(self, n_channels: int, seq_len: int, pred_len: int,
                 d_model: int = 64, n_layers: int = 2, d_state: int = 16,
                 d_conv: int = 4, expand: int = 2, head: str = "flatten",
                 d_head: int = 16, revin: bool = True):
        super().__init__()
        self.n_channels, self.seq_len, self.pred_len = n_channels, seq_len, pred_len
        self.head_type = head
        self.revin = RevIN(n_channels) if revin else None
        self.embed = nn.Linear(n_channels, d_model)
        self.blocks = nn.ModuleList(
            [MMambaBlock(d_model, d_state, d_conv, expand) for _ in range(n_layers)])
        self.norm = nn.LayerNorm(d_model)
        if head == "flatten":
            self.reduce = nn.Linear(d_model, d_head)
            self.head = nn.Linear(seq_len * d_head, pred_len * n_channels)
        elif head == "last":
            self.head = nn.Linear(d_model, pred_len * n_channels)
        else:
            raise ValueError(f"unknown head {head!r}")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x: [B, C, L] -> [B, C, H]"""
        if self.revin is not None:
            x = self.revin.norm(x)
        h = self.embed(x.transpose(1, 2))            # [B, L, d_model]
        h = h.unsqueeze(1)                           # MMambaBlock expects [B, C, N, D]
        for blk in self.blocks:
            h = blk(h)
        h = self.norm(h.squeeze(1))                  # [B, L, d_model]
        if self.head_type == "flatten":
            out = self.head(self.reduce(h).flatten(1))
        else:
            out = self.head(h[:, -1])
        y = out.view(-1, self.n_channels, self.pred_len)
        if self.revin is not None:
            y = self.revin.denorm(y)
        return y
