import numpy as np
import pytest
import torch
import torch.nn.functional as F

from src.models.mamba_ext import capture_internals, hidden_attention_row, scan_mask
from src.models.plain_mamba import PlainMamba
from src.synthetic.gt_generator import GTConfig, GTSeries, LAG, EVT
from src.xai.maskers import mask_interp, mask_mean
from src.xai.sg_shap import (SegmentShap, delta_profile, hidden_attention_profile, player_map_per_channel,
                             segments_mass, segments_mmd, segments_peaks, segments_uniform)

torch.manual_seed(0)


def _model(**kw):
    return PlainMamba(n_channels=3, seq_len=32, pred_len=8, d_model=16, n_layers=2, **kw).eval()


def test_capture_internals_matches_recomputed_delta():
    m = _model()
    x = torch.randn(2, 3, 32)
    with capture_internals(m) as it:
        y = m(x)
    assert y.shape == (2, 3, 8)
    assert len(it.layers) == 2
    layer = m.blocks[0].mamba
    li = it.layers[0]
    assert li.delta.shape == (2, 32, layer.d_inner)
    assert li.B.shape == li.C.shape == (2, 32, layer.d_state)
    # recompute layer-0 delta by hand
    h = m.embed(m.revin.norm(x).transpose(1, 2))
    h = m.blocks[0].norm1(h)
    x_in, _ = layer.in_proj(h).chunk(2, dim=-1)
    xc = F.silu(layer.conv1d(x_in.transpose(1, 2))[:, :, :32].transpose(1, 2))
    dt = F.softplus(layer.dt_proj(layer.x_proj(xc)[..., :layer.dt_rank]))
    assert torch.allclose(dt, li.delta, atol=1e-6)
    assert torch.all(li.delta > 0)


def test_hidden_attention_reconstructs_scan():
    m = _model()
    x = torch.randn(2, 3, 32)
    with capture_internals(m) as it:
        m(x)
    layer, li = m.blocks[1].mamba, it.layers[1]
    assert li.u.shape == li.delta.shape
    h0 = torch.zeros(2, layer.d_inner, layer.d_state)
    y_scan, _ = layer._scan_chunk(li.delta, li.B, li.C, li.u, h0)        # [B, L, d_inner]
    for t in (0, 7, 31):
        y_t = (hidden_attention_row(li, t) * li.u[:, :t + 1]).sum(1)
        assert torch.allclose(y_t, y_scan[:, t], atol=1e-5)


def test_hidden_attention_profile_is_causal_distribution():
    m = _model(head="last", revin=False)
    readout = np.eye(32)[-1]
    p = hidden_attention_profile(m, torch.randn(3, 32), readout)
    assert p.shape == (32,) and np.all(p >= 0) and np.isclose(p.sum(), 1.0, atol=1e-5)


def test_scan_mask_removes_masked_steps_for_last_state_head():
    m = _model(head="last", revin=False)
    x1 = torch.randn(1, 3, 32)
    x2 = x1.clone()
    x2[..., 5:12] = torch.randn(3, 7)                       # differ only inside the masked span
    keep = torch.ones(1, 32, dtype=torch.bool)
    keep[:, 5:12] = False
    with torch.no_grad():
        assert not torch.allclose(m(x1), m(x2))
        with scan_mask(m, keep):
            y1, y2 = m(x1), m(x2)
    assert torch.allclose(y1, y2, atol=1e-6)


def test_hooks_removed_after_context():
    m = _model()
    with capture_internals(m):
        m(torch.randn(1, 3, 32))
    assert all(len(mod._forward_hooks) == 0 for mod in m.modules())


def test_mask_interp():
    x = torch.tensor([[0., 1., 2., 3., 4.], [5., 5., 5., 5., 5.]])
    keep = torch.tensor([[[1, 0, 0, 1, 1], [0, 0, 0, 0, 0]]], dtype=torch.bool)
    out = mask_interp(x, keep)
    assert torch.allclose(out[0, 0], torch.tensor([0., 1., 2., 3., 4.]))   # linear run is recovered
    assert torch.allclose(out[0, 1], torch.zeros(5))                       # all masked -> baseline 0
    keep = torch.tensor([[[0, 0, 1, 1, 0], [1, 1, 1, 1, 1]]], dtype=torch.bool)
    out = mask_interp(x, keep)
    assert torch.allclose(out[0, 0], torch.tensor([2., 2., 2., 3., 3.]))   # edges held
    assert torch.allclose(mask_mean(x, keep)[0, 0], torch.tensor([0., 0., 2., 3., 0.]))


def test_segments_valid():
    rng = np.random.default_rng(0)
    p = rng.random(96) + 1e-3
    p[40:45] += 20
    for b in (segments_uniform(96, 8), segments_mass(p, 8), segments_peaks(p, 8)):
        assert len(b) == 9 and b[0] == 0 and b[-1] == 96 and np.all(np.diff(b) >= 1)
    b = segments_mass(p, 8)
    assert np.diff(b)[np.searchsorted(b, 42) - 1] < 96 / 8   # high-delta region gets a short segment


def test_segments_mmd_finds_change_point():
    rng = np.random.default_rng(0)
    s = np.r_[rng.normal(0, 0.1, 50), rng.normal(3, 0.1, 46)]
    b = segments_mmd(s, 2)
    assert list(b) == [0, 50, 96]
    b = segments_mmd(s, 6)
    assert b[0] == 0 and b[-1] == 96 and len(b) == 7 and 50 in b and np.all(np.diff(b) >= 4)


@pytest.mark.skipif(not torch.cuda.is_available(), reason="no CUDA")
def test_cuda_matches_cpu():
    m = _model(head="last", revin=False)
    x = torch.randn(3, 32)
    f = lambda mm: (lambda xs: mm(xs)[:, 0].mean(-1))
    pm = player_map_per_channel([segments_uniform(32, 4)] * 3)
    cpu = SegmentShap(f(m), nsamples=200).explain_map(x, pm)["phi"]
    m_gpu = m.cuda()
    gpu = SegmentShap(f(m_gpu), nsamples=200).explain_map(x.cuda(), pm)["phi"]
    assert np.allclose(cpu, gpu, atol=1e-4)
    p_gpu = hidden_attention_profile(m_gpu, x.cuda(), np.eye(32)[-1])
    p_cpu = hidden_attention_profile(m_gpu.cpu(), x, np.eye(32)[-1])
    assert np.allclose(p_cpu, p_gpu, atol=1e-5)


def test_per_channel_player_map_shap():
    m = _model()
    x = torch.randn(3, 32)
    f = lambda xs: m(xs)[:, 0].mean(-1)
    pm = player_map_per_channel([segments_uniform(32, 2), segments_uniform(32, 4), segments_uniform(32, 1)])
    assert pm.max() + 1 == 7 and pm.shape == (3, 32)
    res = SegmentShap(f, nsamples=200).explain_map(x, pm)
    assert res["phi"].shape == (7,) and res["efficiency_gap"] < 1e-4


def test_segment_shap_efficiency():
    m = _model()
    x = torch.randn(3, 32)
    f = lambda xs: m(xs)[:, 0].mean(-1)
    prof = delta_profile(m, x.unsqueeze(0))[0]
    res = SegmentShap(f, nsamples=200).explain(x, segments_mass(prof, 4))
    assert res["phi"].shape == (3, 4) and res["cell"].shape == (3, 32)
    assert res["efficiency_gap"] < 1e-4
    assert np.isclose(res["cell"].sum(), res["phi"].sum())


def test_gt_generator_planted_structure():
    cfg = GTConfig(length=3000, noise_y=0.0, seed=1)
    g = GTSeries(cfg)
    d, r = g.data, g.regime
    t = np.arange(100, 3000)
    expected = cfg.a * r[t] * d[t - cfg.k_lag, LAG]
    for j, w in zip((-1, 0, 1), cfg.pulse):
        expected += cfg.b * w * d[t - cfg.d_evt - j, EVT]
    assert np.allclose(d[t, 0], expected, atol=1e-5)
    starts = np.array([200, 500, 1200])
    yhat = g.oracle_forecast(starts, 96, 24)
    t = starts[:, None] + 96 + np.arange(24)
    same_regime = r[t] == r[starts + 95][:, None]
    assert np.allclose(yhat[same_regime], d[t, 0][same_regime], atol=1e-5)   # exact while the regime persists
    m = g.gt_mask(500, 96, 24)
    assert m.shape == (6, 96)
    assert not m[[0, 3, 4, 5]].any()
    lag_pos = np.flatnonzero(m[LAG])
    assert lag_pos.size == 0 or (lag_pos.min() >= 96 - cfg.k_lag and lag_pos.max() < 96 - cfg.k_lag + 24)
    assert np.all(g.is_spike[500 + np.flatnonzero(m[EVT])])
