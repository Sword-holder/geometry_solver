from typing import List, Union
import time

import numpy as np
from sympy import Symbol, Number

# Import Entity and Relationship.
from geometry_solver.entities.entity import Entity
from geometry_solver.relationships.relationship import Relationship
# Import utils to solve problem.
from geometry_solver import theory_manager
from geometry_solver._equation_solver import EquationSolver
from geometry_solver.problem import Problem
from geometry_solver.target import Target
from geometry_solver.common.finder import Finder
from geometry_solver.common.utils import symbol
from geometry_solver._theory_object_pair import TheoryObjectPair
from geometry_solver import equation_solver
from geometry_solver import new_objects
from geometry_solver import solving_path
# Import theories.
import geometry_solver.theories.theory_for_triangle
import geometry_solver.theories.theory_for_collineation
import geometry_solver.theories.theory_for_common_vertex_angle
import geometry_solver.theories.theory_for_opposite_vertical_angle
import geometry_solver.theories.theory_for_supplementary_angle
import geometry_solver.theories.theory_for_perpendicular
import geometry_solver.theories.theory_for_n_line_sector
import geometry_solver.theories.theory_for_n_angle_sector
import geometry_solver.theories.theory_for_parallel


class Solver(object):

    def __init__(self, problem: Problem, targets: List[Target] = []):
        self._problem = problem
        self._targets = []
        self._finder = Finder(problem.entity)

    def add_target(self, target: Target) -> None:
        self._targets.append(target)

    def solve(self) -> Problem:
        start_time = time.time()
        self._init_global_vars()
        print('solving problem....')
        theory_obj_pairs = []
        objects = list(self._problem.entity.children) \
                  + self._problem.relationships
        self._add_new_objs(objects, theory_obj_pairs)
        print('Make {} entity-theory pairs.'.format(len(theory_obj_pairs)))

        epoch = 0
        while not self._solved:
            if not theory_obj_pairs:
                break
            pair = np.random.choice(theory_obj_pairs)
            pair.deduct(self._finder)
            self._solve_equation()
            self._add_new_objs(new_objects, theory_obj_pairs)
            print('epoch {}: chose {} to search.'.format(epoch, pair))
            epoch += 1

        if self._solved:
            print('Solve problem successfully! Here are results:')
            for target in self._targets:
                print(target)
        else:
            print('The problem has no solution')
        
        print(solving_path)
        end_time = time.time()
        print('Use time: {} s'.format(end_time - start_time))
        return self._problem

    @property
    def _solved(self) -> bool:
        for target in self._targets:
            if not target.solved:
                return False
        return True

    def _solve_equation(self) -> None:
        result = equation_solver.solve()
        if result:
            self._update_all_entities(result)

    def _update_all_entities(self, result) -> None:
        for e in self._problem.entity.children:
            self._update_entity(result, e)

    def _update_entity(self, result, e: Entity) -> None:
        for attr, value in e.__dict__.items():
            # If value is unkonwn, check it.
            if value is not None:
                continue
            symbol_ = symbol(e, attr)
            if isinstance(symbol_, Symbol):
                try:
                    value = result[symbol_]
                    if isinstance(value, Number):
                        setattr(e, attr, value)
                except KeyError:
                    pass

    def _add_new_objs(self,
                      objects: List[Union[Entity, Relationship]], 
                      theory_obj_pairs: List[TheoryObjectPair]) -> None:
        for obj in objects:
            theories = theory_manager.theories_suit_to_object(obj)
            for t in theories:
                pair = TheoryObjectPair(t, obj)
                theory_obj_pairs.append(pair)

    def _init_global_vars(self):
        equation_solver.clear()
        new_objects.clear()

