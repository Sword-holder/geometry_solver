from geometry_solver.entities import Angle, Entity, Line, Point, Triangle
from geometry_solver.relationships import Collineation, OppositeVerticalAngle, SupplementaryAngle
from geometry_solver import Problem, Solver, Target, TargetType


def create_problem():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')
    p_e = Point('E')
    
    line_ab = Line('AB', ends=[p_a, p_b], length=None)
    line_ac = Line('AC', ends=[p_a, p_c], length=None)
    line_ad = Line('AD', ends=[p_a, p_d], length=None)
    line_ae = Line('AE', ends=[p_a, p_e], length=None)
    line_bc = Line('BC', ends=[p_b, p_c], length=None)
    line_bd = Line('BD', ends=[p_b, p_d], length=None)
    line_be = Line('BE', ends=[p_b, p_e], length=None)
    line_ce = Line('CE', ends=[p_c, p_e], length=None)
    line_de = Line('DE', ends=[p_d, p_e], length=None)

    angle_bac = Angle('BAC', sides=[line_ab, line_ac], vertex=p_a, angle=60)
    angle_bad = Angle('BAD', sides=[line_ab, line_ad], vertex=p_a, angle=90)
    angle_cad = Angle('CAD', sides=[line_ac, line_ad], vertex=p_a, angle=None)
    angle_abc = Angle('ABC', sides=[line_ab, line_bc], vertex=p_b, angle=90)
    angle_abd = Angle('ABD', sides=[line_ab, line_bd], vertex=p_b, angle=45)
    angle_cbd = Angle('CBD', sides=[line_bc, line_bd], vertex=p_b, angle=None)
    angle_acb = Angle('ACB', sides=[line_ac, line_ab], vertex=p_c, angle=30)
    angle_adb = Angle('ADB', sides=[line_ad, line_bd], vertex=p_d, angle=45)
    angle_aeb = Angle('AEB', sides=[line_ae, line_be], vertex=p_e, angle=None)
    angle_aed = Angle('AED', sides=[line_ae, line_de], vertex=p_e, angle=None)
    angle_bec = Angle('BEC', sides=[line_be, line_ce], vertex=p_e, angle=None)
    angle_ced = Angle('CED', sides=[line_ce, line_de], vertex=p_e, angle=None)

    triangle_abc = Triangle('ABC', vertexes=[p_a, p_b, p_c], sides=[line_ab, line_bc, line_ac], angles=[angle_bac, angle_abc, angle_acb], area=None)
    triangle_abe = Triangle('ABE', vertexes=[p_a, p_b, p_e], sides=[line_ab, line_be, line_ae], angles=[angle_bac, angle_abd, angle_aeb], area=None)
    triangle_abd = Triangle('ABD', vertexes=[p_a, p_b, p_d], sides=[line_ab, line_bd, line_ad], angles=[angle_bad, angle_abd, angle_adb], area=None)
    triangle_ade = Triangle('ADE', vertexes=[p_a, p_d, p_e], sides=[line_ad, line_ae, line_de], angles=[angle_cad, angle_aed, angle_adb], area=None)
    triangle_bce = Triangle('BCE', vertexes=[p_b, p_c, p_e], sides=[line_bc, line_be, line_ce], angles=[angle_cbd, angle_bec, angle_acb], area=None)

    collineation_aec = Collineation('collineation_aec', points=[p_a, p_e, p_c])
    collineation_bed = Collineation('collineation_bed', points=[p_b, p_e, p_d])

    vertical_angle_bfd_cfe = OppositeVerticalAngle('vertical_angle_aed_bec', angle1=angle_aed, angle2=angle_bec, vertex=p_e)
    vertical_angle_dfe_bfc = OppositeVerticalAngle('vertical_angle_aeb_ced', angle1=angle_aeb, angle2=angle_ced, vertex=p_e)

    supplementary_angle_adc_bdc = SupplementaryAngle('suoolementary_angle_aeb_bec', angle1=angle_aeb, angle2=angle_bec)
    supplementary_angle_bfd_bfc = SupplementaryAngle('supplementary_angle_aeb_aed', angle1=angle_aeb, angle2=angle_aed)
    supplementary_angle_dfe_cfe = SupplementaryAngle('supplementary_angle_aed_ced', angle1=angle_aed, angle2=angle_ced)
    supplementary_angle_bfd_dfe = SupplementaryAngle('supplementary_angle_ced_bec', angle1=angle_ced, angle2=angle_bec)

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


def create_target(problem):
    target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child('AEB', type_=Angle),
                    attr='angle')
    return target


def test_simple_example1():
    problem = create_problem()
    target = create_target(problem)
    solver = Solver(problem)
    solver.add_target(target)
    problem = solver.solve()
    assert problem.entity.find_child('AEB', type_=Angle).angle == 75

