import inspect

from sympy import Symbol, Number

from geometry_solver.entities.entity import Entity
from geometry_solver.relationships.relationship import Relationship
from geometry_solver import equation_solver
from geometry_solver import new_objects
from geometry_solver import solving_path
from geometry_solver.common.zh_lib import zh_theory


def _f_decorated(f):
    def decorator(*args):
        equation_set = []
        group_key = '_'.join([f.__name__, args[0].id])
        if inspect.isgeneratorfunction(f):
            for item in f(*args):
                if isinstance(item, Entity) or isinstance(item, Relationship):
                    new_objects.add(item)
                else:
                    equation_set.append(item)
            equation_set = [eq for eq in equation_set if not isinstance(eq, Number)]
            if equation_set:
                if not equation_solver.has_key(group_key):
                    for eq in equation_set:
                        if type(eq) != float and type(eq) != int:
                            solving_path.append_equation(zh_theory[f.__name__], eq)
                equation_solver.set_equation_group(group_key, equation_set)
        else:
            f(*args)
    decorator.__name__ = f.__name__
    return decorator

