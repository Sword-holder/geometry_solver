import pytest

from geometry_solver.entities import Entity, Point, Line, Angle, Triangle
from geometry_solver.relationships import Relationship, SimilarTriangle
from geometry_solver import Problem, Solver, Target, TargetType


def create_problem():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')
    p_e = Point('E')
    p_f = Point('F')
    
    line_ab = Line('AB', ends=[p_a, p_b], length=2)
    line_ac = Line('AC', ends=[p_a, p_c], length=None)
    line_bc = Line('BC', ends=[p_b, p_c], length=4)
    line_de = Line('DE', ends=[p_d, p_e], length=1)
    line_df = Line('DF', ends=[p_d, p_f], length=None)
    line_ef = Line('EF', ends=[p_e, p_f], length=None)

    angle_abc = Angle('ABC', sides=[line_ab, line_bc], vertex=p_b, angle=60)
    angle_acb = Angle('ACB', sides=[line_ac, line_bc], vertex=p_c, angle=30)
    angle_bac = Angle('BAC', sides=[line_ab, line_ac], vertex=p_a, angle=90)
    angle_def = Angle('DEF', sides=[line_de, line_ef], vertex=p_e, angle=60)
    angle_dfe = Angle('DFE', sides=[line_df, line_ef], vertex=p_f, angle=30)
    angle_edf = Angle('EDF', sides=[line_de, line_df], vertex=p_d, angle=90)

    triangle1 = Triangle('ABC', vertexes=[p_a, p_b, p_c], sides=[line_ab, line_ac, line_bc], angles=[angle_acb, angle_abc, angle_bac], area=None)
    triangle2 = Triangle('DEF', vertexes=[p_d, p_e, p_f], sides=[line_de, line_df, line_ef], angles=[angle_dfe, angle_def, angle_edf], area=None)

    entity = Entity('Similar triangle problem')

    entity.add_entity(p_a, p_b, p_c, p_d, p_e, p_f)
    entity.add_entity(line_ab, line_ac, line_bc, line_de, line_df, line_ef)
    entity.add_entity(angle_abc, angle_acb, angle_bac, angle_def, angle_dfe, angle_edf)
    entity.add_entity(triangle1, triangle2)

    problem = Problem(entity=entity)

    print('Create a triangle successfully!')
    print(problem)
    
    return problem


def create_target(problem):
    target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child('EF', Line),
                    attr='length')
    return target


def test_similar_triangle():
    problem = create_problem()
    target = create_target(problem)
    solver = Solver(problem)
    solver.add_target(target)
    problem = solver.solve()
    assert abs(problem.entity.find_child('EF', Line).length - 2) < 0.000001

