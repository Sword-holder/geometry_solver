from geometry_solver.entities.angle import Angle
from geometry_solver.entities.entity import Entity
from geometry_solver.entities.line import Line
from geometry_solver.entities.point import Point
from geometry_solver.entities.triangle import Triangle
from geometry_solver.solver import Solver


def create_problem():
    pa = Point('A')
    pb = Point('B')
    pc = Point('C')
    
    line_ab = Line('AB', ends=[pa, pb], length=None)
    line_bc = Line('BC', ends=[pb, pc], length=None)
    line_ac = Line('AC', ends=[pa, pc], length=None)
    
    angle_abc = Angle('ABC', sides=[line_ab, line_bc], angle=90)
    angle_acb = Angle('ACB', sides=[line_ac, line_bc], angle=40)
    angle_bac = Angle('BAC', sides=[line_ab, line_ac], angle=None)

    triangle = Triangle('ABC', 
                        vertexes=[pa, pb, pc],
                        sides=[line_ab, line_ac, line_bc], 
                        angles=[angle_abc, angle_acb, angle_bac], 
                        area=6)

    problem = Entity('basic problem')
    problem.add_entity(triangle)
    print('Create a triangle successfully!')
    print(problem)
    return problem


def main():
    problem = create_problem()
    solver = Solver(problem)
    solver.solve()


if __name__ == '__main__':
    main()
