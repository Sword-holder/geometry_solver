from typing import List

import numpy as np

from geometry_solver.entities.entity import Entity
from geometry_solver import theory_manager
import geometry_solver.theories.theory_for_triangle
from geometry_solver.target import Target


class Solver(object):


    class EntityTheoryPair(object):
        
        def __init__(self, entity: Entity, theory):
            self.entity = entity
            self.theory = theory

        def __str__(self):
            return '(entity: ' \
                + str(type(self.entity).__name__) \
                + ' ' \
                + str(self.entity.id) \
                + ', theory: ' \
                + str(self.theory.__name__) \
                + ')'


    def __init__(self, problem: Entity, targets: List[Target] = []):
        self._problem = problem
        self._targets = []

    def add_target(self, target: Target) -> None:
        self._targets.append(target)

    def solve(self) -> Entity:
        print('solving problem....')
        entity_theory_pairs = []
        for e in self._problem.children:
            theories = theory_manager.theories_suit_to_entity(e)
            for t in theories:
                pair = self.EntityTheoryPair(e, t)
                entity_theory_pairs.append(pair)
        print('Make {} entity-theory pairs.'.format(len(entity_theory_pairs)))

        epoch = 0
        while not self._solved:
            pair = np.random.choice(entity_theory_pairs)
            pair.theory(pair.entity)
            print('epoch {}: chose {} to search.'.format(epoch, pair))
            epoch += 1

        print('Solve problem successfully! Here are results:')
        for target in self._targets:
            print(target)
        
        return self._problem
    

    @property
    def _solved(self) -> bool:
        for target in self._targets:
            if not target.solved:
                return False
        return True

