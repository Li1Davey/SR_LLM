import time
import numpy as np
from operator import attrgetter

from program import Program


class ExpandingGeneticProgram(object):
    """
    populations: the current list of programs
    hofs: list of the best programs
    timer_log: list of times
    gen_num: number of generations, starting from 0.
    """

    # static variables
    library = None
    gp_helper = None

    def __init__(self, cxpb, mutpb, maxdepth, population_size, tour_size, hof_size, n_generations, nvar):
        """
        Parameters
        ----------
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
        self.gen_num = 0

        self.nvar = nvar
        assert self.library != None
        assert Program.task != None

    def create_init_population(self):
        """
           create the initial population; for every variable, a set of generate random equations.
           save them to self.populations, self.hofs.
           for every single pool: look for every token in library, fill in the leaves with constants or inputs.
        """
        self.populations = dict()
        self.hofs = dict()
        for vari in range(self.nvar):
            self._set_allowed_input_tokens((vari,))
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
                    if (vari,) not in self.populations:
                        self.populations[(vari,)] = []
                    self.populations[(vari,)].append(pr)
                    new_pr = pr.clone()
                    if (vari,) not in self.hofs:
                        self.hofs[(vari,)] = []
                    self.hofs[(vari,)].append(new_pr)
        print("Init done.....")

    def run_with_tree_based_randomized_variable_ordering(self):
        # 1. generate all single variable equations by creating `#nvar` POOLS.
        self.create_init_population()
        print("=" * 20 + "Init Population" + "=" * 20)
        for pool_idx in self.populations:
            for pr in self.populations[pool_idx]:
                pr.print_expression()
            print('-'*50)

        # 2. apply GP for every single POOL
        all_the_pool_idxes = list(self.populations.keys())
        while True:
            for pool_idx in all_the_pool_idxes:
                # 2.1 set the free variables and controlled variables for the given POOL
                # TODO: library, task set_allowed_input_tokens, disable the previous allowed input.
                self._set_allowed_input_tokens(pool_idx)
                for pr in self.populations[pool_idx]:
                    pr.remove_r_evaluate()
                for pr in self.hofs[pool_idx]:
                    pr.remove_r_evaluate()

                # 2.2 revaluate the constants and reward for the given POOL
                for pr in self.populations[pool_idx]:
                    # a cached property in python (evaluated once) force the function to evaluate a new r
                    thisr = pr.r  # how good you fit.
                for pr in self.hofs[pool_idx]:
                    thisr = pr.r

                # 2.3 for the given POOL, do n generation of GP, find the best set of fitted expressions
                for it in range(self.n_generations):
                    print('++++++++++++ VAR {} ITERATION {} ++++++++++++'.format(pool_idx, it))
                    self.one_generation(pool_idx)

                self.update_population(pool_idx)

                for i, pr in enumerate(self.populations[pool_idx]):
                    print('{}-th in population POOL {}'.format(i, pool_idx))
                    # evaluate r again, just incase it has not been evaluated.
                    this_r = pr.r
                    if len(pr.const_pos) == 0 or pr.num_changing_consts == 0:
                        # only expand at those constant node. if there are no constant node,then we are done
                        # if we do not want num_changing_consts, then we also quit.
                        print('there are no constant node. we are done...')
                    else:
                        if not ("expr_objs" in pr.__dict__ and "expr_consts" in pr.__dict__):
                            print('WARNING: pr.expr_objs NOT IN DICT: pr=' + str(pr.__getstate__()))
                            pr.remove_r_evaluate()
                            this_r = pr.r
                            print('pr.expr_objs=', pr.expr_objs)
                            print('pr.expr_consts=', pr.expr_consts)
                    # whether you get very different value for different constant.
                    pr.freeze_equation()
                    pr.remove_r_evaluate()

                    print('pr.r=', pr.r)
                    print('pr=', pr.__getstate__())
                    pr.print_expression()

                for i, pr in enumerate(self.hofs[pool_idx]):
                    print('{}-th in self.hof {}'.format(i, pool_idx))
                    # evaluate r again, just incase it has not been evaluated.
                    pr.remove_r_evaluate()
                    print('pr.r=', pr.r)
                    print('pr=', pr.__getstate__())
                    pr.print_expression()

            new_joint_population_Pools = dict()
            new_pool_idxes = []
            # pick two pools randomly, create a new pool of expression containing expression with the union of free variables
            np.random.shuffle(all_the_pool_idxes)
            for i in range(0, len(all_the_pool_idxes), 2):
                one_pool_idx, another_pool_idx = all_the_pool_idxes[i], all_the_pool_idxes[i + 1]
                new_pool_idx = one_pool_idx + another_pool_idx
                sorted(new_pool_idx)
                if new_pool_idx in new_pool_idxes:
                    print("new_pool_idx {} already in new_pool_idxes {}".format(new_pool_idx, new_pool_idxes))
                    continue
                self._set_allowed_input_tokens(new_pool_idx)

                one_joint_pool = self.merge_two_pools(one_pool_idx, another_pool_idx)

                new_joint_population_Pools[new_pool_idx] = one_joint_pool
                new_pool_idxes.append(new_pool_idx)

    def merge_two_pools(self, one_pool_idx, another_pool_idx):
        """
        TODO set allowed input tokens.
        Given two pools of equations, pick two equations from two pools and apply m
        """
        # self.gp_helper.mate(offspring[i - 1], offspring[i])
        joint_Pool = []
        for pr_var1 in self.populations[one_pool_idx]:
            for pr_var2 in self.populations[another_pool_idx]:
                # if np.random.random() < self.cxpb:
                # TODO: multi-mutate:
                # TODO: have a foor loop that joint_vars_pr has multiple expressions.
                # Want to know the value of placeholder constant.
                # check the simplifications
                # run the optimize to get the constant value
                joint_vars_progs = self.gp_helper.mate_joint_variables_program(pr_var1, pr_var2)
                # TODO: this step check if the joint-program can be splifiicaiton into the original expresiion
                # if self.program_backward_check(joint_vars_pr, pr_var1) \
                #         and self.program_backward_check(joint_vars_pr, pr_var2):
                joint_Pool.append(joint_vars_progs)

        return joint_Pool

    def program_backward_check(self, joint_vars_pr, single_var_pr):
        from functions import PlaceholderConstant
        ### apply the simplicaition step over joint_vars_pr,
        #
        # 1. replacing all extra variables not contained in single_var_pr as constant:
        all_vars_valid = single_var_pr.get_used_variables()

        for i in range(len(joint_vars_pr.traversal)):
            if joint_vars_pr.traversal[i] in all_vars_valid:
                # TODO: if it is a variable, but it is not
                joint_vars_pr.traversal[i] = PlaceholderConstant(np.random.rand() * 10)

        # 2. recursively merges nodes if the leaves are all constants. (currently unclear)
        simplified_joint_vars_pr = joint_vars_pr.simplify()
        # TODO: check X1+C and C+X1; 
        if simplified_joint_vars_pr == single_var_pr:
            return True
        else:
            return False

    def one_generation(self, pool_idx):
        """
        One step of the genetic algorithm.
        This wraps selection, mutation, crossover and hall of fame computation
        over all the individuals in the population for this epoch/step.
        Parameters
        ----------
        iter : int. The current iteration used for logging purposes.
        """
        t1 = time.perf_counter()

        # Select the next generation individuals
        offspring = self.selectTournament(self.population_size, self.tour_size, pool_idx)

        print('offspring after select=')
        print_prs(offspring)
        print("")

        # Vary the pool of individuals
        offspring = self._var_and(offspring)

        print('offspring after _var_and=')
        print_prs(offspring)
        print("")

        # Replace the current population by the offspring
        self.populations[pool_idx] = offspring + self.hofs[pool_idx] + self.populations[pool_idx]

        # Update hall of fame
        self.update_hof(pool_idx)
        print("after update hof after sorted=")
        print_prs(self.hofs[pool_idx])
        timer = time.perf_counter() - t1

        self.timer_log.append(timer)
        self.gen_num += 1

    def update_hof(self, pool_idx):
        """update the set of Hall of Fame for the given pool_idx pool"""
        new_hof = sorted(self.populations[pool_idx], reverse=True, key=attrgetter('r'))

        self.hofs[pool_idx] = []
        for i in range(self.hof_size):
            pr = new_hof[i]
            if pr.r == np.nan or pr.r == np.inf or pr.r == -np.inf:
                print("filter:", pr.r, pr.__getstate__(), end="\t")
                pr.print_expression()
                continue
            self.hofs[pool_idx].append(pr.clone())

    def update_population(self, pool_idx):
        """update the population in the given indexed pool"""
        filtered_population = []
        for pr in self.populations[pool_idx]:
            if pr.r == np.nan or pr.r == np.inf or pr.r == -np.inf:
                print("filter:", pr.r, pr.__getstate__(), end="\t")
                pr.print_expression()
                continue
            filtered_population.append(pr)
        new_population = sorted(filtered_population, reverse=True, key=attrgetter('r'))
        self.populations[pool_idx] = []
        for i in range(min(self.population_size, len(filtered_population))):
            self.populations[pool_idx].append(new_population[i].clone())

    def selectTournament(self, population_size, tour_size, pool_idx):
        offspring = []
        for pp in range(population_size):
            spr = np.random.choice(self.populations[pool_idx], tour_size)
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

    def _set_allowed_input_tokens(self, allowed_input_tokens):
        """Input is a set of free input variables"""
        free_input_tokens = np.zeros(self.nvar, dtype=np.int32)
        for vari in allowed_input_tokens:
            free_input_tokens[vari] = 1
        self.library.set_allowed_input_tokens(free_input_tokens)
        Program.task.set_allowed_inputs(free_input_tokens)

    def print_populations(self):
        for vari in self.populations:
            print(f"vars={vari}")
            for pr in self.populations[vari]:
                print("\t", pr.__getstate__())

    def print_hofs(self):
        for vari in self.hofs:
            print(f"vars={vari}")
            new_hof = sorted(self.hofs[vari], reverse=True, key=attrgetter('r'))
            for pr in new_hof:
                print(pr.__getstate__())
                pr.task.rand_draw_X_non_fixed()
                print('\tvalidate r=', pr.task.reward_function(pr))
                pr.task.print_reward_function_all_metrics(pr)
                pr.print_expression()


def print_prs(prs):
    for pr in prs:
        print('        ' + str(pr.__getstate__()), end="\t")
        pr.print_expression()
