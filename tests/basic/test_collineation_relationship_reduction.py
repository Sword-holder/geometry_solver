import pytest

from geometry_solver.entities import Angle, Entity, Line, Point, Triangle
from geometry_solver.relationships import Relationship, Collineation
from geometry_solver import Problem, Solver, Target, TargetType


def create_problem():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    
    line_ab = Line('AB', ends=[p_a, p_b], length=1)
    line_bc = Line('BC', ends=[p_b, p_c], length=2)
    line_ac = Line('AC', ends=[p_a, p_c], length=None)
    
    r_collineation = Collineation('ABC collineation', [p_a, p_b, p_c])

    entity = Entity('Collineation problem')

    entity.add_entity(p_a, p_b, p_c)
    entity.add_entity(line_ab, line_bc, line_ac)

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
    problem = solver.solve()
    assert problem.entity.find_child('AC').length == 3

