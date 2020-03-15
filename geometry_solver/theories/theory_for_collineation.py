from sympy import Symbol

from geometry_solver import theory_manager as tm
from geometry_solver.relationships.collineation import Collineation
from geometry_solver.common.finder import Finder
from geometry_solver.common.utils import symbol


@tm.theoried(Collineation)
def collineation_line_length_sum(collineation: Collineation, 
                                 finder: Finder) -> None:
    points = collineation.points
    num_points = len(points)
    if num_points < 3:
        return
    
    for i in range(num_points):
        for j in range(i + 1, num_points):
            for k in range(j + 1, num_points):
                line_ij = finder.find_line_by_ends(points[i], points[j])
                line_jk = finder.find_line_by_ends(points[j], points[k])
                line_ik = finder.find_line_by_ends(points[i], points[k])
                yield symbol(line_ij, 'length') \
                    + symbol(line_jk, 'length') \
                    - symbol(line_ik, 'length')

