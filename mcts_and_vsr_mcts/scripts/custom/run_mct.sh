#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./run_mct.sh practice run1 feynman neg_nmse [NUM_EPISODES] [ROLLOUTS] [MAX_LEN] [ETA]

CASE="${1}"
RUN="${2}"
MODE="${3}"
METRIC="${4}"
NUM_EPISODES="${5:-1000}"   # default = 1000
ROLLOUTS="${6:-40}"
MAX_LEN="${7:-20}"
ETA="${8:-0.99}"

BASE=~/workspace/scibench
EQ_FILE="${BASE}/data/unencrypted/custom_equations/${CASE}_report.in"report
OUT_DIR="${BASE}/result/report_tests/${CASE}/${RUN}"
DATA_DIR="${OUT_DIR}/generated_data"
QN_DIR="${OUT_DIR}/qn_logs"

mkdir -p "${DATA_DIR}" "${QN_DIR}" "${OUT_DIR}"

# -----------------------
# Save generated X
# -----------------------
export SCIBENCH_SAVE_X=1
export SCIBENCH_EQ_FILE="${EQ_FILE}"
export SCIBENCH_RUN_TAG="${CASE}_${RUN}"
export SCIBENCH_SAVE_DIR="${DATA_DIR}"

# -----------------------
# Save QN snapshots
# -----------------------
export SCIBENCH_SAVE_QN=1
export SCIBENCH_SAVE_QN_EVERY=5
export SCIBENCH_SAVE_QN_TOPK=2000
export SCIBENCH_QN_DIR="${QN_DIR}"

cd "${BASE}/mcts_and_vsr_mcts"

nohup timeout 48h python main.py \
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
  > "${OUT_DIR}/$(date +%F)_${CASE}_${RUN}_${MODE}_${METRIC}_ep${NUM_EPISODES}.out" 2>&1 &

echo $! > "${OUT_DIR}/pid.txt"

echo "Started ${CASE}/${RUN} (PID $(cat "${OUT_DIR}/pid.txt"))"
echo "Episodes: ${NUM_EPISODES}"
echo "Output: $(ls -1t "${OUT_DIR}"/*.out | head -n 1)"
echo "Data dir: ${DATA_DIR}"
echo "QN dir: ${QN_DIR}"
