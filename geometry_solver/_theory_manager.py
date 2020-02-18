import inspect
from typing import List, Callable, Union

from geometry_solver.entities.entity import Entity
from geometry_solver.relationships.relationship import Relationship
from geometry_solver import equation_solver


class TheoryManager(object):

    def __init__(self):
        self._theoies = {}

    def theoried(self, obj):
        def decorator(f):
            f = self._f_decorated(f)
            self._add_theoty(obj, f)
            print('Theory {} added. It can be applied to {}.'.format(f.__name__, obj.__name__))
        return decorator

    def _f_decorated(self, f):
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
        return decorator       

    def _add_theoty(self, obj, theoy_func: Callable) -> None:
        if obj not in self._theoies:
            self._theoies[obj] = []
        self._theoies[obj].append(theoy_func)

    def theories_suit_to_object(self, obj: Union[Entity, Relationship]) -> List:
        class_ = type(obj)
        if class_ not in self._theoies:
            return []
        return self._theoies[class_]

