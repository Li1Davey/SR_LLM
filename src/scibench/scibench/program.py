import numpy as np
import array
from scibench.tokens import PlaceholderConstant
from scibench import cyfunc



class sciProgram(object):
    """
    The executable program representing the symbolic expression.

    The program comprises unary/binary operators, input variables, and hard-coded constants.

    Parameters
    ----------
    tokens : list of integers
        A list of integers corresponding to tokens in the library.

    Attributes
    ----------
    traversal : list
        List of operators (type: Function) and terminals (type: int, float, or
        str ("const")) encoding the pre-order traversal of the expression tree.

    tokens : np.ndarry (dtype: int)
        Array of integers whose values correspond to indices

    """
    task = None  # Task
    library = None  # Library
    execute = None  # Link to execute. Either cython or python

    def __init__(self, tokens=None):
        """
        Builds the Program from a list of of integers corresponding to Tokens.
        """
        # Can be empty if we are unpickling
        if tokens is not None:
            self._init(tokens)

    def _init(self, tokens):
        # pre-order of the program. the most important thing.
        self.traversal = [sciProgram.library[t] for t in tokens]

        # position of the constant
        self.const_pos = [i for i, t in enumerate(self.traversal) if isinstance(t, PlaceholderConstant)]

        self.len_traversal = len(self.traversal)

        self.invalid = False  # always false.
        self.str = tokens.tostring()
        self.tokens = tokens

    @classmethod
    def set_execute(cls, protected, simulated_exec=False):
        if simulated_exec == True:
            raw_execute = python_execute2d
        else:
            raw_execute = cython_execute

        sciProgram.protected = bool(protected)

        # wrapper used for BOTH protected and unsafe modes
        def execute_checked(traversal, X):
            # avoid expensive warning logging; just ignore and check result
            with np.errstate(all='ignore'):
                y = raw_execute(traversal, X)

            # normalize result to np.array
            if y is None:
                return None, True, 'none', 'invalid'

            y = np.asarray(y)

            # fast reject if any non-finite
            if not np.all(np.isfinite(y)):
                return y, True, 'nonfinite', 'invalid'

            return y, False, None, None

        if sciProgram.protected:
            # protected still returns only y to caller, but we also want invalid info
            def protected_execute(traversal, X):
                y, invalid, error_node, error_type = execute_checked(traversal, X)
                # stash latest flags on class so Program.execute can read if desired
                sciProgram._last_invalid = invalid
                sciProgram._last_error_node = error_node
                sciProgram._last_error_type = error_type
                return y

            sciProgram.execute_function = protected_execute
            sciProgram._last_invalid = False
            sciProgram._last_error_node = None
            sciProgram._last_error_type = None

        else:
            # unsafe mode returns (y, invalid, node, type) already
            def unsafe_execute(traversal, X):
                return execute_checked(traversal, X)

            sciProgram.execute_function = unsafe_execute

    def execute(self, X):
        if not sciProgram.protected:
            result, self.invalid, self.error_node, self.error_type = sciProgram.execute_function(self.traversal, X)
        else:
            result = sciProgram.execute_function(self.traversal, X)
            self.invalid = getattr(sciProgram, "_last_invalid", False)
            self.error_node = getattr(sciProgram, "_last_error_node", None)
            self.error_type = getattr(sciProgram, "_last_error_type", None)
        return result

    def print_expression(self):
        print("\tExpression {}: {}".format(0, self.traversal))

    def __repr__(self):
        """Prints the program's traversal"""
        return ','.join([repr(t) for t in self.traversal])


def python_execute2d(traversal, X):
    """
    Executes the program according to X using Python.

    X : array-like, shape = [batch_size, n_features, n_feature], n_features is the number of features.

    Returns
    -------
    y_hats : array-like, shape = [batch_size, n_features, n_feature]
        The result of executing the program on X.
    """

    apply_stack = []

    for node in traversal:
        apply_stack.append([node])

        while len(apply_stack[-1]) == apply_stack[-1][0].arity + 1:
            token = apply_stack[-1][0]
            terminals = apply_stack[-1][1:]

            if token.input_var is not None:
                intermediate_result = X[:, :]
            else:
                intermediate_result = token(*terminals)
            if len(apply_stack) != 1:
                apply_stack.pop()
                apply_stack[-1].append(intermediate_result)
            else:
                return intermediate_result

    assert False, "Function should never get here!"
    return None


def python_execute(traversal, X):
    """
    Executes the program according to X using Python.

    Parameters
    ----------
    X : array-like, shape = [n_samples, n_features], where n_samples is the number of samples and n_features is the number of features.

    Returns
    -------
    y_hats : array-like, shape = [n_samples]
        The result of executing the program on X.
    """

    apply_stack = []

    for node in traversal:
        apply_stack.append([node])

        while len(apply_stack[-1]) == apply_stack[-1][0].arity + 1:
            token = apply_stack[-1][0]
            terminals = apply_stack[-1][1:]

            if token.input_var is not None:
                intermediate_result = X[:, token.input_var]
            else:
                intermediate_result = token(*terminals)
            if len(apply_stack) != 1:
                apply_stack.pop()
                apply_stack[-1].append(intermediate_result)
            else:
                return intermediate_result

    assert False, "Function should never get here!"
    return None


def cython_execute(traversal, X):
    """
    Execute cython function using given traversal over input X.

    Parameters
    ----------

    traversal : list
        A list of nodes representing the traversal over a Program.
    X : np.array
        The input values to execute the traversal over.

    Returns
    -------

    result : float
        The result of executing the traversal.
    """
    if len(traversal) >= 1:
        is_input_var = array.array('i', [t.input_var is not None for t in traversal])
        return cyfunc.execute(X, len(traversal), traversal, is_input_var)
    else:
        return None
