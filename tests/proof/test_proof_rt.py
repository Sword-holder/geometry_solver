import pytest

from geometry_solver.entities import Angle, Entity, Line, Point, Triangle
from geometry_solver.relationships import Relationship, Collineation
from geometry_solver import Problem, Solver, Target, TargetType
from geometry_solver.state import TriangleState


def create_problem():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    
    line_ab = Line('AB', ends=[p_a, p_b], length=4)
    line_bc = Line('BC', ends=[p_b, p_c], length=3)
    line_ac = Line('AC', ends=[p_a, p_c], length=5)

    angle_abc = Angle('ABC', sides=[line_ab, line_bc], vertex=p_b, angle=None)
    angle_bac = Angle('BAC', sides=[line_ab, line_ac], vertex=p_a, angle=None)
    angle_acb = Angle('ACB', sides=[line_ac, line_bc], vertex=p_c, angle=None)

    triangle_abc = Triangle('ABC', vertexes=[p_a, p_b, p_c], sides=[line_ab, line_bc, line_ac], angles=[angle_acb, angle_bac, angle_abc], area=None)

    entity = Entity('Proof right triangle problem')

    entity.add_entity(p_a, p_b, p_c)
    entity.add_entity(line_ab, line_bc, line_ac)
    entity.add_entity(triangle_abc)

    problem = Problem(entity=entity)

    print('Create a triangle successfully!')
    print(problem)
    
    return problem


def create_target(problem):
    target = Target(TargetType.PROOF,
        entity=problem.entity.find_child('ABC', type_=Triangle).state,
        attr='rt_state',
        value=TriangleState.RT.rt)
    return target


def test_proof_rt():
    # problem = create_problem()
    # target = create_target(problem)
    # solver = Solver(problem)
    # solver.add_target(target)
    # problem = solver.solve()
    # state = problem.entity.find_child('ABC', type_=Triangle).state
    # assert state.rt_state == TriangleState.RT.rt
    pass

