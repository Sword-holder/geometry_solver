from typing import List, Callable, Union

import numpy as np
from sympy import Symbol, Number

from geometry_solver.entities.entity import Entity
from geometry_solver.entities.line import Line
from geometry_solver.entities.angle import Angle
from geometry_solver.relationships.relationship import Relationship
from geometry_solver import theory_manager
from geometry_solver.problem import Problem
from geometry_solver.target import Target
import geometry_solver.theories.theory_for_triangle
import geometry_solver.theories.theory_for_collineation
import geometry_solver.theories.theory_for_common_vertex_angle
from geometry_solver.common.finder import Finder
from geometry_solver import equation_solver
from geometry_solver.common.utils import to_symbol


class Solver(object):


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


    def __init__(self, problem: Problem, targets: List[Target] = []):
        self._problem = problem
        self._targets = []
        self._finder = Finder(problem.entity)

    def add_target(self, target: Target) -> None:
        self._targets.append(target)

    def solve(self) -> Problem:
        print('solving problem....')
        theory_obj_pairs = []
        objects = list(self._problem.entity.children) \
                  + self._problem.relationships
        for obj in objects:
            theories = theory_manager.theories_suit_to_object(obj)
            for t in theories:
                pair = Solver.TheoryObjectPair(t, obj)
                theory_obj_pairs.append(pair)
        print('Make {} entity-theory pairs.'.format(len(theory_obj_pairs)))

        epoch = 0
        while not self._solved:
            if not theory_obj_pairs:
                break
            pair = np.random.choice(theory_obj_pairs)
            pair.deduct(self._finder)
            self._solve_equation()
            print('epoch {}: chose {} to search.'.format(epoch, pair))
            epoch += 1
            break

        if self._solved:
            print('Solve problem successfully! Here are results:')
            for target in self._targets:
                print(target)
        else:
            print('The problem has no solution')
        
        return self._problem

    @property
    def _solved(self) -> bool:
        for target in self._targets:
            if not target.solved:
                return False
        return True

    def _solve_equation(self):
        result = equation_solver.solve()
        for e in self._problem.entity.children:
            attr_map = {Line: 'length', Angle: 'angle'}
            try:
                attr = attr_map[type(e)]
            except KeyError:
                continue
            symbol = to_symbol(e, attr)
            if isinstance(symbol, Symbol):
                try:
                    value = result[symbol]
                    if isinstance(value, Number):
                        setattr(e, attr, value)
                except KeyError:
                    pass

