# Vendored from PriorCast

Unmodified copies from https://github.com/alpermana14/PriorCast
(commit 39cec7f997508d848f87ad0e9326c003adb573c0, 2026-08-10):

- `mamba_block.py`    ← `models/components/mamba_block.py`
- `dataset_loader.py` ← `evaluation/dataset_loader.py`
- `metrics.py`        ← `evaluation/metrics.py`

Do not edit these files; extend them from `src/` instead. On the GPU machine this
folder can be replaced by a git submodule pinned to the same commit.

PriorCast is an earlier project by the same author. It is **not** one of the evaluated
forecasters. Only its plain-PyTorch Mamba layer, data split and metrics are reused here,
and these copies are released under the MIT licence of this repository.
