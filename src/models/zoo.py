"""
Forecasters for the XAI benchmark v2 (plan §12, protocol v2). Every model maps
x [B, C, L] -> y [B, C, H] and uses PriorCast's PurePyTorchMamba, so the same XAI
code (capture_internals, lrp_mode) runs on all of them.

  plain         PlainMamba, head flatten      Mamba scans time steps      (src/models/plain_mamba.py)
  smamba        S-Mamba (Wang et al. 2025)    bidirectional scan over variates
  itransformer  iTransformer (Liu et al. 2024) S-Mamba's non-Mamba twin: attention over variates
  timemachine   TimeMachine (Ahamed & Cheng 2024) scans channels (ch_ind=0) or embedding dims (ch_ind=1)

S-Mamba / iTransformer follow the paper and https://github.com/wzhwzhwzh0921/S-D-Mamba
(no licence, so re-implemented, not copied): inverted embedding Linear(L -> d_model)
per variate, encoder layer x = norm1(x + mixer(x)), norm2(x + FFN(x)), final LayerNorm,
projector Linear(d_model -> H). S-Mamba's mixer is mamba(x) + flip(mamba_r(flip(x)))
with d_conv 2, expand 1.

TimeMachine is ported from https://github.com/Atik-Ahamed/TimeMachine
(TimeMachine_supervised/models/TimeMachine.py, Apache-2.0): two embedding scales
n1, n2, four Mambas, residual connections.

Deviations, applied to every model alike: optional instance normalisation (`norm`,
off on the stationary synthetic tasks), d_state 16, GELU as nn.GELU modules (the
LRP rules in src/xai/mamba_lrp.py patch modules, not functionals).
"""

import torch
import torch.nn as nn

from src.models.plain_mamba import PlainMamba, RevIN
from third_party.priorcast.mamba_block import PurePyTorchMamba


class InstanceNorm(RevIN):
    """Non-affine RevIN (S-Mamba's / TimeMachine's use_norm): weight 1, bias 0, not learned."""

    def __init__(self, n_channels: int, eps: float = 1e-5):
        super().__init__(n_channels, eps)
        del self.weight, self.bias
        self.register_buffer("weight", torch.ones(n_channels, 1))
        self.register_buffer("bias", torch.zeros(n_channels, 1))


class _InvertedLayer(nn.Module):
    def __init__(self, mixer: str, d_model: int, d_ff: int, d_state: int, n_heads: int, dropout: float):
        super().__init__()
        self.mixer = mixer
        if mixer == "mamba":
            self.fwd = PurePyTorchMamba(d_model, d_state, d_conv=2, expand=1)
            self.bwd = PurePyTorchMamba(d_model, d_state, d_conv=2, expand=1)
        else:
            self.attn = nn.MultiheadAttention(d_model, n_heads, dropout=dropout, batch_first=True)
        self.drop = nn.Dropout(dropout)
        self.norm1, self.norm2 = nn.LayerNorm(d_model), nn.LayerNorm(d_model)
        self.ffn = nn.Sequential(nn.Linear(d_model, d_ff), nn.GELU(), nn.Dropout(dropout),
                                 nn.Linear(d_ff, d_model), nn.Dropout(dropout))

    def forward(self, x):
        if self.mixer == "mamba":
            new = self.fwd(x) + self.bwd(x.flip(1)).flip(1)           # S-Mamba adds without dropout
        else:
            new = self.drop(self.attn(x, x, x, need_weights=False)[0])
        x = self.norm1(x + new)
        return self.norm2(x + self.ffn(x))


class InvertedForecaster(nn.Module):
    """Variates as tokens. mixer="mamba" -> S-Mamba, mixer="attention" -> iTransformer."""

    def __init__(self, n_channels: int, seq_len: int, pred_len: int, mixer: str = "mamba",
                 d_model: int = 128, d_ff: int = 128, n_layers: int = 2, d_state: int = 16,
                 n_heads: int = 8, dropout: float = 0.1, norm: bool = False):
        super().__init__()
        self.n_channels, self.seq_len, self.pred_len = n_channels, seq_len, pred_len
        self.revin = InstanceNorm(n_channels) if norm else None
        self.embed = nn.Linear(seq_len, d_model)
        self.drop = nn.Dropout(dropout)
        self.layers = nn.ModuleList([_InvertedLayer(mixer, d_model, d_ff, d_state, n_heads, dropout)
                                     for _ in range(n_layers)])
        self.norm = nn.LayerNorm(d_model)
        self.projector = nn.Linear(d_model, pred_len)

    def forward(self, x):
        if self.revin is not None:
            x = self.revin.norm(x)
        h = self.drop(self.embed(x))                                     # [B, C, d_model]
        for layer in self.layers:
            h = layer(h)
        y = self.projector(self.norm(h))                                 # [B, C, H]
        return self.revin.denorm(y) if self.revin is not None else y


class TimeMachine(nn.Module):
    def __init__(self, n_channels: int, seq_len: int, pred_len: int, n1: int = 256, n2: int = 128,
                 d_state: int = 16, d_conv: int = 2, expand: int = 1, ch_ind: bool = False,
                 residual: bool = True, dropout: float = 0.05, norm: bool = False):
        super().__init__()
        self.n_channels, self.seq_len, self.pred_len = n_channels, seq_len, pred_len
        self.ch_ind, self.residual = ch_ind, residual
        self.revin = RevIN(n_channels) if norm else None
        self.lin1, self.dropout1 = nn.Linear(seq_len, n1), nn.Dropout(dropout)
        self.lin2, self.dropout2 = nn.Linear(n1, n2), nn.Dropout(dropout)
        d1, d2 = (1, 1) if ch_ind else (n2, n1)
        mamba = lambda d: PurePyTorchMamba(d, d_state, d_conv=d_conv, expand=expand)
        self.mamba1, self.mamba2, self.mamba3, self.mamba4 = mamba(d1), mamba(n2), mamba(n1), mamba(d2)
        self.lin3 = nn.Linear(n2, n1)
        self.lin4 = nn.Linear(2 * n1, pred_len)

    def _scan_dims(self, mamba, x):
        """Channel-independent mode scans the embedding dimension (tokens of width 1)."""
        return mamba(x.transpose(1, 2)).transpose(1, 2) if self.ch_ind else mamba(x)

    def forward(self, x):
        if self.revin is not None:
            x = self.revin.norm(x)
        B = x.shape[0]
        if self.ch_ind:
            x = x.reshape(B * self.n_channels, 1, self.seq_len)
        x = self.lin1(x)                                                 # [B, C, n1] or [B*C, 1, n1]
        x_res1 = x
        x = self.dropout1(x)
        x4 = self._scan_dims(self.mamba4, x) + self.mamba3(x)
        x = self.lin2(x)
        x_res2 = x
        x = self.dropout2(x)
        x = self._scan_dims(self.mamba1, x) + self.mamba2(x) + (x_res2 if self.residual else 0)
        x = self.lin3(x)
        if self.residual:
            x = x + x_res1
        y = self.lin4(torch.cat([x, x4], dim=-1)).reshape(B, self.n_channels, self.pred_len)
        return self.revin.denorm(y) if self.revin is not None else y


MODELS = ["plain", "smamba", "itransformer", "timemachine"]
SCAN_AXIS = {"plain": "time", "smamba": "variate", "itransformer": "none (attention)", "timemachine": "channel"}


def build_model(name: str, n_channels: int, seq_len: int, pred_len: int, norm: bool = False) -> nn.Module:
    if name == "plain":
        return PlainMamba(n_channels, seq_len, pred_len, d_model=64, n_layers=2, head="flatten", revin=norm)
    if name == "smamba":
        return InvertedForecaster(n_channels, seq_len, pred_len, mixer="mamba", norm=norm)
    if name == "itransformer":
        return InvertedForecaster(n_channels, seq_len, pred_len, mixer="attention", norm=norm)
    if name == "timemachine":
        return TimeMachine(n_channels, seq_len, pred_len, norm=norm)
    raise ValueError(f"unknown model {name!r}")
