import inspect
import numpy as np


def reverse_list(data):
    """returns the data list reversed"""
    return [i for i in reversed(data)]


def extend_data(data, newPoint):
    return np.concatenate((data.T, np.array([newPoint]))).T


def sort_models(models):
    """sorts a model population by the models' accuracies"""
    return sorted(models, key=lambda m: m[2])


def replace_func(stack, f1, f2):
    return [i if i != f1 else f2 for i in stack]


def input_len(data):
    """determines the number of data records in a data set"""
    el1 = data[0]
    if type(el1) == list or type(el1) == np.ndarray:
        return len(el1)
    else:
        return 1


def var_replace(data, variables):
    """replaces references to variables in data with actual values"""
    return [i(variables) if callable(i) else i for i in data]


def get_numeric_indices(l):  # Returns indices of list that are numeric
    return [i for i in range(len(l)) if type(l[i]) in [int, float]]


def var_count(data):
    """determines the number of variables in a data set"""
    return len(data)


def get_arity(func):  # Returns the arity of a function: used for model evaluations
    """takes a function and returns the function arity"""
    if func == "pop":
        return 1
    return len(inspect.signature(func).parameters)



def model_arity(model):
    """ returns the total arity of a model"""
    return 1 + sum([get_arity(i) - 1 for i in model[0]])


def list_arity(data):
    """the arity of evaluating a list of operators"""
    if len(data) == 0:
        return 0
    return 1 + sum([get_arity(i) - 1 for i in data])


def build_empty_model():
    """ takes no inputs and generates an empty GP model"""
    return [[], [], []]


def variable_select(num):
    """creates a function to select the nth variable"""
    return lambda variables: variables[num]


def model_to_list_form(model):
    model[0] = model[0].tolist()


def model_restore_form(model):
    model[0] = np.array(model[0], dtype=object)
