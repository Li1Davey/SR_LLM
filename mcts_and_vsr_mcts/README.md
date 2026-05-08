# Symbolic Regression with MCTS and LLM

> **Attribution:** The core MCTS algorithm is based on the original implementation
> by Jiang et al. The LLM rule-suggestion pipeline (`suggester.py`), robustness
> guards in `program.py` and `mcts_model.py`, the experiment shell script
> (`run_experiment.sh`), and the plotting utility (`plot_results.py`) are
> extensions added to the original codebase.
> Original repository: [jiangnanhugo/cvgp](https://github.com/jiangnanhugo/cvgp)

---

## Overview

This module implements symbolic regression using Monte Carlo Tree Search (MCTS)
with an optional LLM co-pilot. The search builds mathematical expressions by
expanding a context-free grammar (CFG) parse tree. When LLM suggestions are
enabled, the system periodically queries a language model to propose new
production rules based on the best expressions found so far, dynamically
growing the grammar during the run.

---

## Requirements

```bash
pip install -r requirements.txt
```

To use LLM rule suggestions, set your OpenAI API key:

```bash
export OPENAI_API_KEY=<your-key>
```

No API key is needed when running with `use_llm=false`.

---

## Running an Experiment

```bash
bash run_experiment.sh <equation_name> <run_number> [num_episodes] [prod_rule_mode] [use_llm] [seed]
```

### Parameters

| Parameter | Required | Default | Description |
|---|---|---|---|
| `equation_name` | Yes | — | Equation file name, e.g. `kepler` |
| `run_number` | Yes | — | Unique run ID, e.g. `001` |
| `num_episodes` | No | `30` | Number of MCTS episodes |
| `prod_rule_mode` | No | `livermore2` | Grammar set: `livermore2`, `trigometric`, or `feynman` |
| `use_llm` | No | `false` | Enable LLM rule suggestions: `true` or `false` |
| `seed` | No | time-based | Integer random seed for reproducibility |

### Examples

```bash
# Run with LLM enabled, feynman grammar, 500 episodes
bash run_experiment.sh kepler 001 500 feynman true

# Run without LLM
bash run_experiment.sh kepler 001 500 feynman false

# Controlled ablation — identical seed, only LLM flag differs
bash run_experiment.sh kepler 100a 2000 feynman false 42
bash run_experiment.sh kepler 100b 2000 feynman true  42
```

Results, logs, and the exact command are saved to
`~/workspace/scibench/results/<equation_name>_<run_number>/`.

---

## File Reference

| File | Description |
|---|---|
| `main.py` | Entry point — argument parsing and MCTS launch |
| `mcts_model.py` | MCTS algorithm, UCB policy, HOF, and LLM integration |
| `suggester.py` | LLM prompt construction, rule parsing, and validation pipeline |
| `program.py` | Expression optimization, constant fitting, and reward evaluation |
| `regress_task.py` | Data batch management and oracle interface |
| `production_rules.py` | Grammar for the `livermore2` operator set |
| `production_rules_feynman.py` | Grammar for Feynman physics equations |
| `production_rules_trigometric.py` | Grammar with per-variable sin/cos terminals |
| `utils.py` | Helper functions: pretty-printing, template conversion, generation schedules |
| `run_experiment.sh` | Shell script for launching and logging experiments |
| `plot_results.py` | Plot best-reward-vs-iterations and best-reward-vs-time from run logs |

---

## Component Details

### MCTS Core (original)

The MCTS algorithm builds symbolic expressions by iteratively expanding a
CFG parse tree, maintaining a Hall of Fame (HOF) of the highest-reward
expressions and balancing exploration vs. exploitation through UCB scores
with epsilon-decay.

### Production Rules

Three grammar modules are provided, selectable via `--production_rule_mode`:

- **`livermore2`** — general operator set with optional `sin`, `cos`, `exp`, `log`, `sqrt`, power rules (`n2`–`n5`), and `C/Xi` inverse terminals.
- **`feynman`** — like `livermore2` but terminals emit bare `Xi` without an implicit constant factor, suited for dimensionally-clean Feynman benchmark equations.
- **`trigometric`** — terminals include `C*sin(Xi)` and `C*cos(Xi)` directly, better for equations with known harmonic structure.

### LLM Integration (extension)

When `use_llm=true`, the system queries an OpenAI model every
`num_episodes // 10` episodes. The `suggester.py` pipeline:

1. **Filters** the HOF to a diverse, length-bounded set of expressions.
2. **Builds** a structured prompt with skeleton-analysis instructions, a covered-skeletons summary, and optional trig/domain warnings.
3. **Validates** returned rules: format, deduplication (parenthesis-insensitive), and allowed-token checks.
4. **Rejects** domain-unsafe rules (e.g. `log`/`sqrt` when the domain includes zero; trig over very large ranges).
5. **Logs** every call — prompt, raw response, accepted and rejected rules — to `llm_rule_history.log`.

LLM calls are skipped automatically when the reward threshold is already met
or when the reward has not improved since the previous call. Temperature is
escalated on consecutive empty calls to encourage novel suggestions.

### Expression Optimization

Each candidate expression passes a series of guards before constant fitting:

- Rejects oversized template strings (> 200 chars).
- Rejects chained power towers and exponents > 50.
- Rejects expressions with no free variables.
- Rejects deeply nested unary functions (> 6 calls of the same op).
- Rejects nesting depth > 12 parenthesis levels.

Constants are fitted by `scipy.optimize` (default: `L-BFGS-B`). Post-fit
guards reject expressions that collapse to zero everywhere or simplify to a
bare number.

---

## Plotting Results

```bash
# Single run
python plot_results.py ~/workspace/scibench/results/kepler_001/

# Compare two runs
python plot_results.py ~/workspace/scibench/results/kepler_100a/ \
                       ~/workspace/scibench/results/kepler_100b/
```

Produces `reward_vs_iterations.png` and `reward_vs_time.png` in the first
run's directory.

---

## Reproducibility

Each run prints its random seed at startup and saves the exact launch command
to `command.txt` in the results directory. Pass an explicit `seed` argument to
reproduce a run or create a matched pair for ablation.

---

## Citation

If you use or build on this code, please cite the original work:

```bibtex
@inproceedings{jiang2023mcts,
  title     = {..},
  author    = {Jiang, Nan and others},
  booktitle = {Proceedings of ...},
  year      = {2023}
}
```

> **Note:** Replace the placeholder above with the full citation from the published paper.