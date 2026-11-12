"""
Expose the selective-SSM internals (delta, B, C) of PurePyTorchMamba layers.

PriorCast's PurePyTorchMamba keeps delta/B/C as local variables in forward().
Instead of editing the vendored file we capture them with forward hooks on the
two projections that produce them:

    x_proj  -> [dt_raw | B | C]          (B, C read directly)
    dt_proj -> pre-softplus delta        (delta = softplus(output))

The input of x_proj is the scan input u (post-conv, post-SiLU), which together
with delta/B/C is enough to rebuild Mamba's hidden attention (Ali et al., 2024).

Hooks only fire on the pure-PyTorch backend. The fused mamba_ssm kernel reads
the projection weights without calling the modules, so XAI must run on a
PurePyTorchMamba copy of the trained weights (plan §2).
"""

from dataclasses import dataclass, field

import torch
import torch.nn as nn
import torch.nn.functional as F

from third_party.priorcast.mamba_block import PurePyTorchMamba


@dataclass
class LayerInternals:
    delta: torch.Tensor   # [B, L, d_inner]
    B: torch.Tensor       # [B, L, d_state]
    C: torch.Tensor       # [B, L, d_state]
    u: torch.Tensor       # [B, L, d_inner]  scan input
    A: torch.Tensor       # [d_inner, d_state]  = -exp(A_log)


@dataclass
class MambaInternals:
    layers: list = field(default_factory=list)   # one LayerInternals per Mamba layer, in call order


def mamba_layers(model: nn.Module) -> list:
    layers = [m for m in model.modules() if isinstance(m, PurePyTorchMamba)]
    if not layers:
        raise RuntimeError(
            "No PurePyTorchMamba layers found. If the model was built with mamba_ssm, "
            "load its weights into a pure-PyTorch copy before extracting internals.")
    return layers


class capture_internals:
    """
    Context manager that records delta/B/C of every PurePyTorchMamba layer.

        with capture_internals(model) as internals:
            y = model(x)
        internals.layers[0].delta   # [B, L, d_inner]

    Tensors are detached by default; pass detach=False to keep them in the graph.
    """

    def __init__(self, model: nn.Module, detach: bool = True):
        self.layers = mamba_layers(model)
        self.detach = detach
        self.internals = MambaInternals()
        self._handles = []
        self._pending = {}

    def _x_proj_hook(self, layer):
        def hook(_module, inp, out):
            r, s = layer.dt_rank, layer.d_state
            self._pending[id(layer)] = (out[..., r:r + s], out[..., r + s:], inp[0])
        return hook

    def _dt_proj_hook(self, layer):
        def hook(_module, _inp, out):
            B_ssm, C_ssm, u = self._pending.pop(id(layer))
            delta = F.softplus(out)
            A = -torch.exp(layer.A_log.float())
            if self.detach:
                delta, B_ssm, C_ssm, u, A = (t.detach() for t in (delta, B_ssm, C_ssm, u, A))
            self.internals.layers.append(LayerInternals(delta, B_ssm, C_ssm, u, A))
        return hook

    def __enter__(self) -> MambaInternals:
        for layer in self.layers:
            self._handles.append(layer.x_proj.register_forward_hook(self._x_proj_hook(layer)))
            self._handles.append(layer.dt_proj.register_forward_hook(self._dt_proj_hook(layer)))
        return self.internals

    def __exit__(self, *exc):
        for h in self._handles:
            h.remove()
        self._handles.clear()
        return False


def hidden_attention_row(li: LayerInternals, t: int) -> torch.Tensor:
    """
    alpha[:, s, d] for s <= t, such that the scan output (before the D skip and
    the z gate) is  y_t[d] = sum_s alpha[s, d] * u_s[d]:

        alpha[t, s, d] = sum_n C_t[n] * exp(A[d, n] * sum_{k=s+1..t} delta_k[d]) * delta_s[d] * B_s[n]

    which is PurePyTorchMamba's recurrence h_t = exp(delta_t A) h_{t-1} + delta_t B_t u_t
    unrolled. Returns [B, t+1, d_inner].
    """
    S = li.delta.cumsum(1)                                          # [B, L, D]
    decay = torch.exp((S[:, t:t + 1] - S[:, :t + 1]).unsqueeze(-1) * li.A)   # [B, t+1, D, N]
    w = (li.B[:, :t + 1].unsqueeze(2) * li.C[:, t].view(-1, 1, 1, li.C.shape[-1]))  # [B, t+1, 1, N]
    return (decay * w).sum(-1) * li.delta[:, :t + 1]


class scan_mask:
    """
    Selective-scan masking: remove time steps from every Mamba layer by forcing
    delta_s = 0 (state is held, nothing is written) and zeroing the conv input at s
    (so s does not leak into neighbours through the causal conv).

        with scan_mask(model, keep):      # keep [n, L] bool, n = batch size
            y = model(x)

    This does NOT cut the residual stream: the token at s still reaches the output
    through x + mamba(x) at position s. Removal is complete only when the read-out
    never looks at a masked position (e.g. a last-state head with the final step kept),
    and only without RevIN, whose statistics see the whole window.
    """

    def __init__(self, model: nn.Module, keep: torch.Tensor):
        self.layers = mamba_layers(model)
        self.keep = keep
        self._handles = []

    def __enter__(self):
        drop = ~self.keep                                           # [n, L]
        for layer in self.layers:
            def conv_pre(_m, inp, drop=drop):
                x = inp[0]                                          # [n, d_inner, L]
                return (x.masked_fill(drop.unsqueeze(1), 0.0),)

            def dt_post(_m, _inp, out, drop=drop):                  # out [n, L, d_inner], pre-softplus
                return out.masked_fill(drop.unsqueeze(-1), -1e4)

            self._handles.append(layer.conv1d.register_forward_pre_hook(conv_pre))
            self._handles.append(layer.dt_proj.register_forward_hook(dt_post))
        return self

    def __exit__(self, *exc):
        for h in self._handles:
            h.remove()
        self._handles.clear()
        return False
