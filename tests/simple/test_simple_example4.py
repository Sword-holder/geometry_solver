from geometry_solver.entities import Angle, Entity, Line, Point, Triangle
from geometry_solver.relationships import Collineation, SupplementaryAngle, Perpendicular, NLineSector, CommonVertexAngle
from geometry_solver import Problem, Solver, Target, TargetType


def create_problem():
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_m = Point('M')
    p_n = Point('N')
    
    line_ab = Line('AB', ends=[p_a, p_b], length=5)
    line_ac = Line('AC', ends=[p_a, p_c], length=5)
    line_an = Line('AN', ends=[p_a, p_n], length=None)
    line_bc = Line('BC', ends=[p_b, p_c], length=6)
    line_bm = Line('BM', ends=[p_b, p_m], length=None)
    line_cm = Line('CM', ends=[p_c, p_m], length=None)
    line_cn = Line('CN', ends=[p_c, p_n], length=None)
    line_mn = Line('MN', ends=[p_m, p_n], length=None)

    angle_bac = Angle('BAC', sides=[line_ab, line_ac], angle=None)
    angle_abc = Angle('ABC', sides=[line_ab, line_bc], angle=None)
    angle_acb = Angle('ACB', sides=[line_ac, line_bc], angle=None)
    angle_anm = Angle('ANM', sides=[line_an, line_mn], angle=None)
    angle_cnm = Angle('CNM', sides=[line_cn, line_mn], angle=None)
    angle_bmn = Angle('BMN', sides=[line_bm, line_mn], angle=None)
    angle_cmn = Angle('CMN', sides=[line_cm, line_mn], angle=None)

    triangle_abc = Triangle('ABC', vertexes=[p_a, p_b, p_c], sides=[line_ab, line_ac, line_bc], angles=[angle_acb, angle_abc, angle_bac], area=None)
    triangle_cmn = Triangle('CMN', vertexes=[p_c, p_m, p_n], sides=[line_cm, line_cn, line_mn], angles=[angle_cnm, angle_cmn, angle_acb], area=None)

    collineation_bmc = Collineation('collineation_bmc', points=[p_b, p_m, p_c])
    collineation_anc = Collineation('collineation_anc', points=[p_a, p_n, p_c])

    supplementary_angle_amn_cmn = SupplementaryAngle('supplementary_angle_amn_cmn', angle1=angle_bmn, angle2=angle_cmn)
    supplementary_angle_anm_cnm = SupplementaryAngle('supplementary_angle_anm_cnm', angle1=angle_anm, angle2=angle_cnm)

    perpendicular_mn_cn = Perpendicular('perpendicular_mn_cn', line1=line_mn, line2=line_cn, foot_point=p_n)

    n_line_sector_bc_m = NLineSector('n_angle_sector_bac_ae', line=line_bc, point=p_m, ratio=1/2)

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
                    entity=problem.entity.find_child('MN', type_=Line),
                    attr='length')
    return target


def test_simple_example4():
    problem = create_problem()
    target = create_target(problem)
    solver = Solver(problem)
    solver.add_target(target)
    problem = solver.solve()
    # assert problem.entity.find_child('DAE', type_=Angle).angle == 20

