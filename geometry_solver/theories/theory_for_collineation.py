from sympy import Symbol

from geometry_solver import theory_manager as tm
from geometry_solver.relationships.collineation import Collineation
from geometry_solver import equation_solver
from geometry_solver.common.finder import Finder


@tm.theoried(Collineation)
def collineation_line_length_sum(collineation: Collineation, 
                                 finder: Finder) -> None:
    points = collineation.points
    num_points = len(points)
    if num_points < 3:
        return
    
    equation_set = []
    for i in range(num_points):
        for j in range(i + 1, num_points):
            for k in range(j + 1, num_points):
                line_ij = finder.find_line_by_ends(points[i], points[j])
                line_jk = finder.find_line_by_ends(points[j], points[k])
                line_ik = finder.find_line_by_ends(points[i], points[k])
                for line in [line_ij, line_jk, line_ik]:
                    if line.length is None:
                        line.length = Symbol('_'.join([type(line).__name__, 
                                                       line.id]))
                equation_set.append(line_ij.length
                                    + line_jk.length 
                                    - line_ik.length)
                for line in [line_ij, line_jk, line_ik]:
                    if isinstance(line.length, Symbol):
                        line.length = None

        
    equation_solver.set_equation_group('line_length_sum_' + collineation.id,
                                       equation_set)
    result = equation_solver.solve()
    print(result)
    line = finder.find_line_by_ends(points[0], points[2])
    print(line)
    print(result[Symbol('Line_AC')])
    # for i in range(num_points):
    #     for j in range(i + 1, num_points):
    #         try:
    #             line = finder.find_line_by_ends(points[i], points[j])
    #             print(result[line])
    #         except KeyError:
    #             pass

