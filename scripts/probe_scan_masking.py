"""
Probe: selective-scan masking (delta_s = 0 in every Mamba layer) as a removal operator.

Uses a model trained by scripts/run_sgshap_synthetic_v1.py and time-only players
(each player = one time segment across all channels, since a token mixes channels).

1. Leakage: for segment k, replace it with another window's values and measure
       leak_k = |f_rm(x) - f_rm(x')| / |f(x) - f(x')|
   0 = the removal erases segment k completely. Mean masking is 0 by construction.
2. Exact Shapley over the 8 time segments (256 coalitions) under three removals
   (mean, interp, scan), scored against time-level ground truth, plus how far the
   empty-coalition forecast f(∅) sits from forecasts on real data (off-manifold proxy).

    python -m scripts.probe_scan_masking --run results/sgshap_v1_last
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from scipy.stats import spearmanr
from sklearn.metrics import average_precision_score

from scripts.run_sgshap_synthetic import windows
from src.models.mamba_ext import scan_mask
from src.models.plain_mamba import PlainMamba
from src.synthetic.gt_generator import CHANNELS, TARGET, GTConfig, GTSeries
from src.xai.maskers import MASKERS
from src.xai.sg_shap import SegmentShap, player_map_shared, segments_uniform


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--run", required=True)
    p.add_argument("--n_windows", type=int, default=40)
    p.add_argument("--M", type=int, default=8)
    p.add_argument("--threads", type=int, default=0)
    p.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = p.parse_args()
    dev = args.device
    sys.stdout.reconfigure(encoding="utf-8")
    if args.threads:
        torch.set_num_threads(args.threads)
    run = Path(args.run)
    a = json.loads((run / "summary.json").read_text(encoding="utf-8"))["args"]
    L, H, C, M = a["seq_len"], a["pred_len"], len(CHANNELS), args.M

    gen = GTSeries(GTConfig(length=a["length"], seed=a["seed"]))
    raw = gen.data
    n_tr, n_va = int(0.7 * len(raw)), int(0.1 * len(raw))
    mu, sd = raw[:n_tr].mean(0), raw[:n_tr].std(0)
    data = torch.as_tensor((raw - mu) / sd, device=dev)
    te = np.arange(n_tr + n_va - L, len(raw) - L - H + 1)

    model = PlainMamba(C, L, H, d_model=a["d_model"], n_layers=a["n_layers"], d_state=a.get("d_state", 16),
                       head=a["head"], revin=a["revin"])
    model.load_state_dict(torch.load(run / "model.pt", map_location="cpu"))
    model.to(dev).eval()
    f = lambda xs: model(xs)[:, TARGET].mean(-1)

    def f_scan(xs, keep_t):
        with scan_mask(model, keep_t):
            return f(xs)

    removals = {
        "mean": lambda x, keep: f(MASKERS["mean"](x, keep)),
        "interp": lambda x, keep: f(MASKERS["interp"](x, keep)),
        "scan": lambda x, keep: f_scan(x.unsqueeze(0).expand(len(keep), -1, -1), keep[:, 0, :]),
    }

    starts = te[np.linspace(0, len(te) - 1, args.n_windows).astype(int)]
    x_ex, _ = windows(data, starts, L, H)
    rng = np.random.default_rng(0)
    other, _ = windows(data, rng.choice(te, args.n_windows), L, H)
    with torch.no_grad():
        f_test = torch.cat([f(windows(data, te[i:i + 512], L, H)[0]) for i in range(0, len(te), 512)]).cpu().numpy()
    b = segments_uniform(L, M)
    seg_of_t = np.repeat(np.arange(M), np.diff(b))
    pm = player_map_shared(b, C) % M                                   # time-only: same player for every channel
    score_mask = gen.score_mask(L)

    leak_rows, rows = [], []
    for w, (s, x, xo) in enumerate(zip(starts, x_ex, other)):
        # ---- leakage per segment ----
        with torch.no_grad():
            for k in range(M):
                x2 = x.clone()
                x2[:, b[k]:b[k + 1]] = xo[:, b[k]:b[k + 1]]
                keep = torch.ones(1, L, dtype=torch.bool, device=dev)
                keep[:, b[k]:b[k + 1]] = False
                d_full = abs(f(x.unsqueeze(0)) - f(x2.unsqueeze(0))).item()
                d_scan = abs(f_scan(x.unsqueeze(0), keep) - f_scan(x2.unsqueeze(0), keep)).item()
                if d_full > 1e-3:
                    leak_rows.append({"window": w, "segment": k, "leak_scan": d_scan / d_full})
        # ---- exact time-segment Shapley under each removal ----
        gt = gen.gt_mask(int(s), L, H)
        gt_time = (gt & score_mask).any(0)
        phis = {}
        for name, vf in removals.items():
            res = SegmentShap(None, value_fn=vf, nsamples=2 ** M, seed=0).explain_map(x, pm)
            phis[name] = res["phi"]
            score_t = (np.abs(res["phi"]) / np.diff(b))[seg_of_t]
            rows.append({"window": w, "removal": name,
                         "ap_time": average_precision_score(gt_time, score_t) if gt_time.any() else np.nan,
                         "f_empty": res["base"], "fx": res["fx"], "efficiency_gap": res["efficiency_gap"],
                         "n_evals": res["n_evals"]})
        for i, n1 in enumerate(removals):
            for n2 in list(removals)[i + 1:]:
                rows.append({"window": w, "removal": f"spearman {n1}~{n2}",
                             "ap_time": spearmanr(np.abs(phis[n1]), np.abs(phis[n2])).statistic})
        print(f"window {w + 1}/{len(starts)}", flush=True)

    leak = pd.DataFrame(leak_rows)
    df = pd.DataFrame(rows)
    mu_f, sd_f = f_test.mean(), f_test.std()
    summ = df.groupby("removal", sort=False).agg(ap_time=("ap_time", "mean"), f_empty=("f_empty", "mean"))
    summ["f_empty_z"] = (summ["f_empty"] - mu_f) / sd_f
    leak_by_seg = leak.groupby("segment")["leak_scan"].median()
    lines = [f"# Selective-scan masking probe — head={a['head']}", "",
             f"Leak ratio of scan masking per time segment (median over windows; 0 = complete removal, "
             f"1 = no removal). Segments of {np.diff(b)[0]} steps, segment {M - 1} holds the last step.", "",
             "| segment | " + " | ".join(str(k) for k in leak_by_seg.index) + " |",
             "|---|" + "---|" * len(leak_by_seg),
             "| leak | " + " | ".join(f"{v:.3f}" for v in leak_by_seg.values) + " |", "",
             f"Exact time-segment Shapley (M={M}, {2 ** M} coalitions). f on test data: mean {mu_f:.3f}, sd {sd_f:.3f}.", "",
             "| removal | AP (time-level GT) | f(∅) | z of f(∅) vs test forecasts |", "|---|---|---|---|"]
    for name in removals:
        r = summ.loc[name]
        lines.append(f"| {name} | {r.ap_time:.3f} | {r.f_empty:.3f} | {r.f_empty_z:+.2f} |")
    lines += ["", "Rank agreement of |φ| between removals (Spearman, mean over windows): " +
              ", ".join(f"{k.replace('spearman ', '')} {summ.loc[k].ap_time:.2f}" for k in summ.index if k.startswith("spearman")),
              f"Max efficiency gap = {df['efficiency_gap'].max():.2e}"]
    text = "\n".join(lines) + "\n"
    (run / "scan_masking_probe.md").write_text(text, encoding="utf-8")
    leak.to_csv(run / "scan_masking_leak.csv", index=False)
    df.to_csv(run / "scan_masking_shapley.csv", index=False)
    print(text)


if __name__ == "__main__":
    main()
