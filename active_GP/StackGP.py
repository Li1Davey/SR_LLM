import matplotlib.pyplot as plt
import copy
import time

from sympy import symbols
from function import *
import utils
from regression_task import set_model_quality, evaluate_gp_model, ev_mod_helper


def initialize_gp_models(
        variables,
        ops=default_ops(),
        const=default_const(),
        numberOfModels=100,
        maxLength=10):
    """returns a set of randomly generated models"""

    models = [generate_random_model(variables, ops, const, maxLength) for i in range(numberOfModels)]

    return models


def generate_random_model(variables, ops, const, maxLength):
    """takes as input the variables, operators, constants, and max program length and returns a random program"""
    prog = utils.build_empty_model()  # Generate an empty model with correct structure
    var_choices = [utils.variable_select(i) for i in range(variables)] + const  # All variable and constants choices
    prog[0] = np.array(np.random.choice(ops, random.randint(1, maxLength)), dtype=object)  # Choose random operators
    count_vars = utils.model_arity(prog)  # Count how many variables/constants are needed
    prog[1] = np.random.choice(var_choices, count_vars)  # Choose random variables/constants
    prog[1] = [i() if (callable(i) and i.__name__ != '<lambda>') else i for i in prog[1]]  # If function then evaluate
    return prog


def stack_pass(model, pt):
    i = 0
    t = 0
    p = 0
    s = model[0]
    if i < pt:
        t += 1
    while i < pt:
        if s[i] == "pop":
            t += 1
            p += 1
        else:
            p += max(0, utils.get_arity(s[i]) - t)
            t = max(1, t - utils.get_arity(s[i]) + 1)
        i += 1
    stack1 = model[1][p:]
    stack2 = utils.reverse_list(model[1][:p])[:t + 1]
    return [stack1, stack2]


def stack_grab(stack1, stack2, num):
    tStack1 = copy.deepcopy(stack1)
    tStack2 = copy.deepcopy(stack2)
    if len(stack2) < num:
        newStack = stack2 + stack1[:(num - len(stack2))]
        tStack1 = tStack1[num - len(tStack2):]
        tStack2 = []
    else:
        newStack = stack2[:num]
        tStack2 = tStack2[num:]
    return [newStack, tStack1, tStack2]


def recombination2pt(model1, model2):
    """does 2 point crossover and returns two children models"""
    pts1 = np.sort(random.sample(range(0, len(model1[0]) + 1), 2))
    pts2 = np.sort(random.sample(range(0, len(model2[0]) + 1), 2))
    child1 = utils.build_empty_model()
    child2 = utils.build_empty_model()

    parent1 = copy.deepcopy(model1)
    parent2 = copy.deepcopy(model2)
    parent1[0] = np.array(parent1[0], dtype=object).tolist()
    parent2[0] = np.array(parent2[0], dtype=object).tolist()

    child1[0] = np.array(parent1[0][0:pts1[0]] + parent2[0][pts2[0]:pts2[1]] + parent1[0][pts1[1]:], dtype=object)
    child2[0] = np.array(parent2[0][0:pts2[0]] + parent1[0][pts1[0]:pts1[1]] + parent2[0][pts2[1]:], dtype=object)

    varPts1 = [utils.list_arity(parent1[0][:(pts1[0])]) + 0,
               utils.list_arity(parent2[0][:(pts2[0])]) + 0,
               utils.list_arity(parent2[0][pts2[0]:pts2[1]]),
               utils.list_arity(parent1[0][pts1[0]:pts1[1]])]
    if pts1[0] == 0:
        varPts1[0] += 1
    if pts2[0] == 0:
        varPts1[1] += 1
    child1[1] = parent1[1][:varPts1[0]] + parent2[1][varPts1[1]:(varPts1[1] + varPts1[2] - 1)] + parent1[1][(varPts1[0] + varPts1[3] - 1):]

    varPts2 = [utils.list_arity(parent2[0][:(pts2[0])]) + 0,
               utils.list_arity(parent1[0][:(pts1[0])]) + 0,
               utils.list_arity(parent1[0][pts1[0]:pts1[1]]),
               utils.list_arity(parent2[0][pts2[0]:pts2[1]])]
    if pts1[0] == 0:
        varPts2[1] += 1
    if pts2[0] == 0:
        varPts2[0] += 1
    child2[1] = parent2[1][:varPts2[0]] + parent1[1][varPts2[1]:(varPts2[1] + varPts2[2] - 1)] + parent2[1][(varPts2[0] + varPts2[3] - 1):]
    # print(varPts1,varPts2)

    return [child1, child2]


def mutate(model, variables, ops=default_ops(), const=default_const(), maxLength=10):
    """ mutates a model"""
    new_model = copy.deepcopy(model)
    new_model[0] = np.array(new_model[0], dtype=object).tolist()
    mutation_type = random.randint(0, 7)
    var_choices = [utils.variable_select(i) for i in range(variables)] + const

    if mutation_type == 0:
        op_choice = random.randint(0, len(new_model[0]) - 1)
        if len(new_model[0]) > 0:
            new_model[0][op_choice] = np.random.choice([i for i in ops])

    elif mutation_type == 1:
        var_choice = np.random.choice(var_choices)
        if callable(var_choice) and var_choice.__name__ != '<lambda>':
            var_choice = var_choice()
        new_model[1][random.randint(0, len(new_model[1]) - 1)] = var_choice

    elif mutation_type == 2:
        op_choice = np.random.choice(ops)
        new_model[0] = [op_choice] + new_model[0]
        while utils.model_arity(new_model) > len(new_model[1]):
            var_choice = np.random.choice(var_choices)
            if callable(var_choice) and var_choice.__name__ != '<lambda>':
                var_choice = var_choice()
            new_model[1] = [var_choice] + new_model[1]

    elif mutation_type == 3:
        if len(new_model[0]) > 1:
            op_choice = random.randint(1, len(new_model[0]) - 1)
            new_model[0] = new_model[0][-op_choice:]
            new_model[1] = new_model[1][-utils.list_arity(new_model[0]):]

    elif mutation_type == 4:
        op_choice = np.random.choice([i for i in ops])
        new_model[0].append(op_choice)

    elif mutation_type == 5:
        new_model = recombination2pt(new_model, generate_random_model(variables, ops, const, maxLength))[0]

    elif mutation_type == 6:  # single operator insertion mutation
        singleOps = [op for op in ops if utils.get_arity(op) == 1 and op != 'pop']
        singleOps.append('pop')
        pos = random.randint(0, len(new_model[0]) - 1)
        new_model[0].insert(pos, np.random.choice(singleOps))

    elif mutation_type == 7:  # nudge numeric constant
        pos = utils.get_numeric_indices(new_model[1])
        if len(pos) > 0:  # If there are numeric constants
            pos = random.choice(pos)
            new_model[1][pos] = new_model[1][pos] + np.random.normal(-1, 1)

    if utils.model_arity(new_model) < len(new_model[1]):
        new_model[1] = new_model[1][:utils.model_arity(new_model)]
    elif utils.model_arity(new_model) > len(new_model[1]):
        new_model[1] = new_model[1] + [np.random.choice(var_choices) for i in range(utils.model_arity(new_model) - len(new_model[1]))]
    new_model[1] = [varChoice() if callable(varChoice) and varChoice.__name__ != '<lambda>' else varChoice for varChoice in new_model[1]]
    new_model[0] = np.array(new_model[0], dtype=object)
    return new_model


def pareto_front(fitValues):  # Returns Boolean list of Pareto front elements
    onFront = np.ones(fitValues.shape[0], dtype=bool)
    for i, j in enumerate(fitValues):
        if onFront[i]:
            onFront[onFront] = np.any(fitValues[onFront] < j, axis=1)
            onFront[i] = True
    return onFront


def pareto_tournament(pop):  # selects the Pareto front of a model set
    fitness_values = np.array([mod[2] for mod in pop])
    return (np.array(pop, dtype=object)[pareto_front(fitness_values)]).tolist()


def tournament_model_selection(models, popSize=100, tourneySize=5):
    """returns the Pareto front of a model set"""
    selected_models = []
    while len(selected_models) < popSize:
        tournament = random.sample(models, tourneySize)
        winners = pareto_tournament(tournament)
        selected_models = selected_models + winners

    return selected_models


def model_same_q(model1, model2):  # Checks if two models are the same
    """checks if model1 and model2 are the same and returns True if so, else False"""
    return len(model1[0]) == len(model2[0]) and len(model1[1]) == len(model2[1]) and all(model1[0] == model2[0]) and model1[1] == model2[1]


def delete_duplicate_models(models):  # Removes any models that are the same, does not consider simplified form
    """ deletes models that have the same form without simplifying"""
    uniqueMods = [models[0]]

    for mod in models:
        test = False
        for checkMod in uniqueMods:
            if model_same_q(mod, checkMod):
                test = True
        if not test:
            uniqueMods.append(mod)

    return uniqueMods


def remove_indeterminate_models(models):
    """removes models that have a fitness that results from inf or nan values"""
    return [i for i in models if (not any(np.isnan(i[2]))) and all(np.isfinite(np.isnan(i[2])))]


def select_models(models, selectionSize=0.5):
    """iteratively selects the Pareto front of a model population until n or n*popSize models are selected"""
    tMods = copy.deepcopy(models)
    [utils.model_to_list_form(mod) for mod in tMods]
    pareto_models = []
    if selectionSize <= 1:
        selection = selectionSize * len(models)
    else:
        selection = selectionSize

    while len(pareto_models) < selection:
        front = pareto_tournament(tMods)
        pareto_models = pareto_models + front
        for i in front:
            tMods.remove(i)
    [utils.model_restore_form(mod) for mod in pareto_models]
    return pareto_models


def trim_model(mod):
    """
    trims extra pop operators off the operator stack so that further modifications
    such as a model alignment aren't altered by those pop operators
    """
    model = copy.deepcopy(mod)
    i = 0
    varStack = len(mod[1])
    tempStack = 0
    varStack -= utils.get_arity(model[0][i])
    tempStack += 1
    i += 1
    while varStack > 0:
        if model[0][i] == 'pop':
            varStack -= 1
            tempStack += 1
        else:

            take = utils.get_arity(model[0][i]) - tempStack
            if take > 0:
                varStack -= take
                tempStack = 1
            else:
                tempStack -= utils.get_arity(model[0][i]) - 1
        i += 1
    model[0] = np.array(model[0][:i].tolist() + [j for j in model[0][i:] if not j == 'pop'], dtype=object)
    return model


def align_gp_model(model, data, response):
    """aligns a model such that response-a*f(x)+b are minimized over a and b"""
    prediction = evaluate_gp_model(model, data)
    if (not all(np.isfinite(np.array(prediction)))) or np.all(prediction == prediction[0]):
        return model
    if np.isnan(np.array(prediction)).any() or np.isnan(np.array(response)).any() or not np.isfinite(
            np.array(prediction, dtype=np.float32)).all():
        return model
    try:
        align = np.round(np.polyfit(prediction, response, 1, rcond=1e-16), decimals=14)
    except np.linalg.LinAlgError:
        # print("Alignment failed for: ", model, " with prediction: ", prediction, "and reference data: ", response)
        return model
    newModel = trim_model(model)
    newModel[0] = np.array(newModel[0].tolist() + [mul, add], dtype=object)
    newModel[1] = newModel[1] + align.tolist()
    set_model_quality(newModel, data, response)
    return newModel


def evolve(inputData, responseData, generations=100, ops=default_ops(), const=default_const(),  mutationRate=79,
           crossoverRate=11, spawnRate=10, extinction=False, extinctionRate=10, elitismRate=50, popSize=300, align=True,
           initialPop=[], timeLimit=300, capTime=False, tourneySize=5, tracking=False):
    fullInput, fullResponse = copy.deepcopy(inputData), copy.deepcopy(responseData)
    inData = copy.deepcopy(fullInput)
    resData = copy.deepcopy(fullResponse)
    variable_count = utils.var_count(inData)
    models = initialize_gp_models(variable_count, ops, const, popSize)
    models = models + initialPop
    startTime = time.perf_counter()
    best_fits = []
    for i in range(generations):
        if capTime and time.perf_counter() - startTime > timeLimit:
            break
        for mods in models:
            set_model_quality(mods, inData, resData)

        if tracking:
            best_fits.append(min([mods[2][0] for mods in pareto_tournament(models)]))

            # pareto_models=paretoTournament(models)
        pareto_models = select_models(models, elitismRate / 100 * popSize)
        if extinction and i % extinctionRate:
            models = initialize_gp_models(variable_count, ops, const, popSize)
            for mods in models:
                set_model_quality(mods, inData, resData)

        models = tournament_model_selection(models, popSize, tourneySize)

        crossover_pairs = random.sample(models, round(crossoverRate / 100 * popSize))
        to_mutate = random.sample(models, round(mutationRate / 100 * popSize))

        child_models = pareto_models

        for j in range(round(len(crossover_pairs) / 2) - 1):
            child_models = child_models + recombination2pt(crossover_pairs[j], crossover_pairs[j + round(len(crossover_pairs) / 2)])

        for j in to_mutate:
            child_models = child_models + [mutate(j, variable_count, ops, const)]

        child_models = child_models + initialize_gp_models(variable_count, ops, const, round(spawnRate / 100 * popSize))

        child_models = delete_duplicate_models(child_models)

        for mods in child_models:
            set_model_quality(mods, inData, resData)
        child_models = remove_indeterminate_models(child_models)

        if len(child_models) < popSize:
            child_models = child_models + initialize_gp_models(variable_count, ops, const, popSize - len(child_models))

        models = copy.deepcopy(child_models)

    for mods in models:
        set_model_quality(mods, fullInput, fullResponse)
    models = [trim_model(mod) for mod in models]
    models = delete_duplicate_models(models)
    models = remove_indeterminate_models(models)
    models = utils.sort_models(models)
    if align:
        models = [align_gp_model(mods, fullInput, fullResponse) for mods in models]

    if tracking:
        best_fits.append(min([mods[2][0] for mods in pareto_tournament(models)]))
        plt.figure()
        plt.plot(best_fits)
        plt.title("Fitness over Time")
        plt.xlabel("Generations")
        plt.ylabel("Fitness")

    return models


def print_gp_model(mod, inputData=symbols(["x" + str(i) for i in range(100)])):  # Evaluates a model numerically
    def inv1(a):
        return a ** (-1)

    from sympy import tan as tan1, exp as exp1, sqrt as sqrt1, sin as sin1, cos as cos1, acos, asin, atan, tanh as tanh1, log as log1
    def sqrt2(a):
        return sqrt1(a)

    def log2(a):
        return log1(a)

    model = copy.deepcopy(mod)
    model[0] = utils.replace_func(model[0], exp, exp1)
    model[0] = utils.replace_func(model[0], tan, tan1)
    model[0] = utils.replace_func(model[0], sqrt, sqrt2)
    model[0] = utils.replace_func(model[0], inv, inv1)
    model[0] = utils.replace_func(model[0], sin, sin1)
    model[0] = utils.replace_func(model[0], cos, cos1)
    model[0] = utils.replace_func(model[0], arccos, acos)
    model[0] = utils.replace_func(model[0], arcsin, asin)
    model[0] = utils.replace_func(model[0], arctan, atan)
    model[0] = utils.replace_func(model[0], tanh, tanh1)
    model[0] = utils.replace_func(model[0], log, log2)
    response = ev_mod_helper(model[1], model[0], [], np.array(inputData))[2][0]
    return response
