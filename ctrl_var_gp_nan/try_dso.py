import functions
from library import Library, Token, PlaceholderConstant
import execute

from program import Program
import regress_task
from const import ScipyMinimize

import gp_xyx

import numpy as np

def try_dso_v1():
    # XYX: v1 needs to be fixed to be able to run again.
    nvar = 3
    nins = 5

    # get all the functions and variables ready
    var_x = []
    for i in range(nvar):
        xi = Token(None, 'X_'+str(i), 0, 0., i)
        var_x.append(xi)

    unprotected_ops = [
        # Binary operators
        Token(np.add, "add", arity=2, complexity=1),
        Token(np.subtract, "sub", arity=2, complexity=1),
        Token(np.multiply, "mul", arity=2, complexity=1)
    ]
    protected_library = Library(unprotected_ops + functions.protected_ops + var_x)

    # get program ready
    Program.library = protected_library
    #Program.execute = execute.python_execute
    Program.set_execute(True) #protected = True

    # run a program
    preorder = ['div', 'X_0', 'add', 'X_2', 'X_1']
    preorder_actions = protected_library.actionize(preorder)
    print('preorder_actions=', preorder_actions)
    
    pr = Program(preorder_actions)

    print('pr=', pr.__getstate__())

    # actually execute it
    x = np.random.rand(nins, nvar)
    print('x=', x)

    print('pr.traversal=', pr.traversal)
    result = pr.execute(x)

    print('result=', result)
    print('x0/(x2+x1)=', x[:,0] / (x[:,2] + x[:,1]))

    
def try_dso_v2():
    nvar = 3
    nins = 5

    # get all the functions and variables ready
    var_x = []
    for i in range(nvar):
        xi = Token(None, 'X_'+str(i), 0, 0., i)
        var_x.append(xi)

    unprotected_ops = [
        # Binary operators
        Token(np.add, "add", arity=2, complexity=1),
        Token(np.subtract, "sub", arity=2, complexity=1),
        Token(np.multiply, "mul", arity=2, complexity=1)
    ]
    named_const = [PlaceholderConstant(1.0)]
    protected_library = Library(unprotected_ops + functions.protected_ops + var_x + named_const)

    allowed_input_tokens = np.array([1, 1, 0])
    protected_library.set_allowed_input_tokens(allowed_input_tokens)

    # get program ready
    Program.library = protected_library    
    #Program.execute = execute.python_execute
    Program.set_execute(True) #protected = True

    # create the true program
    preorder = ['add', 'const', 'X_0']
    preorder_actions = protected_library.actionize(preorder)
    true_pr_allow_change = np.array([0, 0, 0])
    true_pr = Program(preorder_actions, true_pr_allow_change)
    true_pr.traversal[1] = PlaceholderConstant(-5.0)     # actually make it X0 + 5

    # create the approximate program
    preorder = ['sub', 'X_0', 'const']
    preorder_actions = protected_library.actionize(preorder)
    pr_allow_change = np.array([1, 1, 1])
    pr = Program(preorder_actions, pr_allow_change)

    # set the task
    Program.task = regress_task.RegressTaskV1(256, allowed_input_tokens, true_pr)

    # set const_optimizer
    Program.const_optimizer = ScipyMinimize()

    pr.optimize()
    
    # print('pr=', pr.__getstate__())

    # # actually execute it
    # x = np.random.rand(nins, nvar)
    # print('x=', x)

    # print('pr.traversal=', pr.traversal)
    # result = pr.execute(x)

    # print('result=', result)
    # print('x0/(x2+x1)=', x[:,0] / (x[:,2] + x[:,1]))

    
def try_gp_helper():
    nvar = 3
    nins = 5

    # get all the functions and variables ready
    var_x = []
    for i in range(nvar):
        xi = Token(None, 'X_'+str(i), 0, 0., i)
        var_x.append(xi)

    unprotected_ops = [
        # Binary operators
        Token(np.add, "add", arity=2, complexity=1),
        Token(np.subtract, "sub", arity=2, complexity=1),
        Token(np.multiply, "mul", arity=2, complexity=1)
    ]
    named_const = [PlaceholderConstant(1.0)]
    protected_library = Library(unprotected_ops + functions.protected_ops + var_x + named_const)

    allowed_input_tokens = np.array([1, 1, 0])
    protected_library.set_allowed_input_tokens(allowed_input_tokens)

    # get program ready
    Program.library = protected_library    
    #Program.execute = execute.python_execute
    Program.set_execute(True) #protected = True

    protected_library.print_library()

    # create program a
    a_preorder = ['add', 'const', 'X_0']
    a_preorder_actions = protected_library.actionize(a_preorder)
    a_pr_allow_change = np.array([1, 1, 1])
    a_pr = Program(a_preorder_actions, a_pr_allow_change)

    # create program b
    b_preorder = ['sub', 'X_1', 'mul', 'const', 'X_0']
    b_preorder_actions = protected_library.actionize(b_preorder)
    b_pr_allow_change = np.array([1, 1, 1, 1, 1])
    b_pr = Program(b_preorder_actions, b_pr_allow_change)

    # initialize gp_helper
    gp_helper = gp_xyx.GPHelper()
    gp_helper.library = protected_library

    print('before mate')
    print('a_pr.state=', a_pr.__getstate__())
    print('b_pr.state=', b_pr.__getstate__())

    gp_helper.mate(a_pr, b_pr)
    
    print('after mate')
    print('a_pr.state=', a_pr.__getstate__())
    print('b_pr.state=', b_pr.__getstate__())

    print('')
    gp_helper.mutUniform(a_pr, 3)
    print('after mutUniform')
    print('a_pr.state=', a_pr.__getstate__())

    print('')
    print('before mutNodeReplacement')
    print('b_pr.state=', b_pr.__getstate__())
    gp_helper.mutNodeReplacement(b_pr)
    print('after mutNodeReplacement')
    print('b_pr.state=', b_pr.__getstate__())

    print('')
    print('before mutInsert')
    print('b_pr.state=', b_pr.__getstate__())
    gp_helper.mutInsert(b_pr, 3)
    print('after mutInsert')
    print('b_pr.state=', b_pr.__getstate__())

    print('')
    print('before mutShrink')
    print('b_pr.state=', b_pr.__getstate__())
    gp_helper.mutShrink(b_pr)
    print('after mutShrink')
    print('b_pr.state=', b_pr.__getstate__())

    print('\nGP Init Population')
    gp = gp_xyx.GeneticProgram()
    gp.library = protected_library
    gp.gp_helper = gp_helper
    gp.create_init_population()
    gp.print_population()
    

if __name__ == '__main__':
    # try_dso_v2()
    try_gp_helper()
