"""
Opsi A (plan §12, 2026-11-11): explain one OFFICIAL checkpoint with the 13 benchmark methods and score
deletion / insertion AOPC under the mean and interpolation maskers. Run inside WSL:
    ~/venv_opsA/bin/python -m scripts.opsA_explain --model smamba --dataset etth1 --seed 0
Output: results/opsA/<model>_<dataset>_s<seed>/{summary.json, xai/per_window.csv, xai/sanity.csv, xai/summary.md}
Same budgets and metrics as scripts/bench_explain.py; the explained scalar is the mean forecast of OT.
"""
import argparse
import json
import sys
import time
import types
from pathlib import Path

import numpy as np
import pandas as pd
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.bench_explain import Explainers, hsic_groups                              # noqa: E402
from src.xai.faithfulness import deletion_insertion, rank_similarity                    # noqa: E402
from src.xai.mamba_lrp import grad_x_input                                              # noqa: E402
from src.xai.official_adapter import (ROOT, OfficialForecaster, build_official, find_checkpoint,  # noqa: E402
                                      official_args, official_dataset, official_lrp_mode, test_mse)

METHODS = ["Random", "GxI", "IG", "IG-U4", "IG-U8", "IG-U16", "SHAP-C", "SHAP-U4", "SHAP-U8", "SHAP-U16",
           "SHAP-MMD8", "GS-SHAP", "MambaLRP"]
# H = 96 test MSE reported by the authors (plan §12: inclusion = ours <= 1.10 x paper)
PAPER_MSE = {("smamba", "etth1"): 0.386, ("smamba", "weather"): 0.165,
             ("timemachine", "etth1"): 0.364, ("timemachine", "weather"): 0.164}


class OfficialExplainers(Explainers):
    def run(self, name, x, model=None, f=None):
        if name == "MambaLRP":
            with official_lrp_mode(model or self.model):
                return grad_x_input(f or self.f, x)[0], 1, None
        return super().run(name, x, model, f)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True, choices=["smamba", "timemachine"])
    p.add_argument("--dataset", required=True, choices=["etth1", "weather"])
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--n_explain", type=int, default=50)
    p.add_argument("--n_sanity", type=int, default=8)
    p.add_argument("--shap_mult", type=float, default=1.0)
    p.add_argument("--ig_steps", type=int, default=32)
    p.add_argument("--shap_batch", type=int, default=512)
    p.add_argument("--gsshap_budget", type=int, default=1500)
    p.add_argument("--methods", nargs="*", default=None)
    p.add_argument("--device", default="cuda")
    return p.parse_args()


def main():
    a = parse_args()
    dev = a.device
    out = ROOT / "results" / "opsA" / f"{a.model}_{a.dataset}_s{a.seed}"
    (out / "xai").mkdir(parents=True, exist_ok=True)
    args = official_args(a.model, a.dataset, a.seed)
    ckpt = find_checkpoint(out.parent / "ckpt" / out.name)
    model = build_official(a.model, args).to(dev)
    model.load_state_dict(torch.load(ckpt, map_location=dev))
    fc = OfficialForecaster(a.model, model).to(dev).eval()
    torch.manual_seed(a.seed + 999)
    rfc = OfficialForecaster(a.model, build_official(a.model, args)).to(dev).eval()

    test_set = official_dataset(a.model, args, "test")
    train_set = official_dataset(a.model, args, "train")
    cols = list(pd.read_csv(Path(args.root_path) / args.data_path, nrows=0).columns[1:])
    if cols[-1] != args.target:                                            # Dataset_Custom moves the target last
        cols = [c for c in cols if c != args.target] + [args.target]
    C, L, tgt = len(cols), args.seq_len, len(cols) - 1
    task = types.SimpleNamespace(name=a.dataset, channels=cols, L=L,
                                 X={"train": train_set.data_x.T[None].astype(np.float32)})

    mse = test_mse(fc, test_set, dev)
    paper = PAPER_MSE[(a.model, a.dataset)]
    summ = {"args": vars(args) | {"model": a.model, "task": a.dataset, "seed": a.seed}, "checkpoint": str(ckpt),
            "n_params": sum(p.numel() for p in model.parameters()), "test_mse": mse, "paper_mse": paper,
            "ratio_to_paper": (mse / paper) if paper else None,
            "passes_inclusion": (mse <= 1.10 * paper) if paper else None, "n_test_windows": len(test_set)}
    (out / "summary.json").write_text(json.dumps(summ, indent=1), encoding="utf-8")
    print(f"{out.name}: test MSE {mse:.4f} (paper {paper}), {len(test_set)} test windows", flush=True)

    f = lambda xs: fc(xs)[:, :, tgt].mean(-1)
    f_r = lambda xs: rfc(xs)[:, :, tgt].mean(-1)
    groups = hsic_groups(task, a.seed, out.parent / f"hsic_{a.dataset}_s{a.seed}.json")
    methods = [m for m in METHODS if a.methods is None or m in a.methods]
    ex = OfficialExplainers(fc, f, task, groups, a.seed, a)
    idx = np.linspace(0, len(test_set) - 1, a.n_explain).astype(int)
    print(f"methods {methods}, HSIC groups {groups}", flush=True)

    rows, sanity = [], []
    for w, i in enumerate(idx):
        item = test_set[int(i)]
        x = torch.as_tensor(np.asarray(item[0]).T, dtype=torch.float32, device=dev)          # [C, L]
        fc.x_mark = rfc.x_mark = torch.as_tensor(np.asarray(item[2]), dtype=torch.float32, device=dev)
        with torch.no_grad():
            fx = f(x.unsqueeze(0)).item()
        for name in methods:
            t0 = time.time()
            attr, n_ev, eff = ex.run(name, x)
            row = {"window": w, "index": int(i), "method": name, "seconds": time.time() - t0, "n_evals": n_ev,
                   "efficiency_gap": eff, "fx": fx, "sum_attr": float(attr.sum())}
            for mk in ("mean", "interp"):
                row.update({f"{k}_{mk}": v for k, v in deletion_insertion(f, x, attr, masker=mk).items()})
            rows.append(row)
            if w < a.n_sanity and name != "Random":
                attr_r = ex.run(name, x, model=rfc, f=f_r)[0]
                sanity.append({"window": w, "method": name, "spearman": rank_similarity(attr, attr_r)})
        print(f"window {w + 1}/{len(idx)}", flush=True)

    df, sd = pd.DataFrame(rows), pd.DataFrame(sanity)
    df.to_csv(out / "xai" / "per_window.csv", index=False)
    sd.to_csv(out / "xai" / "sanity.csv", index=False)
    cols_ = ["del_aopc_mean", "ins_aopc_mean", "del_aopc_interp", "ins_aopc_interp", "n_evals", "seconds"]
    agg = df.groupby("method", sort=False)[cols_].mean()
    agg["sanity_spearman"] = sd.groupby("method", sort=False)["spearman"].mean() if len(sd) else np.nan
    md = [f"# {out.name}", "", f"test MSE {mse:.4f} (paper {paper}), checkpoint `{ckpt.name}`", "",
          agg.to_markdown(floatfmt=".3f")]
    (out / "xai" / "summary.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(agg.round(3).to_string(), flush=True)


if __name__ == "__main__":
    main()
