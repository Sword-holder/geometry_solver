from geometry_solver.entities.angle import Angle
from geometry_solver.entities.entity import Entity
from geometry_solver.entities.line import Line
from geometry_solver.entities.point import Point
from geometry_solver.entities.triangle import Triangle
from geometry_solver.relationships.relationship import Relationship
from geometry_solver.relationships.collineation import Collineation
from geometry_solver.problem import Problem
from geometry_solver.solver import Solver
from geometry_solver.target import Target, TargetType


def create_problem():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    
    line_ab = Line('AB', ends=[p_a, p_b], length=1)
    line_bc = Line('BC', ends=[p_b, p_c], length=2)
    line_ac = Line('AC', ends=[p_a, p_c], length=None)
    
    r_collineation = Collineation('ABC collineation', [p_a, p_b, p_c])

    entity = Entity('Collineation problem')

    entity.add_entities([p_a, p_b, p_c])
    entity.add_entities([line_ab, line_bc, line_ac])

    problem = Problem(entity=entity, relationships=[r_collineation])

    print('Create a triangle successfully!')
    print(problem)
    
    return problem


def create_target(problem):
    target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child('AC'),
                    attr='length')
    return target


def test_collineation_relationship_reduction():
    problem = create_problem()
    target = create_target(problem)
    solver = Solver(problem)
    solver.add_target(target)
    solver.solve()

