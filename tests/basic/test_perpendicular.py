import pytest

from geometry_solver.entities import Entity, Point, Line, Angle, Triangle
from geometry_solver.relationships import Relationship, Perpendicular, Collineation
from geometry_solver import Problem, Solver, Target, TargetType


def create_problem():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')
    p_e = Point('E')
    
    line_ab = Line('AB', ends=[p_a, p_b], length=None)
    line_ae = Line('AE', ends=[p_a, p_e], length=None)
    line_be = Line('BE', ends=[p_b, p_e], length=None)
    line_cd = Line('CD', ends=[p_c, p_d], length=None)
    line_ce = Line('CE', ends=[p_c, p_e], length=None)
    line_de = Line('DE', ends=[p_d, p_e], length=None)

    angle_bac = Angle('AEC', sides=[line_ae, line_ce], vertex=p_e, angle=None)
    angle_aed = Angle('AED', sides=[line_ae, line_de], vertex=p_e, angle=None)
    angle_bec = Angle('BEC', sides=[line_be, line_ce], vertex=p_e, angle=None)
    angle_bed = Angle('BED', sides=[line_be, line_de], vertex=p_e, angle=None)

    col1 = Collineation('Collineation AEB', points=[p_a, p_e, p_b])
    col2 = Collineation('Collineation CED', points=[p_c, p_e, p_d])
    perp = Perpendicular('Perpendicular AB DE', line1=line_ab, line2=line_de, foot_point=p_e)

    entity = Entity('Perpendicular problem')

    entity.add_entity(p_a, p_b, p_c, p_d, p_e)
    entity.add_entity(line_ab, line_ae, line_be, line_cd, line_ce, line_de)
    entity.add_entity(angle_bac, angle_aed, angle_bec, angle_bed)

    problem = Problem(entity=entity, relationships=[col1, col2, perp])

    print('Create a triangle successfully!')
    print(problem)
    
    return problem


def create_target(problem):
    target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child('BEC'),
                    attr='angle')
    return target


def test_perpendicular():
    problem = create_problem()
    target = create_target(problem)
    solver = Solver(problem)
    solver.add_target(target)
    problem = solver.solve()
    assert problem.entity.find_child('BEC').angle == 90


########################################################################

def create_problem2():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_e = Point('E')
    
    line_ab = Line('AB', ends=[p_a, p_b], length=None)
    line_ae = Line('AE', ends=[p_a, p_e], length=None)
    line_be = Line('BE', ends=[p_b, p_e], length=None)
    line_ce = Line('CE', ends=[p_c, p_e], length=None)

    angle_bac = Angle('AEC', sides=[line_ae, line_ce], vertex=p_e, angle=None)
    angle_bec = Angle('BEC', sides=[line_be, line_ce], vertex=p_e, angle=None)

    col = Collineation('Collineation AEB', points=[p_a, p_e, p_b])
    perp = Perpendicular('Perpendicular AB CE', line1=line_ab, line2=line_ce, foot_point=p_e)

    entity = Entity('Perpendicular problem')

    entity.add_entity(p_a, p_b, p_c, p_e)
    entity.add_entity(line_ab, line_ae, line_be, line_ce)
    entity.add_entity(angle_bac, angle_bec)

    problem = Problem(entity=entity, relationships=[col, perp])

    print('Create a triangle successfully!')
    print(problem)
    
    return problem


def create_target2(problem):
    target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child('BEC'),
                    attr='angle')
    return target


def test_perpendicular2():
    problem = create_problem2()
    target = create_target2(problem)
    solver = Solver(problem)
    solver.add_target(target)
    problem = solver.solve()
    assert problem.entity.find_child('BEC').angle == 90