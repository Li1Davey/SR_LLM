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
