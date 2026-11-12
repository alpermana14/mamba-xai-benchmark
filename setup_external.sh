#!/usr/bin/env bash
# Fetch the third-party code this benchmark runs but does not redistribute, at the pinned commits.
#   GroupSegment-SHAP and S-D-Mamba carry no licence, so they are cloned, never copied into this repo.
#   TimeMachine (Apache-2.0) is cloned the same way for consistency.
# Two one-line fixes are applied to the official clones (NumPy 2 removed np.Inf; S-Mamba reads its seed from $SEED).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

clone() {  # url dir commit
  if [ ! -d "$2/.git" ]; then git clone -q "$1" "$2"; fi
  git -C "$2" checkout -q "$3"
  echo "$2 @ $3"
}

clone https://github.com/jirungx/GroupSegment-SHAP.git "$ROOT/external/GroupSegment-SHAP" 8ed7e2a57d0461a1fd9ba6ba7bc6ab6b44df2b3e
clone https://github.com/wzhwzhwzh0921/S-D-Mamba.git   "$ROOT/third_party/official/S-D-Mamba" e7e8bf04066135afa43d85b0a87afa97cda16e3f
clone https://github.com/Atik-Ahamed/TimeMachine.git   "$ROOT/third_party/official/TimeMachine" 5bf17a728349c674eceafc28a90f22b904e38c2d

SDM="$ROOT/third_party/official/S-D-Mamba"
sed -i 's/np\.Inf/np.inf/g' "$SDM/utils/tools.py" "$ROOT/third_party/official/TimeMachine/TimeMachine_supervised/utils/tools.py"
sed -i "s/^\(\s*\)fix_seed = 2023/\1fix_seed = int(__import__('os').environ.get('SEED', '2023'))/" "$SDM/run.py"
echo "patched np.Inf and the S-Mamba seed"
