# README: Vertical Symbolic Regression #

### Directory

### Data Oracle

- `data`: the generated dataset. Every file represent a ground-truth expression.
- `scibench`: the dataoracle API.

#### Baselines
- `dso_classic`: public code implementation from https://github.com/brendenpetersen/deep-symbolic-optimization. It contains the imeplementation of methods `DSR, PQT, VPG, GPMeld `.
- `gp_and_cvgp`: the re-implementation of the our proposed control variable genetic programming algorithm (https://github.com/jiangnanhugo/cvgp) and the classic genetic programming algorithm. We change the code that is relevant to the dataloader.
- `Eureqa`: the commercial genetic search algorithm.
- `mcts_and_cvmcts`: the classic Monte Carlo Tree Search algorithm and the Adaptation to our VSR algorithm. 

#### Extra
- plots: the jupyter notebook to generate our figure.
- result: contains all the output of all the programs, the training logs.


### 3. Look at the summarized result
Just open the `result` and `plots` folders.

