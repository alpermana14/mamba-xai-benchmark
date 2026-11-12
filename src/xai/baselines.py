"""
Cell-level attribution baselines: Integrated Gradients, GradientSHAP
(shap.GradientExplainer = Expected Gradients) and random.

Every function returns (attr [C, L] numpy, n_evals) where n_evals counts
forward(+backward) passes per explained window.
"""

import numpy as np
import shap
import torch
import torch.nn as nn


def integrated_gradients(f, x: torch.Tensor, baseline: torch.Tensor | None = None, steps: int = 32):
    if baseline is None:
        baseline = torch.zeros_like(x)
    alphas = (torch.arange(steps, dtype=x.dtype, device=x.device) + 0.5) / steps
    path = (baseline + alphas.view(-1, 1, 1) * (x - baseline)).requires_grad_(True)
    grads, = torch.autograd.grad(f(path).sum(), path)
    return ((x - baseline) * grads.mean(0)).detach().cpu().numpy(), steps


class _Scalar(nn.Module):
    def __init__(self, f):
        super().__init__()
        self.f = f

    def forward(self, x):
        return self.f(x).unsqueeze(-1)


def gradient_shap(f, model: nn.Module, x: torch.Tensor, background: torch.Tensor, nsamples: int = 200,
                  seed: int = 0):
    """model is only passed so shap can find its parameters / device."""
    wrapper = _Scalar(f)
    wrapper.add_module("model", model)
    explainer = shap.GradientExplainer(wrapper, background)
    vals = explainer.shap_values(x.unsqueeze(0), nsamples=nsamples, rseed=seed)
    return np.asarray(vals).reshape(x.shape), nsamples


def random_attr(x: torch.Tensor, seed: int = 0):
    return np.random.default_rng(seed).standard_normal(tuple(x.shape)), 0
