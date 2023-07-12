import time
import numpy as np
from operator import attrgetter
from program import Program
from utils import Node, create_node


class ExpandingGeneticProgram(object):
    """
    populations: the current list of programs
    hofs: list of the best programs
    """

    # static variables
    library = None
    gp_helper = None

    def __init__(self, cxpb, mutpb, maxdepth, population_size, tour_size, hof_size, n_generations, nvar):
        """
        cxpb: probability of mate
        mutpb: probability of mutations
        maxdepth: the maxdepth of the tree during mutation
        population_size: the size of the selected populations (at the end of each generation)
        tour_size: the size of the tournament for selection
        hof_size: the size of the best programs retained
        n_generations: the number of generations to be applied over each pool
        nvar: number of variables
        """
        self.cxpb = cxpb
        self.mutpb = mutpb
        self.maxdepth = maxdepth
        self.population_size = population_size
        self.tour_size = tour_size
        self.hof_size = hof_size

        self.n_generations = n_generations

        self.timer_log = []

        self.nvar = nvar
        self.full_vars = [i for i in range(self.nvar)]
        assert self.library != None
        assert Program.task != None

    def create_init_population(self):
        """
           create the initial population; for every variable, generate a set of generate random equations.
           save them to self.populations, self.hofs.
           look for every token in library, fill in the leaves with constants or inputs.
        """
        self.populations = []
        self.hofs = []

        for vari in range(self.nvar):
            tmp_node = Node(prev_vf=[-1, ], next_vf=[vari, ])
            self._set_dataX_allowed_input_tokens(tmp_node.total_vf)
            self._set_library_allowed_input_tokens(tmp_node.next_vf)

            for i, t in enumerate(self.library.tokens):
                if self.library.allowed_tokens[i]:
                    tree = [i]
                    for j in range(t.arity):
                        t_idx = np.random.choice(self.library.tokens_of_arity[0])
                        while self.library.allowed_tokens[t_idx] == 0:
                            t_idx = np.random.choice(self.library.tokens_of_arity[0])
                        tree.append(t_idx)
                    tree = np.array(tree)
                    pr = Program(tree, np.ones(tree.size, dtype=np.int32))
                    pr.cur_node=tmp_node
                    self.populations.append(pr)
                    new_pr = pr.clone()
                    self.hofs.append(new_pr)

    def run_with_tree_based_randomized_variable_ordering(self):
        # 1. generate all single variable equations by creating `#nvar` POOLS.

        self.create_init_population()
        # 2. apply GP
        for round_idx in range(self.nvar + 1):
            for pr in self.populations:
                # 2.1 set the free variables and controlled variables for the given POOL
                # 2.2 re-evaluate the constants and reward for the given POOL
                self._set_dataX_allowed_input_tokens(pr.cur_node.total_vf)
                # a cached property in python (evaluated once) force the function to evaluate a new r
                pr.remove_r_evaluate()
                # finds the best constants on control variable data
                _ = pr.r  # goodness-of-fit
            for pr in self.hofs:
                self._set_dataX_allowed_input_tokens(pr.cur_node.total_vf)
                pr.remove_r_evaluate()
                _ = pr.r

            # 2.3  do n generation of GP,
            for it in range(self.n_generations):
                print('++++++++++++ ITERATION {} ++++++++++++'.format(it))
                self.one_generation()
            # 2.4 find the best set of fitted expressions
            self.update_population()
            print_prs(self.populations)

            # 2.5 freeze tokens in the expressions
            for i, pr in enumerate(self.populations):
                # evaluate r again, just incase it has not been evaluated.
                self._set_dataX_allowed_input_tokens(pr.cur_node)
                this_r = pr.r
                if len(pr.const_pos) == 0 or pr.num_changing_consts == 0:
                    # only expand at those constant node. if there are no constant node,then we are done
                    # if we do not want num_changing_consts, then we also quit.
                    print('there are no constant node. we are done...')
                else:
                    pr.remove_r_evaluate()
                    this_r = pr.r
                # whether you get very different value for different constant.
                pr.freeze_equation()

    def one_generation(self, verbose=False):
        """
        One step of the genetic algorithm.
        This wraps selection, mutation, crossover and hall of fame computation
        over all the individuals in the population for this epoch/step.
        """
        t1 = time.perf_counter()

        # Select the next generation individuals
        offspring = self.selectTournament(self.population_size, self.tour_size)
        if verbose:
            print('offspring after select=')
            print_prs(offspring)

        # Vary the pool of individuals
        offspring = self._var_and(offspring)
        if verbose:
            print('offspring after mutation and cross-over=')
            print_prs(offspring)

        # Replace the current population by the offspring
        self.populations = offspring + self.hofs

        # Update hall of fame
        self.update_hof()
        if verbose:
            print("after update hof=")
            print_prs(self.hofs)
        timer = time.perf_counter() - t1
        self.timer_log.append(timer)

    def update_hof(self):
        """update the set of Hall of Fame for the given pool_idx pool"""
        new_hof = sorted(self.populations, reverse=True, key=attrgetter('r'))

        self.hofs = []
        for i in range(self.hof_size):
            pr = new_hof[i]
            if pr.r == np.nan or pr.r == np.inf or pr.r == -np.inf:
                print("filter:", pr.r, pr.__getstate__(), end="\t")
                pr.print_expression()
                continue
            self.hofs.append(pr.clone())

    def update_population(self):
        """update the population. sort by fitness score and cut by population_size.
        evaluated on all random dataset.
        """
        filtered_population = []
        for pr in self.populations:
            if pr.r == np.nan or pr.r == np.inf or pr.r == -np.inf:
                print("filter:", pr.r, pr.__getstate__(), end="\t")
                pr.print_expression()
                continue
            filtered_population.append(pr)
        self._set_dataX_allowed_input_tokens(self.full_vars)
        new_population = sorted(filtered_population, reverse=True, key=attrgetter('r'))
        self.populations = []
        for i in range(min(self.population_size, len(filtered_population))):
            self.populations.append(new_population[i].clone())

    def selectTournament(self, population_size, tour_size):
        """evaluate on full data for tournament"""
        offspring = []
        self._set_dataX_allowed_input_tokens(self.full_vars)
        for pp in range(population_size):
            spr = np.random.choice(self.populations, tour_size)
            maxspr = max(spr, key=attrgetter('r'))
            maxspri = maxspr.clone()
            offspring.append(maxspri)
        return offspring

    def _var_and(self, offspring):
        """Apply crossover AND mutation to each individual in a population, given a constant probability."""

        # Apply crossover on the offspring
        np.random.shuffle(offspring)
        for i in range(1, len(offspring), 2):
            if np.random.random() < self.cxpb:
                self.gp_helper.mate(offspring[i - 1], offspring[i])

        # Apply mutation on the offspring
        for i in range(len(offspring)):
            if np.random.random() < self.mutpb:
                self.gp_helper.multi_mutate(offspring[i], self.maxdepth)

        return offspring

    def _set_library_allowed_input_tokens(self, allowed_input_token, verbose=False):
        """Input is a set of free input variables"""
        # print("set library allow input tokens.....")
        free_input_tokens = np.zeros(self.nvar, dtype=np.int32)
        for vari in allowed_input_token:
            if 0 <= vari < len(free_input_tokens):
                free_input_tokens[vari] = 1
        self.library.set_allowed_input_tokens(free_input_tokens)
        if verbose:
            print("For library:", self.library.allowed_tokens, self.library.allowed_input_tokens)

    def _set_dataX_allowed_input_tokens(self, allowed_input_token, verbose=False):
        """Input is a set of free input variables"""
        # print("set Program allow input tokens.....")
        free_input_tokens = np.zeros(self.nvar, dtype=np.int32)
        for vari in allowed_input_token:
            if 0 <= vari < len(free_input_tokens):
                free_input_tokens[vari] = 1
        Program.task.set_allowed_inputs(free_input_tokens)
        if verbose:
            print("For dataX:", Program.task.allowed_input, Program.task.fixed_column)

    def print_final_hofs(self):
        self._set_dataX_allowed_input_tokens(self.full_vars)
        # new_hof = sorted(self.hofs, reverse=True, key=attrgetter('r'))
        for pr in self.hofs:
            print("\t", pr.__getstate__())
            pr.task.rand_draw_X_non_fixed()
            print('\tvalidate r=', pr.task.reward_function(pr))
            pr.task.print_reward_function_all_metrics(pr)
            pr.print_expression()


def print_prs(prs):
    for pr in prs:
        print('        ' + str(pr.__getstate__()), end="\t")
        pr.print_expression()
    print("")
