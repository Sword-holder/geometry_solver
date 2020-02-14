from geometry_solver.entities.angle import Angle
from geometry_solver.entities.entity import Entity
from geometry_solver.entities.line import Line
from geometry_solver.entities.point import Point
from geometry_solver.entities.triangle import Triangle
from geometry_solver.problem import Problem
from geometry_solver.solver import Solver
from geometry_solver.target import Target, TargetType


def create_problem():
    pa = Point('A')
    pb = Point('B')
    pc = Point('C')
    
    line_ab = Line('AB', ends=[pa, pb], length=None)
    line_bc = Line('BC', ends=[pb, pc], length=None)
    line_ac = Line('AC', ends=[pa, pc], length=None)
    
    angle_abc = Angle('ABC', sides=[line_ab, line_bc], angle=90)
    angle_acb = Angle('ACB', sides=[line_ac, line_bc], angle=30)
    angle_bac = Angle('BAC', sides=[line_ab, line_ac], angle=None)

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
    solver.solve()

