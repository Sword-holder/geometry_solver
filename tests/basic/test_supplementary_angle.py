import pytest

from geometry_solver.entities import Entity, Point, Line, Angle, Triangle
from geometry_solver.relationships import Relationship, SupplementaryAngle
from geometry_solver import Problem, Solver, Target, TargetType


def create_problem():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')
    
    line_ba = Line('BA', ends=[p_b, p_a], length=None)
    line_bc = Line('BC', ends=[p_b, p_c], length=None)
    line_bd = Line('BD', ends=[p_b, p_d], length=None)

    angle_bac = Angle('ABD', sides=[line_ba, line_bd], vertex=p_b, angle=50)
    angle_cad = Angle('CBD', sides=[line_bc, line_bd], vertex=p_b, angle=None)

    r = SupplementaryAngle('CommonVertexAngle ABD and CBD', 
                           angle1=angle_bac,
                           angle2=angle_cad)

    entity = Entity('SupplementaryAngle problem')

    entity.add_entity(p_a, p_b, p_c, p_d)
    entity.add_entity(line_ba, line_bc, line_bd)
    entity.add_entity(angle_bac, angle_cad)

    problem = Problem(entity=entity, relationships=[r])

    print('Create a triangle successfully!')
    print(problem)
    
    return problem


def create_target(problem):
    target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child('CBD'),
                    attr='angle')
    return target


def test_supplementary_angle():
    problem = create_problem()
    target = create_target(problem)
    solver = Solver(problem)
    solver.add_target(target)
    problem = solver.solve()
    assert problem.entity.find_child('CBD').angle == 130

