#!/usr/bin/env bash
# Opsi A: explain all 12 official checkpoints (after scripts/opsA_train.sh), then analyse. Run inside WSL:
#   bash scripts/opsA_explain_all.sh
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="$HOME/venv_opsA/bin/python"
cd "$ROOT"
stamp() { date +%H:%M:%S; }
for seed in 0 1 2; do
  for data in etth1 weather; do
    for model in smamba timemachine; do
      run="results/opsA/${model}_${data}_s${seed}"
      if [ -f "$run/xai/per_window.csv" ] && [ "$(wc -l < "$run/xai/per_window.csv")" -gt 600 ]; then
        echo "[$(stamp)] skip $run"; continue
      fi
      if ! ls "results/opsA/ckpt/${model}_${data}_s${seed}"/*/checkpoint.pth >/dev/null 2>&1; then
        echo "[$(stamp)] NO CHECKPOINT $run"; continue
      fi
      echo "[$(stamp)] explain $run"
      $PY -m scripts.opsA_explain --model $model --dataset $data --seed $seed > "$run.explain.log" 2>&1
      echo "[$(stamp)] done $run exit $? | $(grep -m1 'test MSE' "$run.explain.log")"
    done
  done
done
$PY -m scripts.opsA_analyze
echo "[$(stamp)] ALL DONE"
