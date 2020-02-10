from typing import List, Callable

from geometry_solver.entities.entity import Entity


class TheoryManager(object):

    def __init__(self):
        self._theoies = {}

    def theoried(self, obj):
        def decorator(f):
            self._add_theoty(obj, f)
            print('Theory {} added. It can be applied to {}.'.format(f.__name__, obj.__name__))
        return decorator

    def _add_theoty(self, obj, theoy_func: Callable) -> None:
        if obj not in self._theoies:
            self._theoies[obj] = []
        self._theoies[obj].append(theoy_func)

    def theories_suit_to_entity(self, entity: Entity) -> List:
        class_ = type(entity)
        if class_ not in self._theoies:
            return []
        return self._theoies[class_]

