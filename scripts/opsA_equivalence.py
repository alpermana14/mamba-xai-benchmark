"""
Opsi A, technical preconditions (plan §12, 2026-11-11). Run inside WSL with the mamba_ssm venv:
    ~/venv_opsA/bin/python -m scripts.opsA_equivalence

(i)   mamba_ref_forward == mamba_ssm.Mamba forward (values and input gradients), at the shapes of
      S-Mamba (d_state 2) and TimeMachine (d_model 1, d_state 256) and a generic one;
(ii)  PurePyTorchMamba (our zoo backend) with copied weights == mamba_ssm.Mamba;
(iii) official_lrp_mode leaves the forward value of a freshly built official S-Mamba and TimeMachine
      unchanged, and MambaLRP relevance differs from Gradient x Input (the detaches are active).
Writes results/opsA/equivalence.md.
"""
import sys
import time
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mamba_ssm.modules.mamba_simple import Mamba                                              # noqa: E402

from src.xai.official_adapter import (OfficialForecaster, build_official, mamba_ref_forward,  # noqa: E402
                                      official_args, official_lrp_mode, official_mamba_lrp)
from src.xai.mamba_lrp import grad_x_input                                                    # noqa: E402
from third_party.priorcast.mamba_block import PurePyTorchMamba                                # noqa: E402

TOL = 1e-4
dev = "cuda"
lines = ["# Opsi A: equivalence of the reference forward, our zoo backend and the mamba_ssm kernel", ""]
ok_all = True


def report(name, val, tol=TOL):
    global ok_all
    ok = val < tol
    ok_all &= ok
    lines.append(f"| {name} | {val:.2e} | {'pass' if ok else 'FAIL'} |")
    print(f"{name}: {val:.2e} {'pass' if ok else 'FAIL'}", flush=True)


lines += ["| check | max abs diff | verdict |", "|---|---|---|"]
torch.manual_seed(0)
for tag, d_model, d_state, L, B in [("S-Mamba shape", 256, 2, 11, 4), ("TimeMachine shape", 1, 256, 512, 7),
                                     ("generic", 64, 16, 96, 3)]:
    m = Mamba(d_model=d_model, d_state=d_state, d_conv=2, expand=1).to(dev).eval()
    x = torch.randn(B, L, d_model, device=dev, requires_grad=True)
    y_k = m(x)
    g_k, = torch.autograd.grad(y_k.square().sum(), x)
    x2 = x.detach().clone().requires_grad_(True)
    y_r = mamba_ref_forward(m, x2)
    g_r, = torch.autograd.grad(y_r.square().sum(), x2)
    report(f"(i) ref vs kernel, value, {tag}", (y_k - y_r).abs().max().item())
    report(f"(i) ref vs kernel, input gradient, {tag}", (g_k - g_r).abs().max().item() / (g_k.abs().max().item() + 1e-12))
    # (ii) our zoo backend with the kernel's weights
    if d_model >= 16:                                                       # PurePyTorchMamba's dt_rank = ceil(d/16)
        ours = PurePyTorchMamba(d_model, d_state, d_conv=2, expand=1).to(dev).eval()
        missing = ours.load_state_dict(m.state_dict(), strict=True)
        with torch.no_grad():
            y_o = ours(x.detach())
        report(f"(ii) PurePyTorchMamba vs kernel, {tag}", (y_k - y_o).abs().max().item())
    # speed
    with torch.no_grad():
        for fn, nm in ((lambda: m(x.detach()), "kernel"), (lambda: mamba_ref_forward(m, x.detach()), "reference")):
            torch.cuda.synchronize(); t0 = time.time()
            for _ in range(20):
                fn()
            torch.cuda.synchronize()
            lines.append(f"| speed {tag} {nm} | {(time.time() - t0) / 20 * 1e3:.2f} ms | – |")

# (iii) official models, random init (no checkpoint needed)
for kind, dataset in (("smamba", "etth1"), ("timemachine", "etth1"), ("smamba", "weather"), ("timemachine", "weather")):
    a = official_args(kind, dataset)
    torch.manual_seed(1)
    fc = OfficialForecaster(kind, build_official(kind, a)).to(dev).eval()
    C = a.enc_in
    x = torch.randn(C, 96, device=dev)
    fc.x_mark = torch.randn(96, 4, device=dev)
    f = lambda xs: fc(xs)[:, :, C - 1].mean(-1)
    with torch.no_grad():
        v0 = f(x.unsqueeze(0)).item()
        if kind == "smamba":                                                # wrapper re-expression vs official forward
            xm = fc.x_mark.unsqueeze(0)
            v_off = fc.model(x.unsqueeze(0).transpose(1, 2), xm, None, None)[:, :, C - 1].mean(-1).item()
            report(f"(iii) wrapper equals official forward, {kind} {dataset}", abs(v0 - v_off) / (abs(v_off) + 1e-6))
        with official_lrp_mode(fc):
            v1 = f(x.unsqueeze(0)).item()
    report(f"(iii) LRP mode keeps forward value, {kind} {dataset}", abs(v0 - v1) / (abs(v0) + 1e-6))
    gxi = grad_x_input(f, x)[0]
    lrp = official_mamba_lrp(f, fc, x)[0]
    diff = float(abs(gxi - lrp).max() / (abs(gxi).max() + 1e-12))
    lines.append(f"| (iii) MambaLRP differs from GxI, {kind} {dataset} | {diff:.2e} | {'pass' if diff > 1e-6 else 'FAIL (detaches inactive)'} |")
    ok_all &= diff > 1e-6
    lines.append(f"| (iii) sum of relevance / f(x), {kind} {dataset} | {float(lrp.sum()) / (v0 + 1e-12):.3f} | descriptive |")

lines += ["", f"**Overall: {'all checks pass' if ok_all else 'FAILURES, fix the adapter before any explanation run'}**"]
out = Path("results/opsA"); out.mkdir(parents=True, exist_ok=True)
(out / "equivalence.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines[-2:]))
sys.exit(0 if ok_all else 1)
