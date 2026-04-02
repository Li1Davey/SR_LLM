#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./run_mct.sh case1 run300 livermore2 neg_nmse 5000 40 1
# The third argument is the grammar mode. Prefer 'livermore2' for the current
# search because it includes coefficiented variable atoms like C*Xi and C/Xi.

CASE="${1}"
RUN="${2}"
MODE="${3}"
METRIC="${4}"
NUM_EPISODES="${5:-1000}"
ROLLOUTS="${6:-40}"
KEY="${7:-0}"   # 0=disable LLM production-rule generation, 1=enable

BASE=~/workspace/scibench
EQ_FILE="${BASE}/data/unencrypted/custom_equations/${CASE}_report.in"
OUT_DIR="${BASE}/result/report_tests/${CASE}/${RUN}"
QN_DIR="${OUT_DIR}/qn_logs"
SUPEXP_FILE="${OUT_DIR}/supexp.txt"

mkdir -p "${OUT_DIR}" "${QN_DIR}"

unset SCIBENCH_SAVE_X
unset SCIBENCH_SAVE_DIR

export SCIBENCH_SAVE_QN=1
export SCIBENCH_SAVE_QN_EVERY="${SCIBENCH_SAVE_QN_EVERY:-500}"
export SCIBENCH_SAVE_QN_TOPK=2000
export SCIBENCH_MAX_LEN="${SCIBENCH_MAX_LEN:-30}"
export SCIBENCH_ETA="${SCIBENCH_ETA:-0.9999}"
export SCIBENCH_BATCH_SIZE="${SCIBENCH_BATCH_SIZE:-256}"
export SCIBENCH_MAX_OPT_ITER="${SCIBENCH_MAX_OPT_ITER:-100}"
export SCIBENCH_PRINT_FREQ="${SCIBENCH_PRINT_FREQ:-20}"
export SCIBENCH_QN_DIR="${QN_DIR}"
export SCIBENCH_VERBOSE="${SCIBENCH_VERBOSE:-0}"
export SCIBENCH_EQ_FILE="${EQ_FILE}"
export SCIBENCH_RUN_TAG="${CASE}_${RUN}"

BASE_SUPEXP="${BASE}/mcts_and_vsr_mcts/supexp.txt"
if [[ -f "${BASE_SUPEXP}" ]]; then
  cp -f "${BASE_SUPEXP}" "${SUPEXP_FILE}"
else
  : > "${SUPEXP_FILE}"
fi
export SCIBENCH_SUPEXP_FILE="${SUPEXP_FILE}"
export SCIBENCH_SUPEXP_USE=1

if [[ "${KEY}" == "1" ]]; then
  export SCIBENCH_PR_FEEDBACK_ENABLE=1
  export SCIBENCH_PR_MODEL="${SCIBENCH_PR_MODEL:-gpt-4.1-mini}"
  export SCIBENCH_PR_TIMEOUT_SECONDS="${SCIBENCH_PR_TIMEOUT_SECONDS:-5}"
  export SCIBENCH_PR_MIN_HOF="${SCIBENCH_PR_MIN_HOF:-2}"
  export SCIBENCH_PR_MIN_HOF_CHANGES="${SCIBENCH_PR_MIN_HOF_CHANGES:-8}"
  export SCIBENCH_PR_MIN_BEST_REWARD="${SCIBENCH_PR_MIN_BEST_REWARD:--1e9}"
  export SCIBENCH_PR_MIN_REWARD_DELTA="${SCIBENCH_PR_MIN_REWARD_DELTA:-0.0}"
  export SCIBENCH_PR_MAX_CALLS="${SCIBENCH_PR_MAX_CALLS:-40}"
  export SCIBENCH_PR_COOLDOWN_SECONDS="${SCIBENCH_PR_COOLDOWN_SECONDS:-300}"

  if [[ -z "${OPENAI_API_KEY:-}" ]]; then
    echo "[ERROR] KEY=1 but OPENAI_API_KEY is not set"
    exit 1
  fi

  echo "[INFO] LLM production-rule feedback ENABLED"
  echo "[INFO] Per-run supexp file: ${SUPEXP_FILE}"
else
  export SCIBENCH_PR_FEEDBACK_ENABLE=0
  echo "[INFO] LLM production-rule feedback disabled"
fi

cd "${BASE}/mcts_and_vsr_mcts"

OUT_FILE="${OUT_DIR}/$(date +%F)_${CASE}_${RUN}_${MODE}_${METRIC}_ep${NUM_EPISODES}.out"

nohup timeout 96h python main.py   --equation_name "${EQ_FILE}"   --optimizer L-BFGS-B   --metric_name "${METRIC}"   --num_episodes "${NUM_EPISODES}"   --num_per_episodes "${ROLLOUTS}"   --noise_type normal   --noise_scale 0.0   --production_rule_mode "${MODE}"   > "${OUT_FILE}" 2>&1 &

echo $! > "${OUT_DIR}/pid.txt"

echo "Started ${CASE}/${RUN} (PID $(cat "${OUT_DIR}/pid.txt"))"
echo "Output: ${OUT_FILE}"
echo "QN logs: ${QN_DIR}"
echo "supexp file: ${SUPEXP_FILE}"
