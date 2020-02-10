from geometry_solver.entities.angle import Angle
from geometry_solver.entities.entity import Entity
from geometry_solver.entities.line import Line
from geometry_solver.entities.point import Point
from geometry_solver.entities.triangle import Triangle
from geometry_solver.solver import Solver
from geometry_solver.target import Target, TargetType


def create_triangle():
    pa = Point('A')
    pb = Point('B')
    pc = Point('C')
    
    line_ab = Line('AB', ends=[pa, pb], length=3)
    line_bc = Line('BC', ends=[pb, pc], length=4)
    line_ac = Line('AC', ends=[pa, pc], length=5)
    
    angle_abc = Angle('ABC', sides=[line_ab, line_bc], angle=None)
    angle_acb = Angle('ACB', sides=[line_ac, line_bc], angle=None)
    angle_bac = Angle('BAC', sides=[line_ab, line_ac], angle=None)

    triangle = Triangle('ABC', 
                        vertexes=[pa, pb, pc],
                        sides=[line_ab, line_bc, line_ac], 
                        angles=[angle_acb, angle_bac, angle_abc], 
                        area=6)
    return triangle


def create_problem(entity):
    problem = Entity('basic problem: test triangle sides angle reduction')
    problem.add_entity(entity)
    print('Create a triangle successfully!')
    print(problem)
    return problem


def create_target(triangle):
    target = Target(TargetType.EVALUATION,
                    entity=triangle.angles[2],
                    attr='angle')
    return target


def test_triangle_sides_angle_reduction():
    triangle = create_triangle()
    problem = create_problem(triangle)
    target = create_target(triangle)
    solver = Solver(problem)
    solver.add_target(target)
    solver.solve()

