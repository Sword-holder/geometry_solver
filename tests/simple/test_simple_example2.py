from geometry_solver.entities import Angle, Entity, Line, Point, Triangle
from geometry_solver.relationships import Collineation, SupplementaryAngle, Perpendicular
from geometry_solver import Problem, Solver, Target, TargetType


def create_problem():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')
    p_e = Point('E')
    
    line_ab = Line('AB', ends=[p_a, p_b], length=None)
    line_ac = Line('AC', ends=[p_a, p_c], length=None)
    line_ae = Line('AE', ends=[p_a, p_e], length=None)
    line_bc = Line('BC', ends=[p_b, p_c], length=None)
    line_bd = Line('BD', ends=[p_b, p_d], length=210)
    line_be = Line('BE', ends=[p_b, p_e], length=None)
    line_ce = Line('CE', ends=[p_c, p_e], length=None)
    line_de = Line('DE', ends=[p_d, p_e], length=None)

    angle_abd = Angle('ABD', sides=[line_ab, line_bd], angle=120)
    angle_dbe = Angle('DBE', sides=[line_bd, line_be], angle=None)
    angle_bde = Angle('BDE', sides=[line_bd, line_de], angle=30)
    angle_aed = Angle('AED', sides=[line_ae, line_de], angle=None)

    triangle_bde = Triangle('BDE', vertexes=[p_b, p_d, p_e], sides=[line_bd, line_be, line_de], angles=[angle_aed, angle_bde, angle_dbe], area=None)

    collineation_abce = Collineation('collineation_abce', points=[p_a, p_b, p_c, p_e])

    supplementary_angle_abd_dbe = SupplementaryAngle('supplementary_angle_abd_dbe', angle1=angle_abd, angle2=angle_dbe)

    perpendicular_ae_de = Perpendicular('perpendicular_ae_de', line1=line_ae, line2=line_de, foot_point=p_e)

    entities = []
    relationships = []
    entity_prefix = ('p_', 'line_', 'angle_', 'triangle_')
    relationship_prefix = ('collineation_', 'supplementary_angle_', 'perpendicular_')
    for name, var in locals().items():
        if name.startswith(entity_prefix):
            entities.append(var)
        elif name.startswith(relationship_prefix):
            relationships.append(var)

    entity = Entity('Example')

    entity.add_entity(*entities)

    problem = Problem(entity=entity, relationships=relationships)

    print('Create problem successfully!')
    print(problem)
    
    return problem


def create_target(problem):
    target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child('DE', type_=Line),
                    attr='length')
    return target


def test_simple_example2():
    problem = create_problem()
    target = create_target(problem)
    solver = Solver(problem)
    solver.add_target(target)
    problem = solver.solve()
    assert problem.entity.find_child('DE', type_=Line).length - (3**(1/2) / 2) * 210 < 0.00001

