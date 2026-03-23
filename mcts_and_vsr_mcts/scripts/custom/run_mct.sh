#!/usr/bin/env bash
set -euo pipefail

CASE="${1}"
RUN="${2}"
MODE="${3}"
METRIC="${4}"
NUM_EPISODES="${5:-1000}"
ROLLOUTS="${6:-40}"
MAX_LEN="${7:-20}"
ETA="${8:-1.0}"
KEY="${9:-0}"   # 0 = no LLM supexp generation, 1 = enable LLM supexp generation

BASE=~/workspace/scibench
EQ_FILE="${BASE}/data/unencrypted/custom_equations/${CASE}_report.in"
OUT_DIR="${BASE}/result/report_tests/${CASE}/${RUN}"
QN_DIR="${OUT_DIR}/qn_logs"
mkdir -p "${OUT_DIR}" "${QN_DIR}"

# Each run gets its own supexp.txt, initialized from the base file.
# This prevents cross-run contamination while still letting each run
# start from the shared base supexp rules.
SUPEXP_FILE="${OUT_DIR}/supexp.txt"
BASE_SUPEXP="${BASE}/mcts_and_vsr_mcts/supexp.txt"

if [[ -f "${BASE_SUPEXP}" ]]; then
  cp "${BASE_SUPEXP}" "${SUPEXP_FILE}"
else
  echo "# auto-generated supexp suggestions will be appended below" > "${SUPEXP_FILE}"
fi

# Remove all scibench env overrides tied to modified sampling / grammar / token behavior
unset SCIBENCH_PROTECTED
unset SCIBENCH_PROTECTED_EPS
unset SCIBENCH_EXP_CLIP
unset SCIBENCH_POW_ABS_CLIP

unset SCIBENCH_ENSURE_X0_NE_X1
unset SCIBENCH_XPAIR_EPS
unset SCIBENCH_XPAIR_REL_EPS
unset SCIBENCH_XPAIR_MAX_TRIES

unset SCIBENCH_SAFE_GRAMMAR
unset SCIBENCH_USE_DELTA
unset SCIBENCH_DELTA_BASE_IDX
unset SCIBENCH_DELTA_VAR_IDX
unset SCIBENCH_DELTA_CLAMP
unset SCIBENCH_MAX_OPT_ITER

unset SCIBENCH_SAVE_X
unset SCIBENCH_SAVE_DIR

# Keep QN diagnostics enabled without restoring curriculum
export SCIBENCH_SAVE_QN=1
export SCIBENCH_SAVE_QN_EVERY="${SCIBENCH_SAVE_QN_EVERY:-500}"
export SCIBENCH_SAVE_QN_TOPK=2000
export SCIBENCH_QN_DIR="${QN_DIR}"
export SCIBENCH_EQ_FILE="${EQ_FILE}"
export SCIBENCH_RUN_TAG="${CASE}_${RUN}"

# LLM supexp feedback
if [[ "${KEY}" == "1" ]]; then
  export SCIBENCH_SUPEXP_ENABLE=1
  export SCIBENCH_SUPEXP_FILE="${SUPEXP_FILE}"
  export SCIBENCH_SUPEXP_AUTO_APPEND=1
  export SCIBENCH_SUPEXP_TOPK=8
  export SCIBENCH_SUPEXP_COOLDOWN_SECONDS=120
  export SCIBENCH_SUPEXP_MIN_HOF=2
  export SCIBENCH_SUPEXP_MIN_BEST_REWARD=0.5
  export SCIBENCH_SUPEXP_MIN_REWARD_DELTA=0.05
  export SCIBENCH_SUPEXP_MAX_CALLS=40
  export SCIBENCH_SUPEXP_MIN_HOF_CHANGES=4
  export SCIBENCH_SUPEXP_USE=1
  export SCIBENCH_SUPEXP_SEED_DEFAULTS=1
  export SCIBENCH_SUPEXP_PREFER_HEURISTICS_FIRST=1
  export SCIBENCH_SUPEXP_REQUIRE_APPEND_GAIN=1
  export SCIBENCH_BATCHSIZE=256

  if [[ -z "${OPENAI_API_KEY:-}" ]]; then
    echo "[ERROR] KEY=1 but OPENAI_API_KEY is not set"
    exit 1
  fi

  echo "[INFO] LLM supexp feedback ENABLED"
  echo "[INFO] Run-local supexp file initialized from: ${BASE_SUPEXP}"
  echo "[INFO] New suggestions will append only to: ${SUPEXP_FILE}"
else
  export SCIBENCH_SUPEXP_ENABLE=0
  export SCIBENCH_SUPEXP_FILE="${SUPEXP_FILE}"
  export SCIBENCH_SUPEXP_AUTO_APPEND=0
  echo "[INFO] LLM supexp feedback disabled"
  echo "[INFO] Run-local supexp file initialized from: ${BASE_SUPEXP}"
fi

cd "${BASE}/mcts_and_vsr_mcts"

OUT_FILE="${OUT_DIR}/$(date +%F)_${CASE}_${RUN}_${MODE}_${METRIC}_ep${NUM_EPISODES}.out"

nohup timeout 96h python main.py \
  --equation_name "${EQ_FILE}" \
  --optimizer L-BFGS-B \
  --metric_name "${METRIC}" \
  --num_episodes "${NUM_EPISODES}" \
  --num_rollouts "${ROLLOUTS}" \
  --max_len "${MAX_LEN}" \
  --eta "${ETA}" \
  --noise_type normal \
  --noise_scale 0.0 \
  --production_rule_mode "${MODE}" \
  > "${OUT_FILE}" 2>&1 &

echo $! > "${OUT_DIR}/pid.txt"

echo "Started ${CASE}/${RUN} (PID $(cat "${OUT_DIR}/pid.txt"))"
echo "Output: ${OUT_FILE}"
echo "QN logs: ${QN_DIR}"
echo "supexp file for this run: ${SUPEXP_FILE}"