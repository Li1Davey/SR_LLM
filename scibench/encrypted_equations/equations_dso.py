from collections import OrderedDict
import sympy
from base import KnownEquation

EQUATION_CLASS_DICT = OrderedDict()


def register_eq_class(cls):
    EQUATION_CLASS_DICT[cls.__name__] = cls
    return cls


def get_eq_obj(key, **kwargs):
    if key in EQUATION_CLASS_DICT:
        return EQUATION_CLASS_DICT[key](**kwargs)
    raise KeyError(f'`{key}` is not expected as a equation object key')

@register_eq_class
class Keijzer_1(KnownEquation):
    _eq_name = 'Keijzer_1'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = 0.3*x[0]*sympy.sin(2*sympy.pi*x[0])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (0.300000000000000, 'const'), ('X_0', 'var'), ('sin', 'unary'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var')]

@register_eq_class
class Keijzer_2(KnownEquation):
    _eq_name = 'Keijzer_2'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = 0.3*x[0]*sympy.sin(2*sympy.pi*x[0])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (0.300000000000000, 'const'), ('X_0', 'var'), ('sin', 'unary'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var')]

@register_eq_class
class Keijzer_3(KnownEquation):
    _eq_name = 'Keijzer_3'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = 0.3*x[0]*sympy.sin(2*sympy.pi*x[0])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (0.300000000000000, 'const'), ('X_0', 'var'), ('sin', 'unary'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var')]

@register_eq_class
class Keijzer_4(KnownEquation):
    _eq_name = 'Keijzer_4'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = x[0]*x[0]*x[0]*sympy.exp(-x[0])*sympy.cos(x[0])*sympy.sin(x[0])*(sympy.sin(x[0])*sympy.sin(x[0])*sympy.cos(x[0])-1)
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), (3, 'const'), ('add', 'binary'), (-1, 'const'), ('mul', 'binary'), ('sin', 'unary'), ('X_0', 'var'), (2, 'const'), ('cos', 'unary'), ('X_0', 'var'), ('cos', 'unary'), ('X_0', 'var'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('sin', 'unary'), ('X_0', 'var')]

@register_eq_class
class Keijzer_5(KnownEquation):
    _eq_name = 'Keijzer_5'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = (30*x[0]*x[2])/((x[0]-10)*x[1]*x[1])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (30, 'const'), ('X_0', 'var'), ('X_2', 'var'), ('X_1', 'var'), (-2, 'const'), ('add', 'binary'), (-10, 'const'), ('X_0', 'var'), (-1, 'const')]

@register_eq_class
class Keijzer_6(KnownEquation):
    _eq_name = 'Keijzer_6'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = (x[0]*(x[0]+1))/(2)
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), (1, 'const'), ('X_0', 'var')]

@register_eq_class
class Keijzer_7(KnownEquation):
    _eq_name = 'Keijzer_7'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.log(x[0])
        self.sympy_eq_preorder_traversal = [('log', 'unary'), ('X_0', 'var')]

@register_eq_class
class Keijzer_8(KnownEquation):
    _eq_name = 'Keijzer_8'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sqrt(x[0])
        self.sympy_eq_preorder_traversal = [('X_0', 'var')]

@register_eq_class
class Keijzer_9(KnownEquation):
    _eq_name = 'Keijzer_9'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.log(x[0]+sympy.sqrt(x[0]*x[0]+1))
        self.sympy_eq_preorder_traversal = [('log', 'unary'), ('add', 'binary'), ('X_0', 'var'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Keijzer_10(KnownEquation):
    _eq_name = 'Keijzer_10'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],x[1])
        self.sympy_eq_preorder_traversal = [('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Keijzer_11(KnownEquation):
    _eq_name = 'Keijzer_11'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = x[0]*x[1]+sympy.sin((x[0]-1)*(x[1]-1))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('sin', 'unary'), ('mul', 'binary'), ('add', 'binary'), (-1, 'const'), ('X_0', 'var'), ('add', 'binary'), (-1, 'const'), ('X_1', 'var')]

@register_eq_class
class Keijzer_12(KnownEquation):
    _eq_name = 'Keijzer_12'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],4)-sympy.Pow(x[0],3)+ sympy.Pow(x[1],2)/2-x[1]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const')]

@register_eq_class
class Keijzer_13(KnownEquation):
    _eq_name = 'Keijzer_13'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 6*sympy.sin(x[0])*sympy.cos(x[1])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (6, 'const'), ('cos', 'unary'), ('X_1', 'var'), ('sin', 'unary'), ('X_0', 'var')]

@register_eq_class
class Keijzer_14(KnownEquation):
    _eq_name = 'Keijzer_14'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 8/(2+sympy.Pow(x[0],2)+sympy.Pow(x[1],2))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (8, 'const'), ('add', 'binary'), (2, 'const'), ('X_0', 'var'), (2, 'const'), ('X_1', 'var'), (2, 'const'), (-1, 'const')]

@register_eq_class
class Keijzer_15(KnownEquation):
    _eq_name = 'Keijzer_15'
    _function_set = ['add', 'mul', 'div', 'exp', 'log', 'pow', 'inv', 'neg', 'sqrt', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (sympy.Pow(x[0],3))/(5)+(sympy.Pow(x[1],3))/(2)-x[1]-x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('X_1', 'var'), (3, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), ('X_0', 'var'), (3, 'const')]

@register_eq_class
class Korns_1(KnownEquation):
    _eq_name = 'Korns_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'n2', 'n3', 'sqrt', 'tan', 'tanh', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 1.57+24.3*x[3]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (1.57000000000000, 'const'), ('mul', 'binary'), (24.3000000000000, 'const'), ('X_3', 'var')]

@register_eq_class
class Korns_2(KnownEquation):
    _eq_name = 'Korns_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'n2', 'n3', 'sqrt', 'tan', 'tanh', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.23+14.2*((x[3]+x[1]))/((3*x[4]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (0.230000000000000, 'const'), ('mul', 'binary'), ('X_4', 'var'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), (14.2000000000000, 'const'), ('X_1', 'var'), ('mul', 'binary'), (14.2000000000000, 'const'), ('X_3', 'var')]

@register_eq_class
class Korns_3(KnownEquation):
    _eq_name = 'Korns_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'n2', 'n3', 'sqrt', 'tan', 'tanh', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 4.9*((x[3]-x[0]+(x[1])/(x[4])))/((3*x[4]))-5.41
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-5.41000000000000, 'const'), ('mul', 'binary'), ('X_4', 'var'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), (4.90000000000000, 'const'), ('X_3', 'var'), ('mul', 'binary'), (-4.90000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (4.90000000000000, 'const'), ('X_1', 'var'), ('X_4', 'var'), (-1, 'const')]

@register_eq_class
class Korns_4(KnownEquation):
    _eq_name = 'Korns_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'n2', 'n3', 'sqrt', 'tan', 'tanh', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.13*sympy.sin(x[2])-2.3
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-2.30000000000000, 'const'), ('mul', 'binary'), (0.130000000000000, 'const'), ('sin', 'unary'), ('X_2', 'var')]

@register_eq_class
class Korns_5(KnownEquation):
    _eq_name = 'Korns_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'n2', 'n3', 'sqrt', 'tan', 'tanh', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 3+2.13*sympy.log(abs(x[4]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (3, 'const'), ('mul', 'binary'), (2.13000000000000, 'const'), ('log', 'unary'), ('X_4', 'var')]

@register_eq_class
class Korns_6(KnownEquation):
    _eq_name = 'Korns_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'n2', 'n3', 'sqrt', 'tan', 'tanh', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 1.3+0.13*sympy.sqrt(abs(x[0]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (1.30000000000000, 'const'), ('mul', 'binary'), (0.130000000000000, 'const'), ('X_0', 'var')]

@register_eq_class
class Korns_7(KnownEquation):
    _eq_name = 'Korns_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'n2', 'n3', 'sqrt', 'tan', 'tanh', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 2.1380940889*(1-sympy.exp(-0.54723748542*x[0]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (2.13809408890000, 'const'), ('mul', 'binary'), (-2.13809408890000, 'const'), ('exp', 'unary'), ('mul', 'binary'), (-0.547237485420000, 'const'), ('X_0', 'var')]

@register_eq_class
class Korns_8(KnownEquation):
    _eq_name = 'Korns_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'n2', 'n3', 'sqrt', 'tan', 'tanh', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 6.87+11*sympy.sqrt(abs(7.23*x[0]*x[3]*x[4]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (6.87000000000000, 'const'), ('mul', 'binary'), (11, 'const'), ('mul', 'binary'), (7.23000000000000, 'const'), ('X_0', 'var'), ('X_3', 'var'), ('X_4', 'var')]

@register_eq_class
class Korns_9(KnownEquation):
    _eq_name = 'Korns_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'n2', 'n3', 'sqrt', 'tan', 'tanh', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = (sympy.sqrt(abs(x[0])))/(sympy.log(abs(x[1])))*(sympy.exp(x[2]))/(sympy.Pow(x[3],2))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('log', 'unary'), ('X_1', 'var'), (-1, 'const'), ('X_3', 'var'), (2, 'const'), (-1, 'const'), ('exp', 'unary'), ('X_2', 'var')]

@register_eq_class
class Korns_10(KnownEquation):
    _eq_name = 'Korns_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'n2', 'n3', 'sqrt', 'tan', 'tanh', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 0.81+24.3*(2*x[1]+3*sympy.Pow(x[2],2))/(((4*sympy.Pow(x[3],3)+5*sympy.Pow(x[4],4))))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (0.810000000000000, 'const'), ('mul', 'binary'), ('add', 'binary'), ('mul', 'binary'), (4, 'const'), ('X_3', 'var'), (3, 'const'), ('mul', 'binary'), (5, 'const'), ('X_4', 'var'), (4, 'const'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), (72.9000000000000, 'const'), ('X_2', 'var'), (2, 'const'), ('mul', 'binary'), (48.6000000000000, 'const'), ('X_1', 'var')]

@register_eq_class
class Korns_11(KnownEquation):
    _eq_name = 'Korns_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'n2', 'n3', 'sqrt', 'tan', 'tanh', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 6.87+11*sympy.cos(7.23*sympy.Pow(x[0],3))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (6.87000000000000, 'const'), ('mul', 'binary'), (11, 'const'), ('cos', 'unary'), ('mul', 'binary'), (7.23000000000000, 'const'), ('X_0', 'var'), (3, 'const')]

@register_eq_class
class Korns_12(KnownEquation):
    _eq_name = 'Korns_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'n2', 'n3', 'sqrt', 'tan', 'tanh', 'const']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 2-2.1*sympy.cos(9.8*x[0])*sympy.sin(1.3*x[4])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (2, 'const'), ('mul', 'binary'), (-2.10000000000000, 'const'), ('cos', 'unary'), ('mul', 'binary'), (9.80000000000000, 'const'), ('X_0', 'var'), ('sin', 'unary'), ('mul', 'binary'), (1.30000000000000, 'const'), ('X_4', 'var')]

@register_eq_class
class Koza_2(KnownEquation):
    _eq_name = 'Koza_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],5)-2*sympy.Pow(x[0],3)+x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-2, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (5, 'const')]

@register_eq_class
class Koza_3(KnownEquation):
    _eq_name = 'Koza_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],6)-2*sympy.Pow(x[0],4)+sympy.Pow(x[0],2)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-2, 'const'), ('X_0', 'var'), (4, 'const'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (6, 'const')]

@register_eq_class
class Meier_3(KnownEquation):
    _eq_name = 'Meier_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (sympy.Pow(x[0],2)*sympy.Pow(x[1],2))/((x[0]+x[1]))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), ('X_0', 'var'), ('X_1', 'var'), (-1, 'const'), ('X_0', 'var'), (2, 'const'), ('X_1', 'var'), (2, 'const')]

@register_eq_class
class Meier_4(KnownEquation):
    _eq_name = 'Meier_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (sympy.Pow(x[0],5))/(sympy.Pow(x[1],3))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_1', 'var'), (3, 'const'), (-1, 'const'), ('X_0', 'var'), (5, 'const')]

@register_eq_class
class Nguyen_1(KnownEquation):
    _eq_name = 'Nguyen_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],3)+sympy.Pow(x[0],2)+x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (3, 'const')]

@register_eq_class
class Nguyen_2(KnownEquation):
    _eq_name = 'Nguyen_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],4)+sympy.Pow(x[0],3)+sympy.Pow(x[0],2)+x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const')]

@register_eq_class
class Nguyen_3(KnownEquation):
    _eq_name = 'Nguyen_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],5)+sympy.Pow(x[0],4)+sympy.Pow(x[0],3)+sympy.Pow(x[0],2)+x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const'), ('X_0', 'var'), (5, 'const')]

@register_eq_class
class Nguyen_4(KnownEquation):
    _eq_name = 'Nguyen_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],6)+sympy.Pow(x[0],5)+sympy.Pow(x[0],4)+sympy.Pow(x[0],3)+sympy.Pow(x[0],2)+x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const'), ('X_0', 'var'), (5, 'const'), ('X_0', 'var'), (6, 'const')]

@register_eq_class
class Nguyen_5(KnownEquation):
    _eq_name = 'Nguyen_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sin(sympy.Pow(x[0],2))*sympy.cos(x[0])-1
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-1, 'const'), ('mul', 'binary'), ('cos', 'unary'), ('X_0', 'var'), ('sin', 'unary'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Nguyen_6(KnownEquation):
    _eq_name = 'Nguyen_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sin(x[0])+sympy.sin(x[0]+sympy.Pow(x[0],2))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('sin', 'unary'), ('X_0', 'var'), ('sin', 'unary'), ('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Nguyen_7(KnownEquation):
    _eq_name = 'Nguyen_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.log(x[0]+1)+sympy.log(sympy.Pow(x[0],2)+1)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('log', 'unary'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), ('log', 'unary'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Nguyen_8(KnownEquation):
    _eq_name = 'Nguyen_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sqrt(x[0])
        self.sympy_eq_preorder_traversal = [('X_0', 'var')]

@register_eq_class
class Nguyen_9(KnownEquation):
    _eq_name = 'Nguyen_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.sin(x[0])+sympy.sin(sympy.Pow(x[1],2))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('sin', 'unary'), ('X_0', 'var'), ('sin', 'unary'), ('X_1', 'var'), (2, 'const')]

@register_eq_class
class Nguyen_10(KnownEquation):
    _eq_name = 'Nguyen_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 2*sympy.sin(x[0])*sympy.cos(x[1])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (2, 'const'), ('cos', 'unary'), ('X_1', 'var'), ('sin', 'unary'), ('X_0', 'var')]

@register_eq_class
class Nguyen_11(KnownEquation):
    _eq_name = 'Nguyen_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],x[1])
        self.sympy_eq_preorder_traversal = [('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Nguyen_12(KnownEquation):
    _eq_name = 'Nguyen_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],4)-sympy.Pow(x[0],3)+(sympy.Pow(x[1],2))/(2)-x[1]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const')]

@register_eq_class
class Nguyen_12a(KnownEquation):
    _eq_name = 'Nguyen_12a'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],4)-sympy.Pow(x[0],3)+sympy.Pow(x[1],2)/2-x[1]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const')]

@register_eq_class
class Constant_1(KnownEquation):
    _eq_name = 'Constant_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = 3.39*sympy.Pow(x[0],3)+2.12*sympy.Pow(x[0],2)+1.78*x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (2.12000000000000, 'const'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (3.39000000000000, 'const'), ('X_0', 'var'), (3, 'const'), ('mul', 'binary'), (1.78000000000000, 'const'), ('X_0', 'var')]

@register_eq_class
class Constant_2(KnownEquation):
    _eq_name = 'Constant_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sin(sympy.Pow(x[0],2))*sympy.cos(x[0])-0.75
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-0.750000000000000, 'const'), ('mul', 'binary'), ('cos', 'unary'), ('X_0', 'var'), ('sin', 'unary'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Constant_3(KnownEquation):
    _eq_name = 'Constant_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.sin(1.5*x[0])*sympy.cos(0.5*x[1])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('cos', 'unary'), ('mul', 'binary'), (0.500000000000000, 'const'), ('X_1', 'var'), ('sin', 'unary'), ('mul', 'binary'), (1.50000000000000, 'const'), ('X_0', 'var')]

@register_eq_class
class Constant_4(KnownEquation):
    _eq_name = 'Constant_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 2.7*sympy.Pow(x[0],x[1])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (2.70000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Constant_5(KnownEquation):
    _eq_name = 'Constant_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sqrt(1.23*x[0])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (1.10905365064094, 'const'), ('X_0', 'var')]

@register_eq_class
class Constant_6(KnownEquation):
    _eq_name = 'Constant_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],0.426)
        self.sympy_eq_preorder_traversal = [('X_0', 'var'), (0.426000000000000, 'const')]

@register_eq_class
class Constant_7(KnownEquation):
    _eq_name = 'Constant_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 2*sympy.sin(1.3*x[0])*sympy.cos(x[1])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (2, 'const'), ('cos', 'unary'), ('X_1', 'var'), ('sin', 'unary'), ('mul', 'binary'), (1.30000000000000, 'const'), ('X_0', 'var')]

@register_eq_class
class Constant_8(KnownEquation):
    _eq_name = 'Constant_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.log(x[0]+1.4)+sympy.log(sympy.Pow(x[0],2)+1.3)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('log', 'unary'), ('add', 'binary'), (1.40000000000000, 'const'), ('X_0', 'var'), ('log', 'unary'), ('add', 'binary'), (1.30000000000000, 'const'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore_1(KnownEquation):
    _eq_name = 'Livermore_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = 1./3+x[0]+sympy.sin(sympy.Pow(x[0],2))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (0.333333333333333, 'const'), ('X_0', 'var'), ('sin', 'unary'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore_2(KnownEquation):
    _eq_name = 'Livermore_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sin(sympy.Pow(x[0],2))*sympy.cos(x[0])-2
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-2, 'const'), ('mul', 'binary'), ('cos', 'unary'), ('X_0', 'var'), ('sin', 'unary'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore_3(KnownEquation):
    _eq_name = 'Livermore_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sin(sympy.Pow(x[0],3))*sympy.cos(sympy.Pow(x[0],2))-1
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-1, 'const'), ('mul', 'binary'), ('cos', 'unary'), ('X_0', 'var'), (2, 'const'), ('sin', 'unary'), ('X_0', 'var'), (3, 'const')]

@register_eq_class
class Livermore_4(KnownEquation):
    _eq_name = 'Livermore_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.log(x[0]+1)+sympy.log(sympy.Pow(x[0],2)+1)+sympy.log(x[0])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('log', 'unary'), ('X_0', 'var'), ('log', 'unary'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), ('log', 'unary'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore_5(KnownEquation):
    _eq_name = 'Livermore_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],4)-sympy.Pow(x[0],3)+sympy.Pow(x[1],2)-x[1]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const'), ('X_1', 'var'), (2, 'const')]

@register_eq_class
class Livermore_6(KnownEquation):
    _eq_name = 'Livermore_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = 4*sympy.Pow(x[0],4)+3*sympy.Pow(x[0],3)+2*sympy.Pow(x[0],2)+x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (3, 'const'), ('X_0', 'var'), (3, 'const'), ('mul', 'binary'), (4, 'const'), ('X_0', 'var'), (4, 'const')]

@register_eq_class
class Livermore_7(KnownEquation):
    _eq_name = 'Livermore_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = (sympy.exp(x[0])-sympy.exp(-1*x[0]))/(2)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('exp', 'unary'), ('X_0', 'var'), ('mul', 'binary'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var')]

@register_eq_class
class Livermore_7a(KnownEquation):
    _eq_name = 'Livermore_7a'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = (sympy.exp(x[0])-sympy.exp(-1*x[0]))/(2)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('exp', 'unary'), ('X_0', 'var'), ('mul', 'binary'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var')]

@register_eq_class
class Livermore_8(KnownEquation):
    _eq_name = 'Livermore_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = (sympy.exp(x[0])+sympy.exp(-1*x[0]))/(2)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('exp', 'unary'), ('X_0', 'var'), ('mul', 'binary'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var')]

@register_eq_class
class Livermore_8a(KnownEquation):
    _eq_name = 'Livermore_8a'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = (sympy.exp(x[0])+sympy.exp(-1*x[0]))/(2)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('exp', 'unary'), ('X_0', 'var'), ('mul', 'binary'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var')]

@register_eq_class
class Livermore_9(KnownEquation):
    _eq_name = 'Livermore_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],9)+sympy.Pow(x[0],8)+sympy.Pow(x[0],7)+sympy.Pow(x[0],6)+sympy.Pow(x[0],5)+sympy.Pow(x[0],4)+sympy.Pow(x[0],3)+sympy.Pow(x[0],2)+x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const'), ('X_0', 'var'), (5, 'const'), ('X_0', 'var'), (6, 'const'), ('X_0', 'var'), (7, 'const'), ('X_0', 'var'), (8, 'const'), ('X_0', 'var'), (9, 'const')]

@register_eq_class
class Livermore_10(KnownEquation):
    _eq_name = 'Livermore_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 6*sympy.sin(x[0])*sympy.cos(x[1])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (6, 'const'), ('cos', 'unary'), ('X_1', 'var'), ('sin', 'unary'), ('X_0', 'var')]

@register_eq_class
class Livermore_11(KnownEquation):
    _eq_name = 'Livermore_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (sympy.Pow(x[0],2)*sympy.Pow(x[1],2))/((x[0]+x[1]))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), ('X_0', 'var'), ('X_1', 'var'), (-1, 'const'), ('X_0', 'var'), (2, 'const'), ('X_1', 'var'), (2, 'const')]

@register_eq_class
class Livermore_12(KnownEquation):
    _eq_name = 'Livermore_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (sympy.Pow(x[0],5))/(sympy.Pow(x[1],3))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_1', 'var'), (3, 'const'), (-1, 'const'), ('X_0', 'var'), (5, 'const')]

@register_eq_class
class Livermore_13(KnownEquation):
    _eq_name = 'Livermore_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],1/3)
        self.sympy_eq_preorder_traversal = [('X_0', 'var')]

@register_eq_class
class Livermore_14(KnownEquation):
    _eq_name = 'Livermore_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],3)+sympy.Pow(x[0],2)+x[0]+sympy.sin(x[0])+sympy.sin(sympy.Pow(x[1],2))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (3, 'const'), ('sin', 'unary'), ('X_0', 'var'), ('sin', 'unary'), ('X_1', 'var'), (2, 'const')]

@register_eq_class
class Livermore_15(KnownEquation):
    _eq_name = 'Livermore_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],1/5)
        self.sympy_eq_preorder_traversal = [('X_0', 'var')]

@register_eq_class
class Livermore_16(KnownEquation):
    _eq_name = 'Livermore_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],2/3)
        self.sympy_eq_preorder_traversal = [('X_0', 'var')]

@register_eq_class
class Livermore_17(KnownEquation):
    _eq_name = 'Livermore_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 4*sympy.sin(x[0])*sympy.cos(x[1])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (4, 'const'), ('cos', 'unary'), ('X_1', 'var'), ('sin', 'unary'), ('X_0', 'var')]

@register_eq_class
class Livermore_18(KnownEquation):
    _eq_name = 'Livermore_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sin(sympy.Pow(x[0],2))*sympy.cos(x[0])-5
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-5, 'const'), ('mul', 'binary'), ('cos', 'unary'), ('X_0', 'var'), ('sin', 'unary'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore_19(KnownEquation):
    _eq_name = 'Livermore_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.log(sympy.Pow(x[0],2)+x[0])+sympy.log(sympy.Pow(x[0],3)+x[0])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('log', 'unary'), ('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('log', 'unary'), ('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (3, 'const')]

@register_eq_class
class Livermore_20(KnownEquation):
    _eq_name = 'Livermore_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],5)+sympy.Pow(x[0],4)+sympy.Pow(x[0],2)+x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (4, 'const'), ('X_0', 'var'), (5, 'const')]

@register_eq_class
class Livermore_21(KnownEquation):
    _eq_name = 'Livermore_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.exp(-1*sympy.Pow(x[0],2))
        self.sympy_eq_preorder_traversal = [('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore_22(KnownEquation):
    _eq_name = 'Livermore_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],8)+sympy.Pow(x[0],7)+sympy.Pow(x[0],6)+sympy.Pow(x[0],5)+sympy.Pow(x[0],4)+sympy.Pow(x[0],3)+sympy.Pow(x[0],2)+x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const'), ('X_0', 'var'), (5, 'const'), ('X_0', 'var'), (6, 'const'), ('X_0', 'var'), (7, 'const'), ('X_0', 'var'), (8, 'const')]

@register_eq_class
class Livermore_23(KnownEquation):
    _eq_name = 'Livermore_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.exp(-0.5*sympy.Pow(x[0],2))
        self.sympy_eq_preorder_traversal = [('exp', 'unary'), ('mul', 'binary'), (-0.500000000000000, 'const'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Pagie_1(KnownEquation):
    _eq_name = 'Pagie_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (1)/((1+sympy.Pow(x[0],-4)))+(1)/((1+sympy.Pow(x[1],-4)))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), (-4, 'const'), (-1, 'const'), ('add', 'binary'), (1, 'const'), ('X_1', 'var'), (-4, 'const'), (-1, 'const')]

@register_eq_class
class Nonic(KnownEquation):
    _eq_name = 'Nonic'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],9)+sympy.Pow(x[0],8)+sympy.Pow(x[0],7)+sympy.Pow(x[0],6)+sympy.Pow(x[0],5)+sympy.Pow(x[0],4)+sympy.Pow(x[0],3)+sympy.Pow(x[0],2)+x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const'), ('X_0', 'var'), (5, 'const'), ('X_0', 'var'), (6, 'const'), ('X_0', 'var'), (7, 'const'), ('X_0', 'var'), (8, 'const'), ('X_0', 'var'), (9, 'const')]

@register_eq_class
class Poly_10(KnownEquation):
    _eq_name = 'Poly_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=10)
        x = self.x
        self.sympy_eq = x[0]*x[1]+x[2]*x[3]+x[4]*x[5]+x[0]*x[6]*x[8]+x[2]*x[5]*x[9]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('X_3', 'var'), ('mul', 'binary'), ('X_4', 'var'), ('X_5', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_6', 'var'), ('X_8', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('X_5', 'var'), ('X_9', 'var')]

@register_eq_class
class R1(KnownEquation):
    _eq_name = 'R1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = (sympy.Pow(x[0]+1,3))/(sympy.Pow(x[0],2)-x[0]+1)
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), (1, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), (-1, 'const'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), (3, 'const')]

@register_eq_class
class R2(KnownEquation):
    _eq_name = 'R2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = ((sympy.Pow(x[0],5)-3*sympy.Pow(x[0],3)+1))/((sympy.Pow(x[0],2)+1))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), (2, 'const'), (-1, 'const'), ('add', 'binary'), (1, 'const'), ('mul', 'binary'), (-3, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (5, 'const')]

@register_eq_class
class R3(KnownEquation):
    _eq_name = 'R3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = ((sympy.Pow(x[0],6)+sympy.Pow(x[0],5)))/((sympy.Pow(x[0],4)+sympy.Pow(x[0],3)+sympy.Pow(x[0],2)+x[0]+1))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const'), (-1, 'const'), ('add', 'binary'), ('X_0', 'var'), (5, 'const'), ('X_0', 'var'), (6, 'const')]

@register_eq_class
class R1a(KnownEquation):
    _eq_name = 'R1a'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = (sympy.Pow(x[0]+1,3))/(sympy.Pow(x[0],2)-x[0]+1)
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), (1, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), (-1, 'const'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), (3, 'const')]

@register_eq_class
class R2a(KnownEquation):
    _eq_name = 'R2a'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = ((sympy.Pow(x[0],5)-3*sympy.Pow(x[0],3)+1))/((sympy.Pow(x[0],2)+1))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), (2, 'const'), (-1, 'const'), ('add', 'binary'), (1, 'const'), ('mul', 'binary'), (-3, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (5, 'const')]

@register_eq_class
class R3a(KnownEquation):
    _eq_name = 'R3a'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = ((sympy.Pow(x[0],6)+sympy.Pow(x[0],5)))/((sympy.Pow(x[0],4)+sympy.Pow(x[0],3)+sympy.Pow(x[0],2)+x[0]+1))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const'), (-1, 'const'), ('add', 'binary'), ('X_0', 'var'), (5, 'const'), ('X_0', 'var'), (6, 'const')]

@register_eq_class
class Sine(KnownEquation):
    _eq_name = 'Sine'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sin(x[0])+sympy.sin(x[0]+sympy.Pow(x[0],2))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('sin', 'unary'), ('X_0', 'var'), ('sin', 'unary'), ('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Vladislavleva_1(KnownEquation):
    _eq_name = 'Vladislavleva_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'n2', 'exp', 'expneg']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (sympy.exp(-sympy.Pow(x[0]-1,2)))/((1.2+sympy.Pow((x[1]-2.5),2)))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), (1.20000000000000, 'const'), ('add', 'binary'), (-2.50000000000000, 'const'), ('X_1', 'var'), (2, 'const'), (-1, 'const'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('add', 'binary'), (-1, 'const'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Vladislavleva_2(KnownEquation):
    _eq_name = 'Vladislavleva_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'n2', 'exp', 'expneg', 'sin', 'cos']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.exp(-x[0])*sympy.Pow(x[0],3)*sympy.cos(x[0])*sympy.sin(x[0])*(sympy.cos(x[0])*sympy.Pow(sympy.sin(x[0]),2)-1)
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), (-1, 'const'), ('mul', 'binary'), ('cos', 'unary'), ('X_0', 'var'), ('sin', 'unary'), ('X_0', 'var'), (2, 'const'), ('cos', 'unary'), ('X_0', 'var'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('X_0', 'var'), (3, 'const'), ('sin', 'unary'), ('X_0', 'var')]

@register_eq_class
class Vladislavleva_3(KnownEquation):
    _eq_name = 'Vladislavleva_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'n2', 'exp', 'expneg', 'sin', 'cos']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.exp(-x[0])*sympy.Pow(x[0],3)*sympy.cos(x[0])*sympy.sin(x[0])*(sympy.cos(x[0])*sympy.Pow(sympy.sin(x[0]),2)-1)*(x[1]-5)
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), (-1, 'const'), ('mul', 'binary'), ('cos', 'unary'), ('X_0', 'var'), ('sin', 'unary'), ('X_0', 'var'), (2, 'const'), ('add', 'binary'), (-5, 'const'), ('X_1', 'var'), ('cos', 'unary'), ('X_0', 'var'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('X_0', 'var'), (3, 'const'), ('sin', 'unary'), ('X_0', 'var')]

@register_eq_class
class Vladislavleva_4(KnownEquation):
    _eq_name = 'Vladislavleva_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'n2']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = (10)/((5+(sympy.Pow((x[0]-3),2)+sympy.Pow((x[1]-3),2)+sympy.Pow((x[2]-3),2)+sympy.Pow((x[3]-3),2)+sympy.Pow((x[4]-3),2))))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (10, 'const'), ('add', 'binary'), (5, 'const'), ('add', 'binary'), (-3, 'const'), ('X_0', 'var'), (2, 'const'), ('add', 'binary'), (-3, 'const'), ('X_1', 'var'), (2, 'const'), ('add', 'binary'), (-3, 'const'), ('X_2', 'var'), (2, 'const'), ('add', 'binary'), (-3, 'const'), ('X_3', 'var'), (2, 'const'), ('add', 'binary'), (-3, 'const'), ('X_4', 'var'), (2, 'const'), (-1, 'const')]

@register_eq_class
class Vladislavleva_5(KnownEquation):
    _eq_name = 'Vladislavleva_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'n2']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 30*(x[0]-1)*(x[2]-1)/((x[0]-10)*sympy.Pow(x[1],2))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), (-10, 'const'), ('X_0', 'var'), (-1, 'const'), ('X_1', 'var'), (2, 'const'), (-1, 'const'), ('add', 'binary'), (-1, 'const'), ('X_2', 'var'), ('add', 'binary'), (-30, 'const'), ('mul', 'binary'), (30, 'const'), ('X_0', 'var')]

@register_eq_class
class Vladislavleva_6(KnownEquation):
    _eq_name = 'Vladislavleva_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'n2', 'exp', 'expneg']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 6*sympy.sin(x[0])*sympy.cos(x[1])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (6, 'const'), ('cos', 'unary'), ('X_1', 'var'), ('sin', 'unary'), ('X_0', 'var')]

@register_eq_class
class Vladislavleva_7(KnownEquation):
    _eq_name = 'Vladislavleva_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'n2', 'exp', 'expneg', 'sin', 'cos']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (x[0]-3)*(x[1]-3)+2*sympy.sin(x[0]-4)*(x[1]-4)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('add', 'binary'), (-3, 'const'), ('X_0', 'var'), ('add', 'binary'), (-3, 'const'), ('X_1', 'var'), ('mul', 'binary'), (2, 'const'), ('add', 'binary'), (-4, 'const'), ('X_1', 'var'), ('sin', 'unary'), ('add', 'binary'), (-4, 'const'), ('X_0', 'var')]

@register_eq_class
class Vladislavleva_8(KnownEquation):
    _eq_name = 'Vladislavleva_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'n2']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (sympy.Pow((x[0]-3),4)+sympy.Pow((x[1]-3),3)-(x[1]-3))/(sympy.Pow((x[1]-2),4)+10)
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), (10, 'const'), ('add', 'binary'), (-2, 'const'), ('X_1', 'var'), (4, 'const'), (-1, 'const'), ('add', 'binary'), (3, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('add', 'binary'), (-3, 'const'), ('X_0', 'var'), (4, 'const'), ('add', 'binary'), (-3, 'const'), ('X_1', 'var'), (3, 'const')]

@register_eq_class
class Jin_1(KnownEquation):
    _eq_name = 'Jin_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'n2', 'n3', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 2.5*sympy.Pow(x[0],4)-1.3*sympy.Pow(x[0],3)+0.5*sympy.Pow(x[1],2)-1.7*x[1]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (0.500000000000000, 'const'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), (2.50000000000000, 'const'), ('X_0', 'var'), (4, 'const'), ('mul', 'binary'), (-1.30000000000000, 'const'), ('X_0', 'var'), (3, 'const'), ('mul', 'binary'), (-1.70000000000000, 'const'), ('X_1', 'var')]

@register_eq_class
class Jin_2(KnownEquation):
    _eq_name = 'Jin_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'n2', 'n3', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 8.0*sympy.Pow(x[0],2)+8.0*sympy.Pow(x[1],3)-15.0
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-15.0000000000000, 'const'), ('mul', 'binary'), (8.00000000000000, 'const'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (8.00000000000000, 'const'), ('X_1', 'var'), (3, 'const')]

@register_eq_class
class Jin_3(KnownEquation):
    _eq_name = 'Jin_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'n2', 'n3', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.2*sympy.Pow(x[0],3)+0.5*sympy.Pow(x[1],3)-1.2*x[1]-0.5*x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (0.500000000000000, 'const'), ('X_1', 'var'), (3, 'const'), ('mul', 'binary'), (0.200000000000000, 'const'), ('X_0', 'var'), (3, 'const'), ('mul', 'binary'), (-0.500000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-1.20000000000000, 'const'), ('X_1', 'var')]

@register_eq_class
class Jin_4(KnownEquation):
    _eq_name = 'Jin_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'n2', 'n3', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 1.5*sympy.exp(x[0])+5.0*sympy.cos(x[1])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (1.50000000000000, 'const'), ('exp', 'unary'), ('X_0', 'var'), ('mul', 'binary'), (5.00000000000000, 'const'), ('cos', 'unary'), ('X_1', 'var')]

@register_eq_class
class Jin_5(KnownEquation):
    _eq_name = 'Jin_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'n2', 'n3', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 6.0*sympy.sin(x[0])*sympy.cos(x[1])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (6.00000000000000, 'const'), ('cos', 'unary'), ('X_1', 'var'), ('sin', 'unary'), ('X_0', 'var')]

@register_eq_class
class Jin_6(KnownEquation):
    _eq_name = 'Jin_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'n2', 'n3', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 1.35*x[0]*x[1]+5.5*sympy.sin((x[0]-1.0)*(x[1]-1.0))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (5.50000000000000, 'const'), ('sin', 'unary'), ('mul', 'binary'), ('add', 'binary'), (-1.00000000000000, 'const'), ('X_0', 'var'), ('add', 'binary'), (-1.00000000000000, 'const'), ('X_1', 'var'), ('mul', 'binary'), (1.35000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Neat_1(KnownEquation):
    _eq_name = 'Neat_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', '1.0']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],4)+sympy.Pow(x[0],3)+sympy.Pow(x[0],2)+x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const')]

@register_eq_class
class Neat_2(KnownEquation):
    _eq_name = 'Neat_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', '1.0']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],5)+sympy.Pow(x[0],4)+sympy.Pow(x[0],3)+sympy.Pow(x[0],2)+x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (3, 'const'), ('X_0', 'var'), (4, 'const'), ('X_0', 'var'), (5, 'const')]

@register_eq_class
class Neat_3(KnownEquation):
    _eq_name = 'Neat_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', '1.0']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sin(sympy.Pow(x[0],2))*sympy.cos(x[0])-1
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-1, 'const'), ('mul', 'binary'), ('cos', 'unary'), ('X_0', 'var'), ('sin', 'unary'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Neat_4(KnownEquation):
    _eq_name = 'Neat_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', '1.0']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.log(x[0]+1)+sympy.log(sympy.Pow(x[0],2)+1)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('log', 'unary'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), ('log', 'unary'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Neat_5(KnownEquation):
    _eq_name = 'Neat_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 2*sympy.sin(x[0])*sympy.cos(x[1])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (2, 'const'), ('cos', 'unary'), ('X_1', 'var'), ('sin', 'unary'), ('X_0', 'var')]

@register_eq_class
class Neat_6(KnownEquation):
    _eq_name = 'Neat_6'
    _function_set = ['add', 'mul', 'inv', 'neg', 'sqrt', '1.0', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.harmonic(x[0])
        self.sympy_eq_preorder_traversal = [('X_0', 'var')]

@register_eq_class
class Neat_7(KnownEquation):
    _eq_name = 'Neat_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'n2', 'n3', 'sqrt', 'tan', 'tanh', 'const']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 2-2.1*sympy.cos(9.8*x[0])*sympy.sin(1.3*x[1])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (2, 'const'), ('mul', 'binary'), (-2.10000000000000, 'const'), ('cos', 'unary'), ('mul', 'binary'), (9.80000000000000, 'const'), ('X_0', 'var'), ('sin', 'unary'), ('mul', 'binary'), (1.30000000000000, 'const'), ('X_1', 'var')]

@register_eq_class
class Neat_8(KnownEquation):
    _eq_name = 'Neat_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'n2', 'exp', 'expneg']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (sympy.exp(-sympy.Pow(x[0]-1,2)))/((1.2+sympy.Pow((x[1]-2.5),2)))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), (1.20000000000000, 'const'), ('add', 'binary'), (-2.50000000000000, 'const'), ('X_1', 'var'), (2, 'const'), (-1, 'const'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('add', 'binary'), (-1, 'const'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Neat_9(KnownEquation):
    _eq_name = 'Neat_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (1)/((1+sympy.Pow(x[0],-4)))+(1)/((1+sympy.Pow(x[1],-4)))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('add', 'binary'), (1, 'const'), ('X_0', 'var'), (-4, 'const'), (-1, 'const'), ('add', 'binary'), (1, 'const'), ('X_1', 'var'), (-4, 'const'), (-1, 'const')]

@register_eq_class
class GrammarVAE_1(KnownEquation):
    _eq_name = 'GrammarVAE_1'
    _function_set = ['add', 'mul', 'div', 'sin', 'exp', '1.0', '2.0', '3.0']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = 1./3+x[0]+sympy.sin(sympy.Pow(x[0],2))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (0.333333333333333, 'const'), ('X_0', 'var'), ('sin', 'unary'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Const_Test_1(KnownEquation):
    _eq_name = 'Const_Test_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', '3.14159265358979323846', '2.71828182845904523536']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = 3.14159265358979323846*x[0]*x[0]
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (3.14159265358979323846, 'const'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Const_Test_2(KnownEquation):
    _eq_name = 'Const_Test_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'const']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = 3.14159265358979323846*x[0]*x[0]
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (3.14159265358979323846, 'const'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Poly_1(KnownEquation):
    _eq_name = 'Poly_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'sqrt', 'poly']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[1]/sympy.sqrt(sympy.Pow(x[0],2)+sympy.Pow(x[1],2)+sympy.Pow(x[2],2))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('X_0', 'var'), (2, 'const'), ('X_1', 'var'), (2, 'const'), ('X_2', 'var'), (2, 'const')]

@register_eq_class
class Poly_2(KnownEquation):
    _eq_name = 'Poly_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'poly']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.Pow(x[0],3)+sympy.Pow(x[0],2)+x[0]+sympy.sin(x[0])+sympy.sin(sympy.Pow(x[1],2))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('X_0', 'var'), (3, 'const'), ('sin', 'unary'), ('X_0', 'var'), ('sin', 'unary'), ('X_1', 'var'), (2, 'const')]

@register_eq_class
class Poly_3(KnownEquation):
    _eq_name = 'Poly_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'sqrt', 'poly']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.cos(x[1])/(sympy.sqrt(12*x[0]*x[1]+1.3+x[0]-0.05*sympy.Pow(x[1],2))+x[0])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (2, 'const'), (3, 'const'), ('add', 'binary'), (0.108333333333333, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-0.00416666666666667, 'const'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), (-1, 'const'), ('cos', 'unary'), ('X_1', 'var')]

@register_eq_class
class Poly_4(KnownEquation):
    _eq_name = 'Poly_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'sqrt', 'poly']

    def __init__(self):
        super().__init__(num_vars=10)
        x = self.x
        self.sympy_eq = sympy.sin(x[3])/(sympy.sqrt(12*x[0]*x[1]+1.3-0.05*x[2]*x[5]*x[9])*sympy.exp(x[6]))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (3, 'const'), ('add', 'binary'), (0.108333333333333, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('mul', 'binary'), (-0.00416666666666667, 'const'), ('X_2', 'var'), ('X_5', 'var'), ('X_9', 'var'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('X_6', 'var'), ('sin', 'unary'), ('X_3', 'var')]

@register_eq_class
class Poly_5(KnownEquation):
    _eq_name = 'Poly_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'exp', 'log', 'const', 'poly']

    def __init__(self):
        super().__init__(num_vars=1)
        x = self.x
        self.sympy_eq = sympy.sin(sympy.Pow(x[0],3)-x[0]-sympy.pi/6)
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (-1, 'const'), ('sin', 'unary'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), (3, 'const'), ('mul', 'binary')]

@register_eq_class
class Livermore2_Vars2_1(KnownEquation):
    _eq_name = 'Livermore2_Vars2_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.sqrt(x[0]+x[1])*(2.97*x[1]**2+2.8*x[1])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('add', 'binary'), ('mul', 'binary'), (2.80000000000000, 'const'), ('X_1', 'var'), ('mul', 'binary'), (2.97000000000000, 'const'), ('X_1', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars2_2(KnownEquation):
    _eq_name = 'Livermore2_Vars2_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = x[0]*x[1]*(x[0]*sympy.sqrt(x[1]*(6.28*x[0]*x[1]+x[0]+7.41*x[1]**3-1.4))+x[0])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), (-1.40000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (7.41000000000000, 'const'), ('X_1', 'var'), (3, 'const'), ('mul', 'binary'), (6.28000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars2_3(KnownEquation):
    _eq_name = 'Livermore2_Vars2_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -2.72*x[0]**2*(x[0]**2*x[1]+x[0]+sympy.sqrt(x[0]**4+0.3))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (-2.72000000000000, 'const'), ('X_0', 'var'), (2, 'const'), ('add', 'binary'), ('X_0', 'var'), ('add', 'binary'), (0.300000000000000, 'const'), ('X_0', 'var'), (4, 'const'), ('mul', 'binary'), ('X_1', 'var'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars2_4(KnownEquation):
    _eq_name = 'Livermore2_Vars2_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 0.29*x[0]+0.29*x[1]+(x[0]-x[1])**2
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), (0.290000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (0.290000000000000, 'const'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars2_5(KnownEquation):
    _eq_name = 'Livermore2_Vars2_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = x[0]*(x[0]+sympy.sin(x[1])-(7.88*x[0]*x[1]**2+x[0]+10.59*x[1]**3)/x[0])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), (-1, 'const'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (10.5900000000000, 'const'), ('X_1', 'var'), (3, 'const'), ('mul', 'binary'), (7.88000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var'), (2, 'const'), ('sin', 'unary'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars2_6(KnownEquation):
    _eq_name = 'Livermore2_Vars2_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 2.01*x[0]/(14.71-4.97*x[1])-x[1]*(-x[0]**2+x[0]-x[1])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (2.01000000000000, 'const'), ('X_0', 'var'), ('add', 'binary'), (14.7100000000000, 'const'), ('mul', 'binary'), (-4.97000000000000, 'const'), ('X_1', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars2_7(KnownEquation):
    _eq_name = 'Livermore2_Vars2_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 1.65*sympy.sqrt(x[0])+2.65*x[0]-1.65*sympy.sqrt(-x[0]+x[1])+1-2.11*x[1]/x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (1, 'const'), ('mul', 'binary'), (1.65000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (2.65000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-1.65000000000000, 'const'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-2.11000000000000, 'const'), ('X_1', 'var'), ('X_0', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars2_8(KnownEquation):
    _eq_name = 'Livermore2_Vars2_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -4.22*x[0]**2+2.08*x[1]**3-2.76*x[1]**2+(sympy.sqrt(x[0])-x[0])*sympy.log(x[1])/sympy.log(x[0])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (2.08000000000000, 'const'), ('X_1', 'var'), (3, 'const'), ('mul', 'binary'), (-2.76000000000000, 'const'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), (-4.22000000000000, 'const'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), ('log', 'unary'), ('X_0', 'var'), (-1, 'const'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('log', 'unary'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars2_9(KnownEquation):
    _eq_name = 'Livermore2_Vars2_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = x[0]**2+x[0]-x[1]-2.18*sympy.sqrt(0.42*x[0]-0.21*x[1]+1)-2.14
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-2.14000000000000, 'const'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-2.18000000000000, 'const'), ('add', 'binary'), (1, 'const'), ('mul', 'binary'), (0.420000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-0.210000000000000, 'const'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars2_10(KnownEquation):
    _eq_name = 'Livermore2_Vars2_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -1.92*x[0]*x[1]*sympy.exp(2*x[1])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (-1.92000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var'), ('exp', 'unary'), ('mul', 'binary'), (2, 'const'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars2_11(KnownEquation):
    _eq_name = 'Livermore2_Vars2_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = x[0]*x[1]+sympy.sqrt(x[1])+3.52*sympy.sin(x[0])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (3.52000000000000, 'const'), ('sin', 'unary'), ('X_0', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars2_12(KnownEquation):
    _eq_name = 'Livermore2_Vars2_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.sqrt((x[0]+x[1]*sympy.exp(-x[1]))*sympy.log(6.27*x[0]**3+4.32*x[0]**2*x[1]-7.87*x[1]**3))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('log', 'unary'), ('add', 'binary'), ('mul', 'binary'), (6.27000000000000, 'const'), ('X_0', 'var'), (3, 'const'), ('mul', 'binary'), (-7.87000000000000, 'const'), ('X_1', 'var'), (3, 'const'), ('mul', 'binary'), (4.32000000000000, 'const'), ('X_1', 'var'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars2_13(KnownEquation):
    _eq_name = 'Livermore2_Vars2_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (x[0]+x[1]*(-1.49*x[0]*x[1]**2+6.81*x[0])+x[1])*sympy.cos(sympy.sqrt(x[0])+2*x[0]-x[1])/x[0]**2
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), (-2, 'const'), ('add', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('mul', 'binary'), (6.81000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-1.49000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var'), (2, 'const'), ('cos', 'unary'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars2_14(KnownEquation):
    _eq_name = 'Livermore2_Vars2_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = x[0]**4/x[1]**4-0.91
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-0.910000000000000, 'const'), ('mul', 'binary'), ('X_0', 'var'), (4, 'const'), ('X_1', 'var'), (-4, 'const')]

@register_eq_class
class Livermore2_Vars2_15(KnownEquation):
    _eq_name = 'Livermore2_Vars2_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 11.57*x[0]**3+x[1]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (11.5700000000000, 'const'), ('X_0', 'var'), (3, 'const')]

@register_eq_class
class Livermore2_Vars2_16(KnownEquation):
    _eq_name = 'Livermore2_Vars2_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 2.0*x[0]/(14.71-4.97*x[1])-x[1]*(-x[0]**2+x[0]-x[1])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (2.00000000000000, 'const'), ('X_0', 'var'), ('add', 'binary'), (14.7100000000000, 'const'), ('mul', 'binary'), (-4.97000000000000, 'const'), ('X_1', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars2_17(KnownEquation):
    _eq_name = 'Livermore2_Vars2_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = -sympy.sqrt(x[0])*x[1]+x[0]-sympy.sin(sympy.log(-5.2*x[0]**3+9.32*x[0]+6.94*x[1]**2))**2
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('sin', 'unary'), ('log', 'unary'), ('add', 'binary'), ('mul', 'binary'), (9.32000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (6.94000000000000, 'const'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), (-5.20000000000000, 'const'), ('X_0', 'var'), (3, 'const'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars2_18(KnownEquation):
    _eq_name = 'Livermore2_Vars2_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (20.08*x[0]*x[1]**2+x[0])/(x[0]*(sympy.sqrt(x[1])+x[1]))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), (-1, 'const'), ('add', 'binary'), ('X_1', 'var'), ('X_1', 'var'), (-1, 'const'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (20.0800000000000, 'const'), ('X_0', 'var'), ('X_1', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars2_19(KnownEquation):
    _eq_name = 'Livermore2_Vars2_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (x[0]-0.48*sympy.cos(x[0])/sympy.sqrt(0.23*x[0]*(x[1]**2+sympy.log(x[1]))+0.23*x[0]+1))*(x[0]+sympy.sin(1))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-0.480000000000000, 'const'), ('add', 'binary'), (1, 'const'), ('mul', 'binary'), (0.230000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (0.230000000000000, 'const'), ('X_0', 'var'), ('add', 'binary'), ('X_1', 'var'), (2, 'const'), ('log', 'unary'), ('X_1', 'var'), ('cos', 'unary'), ('X_0', 'var'), ('add', 'binary'), ('X_0', 'var'), ('sin', 'unary'), (1, 'const')]

@register_eq_class
class Livermore2_Vars2_20(KnownEquation):
    _eq_name = 'Livermore2_Vars2_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = (x[0]**2+x[1])**2*(-x[0]/(-8.62*x[0]**2-5.38*x[0]*x[1])+x[1])**4*sympy.sin(sympy.sqrt(x[0]))**4/x[0]**4
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), (-4, 'const'), ('add', 'binary'), ('X_1', 'var'), ('X_0', 'var'), (2, 'const'), (2, 'const'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('add', 'binary'), ('mul', 'binary'), (-8.62000000000000, 'const'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (-5.38000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var'), (-1, 'const'), (4, 'const'), ('sin', 'unary'), ('X_0', 'var'), (4, 'const')]

@register_eq_class
class Livermore2_Vars2_21(KnownEquation):
    _eq_name = 'Livermore2_Vars2_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = x[0]+sympy.log(x[0]+0.75/(x[0]+x[1]+0.41))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('log', 'unary'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (0.750000000000000, 'const'), ('add', 'binary'), (0.410000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars2_22(KnownEquation):
    _eq_name = 'Livermore2_Vars2_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = sympy.log(x[0]*sympy.exp(x[1])/sympy.sqrt(sympy.cos(1.88*x[1]))-4.09*(0.49*x[0]-1)**2)/sympy.sqrt(x[0])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('log', 'unary'), ('add', 'binary'), ('mul', 'binary'), (-4.09000000000000, 'const'), ('add', 'binary'), (-1, 'const'), ('mul', 'binary'), (0.490000000000000, 'const'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('cos', 'unary'), ('mul', 'binary'), (1.88000000000000, 'const'), ('X_1', 'var'), ('exp', 'unary'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars2_23(KnownEquation):
    _eq_name = 'Livermore2_Vars2_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = x[0]**2+1.37*sympy.sqrt(1-0.53*(-x[1]-2.63)*(sympy.log(x[1])-1.16)/x[0])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (1.37000000000000, 'const'), ('add', 'binary'), (1, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), (-1, 'const'), ('add', 'binary'), (-1.39390000000000, 'const'), ('mul', 'binary'), (-0.530000000000000, 'const'), ('X_1', 'var'), ('add', 'binary'), (-1.16000000000000, 'const'), ('log', 'unary'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars2_24(KnownEquation):
    _eq_name = 'Livermore2_Vars2_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = 3.04*x[0]+3.04*(x[0]-x[1]**2)**2-10.82
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-10.8200000000000, 'const'), ('mul', 'binary'), (3.04000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (3.04000000000000, 'const'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), (2, 'const'), (2, 'const')]

@register_eq_class
class Livermore2_Vars2_25(KnownEquation):
    _eq_name = 'Livermore2_Vars2_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=2)
        x = self.x
        self.sympy_eq = x[0]+x[0]/(9.25*x[0]**2*x[1]+x[0]+x[1]/x[0])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('X_0', 'var'), (-1, 'const'), ('mul', 'binary'), (9.25000000000000, 'const'), ('X_1', 'var'), ('X_0', 'var'), (2, 'const'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars3_1(KnownEquation):
    _eq_name = 'Livermore2_Vars3_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[2]*(-x[1]+x[2]+(-x[0]**2+4.45*x[1]**2+x[2]-sympy.exp(2*sympy.exp(-sympy.sin(x[0]-x[2]))))*sympy.exp(x[0]))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_2', 'var'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('exp', 'unary'), ('mul', 'binary'), (2, 'const'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('sin', 'unary'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('mul', 'binary'), (4.45000000000000, 'const'), ('X_1', 'var'), (2, 'const'), ('exp', 'unary'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars3_2(KnownEquation):
    _eq_name = 'Livermore2_Vars3_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 9.28*(0.91-x[2])**2*(-0.5*x[0]-x[1])**2/(0.34*x[1]**2+1)**2
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (9.28000000000000, 'const'), ('add', 'binary'), (1, 'const'), ('mul', 'binary'), (0.340000000000000, 'const'), ('X_1', 'var'), (2, 'const'), (-2, 'const'), ('add', 'binary'), (0.910000000000000, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), (2, 'const'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-0.500000000000000, 'const'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars3_3(KnownEquation):
    _eq_name = 'Livermore2_Vars3_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -x[0]*(sympy.sqrt(x[0])/(x[1]*(3.51*x[1]**3+1.15*x[1]*x[2]))-x[2]**2)-x[0]-x[2]+sympy.exp(x[0])-sympy.log(x[0])+sympy.log(sympy.sqrt(x[2]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('log', 'unary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), (2, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), (3.51000000000000, 'const'), ('X_1', 'var'), (3, 'const'), ('mul', 'binary'), (1.15000000000000, 'const'), ('X_1', 'var'), ('X_2', 'var'), (-1, 'const'), ('exp', 'unary'), ('X_0', 'var'), ('log', 'unary'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars3_4(KnownEquation):
    _eq_name = 'Livermore2_Vars3_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[0]+0.31*x[1]*x[2]+x[1]+x[2]+sympy.sqrt(sympy.cos(x[1]))-3.19
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-3.19000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var'), ('X_2', 'var'), ('cos', 'unary'), ('X_1', 'var'), ('mul', 'binary'), (0.310000000000000, 'const'), ('X_1', 'var'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars3_5(KnownEquation):
    _eq_name = 'Livermore2_Vars3_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -2.24*x[0]**3*x[2]+x[2]**4*(-x[1]+x[1]/x[0])**4
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('X_2', 'var'), (4, 'const'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('X_0', 'var'), (-1, 'const'), (4, 'const'), ('mul', 'binary'), (-2.24000000000000, 'const'), ('X_2', 'var'), ('X_0', 'var'), (3, 'const')]

@register_eq_class
class Livermore2_Vars3_6(KnownEquation):
    _eq_name = 'Livermore2_Vars3_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[0]*(x[0]+(x[1]-1.23)*(x[0]-x[1]-x[2]))*sympy.sin(sympy.exp(x[1]))**2/x[2]
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('X_2', 'var'), (-1, 'const'), ('sin', 'unary'), ('exp', 'unary'), ('X_1', 'var'), (2, 'const'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('add', 'binary'), (-1.23000000000000, 'const'), ('X_1', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars3_7(KnownEquation):
    _eq_name = 'Livermore2_Vars3_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[0]*(x[1]+x[2]*(x[0]+x[2]))+x[2]*sympy.cos(0.89*x[0]**2)+x[2]+2.08
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (2.08000000000000, 'const'), ('X_2', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('add', 'binary'), ('X_0', 'var'), ('X_2', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('cos', 'unary'), ('mul', 'binary'), (0.890000000000000, 'const'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars3_8(KnownEquation):
    _eq_name = 'Livermore2_Vars3_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[0]/((-x[1]+x[2]+sympy.sqrt(sympy.log(x[2])/(x[0]**2+sympy.sqrt(x[2]))))*(1.21*x[0]**2*x[2]+0.44*x[0]**2+4.95*x[2]**2+sympy.exp(x[1])*sympy.exp(x[1]**4)))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), ('add', 'binary'), ('X_0', 'var'), (2, 'const'), ('X_2', 'var'), (-1, 'const'), ('log', 'unary'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), (4.95000000000000, 'const'), ('X_2', 'var'), (2, 'const'), ('mul', 'binary'), (0.440000000000000, 'const'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), ('exp', 'unary'), ('X_1', 'var'), ('exp', 'unary'), ('X_1', 'var'), (4, 'const'), ('mul', 'binary'), (1.21000000000000, 'const'), ('X_2', 'var'), ('X_0', 'var'), (2, 'const'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars3_9(KnownEquation):
    _eq_name = 'Livermore2_Vars3_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[0]*sympy.sin(0.61*x[0]/sympy.sqrt(0.36*x[0]**2-x[0]*sympy.sqrt(-0.45*x[0]*x[2]**2+x[1])*(x[0]+x[1]**2-1)**4/x[2]))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('sin', 'unary'), ('mul', 'binary'), (0.610000000000000, 'const'), ('X_0', 'var'), ('add', 'binary'), ('mul', 'binary'), (0.360000000000000, 'const'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('X_2', 'var'), (-1, 'const'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-0.450000000000000, 'const'), ('X_0', 'var'), ('X_2', 'var'), (2, 'const'), ('add', 'binary'), (-1, 'const'), ('X_0', 'var'), ('X_1', 'var'), (2, 'const'), (4, 'const')]

@register_eq_class
class Livermore2_Vars3_10(KnownEquation):
    _eq_name = 'Livermore2_Vars3_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -2.85*(x[0]-1.43)*(x[0]+x[1])*(x[0]-x[2])/x[0]
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), (-1, 'const'), ('add', 'binary'), (4.07550000000000, 'const'), ('mul', 'binary'), (-2.85000000000000, 'const'), ('X_0', 'var'), ('add', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars3_11(KnownEquation):
    _eq_name = 'Livermore2_Vars3_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 4.83*x[0]+x[0]/x[1]-3.83*x[1]-3.83*x[2]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (4.83000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-3.83000000000000, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-3.83000000000000, 'const'), ('X_2', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars3_12(KnownEquation):
    _eq_name = 'Livermore2_Vars3_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -1.35*x[0]*x[1]**2+x[1]+x[2]+3.18
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (3.18000000000000, 'const'), ('X_1', 'var'), ('X_2', 'var'), ('mul', 'binary'), (-1.35000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars3_13(KnownEquation):
    _eq_name = 'Livermore2_Vars3_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 0.96*sympy.sqrt(1/(x[0]**2*x[1]*(sympy.sqrt(x[0]*(x[2]+sympy.exp(-x[1]+x[2])))-3.54)))*(x[0]+x[1])/sympy.sin(x[0])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (0.960000000000000, 'const'), ('mul', 'binary'), ('X_0', 'var'), (-2, 'const'), ('X_1', 'var'), (-1, 'const'), ('add', 'binary'), (-3.54000000000000, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_2', 'var'), ('exp', 'unary'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), (-1, 'const'), ('sin', 'unary'), ('X_0', 'var'), (-1, 'const'), ('add', 'binary'), ('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars3_14(KnownEquation):
    _eq_name = 'Livermore2_Vars3_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[1]*(sympy.sqrt(x[0])+x[0]*x[1])*(x[1]-x[2]+sympy.exp((x[0]-x[1])/x[0]))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('exp', 'unary'), ('mul', 'binary'), ('X_0', 'var'), (-1, 'const'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars3_15(KnownEquation):
    _eq_name = 'Livermore2_Vars3_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = sympy.log(x[0]*(x[1]+x[2])/x[1]**2-4.68*x[1]**2*x[2])
        self.sympy_eq_preorder_traversal = [('log', 'unary'), ('add', 'binary'), ('mul', 'binary'), (-4.68000000000000, 'const'), ('X_2', 'var'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), (-2, 'const'), ('add', 'binary'), ('X_1', 'var'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars3_16(KnownEquation):
    _eq_name = 'Livermore2_Vars3_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = sympy.sqrt(x[0])+sympy.exp(x[0]*x[2]*(x[0]+x[1])*(11.13*x[0]*x[2]**2+2*x[0]+x[2])*sympy.cos(x[0]**2))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('exp', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('X_2', 'var'), ('add', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var'), ('mul', 'binary'), (11.1300000000000, 'const'), ('X_0', 'var'), ('X_2', 'var'), (2, 'const'), ('cos', 'unary'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars3_17(KnownEquation):
    _eq_name = 'Livermore2_Vars3_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[0]*sympy.sqrt(x[1])*sympy.cos(x[0])-3.406*x[0]+3.41*x[1]+x[2]+1
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (1, 'const'), ('X_2', 'var'), ('mul', 'binary'), (3.41000000000000, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-3.40600000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('cos', 'unary'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars3_18(KnownEquation):
    _eq_name = 'Livermore2_Vars3_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[0]+x[1]*x[2]-3.03*sympy.sqrt(x[2])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-3.03000000000000, 'const'), ('X_2', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars3_19(KnownEquation):
    _eq_name = 'Livermore2_Vars3_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = 7.14*x[0]*x[1]**2+x[1]**2*x[2]+x[2]*sympy.sqrt(x[0]*(x[0]-x[1]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('X_2', 'var'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), ('X_2', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (7.14000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars3_20(KnownEquation):
    _eq_name = 'Livermore2_Vars3_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[0]+0.71*sympy.sqrt(sympy.sqrt(x[1])/sympy.sqrt(x[2]))-4.21
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-4.21000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (0.710000000000000, 'const'), ('mul', 'binary'), ('X_1', 'var'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars3_21(KnownEquation):
    _eq_name = 'Livermore2_Vars3_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -x[0]**2*x[2]+1.99*x[0]*sympy.sqrt(0.25*(-x[1]-x[2]-1.0))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (0.995000000000000, 'const'), ('X_0', 'var'), ('add', 'binary'), (-1, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars3_22(KnownEquation):
    _eq_name = 'Livermore2_Vars3_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[2]+sympy.sin(x[0]*x[1]-x[1]-x[2]+2.39)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_2', 'var'), ('sin', 'unary'), ('add', 'binary'), (2.39000000000000, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars3_23(KnownEquation):
    _eq_name = 'Livermore2_Vars3_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[0]**2*x[1]/(x[0]+x[2])**(1/4)
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_1', 'var'), ('X_0', 'var'), (2, 'const'), ('add', 'binary'), ('X_0', 'var'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars3_24(KnownEquation):
    _eq_name = 'Livermore2_Vars3_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = -1.35*x[0]*x[1]**2+x[1]+x[2]+3.18
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (3.18000000000000, 'const'), ('X_1', 'var'), ('X_2', 'var'), ('mul', 'binary'), (-1.35000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars3_25(KnownEquation):
    _eq_name = 'Livermore2_Vars3_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=3)
        x = self.x
        self.sympy_eq = x[0]*sympy.sqrt(x[1])*sympy.cos(x[0])-3.41*(x[0]-x[1])+x[2]+1
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (1, 'const'), ('X_2', 'var'), ('mul', 'binary'), (3.41000000000000, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-3.41000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('cos', 'unary'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars4_1(KnownEquation):
    _eq_name = 'Livermore2_Vars4_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]-x[1]*x[2]-x[1]-x[3]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars4_2(KnownEquation):
    _eq_name = 'Livermore2_Vars4_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]*sympy.sqrt(x[1])*x[3]/x[2]
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('X_3', 'var'), ('X_1', 'var'), ('X_2', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars4_3(KnownEquation):
    _eq_name = 'Livermore2_Vars4_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 2*x[0]+x[3]-0.01+x[2]/x[1]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-0.0100000000000000, 'const'), ('X_3', 'var'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('X_1', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars4_4(KnownEquation):
    _eq_name = 'Livermore2_Vars4_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]-x[3]-(-x[0]+sympy.sin(x[0]))**4/(x[0]**8*x[1]**2*x[2]**2)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), (-8, 'const'), ('X_1', 'var'), (-2, 'const'), ('X_2', 'var'), (-2, 'const'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('sin', 'unary'), ('X_0', 'var'), (4, 'const')]

@register_eq_class
class Livermore2_Vars4_5(KnownEquation):
    _eq_name = 'Livermore2_Vars4_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]+sympy.sin(x[1]/(x[0]*x[1]**2*x[3]**2*(-3.22*x[1]*x[3]**2+13.91*x[1]*x[3]+x[2])/2+x[1]))**2
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('sin', 'unary'), ('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), (2, 'const'), ('X_3', 'var'), (2, 'const'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), (13.9100000000000, 'const'), ('X_1', 'var'), ('X_3', 'var'), ('mul', 'binary'), (-3.22000000000000, 'const'), ('X_1', 'var'), ('X_3', 'var'), (2, 'const'), (-1, 'const'), (2, 'const')]

@register_eq_class
class Livermore2_Vars4_6(KnownEquation):
    _eq_name = 'Livermore2_Vars4_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = (-x[0]-0.54*sympy.exp(x[0]*sympy.sqrt(x[3]+sympy.cos(x[1]))*sympy.exp(-2*x[0])))/x[2]
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_2', 'var'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-0.540000000000000, 'const'), ('exp', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_3', 'var'), ('cos', 'unary'), ('X_1', 'var'), ('exp', 'unary'), ('mul', 'binary'), (-2, 'const'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars4_7(KnownEquation):
    _eq_name = 'Livermore2_Vars4_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]+sympy.cos(x[1]/sympy.log(x[1]**2*x[2]+x[3]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('cos', 'unary'), ('mul', 'binary'), ('X_1', 'var'), ('log', 'unary'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('X_1', 'var'), (2, 'const'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars4_8(KnownEquation):
    _eq_name = 'Livermore2_Vars4_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]*(x[0]+x[3]+sympy.sin((-x[0]*sympy.exp(sympy.exp(x[2]))+x[1])/(-4.47*x[0]**2*x[2]+8.31*x[2]**3+5.27*x[2]**2)))-x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_0', 'var'), ('X_3', 'var'), ('sin', 'unary'), ('mul', 'binary'), ('add', 'binary'), ('mul', 'binary'), (5.27000000000000, 'const'), ('X_2', 'var'), (2, 'const'), ('mul', 'binary'), (8.31000000000000, 'const'), ('X_2', 'var'), (3, 'const'), ('mul', 'binary'), (-4.47000000000000, 'const'), ('X_2', 'var'), ('X_0', 'var'), (2, 'const'), (-1, 'const'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('exp', 'unary'), ('exp', 'unary'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars4_9(KnownEquation):
    _eq_name = 'Livermore2_Vars4_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]-x[3]+sympy.cos(x[0]*(x[0]+x[1])*(x[0]**2*x[1]+x[2])+x[2])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('cos', 'unary'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars4_10(KnownEquation):
    _eq_name = 'Livermore2_Vars4_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]+(x[0]*(x[3]+(sympy.sqrt(x[1])-sympy.sin(x[2]))/x[2]))**(1/4)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), ('X_2', 'var'), (-1, 'const'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('sin', 'unary'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars4_11(KnownEquation):
    _eq_name = 'Livermore2_Vars4_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 2*x[0]+x[1]*(x[0]+sympy.sin(x[1]*x[2]))+sympy.sin(2/x[3])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('X_0', 'var'), ('sin', 'unary'), ('mul', 'binary'), ('X_1', 'var'), ('X_2', 'var'), ('sin', 'unary'), ('mul', 'binary'), (2, 'const'), ('X_3', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars4_12(KnownEquation):
    _eq_name = 'Livermore2_Vars4_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]*x[1]+16.97*x[2]-x[3]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), (16.9700000000000, 'const'), ('X_2', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars4_13(KnownEquation):
    _eq_name = 'Livermore2_Vars4_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[3]*(-x[2]-sympy.sin(x[0]**2-x[0]+x[1]))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_3', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('sin', 'unary'), ('add', 'binary'), ('X_1', 'var'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars4_14(KnownEquation):
    _eq_name = 'Livermore2_Vars4_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]+sympy.cos(x[1]**2*(-x[1]+x[2]+3.23)+x[3])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('cos', 'unary'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), ('X_1', 'var'), (2, 'const'), ('add', 'binary'), (3.23000000000000, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars4_15(KnownEquation):
    _eq_name = 'Livermore2_Vars4_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]*(x[1]+sympy.log(x[2]+x[3]+sympy.exp(x[1]**2)-0.28/x[0]))-x[2]-x[3]/(2*x[0]*x[2])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_1', 'var'), ('log', 'unary'), ('add', 'binary'), ('X_2', 'var'), ('X_3', 'var'), ('mul', 'binary'), (-0.280000000000000, 'const'), ('X_0', 'var'), (-1, 'const'), ('exp', 'unary'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), ('X_3', 'var'), ('X_0', 'var'), (-1, 'const'), ('X_2', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars4_16(KnownEquation):
    _eq_name = 'Livermore2_Vars4_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[2]*(-x[3]+1.81/x[2])+sympy.sqrt(x[1]*(-x[0]**2*sympy.exp(x[1])-x[1]))-2.34*x[3]/x[0]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), (2, 'const'), ('exp', 'unary'), ('X_1', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), (1.81000000000000, 'const'), ('X_2', 'var'), (-1, 'const'), ('mul', 'binary'), (-2.34000000000000, 'const'), ('X_3', 'var'), ('X_0', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars4_17(KnownEquation):
    _eq_name = 'Livermore2_Vars4_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]**2-x[1]-x[2]**2-x[3]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars4_18(KnownEquation):
    _eq_name = 'Livermore2_Vars4_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]+sympy.sin(2*x[1]+x[2]-x[3]*sympy.exp(x[0])+2.96*sympy.sqrt(-0.36*x[1]**3+x[1]*x[2]**2+0.94)+sympy.log((-x[0]+x[1])*sympy.log(x[1])))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('sin', 'unary'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), (2, 'const'), ('X_1', 'var'), ('mul', 'binary'), (2.96000000000000, 'const'), ('add', 'binary'), (0.940000000000000, 'const'), ('mul', 'binary'), (-0.360000000000000, 'const'), ('X_1', 'var'), (3, 'const'), ('mul', 'binary'), ('X_1', 'var'), ('X_2', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('exp', 'unary'), ('X_0', 'var'), ('log', 'unary'), ('mul', 'binary'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('log', 'unary'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars4_19(KnownEquation):
    _eq_name = 'Livermore2_Vars4_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = (x[0]**3*x[1]-2.86*x[0]+x[3])/x[2]
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_2', 'var'), (-1, 'const'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), (-2.86000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('X_0', 'var'), (3, 'const')]

@register_eq_class
class Livermore2_Vars4_20(KnownEquation):
    _eq_name = 'Livermore2_Vars4_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]+x[1]+6.21+1/(x[2]*x[3]+x[2]+2.08)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (6.21000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var'), ('add', 'binary'), (2.08000000000000, 'const'), ('X_2', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('X_3', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars4_21(KnownEquation):
    _eq_name = 'Livermore2_Vars4_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]*(x[1]-x[2]+x[3])+x[3]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_1', 'var'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars4_22(KnownEquation):
    _eq_name = 'Livermore2_Vars4_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = x[0]-x[1]*x[2]+x[1]*sympy.exp(x[0])-x[3]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('exp', 'unary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars4_23(KnownEquation):
    _eq_name = 'Livermore2_Vars4_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -x[0]/x[1]-2.23*x[1]*x[2]+x[1]-2.23*x[2]/sympy.sqrt(x[3])-2.23*sympy.sqrt(x[3])+sympy.log(x[0])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-2.23000000000000, 'const'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('X_1', 'var'), (-1, 'const'), ('mul', 'binary'), (-2.23000000000000, 'const'), ('X_1', 'var'), ('X_2', 'var'), ('mul', 'binary'), (-2.23000000000000, 'const'), ('X_2', 'var'), ('X_3', 'var'), ('log', 'unary'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars4_24(KnownEquation):
    _eq_name = 'Livermore2_Vars4_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = -4.81*sympy.log(sympy.sqrt(x[0]*sympy.sqrt(sympy.log(x[0]*(x[0]*x[1]+x[0]+x[3]+sympy.log(x[2]))))))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), (-4.81000000000000, 'const'), ('log', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('log', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_0', 'var'), ('X_3', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('log', 'unary'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars4_25(KnownEquation):
    _eq_name = 'Livermore2_Vars4_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=4)
        x = self.x
        self.sympy_eq = 0.38+(-x[0]/x[3]+sympy.cos(2*x[0]*x[2]/(x[3]*(x[0]+x[1]*x[2])))/x[3])/x[1]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (0.380000000000000, 'const'), ('mul', 'binary'), ('X_1', 'var'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), ('X_3', 'var'), (-1, 'const'), ('cos', 'unary'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var'), ('X_2', 'var'), ('X_3', 'var'), (-1, 'const'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('X_2', 'var'), (-1, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('X_3', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars5_1(KnownEquation):
    _eq_name = 'Livermore2_Vars5_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -x[0]+x[1]-x[2]+x[3]-x[4]-4.75
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-4.75000000000000, 'const'), ('X_1', 'var'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var')]

@register_eq_class
class Livermore2_Vars5_2(KnownEquation):
    _eq_name = 'Livermore2_Vars5_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = x[2]*(x[0]+x[4]+0.27/(x[2]**2+(x[1]+x[3])/(x[0]*x[1]+x[1])))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_2', 'var'), ('add', 'binary'), ('X_0', 'var'), ('X_4', 'var'), ('mul', 'binary'), (0.270000000000000, 'const'), ('add', 'binary'), ('X_2', 'var'), (2, 'const'), ('mul', 'binary'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), (-1, 'const'), ('add', 'binary'), ('X_1', 'var'), ('X_3', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars5_3(KnownEquation):
    _eq_name = 'Livermore2_Vars5_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 2*x[0]*x[1]*x[2]+x[4]-sympy.sin(x[0]*sympy.log(x[1])-x[0]+x[3])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_4', 'var'), ('mul', 'binary'), (-1, 'const'), ('sin', 'unary'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('log', 'unary'), ('X_1', 'var'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var'), ('X_1', 'var'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars5_4(KnownEquation):
    _eq_name = 'Livermore2_Vars5_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = x[1]+x[2]*x[3]+x[4]**2+sympy.sin(x[0])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_1', 'var'), ('X_4', 'var'), (2, 'const'), ('mul', 'binary'), ('X_2', 'var'), ('X_3', 'var'), ('sin', 'unary'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars5_5(KnownEquation):
    _eq_name = 'Livermore2_Vars5_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = x[4]+0.36*sympy.sqrt(sympy.log(x[0]*x[1]+x[2]+sympy.log(x[1]+x[3])))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_4', 'var'), ('mul', 'binary'), (0.360000000000000, 'const'), ('log', 'unary'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('log', 'unary'), ('add', 'binary'), ('X_1', 'var'), ('X_3', 'var')]

@register_eq_class
class Livermore2_Vars5_6(KnownEquation):
    _eq_name = 'Livermore2_Vars5_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = x[0]*x[3]+x[0]+x[1]+x[4]+sympy.sqrt(0.08*x[0]/(x[2]*x[4])+x[2])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('X_4', 'var'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), (0.0800000000000000, 'const'), ('X_0', 'var'), ('X_2', 'var'), (-1, 'const'), ('X_4', 'var'), (-1, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('X_3', 'var')]

@register_eq_class
class Livermore2_Vars5_7(KnownEquation):
    _eq_name = 'Livermore2_Vars5_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = x[0]*x[4]+sympy.sqrt(x[0]*x[1]*sympy.cos(x[0])-x[0]/(x[1]+x[2]+x[3]+8.05))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('add', 'binary'), (8.05000000000000, 'const'), ('X_1', 'var'), ('X_2', 'var'), ('X_3', 'var'), (-1, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('cos', 'unary'), ('X_0', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_4', 'var')]

@register_eq_class
class Livermore2_Vars5_8(KnownEquation):
    _eq_name = 'Livermore2_Vars5_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = sympy.sqrt(x[1])*x[2]-x[3]-0.07*(x[0]+(x[0]-x[1])*sympy.sqrt(x[1]-0.99))*sympy.cos(x[4])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), (0.0700000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (0.0700000000000000, 'const'), ('add', 'binary'), (-0.990000000000000, 'const'), ('X_1', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('cos', 'unary'), ('X_4', 'var')]

@register_eq_class
class Livermore2_Vars5_9(KnownEquation):
    _eq_name = 'Livermore2_Vars5_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = x[0]*(x[2]+(x[0]+x[1])/(x[1]*x[3]+x[4]))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), ('add', 'binary'), ('X_4', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('X_3', 'var'), (-1, 'const'), ('add', 'binary'), ('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars5_10(KnownEquation):
    _eq_name = 'Livermore2_Vars5_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = x[0]/(x[3]*(-0.25*x[0]*x[2]*x[3]+x[1]-8.43*x[3]*x[4])*sympy.sin(x[2]+sympy.log(x[1])))+x[3]*x[4]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('X_3', 'var'), ('X_4', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_3', 'var'), (-1, 'const'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-8.43000000000000, 'const'), ('X_3', 'var'), ('X_4', 'var'), ('mul', 'binary'), (-0.250000000000000, 'const'), ('X_0', 'var'), ('X_2', 'var'), ('X_3', 'var'), (-1, 'const'), ('sin', 'unary'), ('add', 'binary'), ('X_2', 'var'), ('log', 'unary'), ('X_1', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars5_11(KnownEquation):
    _eq_name = 'Livermore2_Vars5_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -x[3]**2+sympy.sqrt((x[0]*(x[2]+x[4])-x[1]+x[4])/x[2])+0.47*sympy.sqrt(x[2]*(x[0]-sympy.sqrt(x[1])+x[1])/x[1])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('X_2', 'var'), (-1, 'const'), ('add', 'binary'), ('X_4', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_2', 'var'), ('X_4', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), (2, 'const'), ('mul', 'binary'), (0.470000000000000, 'const'), ('mul', 'binary'), ('X_2', 'var'), ('X_1', 'var'), (-1, 'const'), ('add', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars5_12(KnownEquation):
    _eq_name = 'Livermore2_Vars5_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = x[0]*(x[1]-1/(x[2]*(x[3]+x[4])))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), (-1, 'const'), ('add', 'binary'), ('X_3', 'var'), ('X_4', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars5_13(KnownEquation):
    _eq_name = 'Livermore2_Vars5_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = sympy.sqrt(x[0]*(x[4]*(x[1]-1.52)-sympy.cos(4.03*x[2]+x[3])))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('cos', 'unary'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), (4.03000000000000, 'const'), ('X_2', 'var'), ('mul', 'binary'), ('X_4', 'var'), ('add', 'binary'), (-1.52000000000000, 'const'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars5_14(KnownEquation):
    _eq_name = 'Livermore2_Vars5_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -x[0]/(x[1]*x[4])+sympy.cos(x[0]*x[2]*x[3]*sympy.exp(-x[1]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('X_1', 'var'), (-1, 'const'), ('X_4', 'var'), (-1, 'const'), ('cos', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('X_2', 'var'), ('X_3', 'var'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars5_15(KnownEquation):
    _eq_name = 'Livermore2_Vars5_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -x[3]+sympy.log(x[0]/sympy.log(11.06*x[1]*x[4]**2)+x[2])-sympy.cos(x[1]+x[4]+sympy.sqrt(x[1]*x[4]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('cos', 'unary'), ('add', 'binary'), ('X_1', 'var'), ('X_4', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('X_4', 'var'), ('log', 'unary'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('log', 'unary'), ('mul', 'binary'), (11.0600000000000, 'const'), ('X_1', 'var'), ('X_4', 'var'), (2, 'const'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars5_16(KnownEquation):
    _eq_name = 'Livermore2_Vars5_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = x[1]+0.33*x[4]*(x[0]/(x[0]**2+x[1])+x[2]*x[3]**(3/2))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (0.330000000000000, 'const'), ('X_4', 'var'), ('add', 'binary'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_1', 'var'), ('X_0', 'var'), (2, 'const'), (-1, 'const'), ('mul', 'binary'), ('X_2', 'var'), ('X_3', 'var')]

@register_eq_class
class Livermore2_Vars5_17(KnownEquation):
    _eq_name = 'Livermore2_Vars5_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = x[0]-sympy.sin(x[1])+sympy.sin(x[2])-sympy.cos(-x[1]+sympy.sqrt(x[3])+x[4])+0.78
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (0.780000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('cos', 'unary'), ('add', 'binary'), ('X_4', 'var'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('sin', 'unary'), ('X_1', 'var'), ('sin', 'unary'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars5_18(KnownEquation):
    _eq_name = 'Livermore2_Vars5_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = x[0]*x[1]-x[3]-(sympy.sqrt(x[2]**2/(x[0]*(x[2]+x[3])))-1.13/x[2])/x[4]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), ('X_0', 'var'), (-1, 'const'), ('X_2', 'var'), (2, 'const'), ('add', 'binary'), ('X_2', 'var'), ('X_3', 'var'), (-1, 'const'), ('mul', 'binary'), (-1.13000000000000, 'const'), ('X_2', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars5_19(KnownEquation):
    _eq_name = 'Livermore2_Vars5_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = 4.53*x[0]*x[1]+x[0]-x[0]*sympy.cos(sympy.sqrt(x[1]))/x[1]-x[2]-x[3]-x[4]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var'), ('mul', 'binary'), (4.53000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('X_1', 'var'), (-1, 'const'), ('cos', 'unary'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars5_20(KnownEquation):
    _eq_name = 'Livermore2_Vars5_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -sympy.exp(x[0]+x[4])+sympy.sin(x[0]-4.81)/(0.21*(x[4]-sympy.log(x[2]+x[3])-sympy.exp(x[4]))/x[1])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('exp', 'unary'), ('add', 'binary'), ('X_0', 'var'), ('X_4', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('mul', 'binary'), (0.210000000000000, 'const'), ('X_4', 'var'), ('mul', 'binary'), (-0.210000000000000, 'const'), ('exp', 'unary'), ('X_4', 'var'), ('mul', 'binary'), (-0.210000000000000, 'const'), ('log', 'unary'), ('add', 'binary'), ('X_2', 'var'), ('X_3', 'var'), (-1, 'const'), ('sin', 'unary'), ('add', 'binary'), (-4.81000000000000, 'const'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars5_21(KnownEquation):
    _eq_name = 'Livermore2_Vars5_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = sympy.sqrt(x[3])*(2*x[0]+sympy.cos(x[0]*(x[2]*x[3]*sympy.exp(x[0]*x[1])+x[2]-sympy.log(x[2])-3.49))/x[4])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_3', 'var'), ('add', 'binary'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var'), ('mul', 'binary'), ('X_4', 'var'), (-1, 'const'), ('cos', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), (-3.49000000000000, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('log', 'unary'), ('X_2', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('X_3', 'var'), ('exp', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars5_22(KnownEquation):
    _eq_name = 'Livermore2_Vars5_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -x[0]-x[1]+x[2]+sympy.sqrt(x[0]-x[1]*(sympy.sin(x[2])-sympy.log(x[0]*x[4]/(x[1]**2+x[3]))/x[3]))-0.73
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-0.730000000000000, 'const'), ('X_2', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), (-1, 'const'), ('log', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('X_4', 'var'), ('add', 'binary'), ('X_3', 'var'), ('X_1', 'var'), (2, 'const'), (-1, 'const'), ('sin', 'unary'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars5_23(KnownEquation):
    _eq_name = 'Livermore2_Vars5_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = x[0]*(x[1]/(x[2]+sympy.sqrt(x[1]*(x[3]+x[4]))*(-x[2]+x[3]))-x[4])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), ('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('X_3', 'var'), ('X_4', 'var'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars5_24(KnownEquation):
    _eq_name = 'Livermore2_Vars5_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = -x[1]*x[4]+sympy.sqrt(x[0]+x[1]*(-x[0]+x[3]*sympy.cos(sympy.sqrt(x[2])+x[2])-(x[1]+7.84*x[2]**2*x[4])/x[4])+x[1]/x[2])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('X_2', 'var'), (-1, 'const'), ('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('mul', 'binary'), ('X_3', 'var'), ('cos', 'unary'), ('add', 'binary'), ('X_2', 'var'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var'), (-1, 'const'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (7.84000000000000, 'const'), ('X_4', 'var'), ('X_2', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('X_4', 'var')]

@register_eq_class
class Livermore2_Vars5_25(KnownEquation):
    _eq_name = 'Livermore2_Vars5_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=5)
        x = self.x
        self.sympy_eq = x[0]+sympy.log(x[0]*(-3.57*x[0]**2*x[1]+x[0]+x[1]+x[2]*sympy.log(-x[0]*x[3]*sympy.sin(x[2])/x[4]+x[2])))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('log', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('log', 'unary'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('X_3', 'var'), ('X_4', 'var'), (-1, 'const'), ('sin', 'unary'), ('X_2', 'var'), ('mul', 'binary'), (-3.57000000000000, 'const'), ('X_1', 'var'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars6_1(KnownEquation):
    _eq_name = 'Livermore2_Vars6_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]-x[5]+(x[0]+x[3]+x[4])*sympy.sqrt(x[0]**2+x[1]-x[2])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var'), ('mul', 'binary'), ('add', 'binary'), ('X_1', 'var'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('add', 'binary'), ('X_0', 'var'), ('X_3', 'var'), ('X_4', 'var')]

@register_eq_class
class Livermore2_Vars6_2(KnownEquation):
    _eq_name = 'Livermore2_Vars6_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]*(2*x[1]+x[1]/x[2]+x[3]+sympy.log(x[0]*x[4]*x[5]))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), (2, 'const'), ('X_1', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('X_2', 'var'), (-1, 'const'), ('log', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('X_4', 'var'), ('X_5', 'var')]

@register_eq_class
class Livermore2_Vars6_3(KnownEquation):
    _eq_name = 'Livermore2_Vars6_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = sympy.sqrt(x[1]+x[4]-x[5]+x[2]**4*x[3]**4/(x[0]*x[1]**4))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_1', 'var'), ('X_4', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var'), ('mul', 'binary'), ('X_0', 'var'), (-1, 'const'), ('X_1', 'var'), (-4, 'const'), ('X_2', 'var'), (4, 'const'), ('X_3', 'var'), (4, 'const')]

@register_eq_class
class Livermore2_Vars6_4(KnownEquation):
    _eq_name = 'Livermore2_Vars6_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]*(x[1]*(x[0]**2+x[0])-x[1]+x[2]**2-x[2]-x[4]-x[5]-sympy.sin(x[3])-sympy.cos(x[3]))**2
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_2', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var'), ('mul', 'binary'), (-1, 'const'), ('cos', 'unary'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('sin', 'unary'), ('X_3', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('X_0', 'var'), ('X_0', 'var'), (2, 'const'), (2, 'const')]

@register_eq_class
class Livermore2_Vars6_5(KnownEquation):
    _eq_name = 'Livermore2_Vars6_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[1]*sympy.sqrt(x[0]*x[1])*(x[0]*x[2]-x[2]-x[3])+x[4]+x[5]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_4', 'var'), ('X_5', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars6_6(KnownEquation):
    _eq_name = 'Livermore2_Vars6_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = (x[0]/(x[1]*x[2]+sympy.log(sympy.cos(x[0]))**2)-x[1]*x[3]+sympy.sin((x[1]*x[3]+x[4])/x[5])+sympy.cos(x[2]))*sympy.log(x[0])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('log', 'unary'), ('cos', 'unary'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), ('X_1', 'var'), ('X_2', 'var'), (-1, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('X_3', 'var'), ('cos', 'unary'), ('X_2', 'var'), ('sin', 'unary'), ('mul', 'binary'), ('X_5', 'var'), (-1, 'const'), ('add', 'binary'), ('X_4', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('X_3', 'var'), ('log', 'unary'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars6_7(KnownEquation):
    _eq_name = 'Livermore2_Vars6_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]*sympy.sqrt(x[0]-x[5]**2+sympy.sin((x[0]*sympy.exp(-x[1])-x[3]*(x[1]+x[2]**2))/(x[1]+x[4])))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var'), (2, 'const'), ('sin', 'unary'), ('mul', 'binary'), ('add', 'binary'), ('X_1', 'var'), ('X_4', 'var'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), ('X_0', 'var'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('add', 'binary'), ('X_1', 'var'), ('X_2', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars6_8(KnownEquation):
    _eq_name = 'Livermore2_Vars6_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]+x[1]**2+0.34*x[2]*x[4]-x[3]+x[5]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_5', 'var'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), (0.340000000000000, 'const'), ('X_2', 'var'), ('X_4', 'var')]

@register_eq_class
class Livermore2_Vars6_9(KnownEquation):
    _eq_name = 'Livermore2_Vars6_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[3]*(x[0]+sympy.exp(13.28*x[2]**2*x[5]-x[4]**2*sympy.log(x[1]**4))/(x[0]*x[2]-x[1]**2+x[1]-x[5]-sympy.log(x[2])))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_3', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('log', 'unary'), ('X_2', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_2', 'var'), (-1, 'const'), ('exp', 'unary'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var'), (2, 'const'), ('log', 'unary'), ('X_1', 'var'), (4, 'const'), ('mul', 'binary'), (13.2800000000000, 'const'), ('X_5', 'var'), ('X_2', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars6_10(KnownEquation):
    _eq_name = 'Livermore2_Vars6_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]+61.36*x[1]**6+x[1]/(x[0]*x[2]*(x[3]-sympy.cos(x[3]*(2*x[0]*x[1]*x[5]/x[4]+x[4]))))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (61.3600000000000, 'const'), ('X_1', 'var'), (6, 'const'), ('mul', 'binary'), ('X_1', 'var'), ('X_0', 'var'), (-1, 'const'), ('X_2', 'var'), (-1, 'const'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('cos', 'unary'), ('mul', 'binary'), ('X_3', 'var'), ('add', 'binary'), ('X_4', 'var'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var'), ('X_1', 'var'), ('X_5', 'var'), ('X_4', 'var'), (-1, 'const'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars6_11(KnownEquation):
    _eq_name = 'Livermore2_Vars6_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = (x[0]+x[0]/(x[1]+x[3]*(8.13*x[0]**2*x[5]+x[0]*x[1]*x[2]+2*x[1]+x[4]+x[5])))**2
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), ('X_3', 'var'), ('add', 'binary'), ('X_4', 'var'), ('X_5', 'var'), ('mul', 'binary'), (2, 'const'), ('X_1', 'var'), ('mul', 'binary'), (8.13000000000000, 'const'), ('X_5', 'var'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('X_2', 'var'), (-1, 'const'), (2, 'const')]

@register_eq_class
class Livermore2_Vars6_12(KnownEquation):
    _eq_name = 'Livermore2_Vars6_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = (sympy.sqrt(2)*sympy.sqrt(x[0])-x[1]-x[2]/sympy.sqrt(x[3]*(8.29*x[0]*x[2]**2+x[0]*x[4])+x[3]+x[5]))/x[5]
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_5', 'var'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('add', 'binary'), ('X_3', 'var'), ('X_5', 'var'), ('mul', 'binary'), ('X_3', 'var'), ('add', 'binary'), ('mul', 'binary'), ('X_0', 'var'), ('X_4', 'var'), ('mul', 'binary'), (8.29000000000000, 'const'), ('X_0', 'var'), ('X_2', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars6_13(KnownEquation):
    _eq_name = 'Livermore2_Vars6_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]+x[4]+0.21*sympy.sqrt(x[0]/(x[1]**2*x[2]**2*sympy.sqrt(x[5])*(sympy.sqrt(x[2])+x[2]+2*x[5]+(x[1]+x[3]+x[4])/x[4])))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_4', 'var'), ('mul', 'binary'), (0.210000000000000, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), (-2, 'const'), ('X_2', 'var'), (-2, 'const'), ('X_5', 'var'), ('add', 'binary'), ('X_2', 'var'), ('X_2', 'var'), ('mul', 'binary'), (2, 'const'), ('X_5', 'var'), ('mul', 'binary'), ('X_4', 'var'), (-1, 'const'), ('add', 'binary'), ('X_1', 'var'), ('X_3', 'var'), ('X_4', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars6_14(KnownEquation):
    _eq_name = 'Livermore2_Vars6_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -2.07*x[5]+sympy.log(x[1]-x[5]-sympy.sqrt(x[2]*(x[4]+sympy.log(-x[0]+x[4]+1))/x[3]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-2.07000000000000, 'const'), ('X_5', 'var'), ('log', 'unary'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var'), ('mul', 'binary'), (-1, 'const'), ('mul', 'binary'), ('X_2', 'var'), ('X_3', 'var'), (-1, 'const'), ('add', 'binary'), ('X_4', 'var'), ('log', 'unary'), ('add', 'binary'), (1, 'const'), ('X_4', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars6_15(KnownEquation):
    _eq_name = 'Livermore2_Vars6_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]*(x[0]+sympy.cos(x[1]**2*x[2]*x[3]*(x[4]-0.43*x[5]**2)))/x[3]
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('X_3', 'var'), (-1, 'const'), ('add', 'binary'), ('X_0', 'var'), ('cos', 'unary'), ('mul', 'binary'), ('X_2', 'var'), ('X_3', 'var'), ('X_1', 'var'), (2, 'const'), ('add', 'binary'), ('X_4', 'var'), ('mul', 'binary'), (-0.430000000000000, 'const'), ('X_5', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars6_16(KnownEquation):
    _eq_name = 'Livermore2_Vars6_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -sympy.sqrt(x[0])-x[0]+x[1]-x[3]-x[4]-sympy.sqrt(x[5]/x[2])-3.26
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (-3.26000000000000, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('mul', 'binary'), ('X_5', 'var'), ('X_2', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars6_17(KnownEquation):
    _eq_name = 'Livermore2_Vars6_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]/(x[1]*x[3]*(-x[4]+sympy.log(x[5]**2*sympy.cos(2*x[1]+x[2]**2-x[3])**2))*(129.28*x[0]**2*x[1]**2+x[2]))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), (-1, 'const'), ('X_3', 'var'), (-1, 'const'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), (129.280000000000, 'const'), ('X_0', 'var'), (2, 'const'), ('X_1', 'var'), (2, 'const'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var'), ('log', 'unary'), ('mul', 'binary'), ('X_5', 'var'), (2, 'const'), ('cos', 'unary'), ('add', 'binary'), ('X_2', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), (2, 'const'), ('X_1', 'var'), (2, 'const'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars6_18(KnownEquation):
    _eq_name = 'Livermore2_Vars6_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = sympy.sqrt(x[4])*(2*x[0]+sympy.cos(x[0]*(x[2]*x[3]*sympy.exp(x[0]*x[1])+x[2]-sympy.log(x[2])-3.49))/x[5])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_4', 'var'), ('add', 'binary'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var'), ('mul', 'binary'), ('X_5', 'var'), (-1, 'const'), ('cos', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), (-3.49000000000000, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('log', 'unary'), ('X_2', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('X_3', 'var'), ('exp', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars6_19(KnownEquation):
    _eq_name = 'Livermore2_Vars6_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]+x[1]+x[2]+0.84*sympy.sqrt(-x[2]*x[5]+x[3]-x[4]+sympy.sqrt((x[1]+sympy.log(x[2]+sympy.exp(x[1])))/(x[1]-x[3])))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('X_2', 'var'), ('mul', 'binary'), (0.840000000000000, 'const'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), (-1, 'const'), ('add', 'binary'), ('X_1', 'var'), ('log', 'unary'), ('add', 'binary'), ('X_2', 'var'), ('exp', 'unary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('X_5', 'var')]

@register_eq_class
class Livermore2_Vars6_20(KnownEquation):
    _eq_name = 'Livermore2_Vars6_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = (x[0]-0.97*x[0]/(x[4]-x[5]*(x[0]**(3/2)*x[3]+x[5]))-x[1]+x[2]+sympy.sin(x[0]**2)/x[0])**2
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), ('X_0', 'var'), (-1, 'const'), ('sin', 'unary'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (-0.970000000000000, 'const'), ('X_0', 'var'), ('add', 'binary'), ('X_4', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var'), ('add', 'binary'), ('X_5', 'var'), ('mul', 'binary'), ('X_3', 'var'), ('X_0', 'var'), (-1, 'const'), (2, 'const')]

@register_eq_class
class Livermore2_Vars6_21(KnownEquation):
    _eq_name = 'Livermore2_Vars6_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]+x[2]+(x[0]+sympy.sin(-3.47*x[1]*sympy.log(x[5])/x[4]+x[3]+25.56*sympy.exp(x[4]**2)/x[1])**2)*sympy.sin(x[1])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_2', 'var'), ('mul', 'binary'), ('add', 'binary'), ('X_0', 'var'), ('sin', 'unary'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), (25.5600000000000, 'const'), ('X_1', 'var'), (-1, 'const'), ('exp', 'unary'), ('X_4', 'var'), (2, 'const'), ('mul', 'binary'), (-3.47000000000000, 'const'), ('X_1', 'var'), ('X_4', 'var'), (-1, 'const'), ('log', 'unary'), ('X_5', 'var'), (2, 'const'), ('sin', 'unary'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars6_22(KnownEquation):
    _eq_name = 'Livermore2_Vars6_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]+(x[3]+sympy.sin(-0.22*(x[2]-x[3]+1.0))*sympy.cos(x[5]))*sympy.cos(x[1]+2.27*x[4])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('cos', 'unary'), ('X_5', 'var'), ('sin', 'unary'), ('add', 'binary'), (0.220000000000000, 'const'), ('mul', 'binary'), (0.220000000000000, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-0.220000000000000, 'const'), ('X_3', 'var'), ('cos', 'unary'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (2.27000000000000, 'const'), ('X_4', 'var')]

@register_eq_class
class Livermore2_Vars6_23(KnownEquation):
    _eq_name = 'Livermore2_Vars6_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]+x[3]+sympy.log(x[0]**2+x[0]*(-x[5]+1.88*sympy.sqrt(0.71*x[0]+x[1]+0.28*(x[2]-x[3]/x[4]))))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_3', 'var'), ('log', 'unary'), ('add', 'binary'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var'), ('mul', 'binary'), (1.88000000000000, 'const'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (0.710000000000000, 'const'), ('X_0', 'var'), ('mul', 'binary'), (0.280000000000000, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-0.280000000000000, 'const'), ('X_3', 'var'), ('X_4', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars6_24(KnownEquation):
    _eq_name = 'Livermore2_Vars6_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = -0.59*(1.42*(0.24*x[1]+sympy.sqrt(x[2])/(x[5]*sympy.sqrt(-x[3]+x[4])))**(1/4)+sympy.sin(x[0]))/x[5]
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_5', 'var'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), (-0.837800000000000, 'const'), ('add', 'binary'), ('mul', 'binary'), (0.240000000000000, 'const'), ('X_1', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('X_5', 'var'), (-1, 'const'), ('add', 'binary'), ('X_4', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), (-0.590000000000000, 'const'), ('sin', 'unary'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars6_25(KnownEquation):
    _eq_name = 'Livermore2_Vars6_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=6)
        x = self.x
        self.sympy_eq = x[0]-x[1]**2-x[2]+x[4]*sympy.cos(x[2])+x[4]+x[5]-2.19*sympy.sqrt(-x[2]-0.44/x[3])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_4', 'var'), ('X_5', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), (-2.19000000000000, 'const'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-0.440000000000000, 'const'), ('X_3', 'var'), (-1, 'const'), ('mul', 'binary'), ('X_4', 'var'), ('cos', 'unary'), ('X_2', 'var')]

@register_eq_class
class Livermore2_Vars7_1(KnownEquation):
    _eq_name = 'Livermore2_Vars7_1'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[5]*x[6]*(x[2]+sympy.cos(-4*x[0]**2+x[1]*x[2]*x[3]+x[4]))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_5', 'var'), ('X_6', 'var'), ('add', 'binary'), ('X_2', 'var'), ('cos', 'unary'), ('add', 'binary'), ('X_4', 'var'), ('mul', 'binary'), (-4, 'const'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), ('X_1', 'var'), ('X_2', 'var'), ('X_3', 'var')]

@register_eq_class
class Livermore2_Vars7_2(KnownEquation):
    _eq_name = 'Livermore2_Vars7_2'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = -x[3]-x[4]*x[6]+sympy.sqrt(x[0]-x[1]-x[2]-x[3]-2*x[4]*x[5])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), (-2, 'const'), ('X_4', 'var'), ('X_5', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var'), ('X_6', 'var')]

@register_eq_class
class Livermore2_Vars7_3(KnownEquation):
    _eq_name = 'Livermore2_Vars7_3'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[0]+x[1]+x[2]+sympy.cos((x[1]+x[3]*(x[3]+x[4])/x[5]-x[6])**4/x[6])+1
        self.sympy_eq_preorder_traversal = [('add', 'binary'), (1, 'const'), ('X_0', 'var'), ('X_1', 'var'), ('X_2', 'var'), ('cos', 'unary'), ('mul', 'binary'), ('X_6', 'var'), (-1, 'const'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_6', 'var'), ('mul', 'binary'), ('X_3', 'var'), ('X_5', 'var'), (-1, 'const'), ('add', 'binary'), ('X_3', 'var'), ('X_4', 'var'), (4, 'const')]

@register_eq_class
class Livermore2_Vars7_4(KnownEquation):
    _eq_name = 'Livermore2_Vars7_4'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[1]+x[4]+sympy.log(x[3]*sympy.sqrt(x[5])*x[6]*(x[0]+x[2]**2+x[4]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_1', 'var'), ('X_4', 'var'), ('log', 'unary'), ('mul', 'binary'), ('X_3', 'var'), ('X_6', 'var'), ('X_5', 'var'), ('add', 'binary'), ('X_0', 'var'), ('X_4', 'var'), ('X_2', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars7_5(KnownEquation):
    _eq_name = 'Livermore2_Vars7_5'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = (-0.12*x[0]/(x[2]*x[4]**(5/2)*x[5]*(-x[1]+x[2]*x[3]+sympy.cos(2*x[0])))+x[1])*sympy.exp(-x[5]+x[6])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-0.120000000000000, 'const'), ('X_0', 'var'), ('X_2', 'var'), (-1, 'const'), ('X_4', 'var'), ('X_5', 'var'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('X_3', 'var'), ('cos', 'unary'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var'), (-1, 'const'), ('exp', 'unary'), ('add', 'binary'), ('X_6', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var')]

@register_eq_class
class Livermore2_Vars7_6(KnownEquation):
    _eq_name = 'Livermore2_Vars7_6'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[0]**2-sympy.cos(4.69*sympy.exp(x[1]*(x[2]/x[6]-x[5])*(x[3]**3*x[4]+x[3])))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), (2, 'const'), ('mul', 'binary'), (-1, 'const'), ('cos', 'unary'), ('mul', 'binary'), (4.69000000000000, 'const'), ('exp', 'unary'), ('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), ('X_4', 'var'), ('X_3', 'var'), (3, 'const'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('X_6', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars7_7(KnownEquation):
    _eq_name = 'Livermore2_Vars7_7'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[0]/(97.02*x[1]**2*x[5]**4+x[2]+x[5]*sympy.sin(x[6]/x[4]))+x[2]**(1/4)-x[3]*x[6]-sympy.log(x[5])**2
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), (-1, 'const'), ('log', 'unary'), ('X_5', 'var'), (2, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), ('X_5', 'var'), ('sin', 'unary'), ('mul', 'binary'), ('X_6', 'var'), ('X_4', 'var'), (-1, 'const'), ('mul', 'binary'), (97.0200000000000, 'const'), ('X_1', 'var'), (2, 'const'), ('X_5', 'var'), (4, 'const'), (-1, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('X_6', 'var')]

@register_eq_class
class Livermore2_Vars7_8(KnownEquation):
    _eq_name = 'Livermore2_Vars7_8'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = 4.73*x[0]+sympy.cos(x[5]*sympy.sqrt(x[1]**2*x[2]*(x[3]+x[5])**2/(x[4]*(x[1]+x[6]))))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (4.73000000000000, 'const'), ('X_0', 'var'), ('cos', 'unary'), ('mul', 'binary'), ('X_5', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('X_1', 'var'), (2, 'const'), ('X_4', 'var'), (-1, 'const'), ('add', 'binary'), ('X_1', 'var'), ('X_6', 'var'), (-1, 'const'), ('add', 'binary'), ('X_3', 'var'), ('X_5', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars7_9(KnownEquation):
    _eq_name = 'Livermore2_Vars7_9'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[1]-x[5]**2+0.56*sympy.sqrt((-x[0]+x[2]+x[3])/(x[0]*x[1]**3*x[4]*x[6]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var'), (2, 'const'), ('mul', 'binary'), (0.560000000000000, 'const'), ('mul', 'binary'), ('X_0', 'var'), (-1, 'const'), ('X_1', 'var'), (-3, 'const'), ('X_4', 'var'), (-1, 'const'), ('X_6', 'var'), (-1, 'const'), ('add', 'binary'), ('X_2', 'var'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars7_10(KnownEquation):
    _eq_name = 'Livermore2_Vars7_10'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = -2.07*x[6]+sympy.log(x[1]-x[5]-sympy.sqrt(x[2]*(x[4]+sympy.log(-x[0]+x[4]+1))/x[3]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-2.07000000000000, 'const'), ('X_6', 'var'), ('log', 'unary'), ('add', 'binary'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var'), ('mul', 'binary'), (-1, 'const'), ('mul', 'binary'), ('X_2', 'var'), ('X_3', 'var'), (-1, 'const'), ('add', 'binary'), ('X_4', 'var'), ('log', 'unary'), ('add', 'binary'), (1, 'const'), ('X_4', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var')]

@register_eq_class
class Livermore2_Vars7_11(KnownEquation):
    _eq_name = 'Livermore2_Vars7_11'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[1]*(x[0]*sympy.cos(x[1]-x[3]+4.52+x[6]/(x[2]*x[5]))**4/(x[1]*x[2]**2)+2*x[3]+x[4])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('X_4', 'var'), ('mul', 'binary'), (2, 'const'), ('X_3', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var'), (-1, 'const'), ('X_2', 'var'), (-2, 'const'), ('cos', 'unary'), ('add', 'binary'), (4.52000000000000, 'const'), ('X_1', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), ('X_6', 'var'), ('X_2', 'var'), (-1, 'const'), ('X_5', 'var'), (-1, 'const'), (4, 'const')]

@register_eq_class
class Livermore2_Vars7_12(KnownEquation):
    _eq_name = 'Livermore2_Vars7_12'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[0]*(x[1]+x[3]+sympy.cos(sympy.exp(x[5]*x[6]*(x[3]+0.43*x[2]*(x[0]*x[1]+x[0])/(x[0]*x[4])))))
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_1', 'var'), ('X_3', 'var'), ('cos', 'unary'), ('exp', 'unary'), ('mul', 'binary'), ('X_5', 'var'), ('X_6', 'var'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), (0.430000000000000, 'const'), ('X_2', 'var'), ('X_0', 'var'), (-1, 'const'), ('X_4', 'var'), (-1, 'const'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars7_13(KnownEquation):
    _eq_name = 'Livermore2_Vars7_13'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[3]+sympy.sin(sympy.sqrt(x[0]*(x[0]*x[6]*(x[2]+x[5])+1.21)*sympy.exp(-x[4])/sympy.sqrt(x[0]-x[1])))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_3', 'var'), ('sin', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('add', 'binary'), (1.21000000000000, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('X_6', 'var'), ('add', 'binary'), ('X_2', 'var'), ('X_5', 'var'), ('exp', 'unary'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var')]

@register_eq_class
class Livermore2_Vars7_14(KnownEquation):
    _eq_name = 'Livermore2_Vars7_14'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = 4.63*x[0]**2*x[5]+1.31*x[5]-sympy.cos(x[6]*(x[6]+(x[1]**2*x[4]**2*x[5]**2*(x[0]+x[2]*x[3]*x[5])**2+x[5])/x[0]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('cos', 'unary'), ('mul', 'binary'), ('X_6', 'var'), ('add', 'binary'), ('X_6', 'var'), ('mul', 'binary'), ('X_0', 'var'), (-1, 'const'), ('add', 'binary'), ('X_5', 'var'), ('mul', 'binary'), ('X_1', 'var'), (2, 'const'), ('X_4', 'var'), (2, 'const'), ('X_5', 'var'), (2, 'const'), ('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), ('X_2', 'var'), ('X_3', 'var'), ('X_5', 'var'), (2, 'const'), ('mul', 'binary'), (1.31000000000000, 'const'), ('X_5', 'var'), ('mul', 'binary'), (4.63000000000000, 'const'), ('X_5', 'var'), ('X_0', 'var'), (2, 'const')]

@register_eq_class
class Livermore2_Vars7_15(KnownEquation):
    _eq_name = 'Livermore2_Vars7_15'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[2]*x[3]+sympy.log(x[0]*x[1])-3.69/(-x[0]*sympy.exp(-4*x[6])+x[1]*x[4]-1.99+x[5]/sympy.sqrt(x[0]))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-3.69000000000000, 'const'), ('add', 'binary'), (-1.99000000000000, 'const'), ('mul', 'binary'), ('X_1', 'var'), ('X_4', 'var'), ('mul', 'binary'), ('X_5', 'var'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_0', 'var'), ('exp', 'unary'), ('mul', 'binary'), (-4, 'const'), ('X_6', 'var'), (-1, 'const'), ('mul', 'binary'), ('X_2', 'var'), ('X_3', 'var'), ('log', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars7_16(KnownEquation):
    _eq_name = 'Livermore2_Vars7_16'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[3]+sympy.cos(0.78*x[0]*(x[2]+x[5]**2)*(x[1]*x[6]+x[2])/(x[1]+2.19)+x[3]**2*x[4])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_3', 'var'), ('cos', 'unary'), ('add', 'binary'), ('mul', 'binary'), ('X_4', 'var'), ('X_3', 'var'), (2, 'const'), ('mul', 'binary'), (0.780000000000000, 'const'), ('X_0', 'var'), ('add', 'binary'), (2.19000000000000, 'const'), ('X_1', 'var'), (-1, 'const'), ('add', 'binary'), ('X_2', 'var'), ('X_5', 'var'), (2, 'const'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('X_6', 'var')]

@register_eq_class
class Livermore2_Vars7_17(KnownEquation):
    _eq_name = 'Livermore2_Vars7_17'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = (-x[6]+sympy.cos(sympy.sqrt(x[0]*x[4]*(x[0]+1.42)*(-sympy.sqrt(x[1]+x[5])+(-x[3]+x[4]*x[6])/x[2]))))/sympy.sqrt(x[4])
        self.sympy_eq_preorder_traversal = [('mul', 'binary'), ('X_4', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_6', 'var'), ('cos', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('X_4', 'var'), ('add', 'binary'), (1.42000000000000, 'const'), ('X_0', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('add', 'binary'), ('X_1', 'var'), ('X_5', 'var'), ('mul', 'binary'), ('X_2', 'var'), (-1, 'const'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('mul', 'binary'), ('X_4', 'var'), ('X_6', 'var')]

@register_eq_class
class Livermore2_Vars7_18(KnownEquation):
    _eq_name = 'Livermore2_Vars7_18'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[0]+sympy.sqrt(2)*sympy.sqrt(x[0]/x[4])/2+sympy.cos(-x[1]*(-x[2]+3.67/x[0])+x[3]+x[5]*x[6])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (2, 'const'), ('mul', 'binary'), ('X_0', 'var'), ('X_4', 'var'), (-1, 'const'), ('cos', 'unary'), ('add', 'binary'), ('X_3', 'var'), ('mul', 'binary'), ('X_5', 'var'), ('X_6', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_1', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('mul', 'binary'), (3.67000000000000, 'const'), ('X_0', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars7_19(KnownEquation):
    _eq_name = 'Livermore2_Vars7_19'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = 2*x[0]*x[1]+x[3]*sympy.exp(sympy.sqrt(x[1])*(x[4]*(1.22*x[1]*x[3]*x[5]+2.65*x[5])*sympy.sin(x[6])-x[5]-x[6])+x[2])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('X_3', 'var'), ('exp', 'unary'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_6', 'var'), ('mul', 'binary'), ('X_4', 'var'), ('add', 'binary'), ('mul', 'binary'), (2.65000000000000, 'const'), ('X_5', 'var'), ('mul', 'binary'), (1.22000000000000, 'const'), ('X_1', 'var'), ('X_3', 'var'), ('X_5', 'var'), ('sin', 'unary'), ('X_6', 'var'), ('mul', 'binary'), (2, 'const'), ('X_0', 'var'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars7_20(KnownEquation):
    _eq_name = 'Livermore2_Vars7_20'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[0]-sympy.exp(x[3]/(x[2]+x[3]*(x[4]+x[6]+sympy.exp(x[5])/sympy.sqrt(x[2]+x[5]))+3.42*sympy.sqrt(-x[1]**2*x[4])))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('exp', 'unary'), ('mul', 'binary'), ('X_3', 'var'), ('add', 'binary'), ('X_2', 'var'), ('mul', 'binary'), (3.42000000000000, 'const'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var'), ('X_1', 'var'), (2, 'const'), ('mul', 'binary'), ('X_3', 'var'), ('add', 'binary'), ('X_4', 'var'), ('X_6', 'var'), ('mul', 'binary'), ('add', 'binary'), ('X_2', 'var'), ('X_5', 'var'), ('exp', 'unary'), ('X_5', 'var'), (-1, 'const')]

@register_eq_class
class Livermore2_Vars7_21(KnownEquation):
    _eq_name = 'Livermore2_Vars7_21'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[0]*(x[0]+x[1]+x[1]/(8.07*x[0]**2*x[1]*x[2]*x[3]*x[4]*(x[2]+x[3])-x[4])+x[5]+sympy.log(sympy.cos(x[6])))+x[0]+x[1]
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), ('X_0', 'var'), ('X_1', 'var'), ('X_5', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('add', 'binary'), ('mul', 'binary'), (-1, 'const'), ('X_4', 'var'), ('mul', 'binary'), (8.07000000000000, 'const'), ('X_1', 'var'), ('X_2', 'var'), ('X_3', 'var'), ('X_4', 'var'), ('X_0', 'var'), (2, 'const'), ('add', 'binary'), ('X_2', 'var'), ('X_3', 'var'), (-1, 'const'), ('log', 'unary'), ('cos', 'unary'), ('X_6', 'var')]

@register_eq_class
class Livermore2_Vars7_22(KnownEquation):
    _eq_name = 'Livermore2_Vars7_22'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[0]+x[1]*x[4]+x[2]+2.21*sympy.sqrt(0.97*x[3]-1)+sympy.exp(x[3]+x[5]+x[6])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_0', 'var'), ('X_2', 'var'), ('mul', 'binary'), (2.21000000000000, 'const'), ('add', 'binary'), (-1, 'const'), ('mul', 'binary'), (0.970000000000000, 'const'), ('X_3', 'var'), ('mul', 'binary'), ('X_1', 'var'), ('X_4', 'var'), ('exp', 'unary'), ('add', 'binary'), ('X_3', 'var'), ('X_5', 'var'), ('X_6', 'var')]

@register_eq_class
class Livermore2_Vars7_23(KnownEquation):
    _eq_name = 'Livermore2_Vars7_23'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[0]*sympy.cos(x[0])-sympy.sqrt(x[2])*x[3]/(-14.13*x[1]*x[2]*x[4]+13.78*x[1]*x[5]+x[2]+13.04*x[3]*x[5]*x[6]+x[4]+(-x[5]+x[6])**2)+sympy.cos(x[1])
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), ('X_0', 'var'), ('cos', 'unary'), ('X_0', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_3', 'var'), ('X_2', 'var'), ('add', 'binary'), ('X_2', 'var'), ('X_4', 'var'), ('add', 'binary'), ('X_6', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_5', 'var'), (2, 'const'), ('mul', 'binary'), (13.7800000000000, 'const'), ('X_1', 'var'), ('X_5', 'var'), ('mul', 'binary'), (13.0400000000000, 'const'), ('X_3', 'var'), ('X_5', 'var'), ('X_6', 'var'), ('mul', 'binary'), (-14.1300000000000, 'const'), ('X_1', 'var'), ('X_2', 'var'), ('X_4', 'var'), (-1, 'const'), ('cos', 'unary'), ('X_1', 'var')]

@register_eq_class
class Livermore2_Vars7_24(KnownEquation):
    _eq_name = 'Livermore2_Vars7_24'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = x[5]+2*x[6]+sympy.sqrt(sympy.sin(x[0]*(x[0]+x[1]-3.03))+x[6]/(x[0]*x[2]**2*sympy.sqrt(x[4])*sympy.sin(x[3]**2)))
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('X_5', 'var'), ('add', 'binary'), ('mul', 'binary'), ('X_6', 'var'), ('X_0', 'var'), (-1, 'const'), ('X_2', 'var'), (-2, 'const'), ('X_4', 'var'), ('sin', 'unary'), ('X_3', 'var'), (2, 'const'), (-1, 'const'), ('sin', 'unary'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), (-3.03000000000000, 'const'), ('X_0', 'var'), ('X_1', 'var'), ('mul', 'binary'), (2, 'const'), ('X_6', 'var')]

@register_eq_class
class Livermore2_Vars7_25(KnownEquation):
    _eq_name = 'Livermore2_Vars7_25'
    _function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'n2', 'log', 'exp', 'sin', 'cos', '1']

    def __init__(self):
        super().__init__(num_vars=7)
        x = self.x
        self.sympy_eq = -1.16*x[0]*sympy.log(sympy.sqrt(x[3])+x[6])-x[2]*sympy.cos(x[4])/(x[0]*(x[5]+0.95)+x[2]**2*(x[1]+x[5])**2)
        self.sympy_eq_preorder_traversal = [('add', 'binary'), ('mul', 'binary'), (-1.16000000000000, 'const'), ('X_0', 'var'), ('log', 'unary'), ('add', 'binary'), ('X_6', 'var'), ('X_3', 'var'), ('mul', 'binary'), (-1, 'const'), ('X_2', 'var'), ('add', 'binary'), ('mul', 'binary'), ('X_0', 'var'), ('add', 'binary'), (0.950000000000000, 'const'), ('X_5', 'var'), ('mul', 'binary'), ('X_2', 'var'), (2, 'const'), ('add', 'binary'), ('X_1', 'var'), ('X_5', 'var'), (2, 'const'), (-1, 'const'), ('cos', 'unary'), ('X_4', 'var')]

