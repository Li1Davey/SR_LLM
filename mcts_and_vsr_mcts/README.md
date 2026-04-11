Symbolic Regression with MCTS and LLM

This project implements a symbolic regression framework utilizing Monte Carlo Tree Search (MCTS) and a Large Language Model (LLM) to discover mathematical expressions that fit given datasets.

Requirements

Before running the code, ensure that you have the required packages installed. You can do this by using pip:

Bash
Copy Code
pip install -r requirements.txt


Make sure to have the following environment variable configured:

OPENAI_API_KEY: Your API key for OpenAI services.
Running the Code

To execute the experiments using the provided scripts, use the following command:

Bash
Copy Code
bash run_experiment.sh <equation_name> <run_number> [num_episodes] [prod_rule_mode] [extra main.py args]

Parameters:
<equation_name>: The name of the equation file (e.g., kepler).
<run_number>: A unique identifier for the experiment run (e.g., 001).
[num_episodes]: Optional; the number of episodes to run (default is 30).
[prod_rule_mode]: Optional; specifies the production rule mode (default is livermore2). Valid options are:
livermore2
trigometric
feynman
[extra main.py args]: Any additional arguments to pass to main.py.
Example Usage

To run an experiment with the kepler equation, under run number 001, with 500 episodes and using the feynman rule mode, execute the following command:

Bash
Copy Code
bash run_experiment.sh kepler 001 500 feynman

Project Structure
mcts_models.py: Contains the implementation of the MCTS algorithm and logic for interacting with the LLM.
program.py: Implements the core logic for optimizing expressions and evaluating results.
run_experiment.sh: A shell script that sets up the execution environment and runs experiments.
requirements.txt: Lists all Python dependencies required for the project.
data/: Directory containing unencrypted custom equations used in the experiments.
Component Descriptions
MCTS Logic

The MCTS logic interacts with the LLM to generate and evaluate mathematical expressions. It employs guards to ensure that only valid expressions are processed, thus maintaining the integrity of the optimization process.

LLM Integration

The project utilizes an LLM to propose new symbolic expressions based on gathered data and rules. Operators that are not part of the declared function set are filtered out through a hard whitelist mechanism.

Expression Optimization

The optimization process includes checks for the validity of predictions, ensuring that only stable and reliable expressions are considered during evaluations. Invalid predictions lead to immediate rejection to avoid errors in optimization.