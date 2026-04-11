# Monte Carlo Tree Search for Symbolic Regression

This repository contains an MCTS-based symbolic regression workflow adapted from **SymbolicPhysicsLearner**.

## Recent Updates

- LLM-guided grammar expansion: an OpenAI model is queried periodically during search to suggest new production rules, which are validated and integrated into the MCTS grammar in the same run
- Expression safety guards: hard rejection of expressions with astronomically large exponents, oversized string templates, and non-finite rewards before they reach the optimizer
- Fan-out guard: LLM-suggested rules that introduce more than 3 non-terminal nodes are rejected to prevent exponential tree blowup
- UCB policy fix: uniform fallback when all scores are identical or sum to zero, preventing NaN propagation into the search tree
- Hall-of-fame confirmed-entry gating: improvement is only flagged after an expression is verified to have entered the hall of fame, not just because it is unique

## Run the Model

Launch experiments with:

```bash
bash run_experiment.sh <equation_name> <run_number> [num_episodes] [prod_rule_mode] [extra args]
