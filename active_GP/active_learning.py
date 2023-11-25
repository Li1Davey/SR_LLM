import dill
import os
import copy
import numpy as np

from StackGP import evolve, select_models, align_gp_model
from utils import extend_data
from regression_task import evaluate_gp_model, fitness
from function import all_ops

from sklearn.cluster import KMeans  # for clustering in ensemble definition
from scipy.optimize import minimize  # for uncertainty maximization
from scipy.stats import differential_entropy, pearsonr


def active_learning_checkpoint(eqNum, version, i, inputData, response, testInput, testResponse, errors, models, minerr):
    path = os.path.join(str(eqNum), str(version))
    file = open(path, "wb+")
    dill.dump([i, inputData, response, testInput, testResponse, errors, models, minerr], file)
    file.close()


def active_learning_checkpoint_load(eqNum, version, i, inputData, response, testInput, testResponse, errors, models, minerr):
    path = os.path.join(str(eqNum), str(version))
    try:
        with open(path, 'rb') as f:
            i, inputData, response, testInput, testResponse, errors, models, minerr = dill.load(f)
    except FileNotFoundError:
        return i, inputData, response, testInput, testResponse, errors, models, minerr
    return i, inputData, response, testInput, testResponse, errors, models, minerr


def sub_sample_space(space):
    newSpace = copy.deepcopy(space)
    newSpace = list(newSpace)
    for i in range(len(newSpace)):
        pts = sorted([np.random.uniform(newSpace[i][0], newSpace[i][1]), np.random.uniform(newSpace[i][0], newSpace[i][1])])
        newSpace[i] = tuple(pts)
    return tuple(newSpace)


def active_learning(func, dims, ranges, rangesP, eqNum=1, version=1, iterations=100):
    # func should be a lamda function of form lambda data: f(data[0],data[1],...)
    try:
        with open(os.path.join(str(eqNum), str(version)) + ".txt", 'rb') as f:
            return -1
    except FileNotFoundError:
        pass
    inputData = []
    testInput = []
    found = False
    for i in range(dims):
        inputData.append(np.random.uniform(ranges[i][0], ranges[i][1], 3))
        testInput.append(np.random.uniform(ranges[i][0], ranges[i][1], 200))
    inputData = np.array(inputData)
    testInput = np.array(testInput)
    response = func(inputData)
    testResponse = func(testInput)
    errors = []
    models = []
    minerr = 1
    for i in range(iterations):
        print("input: ", inputData)
        print("\n response: ", response)
        i, inputData, response, testInput, testResponse, errors, models, minerr = active_learning_checkpoint_load(eqNum, version, i,
                                                                                                                  inputData,
                                                                                                                  response, testInput,
                                                                                                                  testResponse, errors,
                                                                                                                  models,
                                                                                                                  minerr)
        if i > iterations - 1:
            break
        i += 1
        models = [evolve(inputData, response, initialPop=models, generations=1000, tracking=False, popSize=300, ops=all_ops(),
                         timeLimit=120,
                         capTime=True, align=False, elitismRate=10)
                  for _ in range(4)]
        models = select_models(models, 20)
        alignedModels = [align_gp_model(mods, inputData, response) for mods in models]
        ensemble = ensemble_select(alignedModels, inputData, response)
        out = maximize_uncertainty(ensemble, dims, rangesP)
        while out in inputData.T:
            out = maximize_uncertainty(ensemble, dims, sub_sample_space(rangesP))
        inputData = extend_data(inputData, out)
        response = func(inputData)
        fitList = np.array([fitness(mod, testInput, testResponse) for mod in alignedModels])
        errors.append(min(fitList[np.logical_not(np.isnan(fitList))]))
        minerr = errors[-1]
        if minerr < 1e-14:
            # print("Points needed in round", j,": ",3+i, " Time needed: ", time.perf_counter()-roundTime)
            if not os.path.exists(str(eqNum)):
                os.makedirs(str(eqNum))
            path = os.path.join(str(eqNum), str(version))
            file = open(path, "wb+")
            dill.dump([i, inputData, response, testInput, testResponse, errors, models, minerr], file)
            file.close()
            file = open(path + '.txt', 'w+')
            file.write(str(i + 3) + '\n')
            file.write(str(errors))
            file.close()
            return 3 + i
            # found = True
            # ptsNeeded.append(3 + i)
            # break
        active_learning_checkpoint(eqNum, version, i, inputData, response, testInput, testResponse, errors, models, minerr)
    if found == False:
        # print("Points needed in round",j,": NA (model not found)")
        path = os.path.join(str(eqNum), str(version))
        file = open(path, "wb")
        dill.dump([-1, inputData, response, testInput, testResponse, errors, models, minerr], file)
        file.close()
        file = open(path + '.txt', "w+")
        file.write(str(i + 3) + "\n")
        file.write(str(errors))
        file.close()
        return -1


def ensemble_select(models, inputData, responseData, number_of_clusters=10):  # Generates a model ensemble using input data partitions
    data = np.transpose(inputData)
    if len(data) < number_of_clusters:
        number_of_clusters = len(data)
    clusters = KMeans(n_clusters=number_of_clusters).fit_predict(data)
    if number_of_clusters > len(set(clusters)):
        number_of_clusters = len(set(clusters))
        clusters = KMeans(n_clusters=number_of_clusters).fit_predict(data)
    dataParts = []
    parts_response = []
    for i in range(number_of_clusters):
        dataParts.append([])
        parts_response.append([])

    for i in range(len(clusters)):
        dataParts[clusters[i]].append(data[i])
        parts_response[clusters[i]].append(responseData[i])

    model_residuals = []

    for i in range(len(models)):
        model_residuals.append([])
    for i in range(len(models)):
        for j in range(number_of_clusters):
            model_residuals[i].append(fitness(models[i], np.transpose(dataParts[j]), parts_response[j]))

    best = []
    for i in range(number_of_clusters):
        ordering = np.argsort(model_residuals[i])
        j = 0
        while ordering[j] in best:
            j += 1
        best.append(ordering[j])
    ensemble = [models[best[i]] for i in range(number_of_clusters)]

    return ensemble


def uncertainty(data):
    wl = None
    if len(data) <= 4:
        wl = 1
    h = differential_entropy(data, window_length=wl)
    if np.isfinite(h):
        return h
    else:
        return 0


def evaluate_model_ensemble(ensemble, inputData):
    responses = [evaluate_gp_model(mod, inputData) for mod in ensemble]
    if type(responses[0]) == np.ndarray:
        responses = np.transpose(responses)
        uncertainties = [uncertainty(res, 0) for res in responses]
    else:

        uncertainties = [uncertainty(responses, 0)]

    return uncertainties


def relative_ensemble_uncertainty(ensemble, inputData):
    output = evaluate_model_ensemble(ensemble, inputData)
    return np.array(output)


def create_uncertainty_func(ensemble):
    return lambda x: -relative_ensemble_uncertainty(ensemble, x)


def maximize_uncertainty(ensemble, varCount, bounds=[]):  # Used to select a new point of maximum uncertainty
    func = create_uncertainty_func(ensemble)
    x0 = [np.mean(bounds[i]) for i in range(varCount)]
    if not bounds:
        pt = minimize(func, x0).x
    else:
        pt = minimize(func, x0, bounds=bounds).x
    return pt
