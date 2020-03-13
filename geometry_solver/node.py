from typing import Set, List, Union

from sympy import Symbol, Number

from geometry_solver import theory_manager
from geometry_solver.entities.entity import Entity
from geometry_solver.relationships.relationship import Relationship
from geometry_solver.problem import Problem
from geometry_solver._equation_solver import EquationSolver
from geometry_solver._path import Path
from geometry_solver._theory_object_pair import TheoryObjectPair
from geometry_solver.common.finder import Finder
from geometry_solver.target import Target, TargetType
from geometry_solver.common.utils import symbol


class Node(object):

    def __init__(self, 
                 problem: Problem, 
                 equation_pool: EquationSolver, 
                 solving_path: Path, 
                 new_objects: set):
        self.problem = problem
        self.equation_pool = equation_pool
        self.solving_path = solving_path
        self.new_objects = new_objects
        self.finder = Finder(problem.entity, problem.relationships)
        self._theory_obj_pairs = self._gen_object_theory_pairs()
        self.targets_info = []

    @property
    def valid_actions(self) -> List:
        return list(self._theory_obj_pairs)

    def take_action(self, pair: TheoryObjectPair) -> bool:
        self.success = False
        pair.deduct(self)
        self._solve_equation()
        self._add_new_objs(self.new_objects, self._theory_obj_pairs)
        return self.success

    def _solve_equation(self) -> None:
        result = self.equation_pool.solve(self.solving_path)
        if result:
            self._update_all_entities(result)

    def _update_all_entities(self, result) -> None:
        for e in self.problem.entity.children:
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
                        # Deduction success if update entity.
                        setattr(e, attr, value)
                        self.success = True
                except KeyError:
                    pass

    def _gen_object_theory_pairs(self):
        theory_obj_pairs = set()
        objects = list(self.problem.entity.children) \
                       + self.problem.relationships
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


    def _target_factory(self, tg_dict):
        tg_entity = self.problem.entity.find_child(tg_dict['entity_id'], 
                type_=tg_dict['entity_type'])
        target = Target(tg_dict['target_type'],
                        entity=tg_entity,
                        attr=tg_dict['attr'])
        return target

    @property
    def solved(self) -> bool:
        for tg_dict in self.targets_info:
            target = self._target_factory(tg_dict)
            if not target.solved:
                return False
        return True

    @property
    def targets(self):
        targets_ = []
        for tg_dict in self.targets_info:
           target = self._target_factory(tg_dict)
           targets_.append(target)
        return targets_

