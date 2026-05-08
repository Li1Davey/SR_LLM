# Symbolic Regression with MCTS and LLM

> **Based on** the original MCTS symbolic regression framework by Jiang et al.
> LLM rule-suggestion pipeline, robustness guards, and experiment tooling
> added as extensions. See [Citation](#citation) below.

---

## Directory Structure

### Data Oracle

| Path | Description |
|---|---|
| `data/` | Generated datasets. Each file encodes a ground-truth expression. |
| `src/scibench/` | Data-oracle API (`Equation_evaluator`, `DataX`). |

The framework exposes an active data-query oracle so the search algorithm
draws fresh batches on demand, rather than loading a static CSV.

### Method Implementations

| Folder | Method |
|---|---|
| `dso_classic/` | DSR, PQT, VPG, GPMeld — from [brendenpetersen/deep-symbolic-optimization](https://github.com/brendenpetersen/deep-symbolic-optimization) |
| `gp_and_vsr_gp/` | Classic GP baseline — adapted from [jiangnanhugo/cvgp](https://github.com/jiangnanhugo/cvgp) |
| `mcts_and_vsr_mcts/` | MCTS with optional LLM grammar expansion (this work) |
| `Eureqa/` | Commercial genetic search baseline |

### Extra

| Folder | Description |
|---|---|
| `plots/` | Jupyter notebooks for paper figures |
| `result/` | Training logs and program outputs |

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

- **GP** → `gp_and_vsr_gp/`
- **MCTS** → `mcts_and_vsr_mcts/`
- **DSR / PQT / VPG** → `dso_classic/`
  Requires the `DSO` library and Python 3.7 (TensorFlow 1.15.4 dependency).
- **Eureqa** → `eureqa/`

Each sub-folder contains a `README.md` and `scripts/` with run instructions.

---

## Citation

If you use this codebase, please cite the original work:

```bibtex
@inproceedings{jiang2023mcts,
  title     = {..},
  author    = {Jiang, Nan and others},
  booktitle = {Proceedings of ...},
  year      = {2023}
}
```

> **Note:** Replace the placeholder above with the full citation from the published paper.