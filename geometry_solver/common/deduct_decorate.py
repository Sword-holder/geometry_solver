import inspect

from geometry_solver import equation_solver


def _f_decorated(f):
    def decorator(*args):
        equation_set = []
        group_key = '_'.join([f.__name__, args[0].id])
        if inspect.isgeneratorfunction(f):
            for eq in f(*args):
                equation_set.append(eq)
            if equation_set:
                equation_solver.set_equation_group(group_key, equation_set)
        else:
            f(*args)
    decorator.__name__ = f.__name__
    return decorator

