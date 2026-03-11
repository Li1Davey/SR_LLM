#!/usr/bin/env bash
set -euo pipefail

CASE="${1}"
RUN="${2}"
MODE="${3}"
METRIC="${4}"
STAGE="${5:-1}"          # 1 or 2
NUM_EPISODES="${6:-1000}"
ROLLOUTS="${7:-40}"
MAX_LEN="${8:-20}"
ETA="${9:-0.99}"
KEY="${10:-0}"   # 0 = no LLM supexp generation, 1 = enable LLM supexp generation

BASE=~/workspace/scibench
EQ_FILE="${BASE}/data/unencrypted/custom_equations/${CASE}_report.in"
OUT_DIR="${BASE}/result/report_tests/${CASE}/${RUN}/stage${STAGE}"
DATA_DIR="${OUT_DIR}/generated_data"
QN_DIR="${OUT_DIR}/qn_logs"
mkdir -p "${DATA_DIR}" "${QN_DIR}" "${OUT_DIR}"

# -----------------------
# Numerical safety (critical)
# -----------------------
export SCIBENCH_PROTECTED=1
export SCIBENCH_PROTECTED_EPS=1e-6
export SCIBENCH_EXP_CLIP=50
export SCIBENCH_POW_ABS_CLIP=1e6

# Avoid X0 ~= X1 degeneracy (important for stage 2)
export SCIBENCH_ENSURE_X0_NE_X1=1
export SCIBENCH_XPAIR_EPS=1e-12
export SCIBENCH_XPAIR_REL_EPS=1e-6
export SCIBENCH_XPAIR_MAX_TRIES=200

# -----------------------
# Curriculum controls
# -----------------------
if [[ "${STAGE}" == "1" ]]; then
  export SCIBENCH_SAFE_GRAMMAR=1
  export SCIBENCH_USE_DELTA=1
  export SCIBENCH_DELTA_BASE_IDX=0
  export SCIBENCH_DELTA_VAR_IDX=1
  export SCIBENCH_MAX_OPT_ITER=25
else
  export SCIBENCH_USE_DELTA=0
  export SCIBENCH_MAX_OPT_ITER=150
fi

# -------------------------------------------------
# LLM supexp feedback (optional)
# -------------------------------------------------
if [[ "${KEY}" == "1" ]]; then
  export SCIBENCH_SUPEXP_ENABLE=1
  export SCIBENCH_SUPEXP_FILE="${OUT_DIR}/supexp.txt"
  export SCIBENCH_SUPEXP_AUTO_APPEND=1
  export SCIBENCH_SUPEXP_TOPK=8
  export SCIBENCH_SUPEXP_COOLDOWN_SECONDS=120
  export SCIBENCH_SUPEXP_MIN_HOF=2
  export SCIBENCH_SUPEXP_MIN_BEST_REWARD=0.5
  export SCIBENCH_SUPEXP_MIN_REWARD_DELTA=0.05
  export SCIBENCH_SUPEXP_MAX_CALLS=40
  export SCIBENCH_SUPEXP_MIN_HOF_CHANGES=4

  if [[ -z "${OPENAI_API_KEY:-}" ]]; then
    echo "[ERROR] KEY=1 but OPENAI_API_KEY is not set"
    exit 1
  fi

  echo "[INFO] LLM supexp feedback ENABLED"
else
  export SCIBENCH_SUPEXP_ENABLE=0
  export SCIBENCH_SUPEXP_FILE="${OUT_DIR}/supexp.txt"
  export SCIBENCH_SUPEXP_AUTO_APPEND=0
  echo "[INFO] LLM supexp feedback disabled"
fi

# -----------------------
# Save generated X (debugging)
# -----------------------
export SCIBENCH_SAVE_X=1
export SCIBENCH_EQ_FILE="${EQ_FILE}"
export SCIBENCH_RUN_TAG="${CASE}_${RUN}_stage${STAGE}"
export SCIBENCH_SAVE_DIR="${DATA_DIR}"

# -----------------------
# Save QN snapshots
# -----------------------
export SCIBENCH_SAVE_QN=1
export SCIBENCH_SAVE_QN_EVERY=5
export SCIBENCH_SAVE_QN_TOPK=2000
export SCIBENCH_QN_DIR="${QN_DIR}"

cd "${BASE}/mcts_and_vsr_mcts"

OUT_FILE="${OUT_DIR}/$(date +%F)_${CASE}_${RUN}_stage${STAGE}_${MODE}_${METRIC}_ep${NUM_EPISODES}.out"

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

echo "Started ${CASE}/${RUN} stage=${STAGE} (PID $(cat "${OUT_DIR}/pid.txt"))"
echo "Output: ${OUT_FILE}"
echo "Data dir: ${DATA_DIR}"
echo "QN dir: ${QN_DIR}"