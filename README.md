# README: SciBench Datasets for Scientific Approach Inspired Symbolic Regression #

### Directory

### Scibench related

- `data`: the generated dataset. Every file represent a ground-truth expression.
- `scibench`: the dataoracle API.

#### Baselines
- `dso_classic`: public code implementation from https://github.com/brendenpetersen/deep-symbolic-optimization. It contains the imeplementation of methods `DSR, PQT, VPG, GPMeld `.
- `ctrl_var_gp`: the inplemenattion of the our proposed control variable genetic programming algorithm and the classic genetic programming algorithm. We change the code that is relevant to the dataloader.
- `Eureqa`: the commercial genetic search algorithm.

#### Exrta
- plots: the jupter notebook to generate our figure.
- result: contains all the output of all the programs, the training logs.


### 3. Look at the summarized result
Just open the `result` and `plots` folders.

