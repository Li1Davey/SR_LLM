from collections import OrderedDict

EQUATION_CLASS_DICT = OrderedDict()


def register_eq_class(cls):
    EQUATION_CLASS_DICT[cls.__name__] = cls
    return cls


def get_eq_obj(key, **kwargs):
    if key in EQUATION_CLASS_DICT:
        return EQUATION_CLASS_DICT[key](**kwargs)
    raise KeyError(f'`{key}` is not expected as a equation object key')
