from geometry_solver.entities import Angle, Entity, Line, Point, Triangle
from geometry_solver.relationships import Collineation, OppositeVerticalAngle, SupplementaryAngle
from geometry_solver import Problem, Solver, Target, TargetType


def create_problem():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')
    p_e = Point('E')
    p_f = Point('F')
    
    line_ab = Line('AB', ends=[p_a, p_b], length=None)
    line_ac = Line('AC', ends=[p_a, p_c], length=None)
    line_ad = Line('AD', ends=[p_a, p_d], length=None)
    line_ae = Line('AE', ends=[p_a, p_e], length=None)
    line_bc = Line('BC', ends=[p_b, p_c], length=None)
    line_bd = Line('BD', ends=[p_b, p_d], length=None)
    line_be = Line('BE', ends=[p_b, p_e], length=None)
    line_bf = Line('BF', ends=[p_b, p_f], length=None)
    line_cd = Line('CD', ends=[p_c, p_d], length=None)
    line_ce = Line('CE', ends=[p_c, p_e], length=None)
    line_cf = Line('CF', ends=[p_c, p_f], length=None)
    line_df = Line('DF', ends=[p_d, p_f], length=None)
    line_ef = Line('EF', ends=[p_e, p_f], length=None)

    angle_bac = Angle('BAC', sides=[line_ab, line_ac], vertex=p_a, angle=45)
    angle_abc = Angle('ABC', sides=[line_ab, line_bc], vertex=p_b, angle=None)
    angle_abe = Angle('ABE', sides=[line_ab, line_be], vertex=p_b, angle=40)
    angle_cbe = Angle('CBE', sides=[line_bc, line_be], vertex=p_b, angle=None)
    angle_acb = Angle('ACB', sides=[line_ac, line_ab], vertex=p_c, angle=None)
    angle_acd = Angle('ACD', sides=[line_ac, line_cd], vertex=p_c, angle=20)
    angle_bcd = Angle('BCD', sides=[line_bc, line_cd], vertex=p_c, angle=None)
    angle_bdc = Angle('BDC', sides=[line_bd, line_cd], vertex=p_d, angle=None)
    angle_adc = Angle('ADC', sides=[line_ad, line_cd], vertex=p_d, angle=None)
    angle_aeb = Angle('AEB', sides=[line_ae, line_be], vertex=p_e, angle=None)
    angle_bec = Angle('BEC', sides=[line_be, line_ce], vertex=p_e, angle=None)
    angle_bfd = Angle('BFD', sides=[line_df, line_bf], vertex=p_f, angle=None)
    angle_dfe = Angle('DFE', sides=[line_df, line_ef], vertex=p_f, angle=None)
    angle_cfe = Angle('CFE', sides=[line_cf, line_ef], vertex=p_f, angle=None)
    angle_bfc = Angle('BFC', sides=[line_bf, line_cf], vertex=p_f, angle=None)

    triangle_abc = Triangle('ABC', vertexes=[p_a, p_b, p_c], sides=[line_ab, line_bc, line_ac], angles=[angle_bac, angle_abc, angle_acb], area=None)
    triangle_abe = Triangle('ABE', vertexes=[p_a, p_b, p_e], sides=[line_ab, line_be, line_ae], angles=[angle_bac, angle_abe, angle_aeb], area=None)
    triangle_acd = Triangle('ACD', vertexes=[p_a, p_c, p_d], sides=[line_ad, line_ac, line_cd], angles=[angle_bac, angle_adc, angle_acd], area=None)
    triangle_bcd = Triangle('BCD', vertexes=[p_b, p_c, p_d], sides=[line_bc, line_bd, line_cd], angles=[angle_abc, angle_bdc, angle_bcd], area=None)
    triangle_bdf = Triangle('BDF', vertexes=[p_b, p_d, p_f], sides=[line_bd, line_bf, line_df], angles=[angle_abe, angle_bdc, angle_bfd], area=None)
    triangle_bce = Triangle('BCE', vertexes=[p_b, p_c, p_e], sides=[line_bc, line_be, line_ce], angles=[angle_cbe, angle_bec, angle_acb], area=None)
    triangle_bcf = Triangle('BCF', vertexes=[p_b, p_c, p_f], sides=[line_bc, line_bf, line_cf], angles=[angle_cbe, angle_bcd, angle_bfc], area=None)
    triangle_cef = Triangle('CEF', vertexes=[p_c, p_e, p_f], sides=[line_ce, line_cf, line_ef], angles=[angle_acd, angle_cfe, angle_bec], area=None)

    collineation_adb = Collineation('collineation_adb', points=[p_a, p_d, p_b])
    collineation_aec = Collineation('collineation_aec', points=[p_a, p_e, p_c])
    collineation_cfd = Collineation('collineation_cfd', points=[p_c, p_f, p_d])
    collineation_bfe = Collineation('collineation_bfe', points=[p_b, p_f, p_e])

    vertical_angle_bfd_cfe = OppositeVerticalAngle('vertical_angle_bfd_cfe', angle1=angle_bfd, angle2=angle_cfe, vertex=p_f)
    vertical_angle_dfe_bfc = OppositeVerticalAngle('vertical_angle_dfe_bfc', angle1=angle_dfe, angle2=angle_bfc, vertex=p_f)

    supplementary_angle_adc_bdc = SupplementaryAngle('suoolementary_angle_adc_bdc', angle1=angle_adc, angle2=angle_bdc)
    supplementary_angle_bec_aeb = SupplementaryAngle('supplementary_angle_bec_aeb', angle1=angle_bec, angle2=angle_aeb)
    supplementary_angle_bfd_bfc = SupplementaryAngle('supplementary_angle_bfd_bfc', angle1=angle_bfd, angle2=angle_bfc)
    supplementary_angle_dfe_cfe = SupplementaryAngle('supplementary_angle_dfe_cfe', angle1=angle_dfe, angle2=angle_cfe)
    supplementary_angle_bfd_dfe = SupplementaryAngle('supplementary_angle_bfd_dfe', angle1=angle_bfd, angle2=angle_dfe)
    supplementary_angle_bfc_cfe = SupplementaryAngle('supplementary_angle_bfc_cfe', angle1=angle_bfc, angle2=angle_cfe)

    entities = []
    relationships = []
    for name, var in locals().items():
        if name.startswith(('p', 'line', 'angle', 'triangle')):
            entities.append(var)
        elif name.startswith(('collineation', 'vertical_angle', 'supplementary_angle')):
            relationships.append(var)

    entity = Entity('Example')

    entity.add_entity(*entities)

    problem = Problem(entity=entity, relationships=relationships)

    print('Create problem successfully!')
    print(problem)
    
    return problem


def create_target1(problem):
    target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child('CFE', type_=Angle),
                    attr='angle')
    return target

def create_target2(problem):
    target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child('BDC', type_=Angle),
                    attr='angle')
    return target


def test_simple_example():
    problem = create_problem()
    target1 = create_target1(problem)
    target2 = create_target2(problem)
    solver = Solver(problem)
    solver.add_target(target1)
    solver.add_target(target2)
    problem = solver.solve()
    assert problem.entity.find_child('CFE', type_=Angle).angle == 75
    assert problem.entity.find_child('BDC', type_=Angle).angle == 65

