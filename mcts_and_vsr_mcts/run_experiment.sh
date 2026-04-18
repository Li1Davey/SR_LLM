#!/bin/bash
# Usage:
#   bash run_experiment.sh <equation_name> <run_number> [num_episodes] [prod_rule_mode] [use_llm] [seed]
#
# Examples:
#   bash run_experiment.sh kepler  001 500 feynman true  42
#   bash run_experiment.sh kepler  001 500 feynman false 42
#   bash run_experiment.sh pendulum 001 500 trigometric false

EQ_NAME="$1"
RUN_NUM="$2"
NUM_EPISODES="${3:-30}"
PROD_RULE_MODE="${4:-livermore2}"
USE_LLM="${5:-false}"
SEED="${6:-}"

# Validate production_rule_mode
if [[ "$PROD_RULE_MODE" != "livermore2" && "$PROD_RULE_MODE" != "trigometric" && "$PROD_RULE_MODE" != "feynman" ]]; then
    echo "ERROR: Invalid production_rule_mode '$PROD_RULE_MODE'"
    echo "       Must be one of: livermore2 | trigometric | feynman"
    exit 1
fi

# Validate use_llm
if [[ "$USE_LLM" != "true" && "$USE_LLM" != "false" ]]; then
    echo "ERROR: Invalid use_llm '$USE_LLM'"
    echo "       Must be one of: true | false"
    exit 1
fi

# Validate seed if provided
if [[ -n "$SEED" && ! "$SEED" =~ ^[0-9]+$ ]]; then
    echo "ERROR: Invalid seed '$SEED'"
    echo "       Must be a non-negative integer"
    exit 1
fi

SEED_ARG=""
if [[ -n "$SEED" ]]; then
    SEED_ARG="--seed $SEED"
fi

RESULTS_BASE=~/workspace/scibench/results
RUN_DIR="${RESULTS_BASE}/${EQ_NAME}_${RUN_NUM}"
mkdir -p "$RUN_DIR"

EQ_FILE="../data/unencrypted/custom_equations/${EQ_NAME}.in"
LOG_FILE="${RUN_DIR}/run.log"
PID_FILE="${RUN_DIR}/pid.txt"
SUGGEST_LOG="${RUN_DIR}/llm_rule_history.log"

echo "Equation         : $EQ_NAME"
echo "Run dir          : $RUN_DIR"
echo "Log file         : $LOG_FILE"
echo "Eq file          : $EQ_FILE"
echo "Num Episodes     : $NUM_EPISODES"
echo "Prod Rule Mode   : $PROD_RULE_MODE"
echo "Use LLM          : $USE_LLM"
if [[ "$USE_LLM" == "true" ]]; then
    echo "Suggest log      : $SUGGEST_LOG"
fi
echo "Seed             : ${SEED:-time-based}"
echo ""

cat > "${RUN_DIR}/command.txt" <<EOF
python main.py \\
  --equation_name $EQ_FILE \\
  --optimizer L-BFGS-B \\
  --metric_name neg_mse \\
  --noise_type normal \\
  --noise_scale 0.0 \\
  --num_episodes $NUM_EPISODES \\
  --num_rollouts 40 \\
  --max_opt_iter 200 \\
  --production_rule_mode $PROD_RULE_MODE \\
  --suggest_log_path $SUGGEST_LOG \\
  --use_llm $USE_LLM \\
  $SEED_ARG
EOF

nohup timeout 96h python main.py \
  --equation_name "$EQ_FILE" \
  --optimizer L-BFGS-B \
  --metric_name neg_mse \
  --noise_type normal \
  --noise_scale 0.0 \
  --num_episodes "$NUM_EPISODES" \
  --num_rollouts 40 \
  --max_opt_iter 200 \
  --production_rule_mode "$PROD_RULE_MODE" \
  --suggest_log_path "$SUGGEST_LOG" \
  --use_llm "$USE_LLM" \
  $SEED_ARG \
  > "$LOG_FILE" 2>&1 &

echo $! > "$PID_FILE"
echo "Started with PID $(cat $PID_FILE)"
echo "Tail log with:"
echo "  tail -f $LOG_FILE"
if [[ "$USE_LLM" == "true" ]]; then
    echo "Tail LLM suggestions with:"
    echo "  tail -f $SUGGEST_LOG"
fi