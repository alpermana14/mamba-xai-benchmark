import pytest
import torch

from src.models.plain_mamba import PlainMamba
from src.xai.mamba_lrp import grad_x_input, lrp_mode, mamba_lrp

torch.manual_seed(0)


def _model(**kw):
    return PlainMamba(n_channels=3, seq_len=32, pred_len=8, d_model=16, n_layers=2, **kw).eval()


def _zero_biases(m):
    """All biases except dt_proj's, which only feeds delta (constant under the LRP rules)."""
    with torch.no_grad():
        for name, p in m.named_parameters():
            if name.endswith("bias") and "dt_proj" not in name:
                p.zero_()
    return m


@pytest.mark.parametrize("kw", [dict(head="flatten", revin=False), dict(head="last", revin=False),
                                dict(head="flatten", revin=True)])
def test_lrp_mode_keeps_forward_value(kw):
    m = _model(**kw)
    x = torch.randn(4, 3, 32)
    with torch.no_grad():
        y = m(x)
        with lrp_mode(m):
            y_lrp = m(x)
    assert torch.allclose(y, y_lrp, atol=1e-5)
    assert all("forward" not in vars(mod) and "norm" not in vars(mod) for mod in m.modules())


def test_ssm_parameters_are_constant_under_lrp():
    m = _model()
    x = torch.randn(2, 3, 32)
    with lrp_mode(m):
        m(x).sum().backward()
    for blk in m.blocks:
        assert blk.mamba.dt_proj.weight.grad is None and blk.mamba.x_proj.weight.grad is None
    m.zero_grad()
    m(x).sum().backward()
    assert m.blocks[0].mamba.x_proj.weight.grad.abs().sum() > 0


@pytest.mark.parametrize("kw", [dict(head="flatten", revin=False), dict(head="last", revin=False),
                                dict(head="flatten", revin=True)])
def test_lrp_conserves_relevance_without_biases(kw):
    m = _zero_biases(_model(**kw))
    x = torch.randn(3, 32)
    f = lambda xs: m(xs)[:, 0].mean(-1)
    fx = f(x.unsqueeze(0)).item()
    R, n = mamba_lrp(f, m, x)
    assert n == 1 and R.shape == (3, 32)
    assert abs(R.sum() - fx) < 1e-4 * max(1.0, abs(fx))
    if not kw["revin"]:                              # with RevIN f is 1-homogeneous in x, so plain
        gxi, _ = grad_x_input(f, x)                  # Gradient x Input conserves as well (Euler)
        assert abs(gxi.sum() - fx) > 1e-3
