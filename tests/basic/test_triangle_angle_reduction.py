import pytest

from geometry_solver.entities import Angle, Entity, Line, Point, Triangle
from geometry_solver import Problem, Solver, Target, TargetType


def create_problem():
    pa = Point('A')
    pb = Point('B')
    pc = Point('C')
    
    line_ab = Line('AB', ends=[pa, pb], length=None)
    line_bc = Line('BC', ends=[pb, pc], length=None)
    line_ac = Line('AC', ends=[pa, pc], length=None)
    
    angle_abc = Angle('ABC', sides=[line_ab, line_bc], vertex=pb, angle=90)
    angle_acb = Angle('ACB', sides=[line_ac, line_bc], vertex=pc, angle=30)
    angle_bac = Angle('BAC', sides=[line_ab, line_ac], vertex=pa, angle=None)

    triangle = Triangle('ABC', 
                        vertexes=[pa, pb, pc],
                        sides=[line_ab, line_ac, line_bc], 
                        angles=[angle_abc, angle_acb, angle_bac], 
                        area=None)
    entity = Entity('basic problem: test triangle angle reduction.')
    entity.add_entity(triangle)

    problem = Problem(entity=entity)

    print('Create a triangle successfully!')
    print(problem)
    return problem
    


def create_target(problem):
    target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child('BAC', Angle),
                    attr='angle')
    return target


def test_triangle_angle_reduction():
    problem = create_problem()
    target = create_target(problem)
    solver = Solver(problem)
    solver.add_target(target)
    problem = solver.solve()
    assert problem.entity.find_child('BAC', Angle).angle == 60

