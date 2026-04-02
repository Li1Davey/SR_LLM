# Monte Carlo Tree Search for Symbolic Regression and Adaptation to Control Variable Experimentation

This repository contains an MCTS-based symbolic regression workflow adapted from **SymbolicPhysicsLearner**.

Recent updates include:
- improved constant fitting with multi-start optimization
- bounded handling for sensitive constants in exponentials and denominators
- a penalty for collapsed or near-constant predictions
- same-run activation of accepted OpenAI-generated production rules
- search improvements for MCTS, including better rollout behavior and softer action selection
- hall-of-fame ordering kept in **ascending reward order** (lowest to highest)

## Run the model

Launch experiments with:

```bash
./run_mct.sh CASE RUN MODE METRIC [NUM_EPISODES] [ROLLOUTS] [KEY]