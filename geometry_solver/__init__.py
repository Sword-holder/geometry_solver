from typing import List, Union, Set

from geometry_solver._path import Path
solving_path = Path()

from geometry_solver.entities.entity import Entity
from geometry_solver.relationships.relationship import Relationship
new_objects: Set[Union[Entity, Relationship]] = set()

from geometry_solver._equation_solver import EquationSolver
equation_solver = EquationSolver()

from geometry_solver._theory_manager import TheoryManager
theory_manager = TheoryManager()

from geometry_solver.problem import Problem
from geometry_solver.solver import Solver
from geometry_solver.target import Target, TargetType

