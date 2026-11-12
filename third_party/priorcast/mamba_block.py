"""
M-Mamba: channel-independent temporal Mamba block.

Each channel's patch sequence is processed independently through a Mamba SSM
layer, capturing within-channel temporal dependencies with linear complexity.

Input/output shape: [B, C, N, d_model]

The block is structured as:
  LayerNorm → Mamba(d_model) → residual
  LayerNorm → FFN(d_model, d_ff) → residual

Backend selection (automatic):
  1. mamba-ssm (CUDA fused kernels) — fastest, requires compiled mamba-ssm package
  2. PurePyTorchMamba — pure-torch selective SSM, runs on any hardware/GPU
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import math

# ---------------------------------------------------------------------------
# Try to import the fast mamba-ssm kernel; fall back to pure PyTorch.
# ---------------------------------------------------------------------------
try:
    from mamba_ssm import Mamba as _MambaFast
    _MAMBA_SSM_AVAILABLE = True
except ImportError:
    _MAMBA_SSM_AVAILABLE = False


class PurePyTorchMamba(nn.Module):
    """
    Selective State Space Model (Mamba) implemented entirely in PyTorch.

    Matches the Mamba-1 interface: input [B, L, d_model] → output [B, L, d_model].
    Uses a sequential scan (O(L·d_state) memory, O(L·d_model·d_state) flops).
    Slower than the CUDA-fused kernel but correct on any hardware.

    Reference: Gu & Dao (2023), "Mamba: Linear-Time Sequence Modeling with
    Selective State Spaces."
    """

    def __init__(self, d_model: int, d_state: int = 16, d_conv: int = 4, expand: int = 2,
                 dt_min: float = 1e-3, dt_max: float = 0.1):
        super().__init__()
        self.d_model = d_model
        self.d_state = d_state
        self.d_conv = d_conv
        self.d_inner = d_model * expand
        # Low-rank delta projection, same as reference Mamba (dt_rank = d_model/16)
        self.dt_rank = max(1, math.ceil(d_model / 16))

        # Input projection: maps d_model → 2*d_inner (x and z)
        self.in_proj = nn.Linear(d_model, self.d_inner * 2, bias=False)

        # Depthwise conv over the sequence (causal, groups=d_inner)
        self.conv1d = nn.Conv1d(
            self.d_inner, self.d_inner,
            kernel_size=d_conv, padding=d_conv - 1,
            groups=self.d_inner, bias=True,
        )

        # SSM projections (input-dependent B, C, delta)
        self.x_proj = nn.Linear(self.d_inner, self.dt_rank + d_state * 2, bias=False)
        self.dt_proj = nn.Linear(self.dt_rank, self.d_inner, bias=True)

        # SSM parameters
        A = torch.arange(1, d_state + 1, dtype=torch.float32).unsqueeze(0).expand(self.d_inner, -1)
        self.A_log = nn.Parameter(torch.log(A))
        self.D = nn.Parameter(torch.ones(self.d_inner))

        # Output projection
        self.out_proj = nn.Linear(self.d_inner, d_model, bias=False)

        # Reference Mamba delta initialisation: softplus(dt_bias) is distributed
        # log-uniformly in [dt_min, dt_max], so at init the SSM has slow-decaying
        # (long-memory) states.  Default zero-bias gives softplus(0)≈0.69, which
        # makes every state forget within a few tokens.
        dt_init_std = self.dt_rank ** -0.5
        nn.init.uniform_(self.dt_proj.weight, -dt_init_std, dt_init_std)
        dt = torch.exp(
            torch.rand(self.d_inner) * (math.log(dt_max) - math.log(dt_min)) + math.log(dt_min)
        ).clamp(min=1e-4)
        inv_dt = dt + torch.log(-torch.expm1(-dt))  # inverse of softplus
        with torch.no_grad():
            self.dt_proj.bias.copy_(inv_dt)

    def _scan_chunk(self, delta_c, B_c, C_c, u_c, h):
        """
        Recurrent scan over one chunk of the sequence.
        delta_c: [B, c, d_inner], B_c/C_c: [B, c, d_state], u_c: [B, c, d_inner]
        h:       [B, d_inner, d_state] carry state
        The scan runs in fp32 regardless of autocast — bf16 accumulation over
        the recurrence drifts (reference Mamba also keeps the scan in fp32).
        """
        delta_c = delta_c.float()
        B_c, C_c, u_c = B_c.float(), C_c.float(), u_c.float()
        A = -torch.exp(self.A_log.float())                          # [d_inner, d_state]
        dA = torch.exp(delta_c.unsqueeze(-1) * A)                   # [B, c, d_inner, d_state]
        dBu = delta_c.unsqueeze(-1) * B_c.unsqueeze(2) * u_c.unsqueeze(-1)
        ys = []
        for t in range(delta_c.shape[1]):
            h = dA[:, t] * h + dBu[:, t]                            # [B, d_inner, d_state]
            ys.append((h * C_c[:, t].unsqueeze(1)).sum(-1))         # [B, d_inner]
        return torch.stack(ys, dim=1), h

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x: [B, L, d_model] → [B, L, d_model]"""
        B, L, _ = x.shape

        xz = self.in_proj(x)                            # [B, L, 2*d_inner]
        x_in, z = xz.chunk(2, dim=-1)                  # each [B, L, d_inner]

        # Causal depthwise conv
        x_conv = self.conv1d(x_in.transpose(1, 2))[:, :, :L].transpose(1, 2)
        x_conv = F.silu(x_conv)                         # [B, L, d_inner]

        # Input-dependent SSM parameters
        x_proj_out = self.x_proj(x_conv)                # [B, L, dt_rank + 2*d_state]
        delta_raw = x_proj_out[..., :self.dt_rank]      # [B, L, dt_rank]
        B_ssm = x_proj_out[..., self.dt_rank:self.dt_rank + self.d_state]
        C_ssm = x_proj_out[..., self.dt_rank + self.d_state:]

        delta = F.softplus(self.dt_proj(delta_raw))     # [B, L, d_inner]

        # Sequential scan, discretised chunk-by-chunk so the [B, chunk, d_inner,
        # d_state] tensors stay bounded (materialising the full L at once needs
        # B*L*d_inner*d_state floats and OOMs for large B*C).  During training
        # each chunk is gradient-checkpointed: dA/dBu are recomputed in backward
        # instead of stored.  Memory per layer = (L/chunk) carry states stored at
        # chunk boundaries + 2*chunk steps of transient recompute, so the chunk
        # must be neither tiny (boundary states dominate) nor huge (recompute
        # tensors dominate); ~16 balances both for L≈30-160.
        chunk = max(8, min(L, 16))

        use_ckpt = self.training and torch.is_grad_enabled()
        h = torch.zeros(B, self.d_inner, self.d_state, device=x.device, dtype=torch.float32)
        ys = []
        for s in range(0, L, chunk):
            e = min(s + chunk, L)
            args = (delta[:, s:e], B_ssm[:, s:e], C_ssm[:, s:e], x_conv[:, s:e], h)
            if use_ckpt:
                y_c, h = torch.utils.checkpoint.checkpoint(
                    self._scan_chunk, *args, use_reentrant=False)
            else:
                y_c, h = self._scan_chunk(*args)
            ys.append(y_c)
        y = torch.cat(ys, dim=1).to(x_conv.dtype)      # [B, L, d_inner]
        y = y + x_conv * self.D

        # Gate with z
        y = y * F.silu(z)

        return self.out_proj(y)                         # [B, L, d_model]


def _build_mamba(d_model: int, d_state: int, d_conv: int, expand: int) -> nn.Module:
    """Return the fastest available Mamba implementation."""
    if _MAMBA_SSM_AVAILABLE:
        return _MambaFast(d_model=d_model, d_state=d_state, d_conv=d_conv, expand=expand)
    return PurePyTorchMamba(d_model=d_model, d_state=d_state, d_conv=d_conv, expand=expand)


class MMambaBlock(nn.Module):
    def __init__(self, d_model: int, d_state: int = 16, d_conv: int = 4, expand: int = 2):
        super().__init__()
        self.norm1 = nn.LayerNorm(d_model)
        self.mamba = _build_mamba(d_model, d_state, d_conv, expand)
        self.norm2 = nn.LayerNorm(d_model)
        d_ff = d_model * 4
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Linear(d_ff, d_model),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        x: [B, C, N, d_model]
        Returns: [B, C, N, d_model]
        """
        B, C, N, D = x.shape

        # Merge batch and channel dims so Mamba sees [B*C, N, d_model]
        x_flat = x.reshape(B * C, N, D)

        # Mamba branch
        x_flat = x_flat + self.mamba(self.norm1(x_flat))

        # FFN branch
        x_flat = x_flat + self.ffn(self.norm2(x_flat))

        return x_flat.reshape(B, C, N, D)
