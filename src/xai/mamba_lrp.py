"""
MambaLRP (Jafari et al., NeurIPS 2024) for PlainMamba, implemented as Gradient x Input
on a forward pass that detaches the tensors named by the LRP rules (their Sec. 4.4):

    SiLU / GELU        x * [act(x) / x]_cst                 (only the gate factor is constant)
    selective SSM      delta, B, C constant -> A_bar, B_bar, C constant, relevance flows through u
    gate y * silu(z)   half rule: 0.5 * (y g) + 0.5 * [y g]_cst
    LayerNorm, RevIN   (x - mean) / [std]_cst                (LN-rule)
    linear, conv1d     LRP-0 = plain gradient (biases absorb some relevance)

The forward value is unchanged; only the backward pass differs.

    with lrp_mode(model):
        ...                     # any forward/backward here follows the LRP rules
    R, _ = mamba_lrp(f, model, x)
"""

import types

import torch
import torch.nn as nn
import torch.nn.functional as F

from src.models.mamba_ext import mamba_layers
from src.models.plain_mamba import RevIN


def _silu_cst(x):
    return x * torch.sigmoid(x).detach()


def _gelu_cst(x):
    return x * (0.5 * (1.0 + torch.erf(x * 0.5 ** 0.5))).detach()        # exact GELU = x * Phi(x)


def _mamba_forward(self, x):
    """PurePyTorchMamba.forward with the MambaLRP detaches (single scan, eval only)."""
    B, L, _ = x.shape
    x_in, z = self.in_proj(x).chunk(2, dim=-1)
    u = _silu_cst(self.conv1d(x_in.transpose(1, 2))[:, :, :L].transpose(1, 2))
    xp = self.x_proj(u)
    delta = F.softplus(self.dt_proj(xp[..., :self.dt_rank])).detach()
    B_ssm = xp[..., self.dt_rank:self.dt_rank + self.d_state].detach()
    C_ssm = xp[..., self.dt_rank + self.d_state:].detach()
    h0 = torch.zeros(B, self.d_inner, self.d_state, device=x.device, dtype=torch.float32)
    y, _ = self._scan_chunk(delta, B_ssm, C_ssm, u, h0)
    y = y.to(u.dtype) + u * self.D
    yg = y * _silu_cst(z)
    return self.out_proj(0.5 * yg + 0.5 * yg.detach())


def _layernorm_forward(self, x):
    mu = x.mean(-1, keepdim=True)
    std = (x.var(-1, keepdim=True, unbiased=False) + self.eps).sqrt()
    return (x - mu) / std.detach() * self.weight + self.bias


def _gelu_forward(self, x):
    if self.approximate != "none":
        raise NotImplementedError("tanh-approximate GELU")
    return _gelu_cst(x)


def _revin_norm(self, x):
    self._mean = x.mean(-1, keepdim=True)
    self._std = (x.var(-1, keepdim=True, unbiased=False) + self.eps).sqrt().detach()
    return (x - self._mean) / self._std * self.weight + self.bias


class lrp_mode:
    """Swap in the LRP forward passes of every Mamba layer, LayerNorm, GELU and RevIN."""

    def __init__(self, model: nn.Module):
        self.model = model
        self._patched = []

    def __enter__(self):
        mamba = set(map(id, mamba_layers(self.model)))
        for m in self.model.modules():
            if id(m) in mamba:
                self._patch(m, "forward", _mamba_forward)
            elif isinstance(m, nn.LayerNorm):
                self._patch(m, "forward", _layernorm_forward)
            elif isinstance(m, nn.GELU):
                self._patch(m, "forward", _gelu_forward)
            elif isinstance(m, RevIN):
                self._patch(m, "norm", _revin_norm)
            elif isinstance(m, (nn.SiLU, nn.ReLU, nn.Tanh, nn.Sigmoid, nn.Softmax)):
                raise NotImplementedError(f"no LRP rule for {type(m).__name__}")
        return self.model

    def _patch(self, m, name, fn):
        setattr(m, name, types.MethodType(fn, m))
        self._patched.append((m, name))

    def __exit__(self, *exc):
        for m, name in self._patched:
            delattr(m, name)
        self._patched.clear()
        return False


def grad_x_input(f, x: torch.Tensor):
    """x [C, L] -> (x * df/dx [C, L] numpy, n_evals)."""
    xi = x.unsqueeze(0).clone().requires_grad_(True)
    g, = torch.autograd.grad(f(xi).sum(), xi)
    return (xi * g)[0].detach().cpu().numpy(), 1


def mamba_lrp(f, model: nn.Module, x: torch.Tensor):
    """MambaLRP relevance of the scalar f(x) for one window x [C, L]."""
    with lrp_mode(model):
        return grad_x_input(f, x)
