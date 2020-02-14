from geometry_solver import theory_manager as tm
from geometry_solver.relationships.collineation import Collineation


@tm.theoried(Collineation)
def collineation_line_length_sum(collineation: Collineation) -> None:
    points = collineation.points
    num_points = len(points)
    if num_points < 3:
        return
    for i in range(num_points):
        for j in range(i + 1, num_points):
            for k in range(j + 1, num_points):
                print(points[i].id + points[j].id + ' + ' + points[j].id + points[k].id + ' = ' + points[i].id + points[k].id)

