import pytest
import torch

from src.models.mamba_ext import capture_internals
from src.models.zoo import MODELS, TimeMachine, build_model
from src.xai.mamba_lrp import grad_x_input, lrp_mode, mamba_lrp

torch.manual_seed(0)
C, L, H = 5, 24, 6
MAMBA_MODELS = [m for m in MODELS if m != "itransformer"]


def _zero_biases(m):
    with torch.no_grad():
        for name, p in m.named_parameters():
            if name.endswith("bias") and "dt_proj" not in name:
                p.zero_()
    return m


@pytest.mark.parametrize("name", MODELS)
@pytest.mark.parametrize("norm", [False, True])
def test_shapes_and_gradients(name, norm):
    m = build_model(name, C, L, H, norm=norm)
    x = torch.randn(3, C, L)
    y = m(x)
    assert y.shape == (3, C, H)
    y.sum().backward()
    assert all(p.grad is not None for p in m.parameters() if p.requires_grad)


def test_timemachine_channel_independent_mode():
    m = TimeMachine(C, L, H, n1=16, n2=8, ch_ind=True).eval()
    x = torch.randn(2, C, L)
    x2 = x.clone()
    x2[:, 1] = torch.randn(2, L)                      # other channels must not change
    with torch.no_grad():
        d = (m(x) - m(x2)).abs().amax(-1)
    assert d[:, 1].min() > 0 and d[:, [0, 2, 3, 4]].max() == 0


def test_inverted_models_are_variate_permutation_equivariant_only_with_attention():
    x = torch.randn(2, C, L)
    perm = torch.tensor([3, 0, 4, 1, 2])
    with torch.no_grad():
        it = build_model("itransformer", C, L, H).eval()
        assert torch.allclose(it(x)[:, perm], it(x[:, perm]), atol=1e-5)
        sm = build_model("smamba", C, L, H).eval()
        assert not torch.allclose(sm(x)[:, perm], sm(x[:, perm]), atol=1e-5)   # scan order matters


@pytest.mark.parametrize("name", MAMBA_MODELS)
def test_internals_are_captured(name):
    m = build_model(name, C, L, H).eval()
    with torch.no_grad(), capture_internals(m) as internals:
        m(torch.randn(2, C, L))
    assert len(internals.layers) == sum(1 for _ in internals.layers) > 0


@pytest.mark.parametrize("name", MAMBA_MODELS)
@pytest.mark.parametrize("norm", [False, True])
def test_lrp_keeps_forward_and_conserves_without_biases(name, norm):
    m = build_model(name, C, L, H, norm=norm).eval()
    x = torch.randn(4, C, L)
    with torch.no_grad():
        y = m(x)
        with lrp_mode(m):
            assert torch.allclose(y, m(x), atol=1e-5)
    _zero_biases(m)
    f = lambda xs: m(xs)[:, -1].mean(-1)
    fx = f(x[:1]).item()
    R, _ = mamba_lrp(f, m, x[0])
    assert abs(R.sum() - fx) < 1e-4 * max(1.0, abs(fx))
    if not norm:
        gxi, _ = grad_x_input(f, x[0])
        assert abs(gxi.sum() - fx) > 0.05 * abs(fx)


def test_lrp_is_not_defined_for_the_attention_twin():
    with pytest.raises(RuntimeError):
        with lrp_mode(build_model("itransformer", C, L, H)):
            pass
