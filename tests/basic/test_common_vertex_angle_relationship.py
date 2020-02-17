from geometry_solver.entities import Entity, Point, Line, Angle, Triangle
from geometry_solver.relationships import Relationship, CommonVertexAngle
from geometry_solver import Problem, Solver, Target, TargetType


def create_problem():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')
    
    line_ab = Line('AB', ends=[p_a, p_b], length=None)
    line_ac = Line('AC', ends=[p_a, p_c], length=None)
    line_ad = Line('AD', ends=[p_a, p_d], length=None)

    angle_bac = Angle('BAC', sides=[line_ab, line_ac], angle=40)
    angle_cad = Angle('CAD', sides=[line_ac, line_ad], angle=30)
    angle_bad = Angle('BAD', sides=[line_ab, line_ad], angle=None)

    r = CommonVertexAngle('common vertex A', 
                          vertex=p_a,
                          lines=[line_ab, line_ac, line_ad])

    entity = Entity('CommonVertexAngle problem')

    entity.add_entity(p_a, p_b, p_c, p_d)
    entity.add_entity(line_ab, line_ac, line_ad)
    entity.add_entity(angle_bac, angle_cad, angle_bad)

    problem = Problem(entity=entity, relationships=[r])

    print('Create a triangle successfully!')
    print(problem)
    
    return problem


def create_target(problem):
    target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child('BAD'),
                    attr='angle')
    return target


def test_common_vertex_angle_relationship():
    problem = create_problem()
    target = create_target(problem)
    solver = Solver(problem)
    solver.add_target(target)
    solver.solve()

