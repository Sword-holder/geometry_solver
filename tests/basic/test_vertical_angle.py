import pytest

from geometry_solver.entities import Entity, Point, Line, Angle, Triangle
from geometry_solver.relationships import Relationship, OppositeVerticalAngle
from geometry_solver import Problem, Solver, Target, TargetType


def create_problem():
    p_o = Point('O')
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')
    
    line_oa = Line('OA', ends=[p_o, p_a], length=None)
    line_ob = Line('OB', ends=[p_o, p_b], length=None)
    line_oc = Line('OC', ends=[p_o, p_c], length=None)
    line_od = Line('OD', ends=[p_o, p_d], length=None)

    angle_aob = Angle('AOB', sides=[line_oa, line_ob], vertex=p_o, angle=40)
    angle_cod = Angle('COD', sides=[line_oc, line_od], vertex=p_o, angle=None)

    r = OppositeVerticalAngle('vertical angle', 
                              angle1=angle_aob, 
                              angle2=angle_cod, 
                              vertex=p_o)

    entity = Entity('Vertical angle problem')

    entity.add_entity(p_o, p_a, p_b, p_c, p_d)
    entity.add_entity(line_oa, line_ob, line_oc, line_od)
    entity.add_entity(angle_aob, angle_cod)

    problem = Problem(entity=entity, relationships=[r])

    print('Create a triangle successfully!')
    print(problem)
    
    return problem


def create_target(problem):
    target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child('COD'),
                    attr='angle')
    return target


def test_vertical_angle():
    problem = create_problem()
    target = create_target(problem)
    solver = Solver(problem)
    solver.add_target(target)
    problem = solver.solve()
    assert problem.entity.find_child('COD').angle == 40

