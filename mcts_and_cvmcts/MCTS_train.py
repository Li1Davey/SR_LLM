import pandas as pd
import time
import argparse
from MCTS_model import MCTS, score_with_est
from production_rules import *
from utils import simplify_eq


def run_mcts(task: str, num_iterations: int, data_dir='data/', max_len=50, eta=0.9999,
             max_module_init=10, num_aug=5, exp_rate=1 / np.sqrt(2),
             norm_threshold=1e-5):
    """
    Executes the main training loop of Symbolic Physics Learner.
    
    Parameters
    ----------
    task: benchmark task name.
    num_run" number of iterations.
    data_dir : String object.
        directory of training data samples. 
    max_len: maximum allowed length (number of production rules ) of discovered equations.
    eta: penalty factor for rewarding.
    max_module_init : Int object.
        initial maximum length for module transplantation candidates. 
    num_aug : number of trees for module transplantation.
    exp_rate: initial exploration rate.
    norm_threshold: numerical error tolerance for norm calculation, a very small value.
        
    Returns
    -------
    all_eqs: List<Str>. discovered equations.
    success_rate: Float. success rate of all runs performed.
    all_times: List<Float>. runtimes for successful runs.
    """

    # define production rules and non-terminal nodes.
    grammars = production_rules[task]
    nt_nodes = ntn_map[task]

    # read training and testing data as numpy matrix
    train_data = pd.read_csv(data_dir + task + '_train.csv', header=None).to_numpy().T
    test_data = pd.read_csv(data_dir + task + '_test.csv', header=None).to_numpy().T

    num_success = 0
    all_times = []
    all_eqs = []

    # number of module max size increase after each transplantation
    module_grow_step = (max_len - max_module_init) / num_iterations

    best_solution = ('nothing', 0)

    exploration_rate = exp_rate
    max_module = max_module_init
    reward_his = []
    hof = []
    aug_grammars = ['A->A-A,A->C,A->C', 'A->sqrt(A),A->C', 'A->sqrt(A),A->A+A,A->X0,A->A/A, A->X0,A->X0']

    start_time = time.time()
    discovery_time = 0

    for i_itr in range(num_iterations):
        print(f"i_itr={i_itr},")
        mtcs_model = MCTS(data_sample=train_data,
                          base_grammars=grammars,
                          aug_grammars=aug_grammars,
                          nt_nodes=nt_nodes,
                          max_len=max_len,
                          max_module=max_module,
                          aug_grammars_allowed=num_aug,
                          exploration_rate=exploration_rate,
                          eta=eta)

        _, current_solution, population = mtcs_model.MCTS_run(num_iterations,
                                                              num_simulations=10,
                                                              verbose=True)

        end_time = time.time() - start_time

        if not hof:
            hof = population
        else:
            hof = sorted(list(set(hof + population)), key=lambda x: x[1])
        aug_grammars = [x[0] for x in hof[-num_aug:]]
        print("aug_grammars:", aug_grammars)
        reward_his.append(best_solution[1])

        if current_solution[1] > best_solution[1]:
            best_solution = current_solution
        # print(best_solution)
        max_module += module_grow_step
        exploration_rate *= 5

        # check if solution is discovered. Early stop if it is.
        test_score = score_with_est(simplify_eq(best_solution[0]),
                                    0,
                                    test_data,
                                    mtcs_model.input_var_Xs,
                                    eta=eta)[0]
        if test_score >= 1 - norm_threshold:
            num_success += 1
            if discovery_time == 0:
                discovery_time = end_time
                all_times.append(discovery_time)
            break
        print()

    all_eqs.append(simplify_eq(best_solution[0]))
    print('best solution: {}'.format(simplify_eq(best_solution[0])))
    print('test score: {}'.format(test_score))
    print()

    return all_eqs, all_times


def main(args):
    # directory to save discovered results
    output_folder = args.output_dir
    # if true, discovered equations are saved to "output_folder" dir
    save_eqs = True

    task = args.task
    all_eqs, all_times = run_mcts(task,
                                  num_iterations=args.num_run)

    if save_eqs:
        output_file = open(output_folder + task + '.txt', 'w')
        for eq in all_eqs:
            output_file.write(eq + '\n')
        output_file.close()

    print('average discovery time is', np.round(np.mean(all_times), 3), 'seconds')


def get_arguments():
    parser = argparse.ArgumentParser(description='run_model')
    parser.add_argument('--task', default='nguyen-1', type=str, help="dataset name")
    parser.add_argument('--num_run', default=100, type=int, help='number of training iterations')
    parser.add_argument('--output_dir', default='results/', type=str, help='output directory')
    return parser.parse_args()


if __name__ == '__main__':
    main(get_arguments())
