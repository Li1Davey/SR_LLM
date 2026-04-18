Markdown
Copy Code
# Symbolic Regression with MCTS and LLM

This project implements a symbolic regression framework utilizing Monte Carlo Tree Search (MCTS) and a Large Language Model (LLM) to discover mathematical expressions that fit given datasets.

## Requirements

Before running the code, ensure that you have the required packages installed:

```bash
pip install -r requirements.txt


If you intend to use LLM rule suggestions, make sure the following environment variable is configured:

OPENAI_API_KEY: Your API key for OpenAI services.
Running the Code
Bash
Copy Code
bash run_experiment.sh <equation_name> <run_number> [num_episodes] [prod_rule_mode] [use_llm] [seed]

Parameters
Parameter	Required	Default	Description
equation_name	Yes	—	Name of the equation file (e.g. kepler)
run_number	Yes	—	Unique identifier for the run (e.g. 001)
num_episodes	No	30	Number of MCTS episodes
prod_rule_mode	No	livermore2	Production rule set: livermore2, trigometric, or feynman
use_llm	No	false	Enable LLM rule suggestions: true or false
seed	No	time-based	Integer random seed for reproducibility
Example Usage

Run with LLM enabled:

Bash
Copy Code
bash run_experiment.sh kepler 001 500 feynman true


Run without LLM:

Bash
Copy Code
bash run_experiment.sh kepler 001 500 feynman false


Controlled ablation — same seed, only LLM flag differs:

Bash
Copy Code
bash run_experiment.sh kepler 100a 2000 feynman false 42
bash run_experiment.sh kepler 100b 2000 feynman true  42

Project Structure
File	Description
mcts_model.py	MCTS algorithm and LLM integration logic
main.py	Entry point — parses arguments and launches the MCTS run
suggester.py	LLM prompt construction, rule parsing, and validation pipeline
program.py	Expression optimization and reward evaluation
run_experiment.sh	Shell script for launching experiments
requirements.txt	Python dependencies
data/	Unencrypted custom equation files
Component Descriptions
MCTS Logic

The MCTS algorithm builds symbolic expressions by repeatedly expanding a parse tree using a set of production rules. It maintains a hall of fame of the best expressions found and uses UCB scores to balance exploration and exploitation.

LLM Integration

When use_llm=true, the system periodically queries an LLM to suggest new production rules based on the best expressions found so far. The suggester pipeline:

Filters expressions by length to remove noisy expanded forms
Builds a structured prompt with skeleton analysis instructions
Parses and validates returned rules against the existing grammar
Rejects domain-unsafe rules based on variable ranges

LLM calls are skipped automatically if the reward threshold is already met, or if the last two consecutive calls returned no new rules. Set use_llm=false to disable this entirely and run pure MCTS — no OPENAI_API_KEY is required in that case.

Reproducibility

By default, each run uses a time-based random seed. To reproduce a run exactly or compare two runs under identical conditions, pass an explicit integer seed as the sixth argument. The seed used is always printed at startup and saved in command.txt inside the run directory.

Expression Optimization

Each candidate expression is passed through several guards before optimization:

Rejects expressions that are too long or have too many production rules
Rejects chained power towers and astronomically large exponents
Rejects constant-only expressions with no free variables

Invalid expressions are assigned a reward of -999.0 and discarded immediately.