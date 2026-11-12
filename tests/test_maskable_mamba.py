import pytest
import torch

from src.models.maskable_mamba import MaskablePlainMamba, random_time_keep

torch.manual_seed(0)


def _model(mode, head="flatten"):
    m = MaskablePlainMamba(3, 32, 8, d_model=16, n_layers=2, head=head, revin=False, mask_mode=mode).eval()
    with torch.no_grad():
        m.mask_token.normal_()
    return m


@pytest.mark.parametrize("mode", ["skip", "token"])
def test_full_keep_is_plain_forward(mode):
    m = _model(mode)
    x = torch.randn(4, 3, 32)
    with torch.no_grad():
        assert torch.allclose(m(x), m(x, torch.ones(4, 32, dtype=torch.bool)), atol=1e-6)


@pytest.mark.parametrize("mode", ["skip", "token"])
@pytest.mark.parametrize("head", ["flatten", "last"])
def test_removed_steps_do_not_leak(mode, head):
    m = _model(mode, head)
    x1 = torch.randn(1, 3, 32)
    x2 = x1.clone()
    x2[..., 5:12] = torch.randn(3, 7)
    keep = torch.ones(1, 32, dtype=torch.bool)
    keep[:, 5:12] = False
    with torch.no_grad():
        assert not torch.allclose(m(x1), m(x2))
        assert torch.allclose(m(x1, keep), m(x2, keep), atol=1e-6)


def test_skip_and_token_differ_only_when_masking():
    a, b = _model("skip"), _model("token")
    b.load_state_dict(a.state_dict())
    x = torch.randn(2, 3, 32)
    keep = torch.ones(2, 32, dtype=torch.bool)
    keep[:, 8:16] = False
    with torch.no_grad():
        assert torch.allclose(a(x), b(x))
        assert not torch.allclose(a(x, keep), b(x, keep))


def test_random_time_keep():
    g = torch.Generator().manual_seed(0)
    keep = random_time_keep(4000, 96, "cpu", p_clean=0.5, generator=g)
    assert keep.shape == (4000, 96) and keep.dtype == torch.bool
    full = keep.all(1).float().mean().item()
    assert 0.5 < full < 0.62                                   # clean half + masked samples that kept everything
    masked = keep[~keep.all(1)]
    runs = (masked[:, 1:] != masked[:, :-1]).sum(1)            # segment structure: at most 15 switches
    assert runs.max() <= 15
    assert (~keep).all(1).any()                                # empty coalition occurs
