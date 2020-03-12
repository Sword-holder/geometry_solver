from typing import Set, List, Union

from geometry_solver import theory_manager
from geometry_solver.entities.entity import Entity
from geometry_solver.relationships.relationship import Relationship
from geometry_solver.problem import Problem
from geometry_solver._equation_solver import EquationSolver
from geometry_solver._path import Path
from geometry_solver._theory_object_pair import TheoryObjectPair
from geometry_solver.common.finder import Finder


class Node(object):

    def __init__(self, 
                 problem: Problem, 
                 equation_pool: EquationSolver, 
                 solving_path: Path, 
                 new_objects: set,
                 finder: Finder):
        self._problem = problem
        self._equation_pool = equation_pool
        self._solving_path = solving_path
        self._new_objects = new_objects
        self._finder = finder
        self._theory_obj_pairs = self._gen_object_theory_pairs()

    def valid_actions(self):
        return self._theory_obj_pairs

    def take_action(self, pair: TheoryObjectPair):
        pair.deduct(self._finder)
        # self._solve_equation()

    # def _solve_equation(self) -> None:
    #     result = equation_solver.solve()
    #     if result:
    #         self._update_all_entities(result)

    # def _update_all_entities(self, result) -> None:
    #     for e in self._problem.entity.children:
    #         self._update_entity(result, e)

    # def _update_entity(self, result, e: Entity) -> None:
    #     for attr, value in e.__dict__.items():
    #         # If value is unkonwn, check it.
    #         if value is not None:
    #             continue
    #         symbol_ = symbol(e, attr)
    #         if isinstance(symbol_, Symbol):
    #             try:
    #                 value = result[symbol_]
    #                 if isinstance(value, Number):
    #                     setattr(e, attr, value)
    #             except KeyError:
    #                 pass

    def _gen_object_theory_pairs(self):
        theory_obj_pairs = set()
        objects = list(self._problem.entity.children) \
                       + self._problem.relationships
        self._add_new_objs(objects, theory_obj_pairs)
        return theory_obj_pairs


    def _add_new_objs(self,
                      objects: List[Union[Entity, Relationship]], 
                      theory_obj_pairs: Set[TheoryObjectPair]) -> None:
        for obj in objects:
            theories = theory_manager.theories_suit_to_object(obj)
            for t in theories:
                pair = TheoryObjectPair(t, obj)
                theory_obj_pairs.add(pair)


