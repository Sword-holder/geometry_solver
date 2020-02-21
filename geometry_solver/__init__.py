from typing import List, Union

from geometry_solver._equation_solver import EquationSolver
equation_solver = EquationSolver()

from geometry_solver._theory_manager import TheoryManager
theory_manager = TheoryManager()

from geometry_solver.entities.entity import Entity
from geometry_solver.relationships.relationship import Relationship
new_objects: List[Union[Entity, Relationship]] = []

from geometry_solver.problem import Problem
from geometry_solver.solver import Solver
from geometry_solver.target import Target, TargetType

