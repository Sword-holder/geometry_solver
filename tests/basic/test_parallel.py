import pytest

from geometry_solver.entities import Entity, Point, Line, Angle, Triangle
from geometry_solver.relationships import Relationship, Parallel, Collineation
from geometry_solver import Problem, Solver, Target, TargetType


def create_problem():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')
    p_e = Point('E')
    
    line_ab = Line('AB', ends=[p_a, p_b], length=None)
    line_ae = Line('AE', ends=[p_a, p_e], length=None)
    line_eb = Line('EB', ends=[p_e, p_b], length=None)
    line_cd = Line('CD', ends=[p_c, p_d], length=None)
    line_ec = Line('EC', ends=[p_e, p_c], length=None)

    angle_aec = Angle('AEC', sides=[line_ae, line_ec], angle=None)
    angle_dce = Angle('DCE', sides=[line_ec, line_cd], angle=30)

    r1 = Collineation('Collineation AEB', points=[p_a, p_e, p_b])
    r2 = Parallel('Parallel AB and CD', line1=line_ab, line2=line_cd, colllineation1=r1)

    entity = Entity('Parallel problem')

    entity.add_entity(p_a, p_b, p_c, p_d, p_e)
    entity.add_entity(line_ab, line_ae, line_eb, line_cd, line_ec)
    entity.add_entity(angle_aec, angle_dce)

    problem = Problem(entity=entity, relationships=[r1, r2])

    print('Create a triangle successfully!')
    print(problem)
    
    return problem


def create_target(problem):
    target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child('AEC'),
                    attr='angle')
    return target


def test_parallel():
    problem = create_problem()
    target = create_target(problem)
    solver = Solver(problem)
    solver.add_target(target)
    problem = solver.solve()
    assert problem.entity.find_child('AEC').angle == 30

