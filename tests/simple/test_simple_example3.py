from geometry_solver.entities import Angle, Entity, Line, Point, Triangle
from geometry_solver.relationships import Collineation, SupplementaryAngle, Perpendicular, NAngleSector, CommonVertexAngle
from geometry_solver import Problem, Solver, Target, TargetType


def create_problem():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')
    p_e = Point('F')
    
    line_ab = Line('AB', ends=[p_a, p_b], length=None)
    line_ac = Line('AC', ends=[p_a, p_c], length=None)
    line_ad = Line('AD', ends=[p_a, p_d], length=None)
    line_ae = Line('AF', ends=[p_a, p_e], length=None)
    line_bc = Line('BC', ends=[p_b, p_c], length=None)
    line_bd = Line('BD', ends=[p_b, p_d], length=None)
    line_be = Line('BF', ends=[p_b, p_e], length=None)
    line_cd = Line('CD', ends=[p_c, p_d], length=None)
    line_ce = Line('CF', ends=[p_c, p_e], length=None)
    line_de = Line('DF', ends=[p_d, p_e], length=None)

    angle_bae = Angle('BAF', sides=[line_ab, line_ae], vertex=p_a, angle=None)
    angle_bad = Angle('BAD', sides=[line_ab, line_ad], vertex=p_a, angle=None)
    angle_bac = Angle('BAC', sides=[line_ab, line_ac], vertex=p_a, angle=None)
    angle_dae = Angle('DAF', sides=[line_ad, line_ae], vertex=p_a, angle=None)
    angle_cae = Angle('CAF', sides=[line_ac, line_ae], vertex=p_a, angle=None)
    angle_cad = Angle('CAD', sides=[line_ad, line_cd], vertex=p_a, angle=None)
    angle_abc = Angle('ABC', sides=[line_ab, line_bc], vertex=p_b, angle=36)
    angle_acb = Angle('ACB', sides=[line_ac, line_bc], vertex=p_c, angle=76)
    angle_adc = Angle('ADC', sides=[line_ad, line_cd], vertex=p_d, angle=None)
    angle_adb = Angle('ADB', sides=[line_ad, line_bd], vertex=p_d, angle=None)
    angle_aeb = Angle('AFB', sides=[line_ae, line_be], vertex=p_e, angle=None)
    angle_aec = Angle('AFC', sides=[line_ae, line_ce], vertex=p_e, angle=None)

    triangle_abc = Triangle('ABC', vertexes=[p_a, p_b, p_c], sides=[line_ab, line_ac, line_bc], angles=[angle_acb, angle_abc, angle_bac], area=None)
    triangle_abd = Triangle('ABD', vertexes=[p_a, p_b, p_d], sides=[line_ab, line_ad, line_bd], angles=[angle_adb, angle_abc, angle_bad], area=None)
    triangle_abe = Triangle('ABF', vertexes=[p_a, p_b, p_e], sides=[line_ab, line_ae, line_be], angles=[angle_aeb, angle_abc, angle_bae], area=None)
    triangle_acd = Triangle('ACD', vertexes=[p_a, p_c, p_d], sides=[line_ac, line_ad, line_cd], angles=[angle_adc, angle_acb, angle_cad], area=None)
    triangle_ace = Triangle('ACF', vertexes=[p_a, p_c, p_e], sides=[line_ac, line_ae, line_ce], angles=[angle_aec, angle_acb, angle_cae], area=None)
    triangle_ade = Triangle('ADF', vertexes=[p_a, p_d, p_e], sides=[line_ad, line_ae, line_de], angles=[angle_aec, angle_adb, angle_dae], area=None)
    

    collineation_bedc = Collineation('collineation_bedc', points=[p_b, p_e, p_d, p_c])

    supplementary_angle_aeb_aec = SupplementaryAngle('supplementary_angle_aeb_aec', angle1=angle_aeb, angle2=angle_aec)
    supplementary_angle_adb_adc = SupplementaryAngle('supplementary_angle_adb_adc', angle1=angle_adb, angle2=angle_adc)

    perpendicular_ad_bd = Perpendicular('perpendicular_ad_bd', line1=line_ad, line2=line_bd, foot_point=p_d)

    n_angle_sector_bac_ae = NAngleSector('n_angle_sector_bac_ae', angle=angle_bac, line=line_ae, ratio=1/2)

    common_vertex_angle_a = CommonVertexAngle('common_vertex_angle_a', vertex=p_a, lines=[line_ab, line_ae, line_ad, line_ac])

    entities = []
    relationships = []
    entity_prefix = ('p_', 'line_', 'angle_', 'triangle_')
    relationship_prefix = ('collineation_', 'supplementary_angle_', 'perpendicular_', 'n_angle_sector_', 'n_line_sector_')
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
                    entity=problem.entity.find_child('DAF', type_=Angle),
                    attr='angle')
    return target


def test_simple_example3():
    problem = create_problem()
    target = create_target(problem)
    solver = Solver(problem)
    solver.add_target(target)
    problem = solver.solve()
    assert problem.entity.find_child('DAF', type_=Angle).angle == 20

