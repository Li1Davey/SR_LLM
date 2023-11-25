import numpy as np
import math
from scipy.stats import pearsonr
import utils


def ev_mod_helper(varStack, opStack, tempStack, data):
    """is a helper function for evaluateGPModel"""
    stack1 = varStack
    stack2 = opStack
    stack3 = tempStack

    if len(stack2) == 0:
        return [stack3, stack2, stack1]
    op = stack2[0]
    stack2 = stack2[1:]

    if callable(op):

        patt = utils.get_arity(op)
        while patt > len(stack3):
            stack3 = [stack1[0]] + stack3
            stack1 = stack1[1:]
        try:
            temp = op(*utils.var_replace(utils.reverse_list(stack3[:patt]), data))
        except TypeError:
            print("stack3: ", stack3, " patt: ", patt, " data: ", data)
            temp = np.nan
        except OverflowError:
            temp = np.nan
        stack3 = stack3[patt:]
        stack3 = [temp] + stack3

    else:
        if len(stack1) > 0:
            stack3 = utils.var_replace([stack1[0]], data) + stack3
            stack1 = stack1[1:]
    if len(stack2) > 0:
        stack1, stack2, stack3 = ev_mod_helper(stack1, stack2, stack3, data)

    return [stack1, stack2, stack3]


def evaluate_gp_model(model, inputData):
    """numerically evaluates a model using the data stored in inputData"""
    response = ev_mod_helper(model[1], model[0], [], np.array(inputData).astype(float))[2][0]
    if not type(response) == np.ndarray and utils.input_len(inputData) > 1:
        response = np.array([response for i in range(utils.input_len(inputData))])
    return response


def fitness(prog, data, response):
    """returns the 1-R^2 value of a model"""
    predicted = evaluate_gp_model(prog, np.array(data))
    if type(predicted) != list and type(predicted) != np.ndarray:
        predicted = np.array([predicted for i in range(utils.input_len(data))])
    try:
        if np.isnan(predicted).any() or np.isinf(predicted).any():
            return np.nan
    except TypeError:
        return np.nan
    except OverflowError:
        return np.nan
    if (not all(np.isfinite(np.array(predicted, dtype=np.float32)))) or np.all(predicted == predicted[0]):
        return np.nan
    try:
        fit = 1 - pearsonr(predicted, np.array(response))[0] ** 2  # 1-R^2
    except ValueError:
        return 1
    if math.isnan(fit):
        return 1  # If nan return 1 as fitness
    return fit  # Else return actual fitness 1-R^2


def stack_gp_model_complexity(model, *args):
    """returns the complexity of the model"""
    return len(model[0]) + len(model[1]) - model[0].tolist().count("pop")


def set_model_quality(model, inputData, response, modelEvaluationMetrics=[fitness, stack_gp_model_complexity]):
    """ is an inplace operator that sets a models quality"""
    model[2] = [i(model, inputData, response) for i in modelEvaluationMetrics]


class RegressTask(object):
    """
    used to handle input data 'X' for querying the data oracle.
    also used to set the controlled variables in input data `X`
    """

    def __init__(self, batchsize, allowed_input, dataX, data_query_oracle):
        """
            batchsize: batch size
            allowed_input: 1 if the input variable is free. 0 if the input variable is controlled.
            dataX: generate the input data.
        """
        self.batchsize = batchsize
        self.allowed_input = allowed_input
        self.n_input = allowed_input.size
        self.dataX = dataX
        self.data_query_oracle = data_query_oracle

        self.fixed_column = [i for i in range(self.n_input) if self.allowed_input[i] == 0]
        self.X_fixed = np.random.rand(self.n_input)

    def set_allowed_inputs(self, allowed_inputs):
        self.allowed_input = np.copy(allowed_inputs)
        self.fixed_column = [i for i in range(self.n_input) if self.allowed_input[i] == 0]

    def set_allowed_input(self, i, flag):
        self.allowed_input[i] = flag
        self.fixed_column = [i for i in range(self.n_input) if self.allowed_input[i] == 0]

    def rand_draw_X_non_fixed(self):
        self.X = self.dataX.randn(sample_size=self.batchsize).T

    def rand_draw_X_fixed(self):
        self.X_fixed = np.squeeze(self.dataX.randn(sample_size=1))

    def rand_draw_data_with_X_fixed(self):
        self.X = self.dataX.randn(sample_size=self.batchsize).T
        if len(self.fixed_column):
            self.X[:, self.fixed_column] = self.X_fixed[self.fixed_column]

    def evaluate(self):
        return self.data_query_oracle.evaluate(self.X)

    def reward_function(self, p):
        y_hat = p.execute(self.X)
        return self.data_query_oracle._evaluate_loss(self.X, y_hat)
