"""
Benchmark v2 (plan §12): train one forecaster on one ground-truth task with the v1
protocol (AdamW, ReduceLROnPlateau, early stop on val MSE of the target, best-val
weights, full checkpoint every epoch for --resume) and record forecast quality
against the trivial (mean) forecast and, where it exists, the oracle.

    python -m scripts.bench_train --task g2a --model smamba --seed 0
    -> results/bench/g2a/smamba_s0/{model.pt, summary.json, log.txt, training_history.csv, training_curve.png}
"""

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch

from scripts.run_sgshap_synthetic import log
from scripts.run_sgshap_synthetic_v1 import diagnose_training, plot_training
from src.bench.tasks import TASKS, build_task
from src.models.zoo import MODELS, build_model


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--task", required=True, choices=TASKS)
    p.add_argument("--model", required=True, choices=MODELS)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--epochs", type=int, default=100)
    p.add_argument("--patience", type=int, default=10)
    p.add_argument("--lr_patience", type=int, default=3)
    p.add_argument("--batch_size", type=int, default=256)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--weight_decay", type=float, default=1e-2)
    p.add_argument("--grad_clip", type=float, default=1.0)
    p.add_argument("--resume", action="store_true", help="continue from <out>/ckpt.pt")
    p.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    p.add_argument("--out", default=None, help="default results/bench/<task>/<model>_s<seed>")
    return p.parse_args()


@torch.no_grad()
def predict(model, X: torch.Tensor, target: int, bs: int = 1024) -> torch.Tensor:
    model.eval()
    return torch.cat([model(X[i:i + bs])[:, target] for i in range(0, len(X), bs)])


def train(model, X, Y, target, a, fh, oracle_va, ckpt_path: Path):
    decay, no_decay = [], []
    for name, p in model.named_parameters():
        (no_decay if p.ndim < 2 or name.endswith("A_log") else decay).append(p)
    opt = torch.optim.AdamW([{"params": decay, "weight_decay": a.weight_decay},
                             {"params": no_decay, "weight_decay": 0.0}], lr=a.lr)
    sched = torch.optim.lr_scheduler.ReduceLROnPlateau(opt, factor=0.5, patience=a.lr_patience, min_lr=a.lr / 64)
    best, best_state, bad, hist, start = float("inf"), None, 0, [], 0
    rng = np.random.default_rng(a.seed)
    if a.resume:
        ck = torch.load(ckpt_path, map_location=a.device, weights_only=False)
        model.load_state_dict(ck["model"])
        opt.load_state_dict(ck["opt"])
        sched.load_state_dict(ck["sched"])
        best, best_state, bad, hist, start = ck["best"], ck["best_state"], ck["bad"], ck["hist"], ck["epoch"]
        rng.bit_generator.state = ck["rng"]
        torch.set_rng_state(ck["torch_rng"])
        if "cuda_rng" in ck:
            torch.cuda.set_rng_state(ck["cuda_rng"])
        log(f"resumed after epoch {start} (best {best:.4f}, {bad} flat epochs)", fh)
    stop, n = "max_epochs", len(X["train"])
    for ep in range(start, a.epochs):
        model.train()
        t0, tot = time.time(), 0.0
        perm = torch.as_tensor(rng.permutation(n), device=a.device)
        for i in range(0, n, a.batch_size):
            b = perm[i:i + a.batch_size]
            loss = ((model(X["train"][b])[:, target] - Y["train"][b]) ** 2).mean()
            opt.zero_grad()
            loss.backward()
            if a.grad_clip > 0:
                torch.nn.utils.clip_grad_norm_(model.parameters(), a.grad_clip)
            opt.step()
            tot += loss.item() * len(b)
        va = float(((predict(model, X["val"], target) - Y["val"]) ** 2).mean())
        lr = opt.param_groups[0]["lr"]
        sched.step(va)
        hist.append({"epoch": ep + 1, "train": tot / n, "val_y": va, "lr": lr, "seconds": time.time() - t0})
        log(f"epoch {ep + 1:03d} lr {lr:.1e} train {tot / n:.4f} val {va:.4f}"
            + (f" (oracle {oracle_va:.4f}, x{va / oracle_va:.2f})" if np.isfinite(oracle_va) else "")
            + f" ({time.time() - t0:.0f}s)", fh)
        if va < best - 1e-5:
            best, bad = va, 0
            best_state = {k: v.clone() for k, v in model.state_dict().items()}
        else:
            bad += 1
        ck = {"model": model.state_dict(), "opt": opt.state_dict(), "sched": sched.state_dict(), "epoch": ep + 1,
              "best": best, "best_state": best_state, "bad": bad, "hist": hist, "rng": rng.bit_generator.state,
              "torch_rng": torch.get_rng_state()}
        if torch.cuda.is_available():
            ck["cuda_rng"] = torch.cuda.get_rng_state()
        torch.save(ck, ckpt_path)
        if bad >= a.patience:
            stop = "early_stop"
            break
    model.load_state_dict(best_state)
    return model, hist, stop


def main():
    a = parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    torch.manual_seed(a.seed)
    out = Path(a.out or f"results/bench/{a.task}/{a.model}_s{a.seed}")
    out.mkdir(parents=True, exist_ok=True)
    fh = open(out / "log.txt", "a" if a.resume else "w", encoding="utf-8")
    log(f"args {vars(a)}", fh)
    task = build_task(a.task, a.seed)
    X = {k: torch.as_tensor(v, device=a.device) for k, v in task.X.items()}
    Y = {k: torch.as_tensor(v, device=a.device) for k, v in task.Y.items()}
    C, tgt = len(task.channels), task.target
    oracle_va = task.oracle_mse.get("val", float("nan"))
    log(f"task {task.name}: C {C} L {task.L} H {task.H} " + " ".join(f"{k} {len(v)}" for k, v in X.items()), fh)

    model = build_model(a.model, C, task.L, task.H, norm=task.norm).to(a.device)
    n_params = sum(p.numel() for p in model.parameters())
    log(f"model {a.model}: {n_params} parameters", fh)
    t0 = time.time()
    model, hist, stop = train(model, X, Y, tgt, a, fh, oracle_va, out / "ckpt.pt")
    diag = diagnose_training(hist, stop, oracle_va, a.patience)
    diag["seconds"] = time.time() - t0
    diag["seconds_per_epoch"] = float(np.median([h["seconds"] for h in hist]))
    pd.DataFrame(hist).to_csv(out / "training_history.csv", index=False)
    plot_training(hist, oracle_va, out)
    torch.save(model.state_dict(), out / "model.pt")

    fc = {}
    for split in ("test", task.explain_split):
        pred = predict(model, X[split], tgt)
        mse = float(((pred - Y[split]) ** 2).mean())
        trivial = float((Y[split] ** 2).mean())
        fc[split] = {"mse": mse, "trivial_mse": trivial, "skill": 1 - mse / trivial,
                     "oracle_mse": task.oracle_mse.get(split)}
        if task.name.startswith("g2"):
            fc[split]["accuracy"] = float((torch.sign(pred[:, 0]) == Y[split][:, 0]).float().mean())
    fc["passes_quality_gate"] = all(v["mse"] < v["trivial_mse"] for v in fc.values() if isinstance(v, dict))
    log(f"training {diag['seconds']:.0f}s: {diag}", fh)
    log(f"forecast {fc}", fh)
    (out / "summary.json").write_text(json.dumps({"args": vars(a), "task": task.name, "channels": task.channels,
                                                  "n_params": n_params, "training": diag, "forecast": fc},
                                                 indent=2, default=float), encoding="utf-8")
    fh.close()


if __name__ == "__main__":
    main()
