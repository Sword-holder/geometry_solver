from typing import Callable, Union

from geometry_solver.entities.entity import Entity
from geometry_solver.relationships.relationship import Relationship
from geometry_solver.common.finder import Finder


class TheoryObjectPair(object):
        
    def __init__(self, theory: Callable, obj: Union[Entity, Relationship]):
        self.object = obj
        self.theory = theory

    def deduct(self, finder: Finder):
        if isinstance(self.object, Entity):
            self.theory.__call__(self.object)
        else:
            self.theory.__call__(self.object, finder)

    def __str__(self):
        return '(object: ' \
            + str(type(self.object).__name__) \
            + ' ' \
            + str(self.object.id) \
            + ', theory: ' \
            + str(self.theory.__name__) \
            + ')'