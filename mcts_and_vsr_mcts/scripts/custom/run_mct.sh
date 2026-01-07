#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./run_scibench.sh case1 run5 feynman neg_nmse
#
# Arguments:
#   $1 = case name (case1 or case2)
#   $2 = run name  (run5, run6, ...)
#   $3 = production_rule_mode (feynman, livermore2, ...)
#   $4 = metric_name (neg_nmse, neg_nrmse, ...)

CASE="${1}"
RUN="${2}"
MODE="${3}"
METRIC="${4}"

BASE=~/workspace/scibench
EQ_FILE="${BASE}/data/unencrypted/custom_equations/${CASE}_report.in"
OUT_DIR="${BASE}/result/report_tests/${CASE}/${RUN}"
DATA_DIR="${OUT_DIR}/generated_data"

mkdir -p "${DATA_DIR}"
mkdir -p "${OUT_DIR}"

# (Optional) clean old files in run dir (uncomment if you want it each time)
# rm -f "${OUT_DIR}"/*.out "${OUT_DIR}"/pid.txt
# rm -f "${DATA_DIR}"/*

# Environment flags
export SCIBENCH_SAVE_X=1
export SCIBENCH_EQ_FILE="${EQ_FILE}"
export SCIBENCH_RUN_TAG="${CASE}_${RUN}"
export SCIBENCH_SAVE_DIR="${DATA_DIR}"

# If you're also saving QN:
# export SCIBENCH_SAVE_QN=1
# export SCIBENCH_SAVE_QN_EVERY=5
# export SCIBENCH_SAVE_QN_TOPK=2000

cd "${BASE}/mcts_and_vsr_mcts"

# NOTE: --cv_mcts is "moved" here (placed right after python main.py)
nohup timeout 48h python main.py \
  --equation_name "${EQ_FILE}" \
  --optimizer L-BFGS-B \
  --metric_name "${METRIC}" \
  --num_per_episodes 30 \
  --noise_type normal \
  --noise_scale 0.0 \
  --production_rule_mode "${MODE}" \
  > "${OUT_DIR}/$(date +%F)_${CASE}_${RUN}_${MODE}_${METRIC}.out" 2>&1 &

echo $! > "${OUT_DIR}/pid.txt"

echo "Started ${CASE}/${RUN} (PID $(cat "${OUT_DIR}/pid.txt"))"
echo "Output: $(ls -1t "${OUT_DIR}"/*.out | head -n 1)"
echo "Data dir: ${DATA_DIR}"
