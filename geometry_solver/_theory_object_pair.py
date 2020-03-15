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

    def __lt__(self, other):
        if self.object.id == other.object.id:
            return self.theory.__name__ < other.theory.__name__
        return self.object.id < other.object.id

    def deduct(self, node):
        self.theory.__call__(object_=self.object, node=node)

    def __str__(self):
        return '(object: ' \
            + str(type(self.object).__name__) \
            + ' ' \
            + str(self.object.id) \
            + ', theory: ' \
            + str(self.theory.__name__) \
            + ')'