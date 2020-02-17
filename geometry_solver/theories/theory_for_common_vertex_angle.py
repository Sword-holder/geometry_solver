from geometry_solver.relationships.common_vertex_angle import CommonVertexAngle
from geometry_solver import theory_manager as tm
from geometry_solver import equation_solver
from geometry_solver.common.finder import Finder
from geometry_solver.common.utils import to_symbol


@tm.theoried(CommonVertexAngle)
def common_vertex_angle_sum(common_vertex_angle: CommonVertexAngle,
                            finder: Finder) -> None:
    lines = common_vertex_angle.lines
    num_lines = len(lines)

    equation_set = []
    for i in range(num_lines):
        for j in range(i + 1, num_lines):
            for k in range(j + 1, num_lines):
                angle_ij = finder.find_angle_by_sides(lines[i], lines[j])
                angle_jk = finder.find_angle_by_sides(lines[j], lines[k])
                angle_ik = finder.find_angle_by_sides(lines[i], lines[k])
                equation_set.append(to_symbol(angle_ij, 'angle') 
                                    + to_symbol(angle_jk, 'angle') 
                                    - to_symbol(angle_ik, 'angle'))
    
    group_key = 'common_vertex_angle_sum_' + common_vertex_angle.id
    equation_solver.set_equation_group(group_key, equation_set)

