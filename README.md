# Symbolic Regression with MCTS and LLM

> **Based on** the original MCTS symbolic regression framework by Jiang et al.
> LLM rule-suggestion pipeline, robustness guards, and experiment tooling
> added as extensions. See [Citation](#citation) below.

---

## Directory Structure

### Data Oracle

| Path | Description |
| --- | --- |
| `data/` | Generated datasets. Each file encodes a ground-truth expression. |
| `src/scibench/` | Data-oracle API (`Equation_evaluator`, `DataX`). |

The framework exposes an active data-query oracle so the search algorithm
draws fresh batches on demand, rather than loading a static CSV.

### Method Implementations

| Folder | Method |
| --- | --- |
| `mcts_and_mcts_llm/` | MCTS with optional LLM grammar expansion (this work) |
| `src/` | Shared source modules and the `scibench` data-oracle package |

### Results & Outputs

| Folder | Description |
| --- | --- |
| `results/` | Training logs and program outputs |

---

## Installation

```bash
pip install -r requirements.txt
```

Install the data oracle:

```bash
cd src/scibench
pip install -e .
```

### Method-specific setup

- **MCTS / MCTS-LLM** → `mcts_and_mcts_llm/`

Each sub-folder contains a `README.md` and `scripts/` with run instructions.

---

## Citation

If you use this codebase, please cite the original work:

```bibtex
@article{jiang2023vertical,
  title     = {Vertical Symbolic Regression},
  author    = {Jiang, Nan and Nasim, Md and Xue, Yexiang},
  journal   = {arXiv preprint arXiv:2312.11955},
  year      = {2023}
}
```