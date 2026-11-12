#!/usr/bin/env bash
# Opsi A (plan §12, 2026-11-11): train the OFFICIAL S-Mamba and TimeMachine at H = 96 on ETTh1 and
# Weather with the arguments of their own scripts, seeds 0 1 2. Run inside WSL:
#   bash scripts/opsA_train.sh            (SEEDS="0" bash scripts/opsA_train.sh for one seed)
# Checkpoints: results/opsA/ckpt/<model>_<data>_s<seed>/<official setting>/checkpoint.pth
# Logs:        results/opsA/logs/<model>_<data>_s<seed>.log
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="$HOME/venv_opsA/bin/python"
OUT="$ROOT/results/opsA"
mkdir -p "$OUT/ckpt" "$OUT/logs"
SEEDS="${SEEDS:-0 1 2}"
stamp() { date +%H:%M:%S; }

run_smamba() {                      # $1 data  $2 seed
  local data=$1 seed=$2 ck="$OUT/ckpt/smamba_$1_s$2" log="$OUT/logs/smamba_$1_s$2.log"
  if ls "$ck"/*/checkpoint.pth >/dev/null 2>&1; then echo "[$(stamp)] skip smamba $data s$seed"; return; fi
  mkdir -p "$ck"
  cd "$ROOT/third_party/official/S-D-Mamba"
  if [ "$data" = etth1 ]; then
    # scripts/multivariate_forecasting/ETT/S_Mamba_ETTh1.sh, block ETTh1_96_96
    SEED=$seed $PY -u run.py --is_training 1 --root_path "$ROOT/dataset/ETT-small/" --data_path ETTh1.csv \
      --model_id ETTh1_96_96 --model S_Mamba --data ETTh1 --features M --seq_len 96 --pred_len 96 \
      --e_layers 2 --enc_in 7 --dec_in 7 --c_out 7 --des 'Exp' --d_model 256 --d_state 2 --d_ff 256 --itr 1 \
      --learning_rate 0.00007 --checkpoints "$ck/" > "$log" 2>&1
  else
    # scripts/multivariate_forecasting/Weather/S_Mamba.sh, block weather_96_96
    SEED=$seed $PY -u run.py --is_training 1 --root_path "$ROOT/dataset/weather/" --data_path weather.csv \
      --model_id weather_96_96 --model S_Mamba --data custom --features M --seq_len 96 --pred_len 96 \
      --e_layers 3 --enc_in 21 --dec_in 21 --c_out 21 --des 'Exp' --d_model 512 --learning_rate 0.00005 \
      --train_epochs 5 --d_state 2 --d_ff 512 --itr 1 --checkpoints "$ck/" > "$log" 2>&1
  fi
  echo "[$(stamp)] smamba $data s$seed exit $? | $(grep -oE 'mse:[0-9.]+' "$log" | tail -1)"
}

run_timemachine() {                 # $1 data  $2 seed
  local data=$1 seed=$2 ck="$OUT/ckpt/timemachine_$1_s$2" log="$OUT/logs/timemachine_$1_s$2.log"
  if ls "$ck"/*/checkpoint.pth >/dev/null 2>&1; then echo "[$(stamp)] skip timemachine $data s$seed"; return; fi
  mkdir -p "$ck"
  cd "$ROOT/third_party/official/TimeMachine/TimeMachine_supervised"
  mkdir -p logs/LongForecasting csv_results results test_results
  if [ "$data" = etth1 ]; then
    # scripts/TimeMachine/etth1.sh, branch pred_len 96
    $PY -u run_longExp.py --random_seed $seed --is_training 1 --root_path "$ROOT/dataset/ETT-small" \
      --data_path ETTh1.csv --model_id ETTh1_96_96 --model TimeMachine --data ETTh1 --features M \
      --seq_len 96 --pred_len 96 --enc_in 7 --n1 512 --n2 32 --dropout 0.7 --revin 1 --ch_ind 1 --residual 1 \
      --dconv 2 --d_state 256 --e_fact 1 --des 'Exp' --train_epochs 100 --itr 1 --batch_size 512 \
      --learning_rate 0.001 --checkpoints "$ck/" > "$log" 2>&1
  else
    # scripts/TimeMachine/weather.sh, branch pred_len 96
    $PY -u run_longExp.py --random_seed $seed --is_training 1 --root_path "$ROOT/dataset/weather" \
      --data_path weather.csv --model_id weather_96_96 --model TimeMachine --data custom --features M \
      --seq_len 96 --pred_len 96 --enc_in 21 --n1 128 --n2 16 --dropout 0.1 --revin 1 --ch_ind 1 --residual 1 \
      --dconv 2 --d_state 256 --e_fact 1 --des 'Exp' --lradj 'constant' --pct_start 0.2 --itr 1 \
      --batch_size 512 --learning_rate 0.001 --checkpoints "$ck/" > "$log" 2>&1
  fi
  echo "[$(stamp)] timemachine $data s$seed exit $? | $(grep -oE 'mse:[0-9.]+' "$log" | tail -1)"
}

for seed in $SEEDS; do
  for data in etth1 weather; do
    run_smamba $data $seed
    run_timemachine $data $seed
  done
done
echo "[$(stamp)] ALL DONE"
