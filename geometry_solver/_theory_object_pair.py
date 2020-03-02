from typing import Callable, Union

from geometry_solver.entities.entity import Entity
from geometry_solver.relationships.relationship import Relationship
from geometry_solver.common.finder import Finder


class TheoryObjectPair(object):
        
    def __init__(self, theory: Callable, obj: Union[Entity, Relationship]):
        self.object = obj
        self.theory = theory

    def __hash__(self):
        return hash(self.object.id + self.theory.__name__)

    def __eq__(self, other):
        return self.object == other.object and self.theory == other.theory

    def deduct(self, finder: Finder):
        self.theory.__call__(self.object, finder)

    def __str__(self):
        return '(object: ' \
            + str(type(self.object).__name__) \
            + ' ' \
            + str(self.object.id) \
            + ', theory: ' \
            + str(self.theory.__name__) \
            + ')'