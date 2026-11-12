# mamba-xai-benchmark

A pre-registered benchmark of attribution methods for Mamba time-series forecasters.

The benchmark asks whether explanation methods built for Mamba beat generic ones, and how much the answer depends on how the evaluation is set up. It varies three axes.

1. **Ground-truth structure.** Sparse cells (G1), variable–time blocks (G2a–c, the GroupSegment-SHAP generator) and feature-level Shapley values (G3, SHAPformer load data).
2. **Attribution resolution.** Cells, uniform segments of 4, 8 or 16 steps, and whole channels.
3. **Masker of the faithfulness metric.** Deletion and insertion AOPC with a mean masker and an interpolation masker.

It covers 14 methods and four forecasters, with three seeds each. The methods are Random, Gradient × Input, Integrated Gradients (plain and segment-aggregated), Kernel SHAP with channel, uniform-segment and MMD-segment players, GroupSegment-SHAP, MambaLRP and step-size-guided SHAP. The forecasters are PlainMamba (scan over time), S-Mamba (scan over variates), TimeMachine (scan over channels) and iTransformer. The public data are ETTh1 and Weather, with ETTh2, ETTm1 and Exchange Rate held out. S-Mamba and TimeMachine were also retrained with their official code to check the public-data findings.

The decision rules were written before the experiments and are reproduced in [PREREGISTRATION.md](PREREGISTRATION.md).

## Main findings

- Mamba-specific explanations did not recover the relevant inputs better than generic ones. MambaLRP beat Integrated Gradients in 1 of 15 model–task combinations and lost in 8.
- Accuracy depended on the resolution far more than on the estimator. At matched resolution, Kernel SHAP did not beat aggregated Integrated Gradients, even with four times more samples.
- Faithfulness rankings changed with the masker. The best method differed between the two maskers in 39 of 40 cells. This replicated on held-out datasets, at longer horizons and on the official S-Mamba and TimeMachine implementations.

## Layout

| Path | Content |
|---|---|
| `src/models/` | Forecasters (`zoo.py`, `plain_mamba.py`) |
| `src/bench/tasks.py` | Ground-truth and public tasks |
| `src/synthetic/` | G1 generator |
| `src/xai/` | Baselines, MambaLRP, step-size-guided SHAP, maskers, faithfulness metrics, adapter for the official models |
| `scripts/bench_*.py` | Training, explanation and analysis of the main benchmark |
| `scripts/opsA_*` | Replication on the official S-Mamba and TimeMachine code |
| `scripts/run_*.py`, `probe_*.py` | Pilot study on G1 |
| `third_party/priorcast/` | Plain-PyTorch Mamba layer, data split and metrics from the author's earlier PriorCast project. It is not an evaluated model. |
| `results/bench/`, `results/opsA/` | Per-run summaries, per-window scores and analysis reports. Model weights are not included. |
| `tests/` | Unit tests |

## Setup

```bash
pip install -r requirements.txt
bash setup_external.sh        # clones GroupSegment-SHAP, S-D-Mamba and TimeMachine at the pinned commits
```

GroupSegment-SHAP and S-D-Mamba have no licence, so this repository does not redistribute them. The setup script clones them from their authors and applies two one-line compatibility fixes.

**Data.** Place the public datasets of the Autoformer/Time-Series-Library collection under `dataset/`, as `ETT-small/ETTh1.csv`, `ETT-small/ETTh2.csv`, `ETT-small/ETTm1.csv`, `weather/weather.csv` and `exchange_rate/exchange_rate.csv`. For G3, download the synthetic data of [SHAPformer](https://github.com/KIT-IAI/SHAPformer) to `dataset/external/shapformer/data/synthetic/` and run `python -m scripts.prepare_shapformer`. G1 and G2 are generated on the fly.

## Reproducing

```bash
# main benchmark, one run (task in g1, g2a, g2b, g2c, g3, etth1, weather, etth2, ettm1, exchange;
# model in plain, smamba, timemachine, itransformer)
python -m scripts.bench_train   --task g2a --model smamba --seed 0
python -m scripts.bench_explain --run results/bench/g2a/smamba_s0

# analyses, after all runs
python -m scripts.bench_analyze        # RQ1-RQ4      -> results/bench/analysis.md
python -m scripts.bench_replication    # masker replication -> results/bench/replication.md
python -m scripts.bench_budget         # Kernel SHAP budget -> results/bench/budget.md

# official-code replication (Linux or WSL with a CUDA GPU)
bash third_party/official/wsl_setup.sh  # venv with mamba_ssm
~/venv_opsA/bin/python -m scripts.opsA_equivalence
bash scripts/opsA_train.sh && bash scripts/opsA_explain_all.sh   # -> results/opsA/analysis.md
```

`python -m scripts.bench_train --help` and `python -m scripts.bench_explain --help` list all options.

## Licence

MIT, see [LICENSE](LICENSE). The third-party code fetched by `setup_external.sh` keeps its own terms.
