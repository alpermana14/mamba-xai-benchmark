"""
Attribution on the OFFICIAL S-Mamba and TimeMachine forecasters (mamba_ssm backend), plan Opsi A.

Layout contract of this repo: a window is x [C, L] (channels x time) and f maps [B, C, L] to one
scalar per window. The official models take [B, L, C] (S-Mamba also x_mark [B, L, 4] time
features). `OfficialForecaster` adapts between the two.

MambaLRP (Jafari et al. 2024) needs a forward pass in which SiLU, the SSM parameters (delta, B, C),
the gate and the normalisation denominators are treated as constants. The fused mamba_ssm kernel
cannot be patched, so `mamba_ref_forward` re-expresses the layer in plain torch from the module's
own parameters (same maths as mamba_ssm's slow path) and `official_lrp_mode` swaps it in.
`scripts/opsA_equivalence.py` checks that the reference forward equals the kernel.

Both official repos define top-level packages `data_provider`, `utils` and `layers`, so only one
repo can be imported per process (`activate_repo`).
"""
from __future__ import annotations

import argparse
import glob
import sys
import types
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from mamba_ssm.modules.mamba_simple import Mamba

ROOT = Path(__file__).resolve().parents[2]
OFFICIAL = ROOT / "third_party" / "official"
REPO_DIR = {"smamba": OFFICIAL / "S-D-Mamba", "timemachine": OFFICIAL / "TimeMachine" / "TimeMachine_supervised"}
_CLASH = ("data_provider", "utils", "layers", "model", "models", "RevIN", "exp", "experiments")
_active = None


def activate_repo(kind: str) -> Path:
    """Put one official repo first on sys.path and drop cached modules of the other."""
    global _active
    d = REPO_DIR[kind]
    if _active == kind:
        return d
    for p in REPO_DIR.values():
        while str(p) in sys.path:
            sys.path.remove(str(p))
    for name in list(sys.modules):
        if name.split(".")[0] in _CLASH:
            del sys.modules[name]
    sys.path.insert(0, str(d))
    _active = kind
    return d


# --------------------------------------------------------------------------- official configs
def official_args(kind: str, dataset: str, seed: int = 0) -> argparse.Namespace:
    """The arguments of the official H = 96 scripts (see plan §12, Opsi A), as a namespace."""
    ett = dict(data="ETTh1", root_path=str(ROOT / "dataset" / "ETT-small") + "/", data_path="ETTh1.csv", enc_in=7)
    wea = dict(data="custom", root_path=str(ROOT / "dataset" / "weather") + "/", data_path="weather.csv", enc_in=21)
    ds = {"etth1": ett, "weather": wea}[dataset]
    common = dict(seq_len=96, label_len=48, pred_len=96, features="M", target="OT", freq="h", embed="timeF",
                  num_workers=0, seed=seed, **ds)
    if kind == "smamba":
        cfg = dict(dec_in=ds["enc_in"], c_out=ds["enc_in"], dropout=0.1, activation="gelu", output_attention=False,
                   use_norm=True, class_strategy="projection", batch_size=32)
        cfg.update(dict(e_layers=2, d_model=256, d_ff=256, d_state=2) if dataset == "etth1" else
                   dict(e_layers=3, d_model=512, d_ff=512, d_state=2))
    else:
        cfg = dict(revin=1, ch_ind=1, residual=1, dconv=2, d_state=256, e_fact=1, batch_size=512)
        cfg.update(dict(n1=512, n2=32, dropout=0.7) if dataset == "etth1" else dict(n1=128, n2=16, dropout=0.1))
    return argparse.Namespace(**common, **cfg)


def build_official(kind: str, args: argparse.Namespace) -> nn.Module:
    activate_repo(kind)
    if kind == "smamba":
        from model.S_Mamba import Model
    else:
        from models.TimeMachine import Model
    return Model(args)


def find_checkpoint(ckpt_dir: Path) -> Path:
    hits = sorted(glob.glob(str(ckpt_dir / "*" / "checkpoint.pth")))
    if len(hits) != 1:
        raise FileNotFoundError(f"{len(hits)} checkpoints under {ckpt_dir}")
    return Path(hits[0])


def official_dataset(kind: str, args: argparse.Namespace, flag: str):
    """The official Dataset object (scaler fitted on train, standard borders)."""
    activate_repo(kind)
    from data_provider.data_factory import data_provider
    data_set, _ = data_provider(args, flag)
    return data_set


# --------------------------------------------------------------------------- wrapper
class OfficialForecaster(nn.Module):
    """[B, C, L] -> forecast [B, H, C]. S-Mamba needs the time features of the window (`x_mark`)."""

    def __init__(self, kind: str, model: nn.Module):
        super().__init__()
        self.kind, self.model, self.lrp, self.x_mark = kind, model, False, None

    def forward(self, xs: torch.Tensor) -> torch.Tensor:
        x_enc = xs.transpose(1, 2)
        if self.kind == "timemachine":
            return self.model(x_enc)
        xm = self.x_mark.to(xs.dtype).unsqueeze(0).expand(x_enc.shape[0], -1, -1)
        return self._smamba_forecast(x_enc, xm, detach_std=self.lrp)

    def _smamba_forecast(self, x_enc, x_mark, detach_std: bool):
        """S_Mamba.Model.forecast without its in-place division (which breaks gradients w.r.t. the input);
        detach_std=True applies the LRP rule to the instance-normalisation denominator. Values are identical
        to the official forward (checked in scripts/opsA_equivalence.py)."""
        m = self.model
        means = x_enc.mean(1, keepdim=True).detach()
        x = x_enc - means
        stdev = torch.sqrt(torch.var(x, dim=1, keepdim=True, unbiased=False) + 1e-5)
        if detach_std:
            stdev = stdev.detach()
        x = x / stdev
        N = x.shape[2]
        enc = m.enc_embedding(x, x_mark)
        enc, _ = m.encoder(enc, attn_mask=None)
        dec = m.projector(enc).permute(0, 2, 1)[:, :, :N]
        dec = dec * stdev[:, 0, :].unsqueeze(1) + means[:, 0, :].unsqueeze(1)
        return dec[:, -m.pred_len:, :]


# --------------------------------------------------------------------------- reference forward + LRP
def _silu_cst(x):
    return x * torch.sigmoid(x).detach()


def _gelu_cst(x):
    return x * (0.5 * (1.0 + torch.erf(x * 0.5 ** 0.5))).detach()


def _relu_cst(x):
    return x * (x > 0).to(x.dtype)


def mamba_ref_forward(m: Mamba, x: torch.Tensor, lrp: bool = False) -> torch.Tensor:
    """Plain-torch forward of a mamba_ssm.Mamba layer, x [B, L, d_model]. lrp=True applies the MambaLRP detaches."""
    B, L, _ = x.shape
    x_in, z = m.in_proj(x).chunk(2, dim=-1)                               # [B, L, d_inner] each
    xc = m.conv1d(x_in.transpose(1, 2))[:, :, :L].transpose(1, 2)
    u = _silu_cst(xc) if lrp else F.silu(xc)
    dt, Bs, Cs = torch.split(m.x_proj(u), [m.dt_rank, m.d_state, m.d_state], dim=-1)
    delta = F.softplus(m.dt_proj(dt))                                      # [B, L, d_inner]
    if lrp:
        delta, Bs, Cs = delta.detach(), Bs.detach(), Cs.detach()
    A = -torch.exp(m.A_log.float())                                        # [d_inner, d_state]
    dA = torch.exp(delta.float().unsqueeze(-1) * A)                        # [B, L, d_inner, d_state]
    dBu = delta.float().unsqueeze(-1) * Bs.float().unsqueeze(2) * u.float().unsqueeze(-1)
    h = torch.zeros(B, m.d_inner, m.d_state, device=x.device, dtype=torch.float32)
    ys = []
    for t in range(L):
        h = dA[:, t] * h + dBu[:, t]
        ys.append((h * Cs[:, t].float().unsqueeze(1)).sum(-1))
    y = torch.stack(ys, 1).to(u.dtype) + u * m.D
    y = y * (_silu_cst(z) if lrp else F.silu(z))
    if lrp:
        y = 0.5 * y + 0.5 * y.detach()                                     # half rule for the gate
    return m.out_proj(y)


def _mamba_lrp_forward(self, hidden_states, inference_params=None):
    return mamba_ref_forward(self, hidden_states, lrp=True)


def _layernorm_lrp(self, x):
    mu = x.mean(-1, keepdim=True)
    std = (x.var(-1, keepdim=True, unbiased=False) + self.eps).sqrt()
    return (x - mu) / std.detach() * self.weight + self.bias


class official_lrp_mode:
    """Swap the LRP forwards into an OfficialForecaster (Mamba layers, LayerNorm, functional GELU/ReLU, RevIN)."""

    def __init__(self, fc: OfficialForecaster):
        self.fc, self._patched, self._attrs = fc, [], []

    def __enter__(self):
        self.fc.lrp = True
        inside = {id(c) for m in self.fc.model.modules() if isinstance(m, Mamba) for c in m.modules() if c is not m}
        for m in self.fc.model.modules():
            if id(m) in inside:                                            # Mamba.act etc.: handled by the ref forward
                continue
            if isinstance(m, Mamba):
                self._patch(m, "forward", _mamba_lrp_forward)
            elif isinstance(m, nn.LayerNorm):
                self._patch(m, "forward", _layernorm_lrp)
            elif isinstance(m, (nn.GELU, nn.ReLU, nn.SiLU, nn.Tanh, nn.Sigmoid, nn.Softmax)):
                raise NotImplementedError(f"no LRP rule for module {type(m).__name__}")
            act = getattr(m, "activation", None)
            if act is F.gelu or act is F.relu:                             # S-Mamba EncoderLayer.activation
                self._attrs.append((m, act))
                m.activation = _gelu_cst if act is F.gelu else _relu_cst
        # TimeMachine's RevIN already detaches mean and stdev in _get_statistics: nothing to patch.
        return self.fc

    def _patch(self, m, name, fn):
        setattr(m, name, types.MethodType(fn, m))
        self._patched.append((m, name))

    def __exit__(self, *exc):
        for m, name in self._patched:
            delattr(m, name)
        for m, act in self._attrs:
            m.activation = act
        self._patched.clear()
        self._attrs.clear()
        self.fc.lrp = False
        return False


def official_mamba_lrp(f, fc: OfficialForecaster, x: torch.Tensor):
    """MambaLRP relevance of the scalar f(x) for one window x [C, L] on an official model."""
    from src.xai.mamba_lrp import grad_x_input
    with official_lrp_mode(fc):
        return grad_x_input(f, x)


# --------------------------------------------------------------------------- evaluation helpers
@torch.no_grad()
def test_mse(fc: OfficialForecaster, data_set, device, batch: int = 256) -> float:
    """Official metric: MSE over all variates and horizon steps in standardised space, on the test split."""
    se, n = 0.0, 0
    for s in range(0, len(data_set), batch):
        items = [data_set[i] for i in range(s, min(s + batch, len(data_set)))]
        x = torch.as_tensor(np.stack([it[0] for it in items]), dtype=torch.float32, device=device)   # [B, L, C]
        y = torch.as_tensor(np.stack([it[1] for it in items]), dtype=torch.float32, device=device)   # [B, ll+H, C]
        if fc.kind == "smamba":
            xm = torch.as_tensor(np.stack([it[2] for it in items]), dtype=torch.float32, device=device)
            out = fc.model(x, xm, None, None)
        else:
            out = fc.model(x)
        H = out.shape[1]
        se += ((out - y[:, -H:, :]) ** 2).sum().item()
        n += out.numel()
    return se / n
