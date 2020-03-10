import math

from geometry_solver import theory_manager as tm
from geometry_solver.relationships.perpendicular import Perpendicular
from geometry_solver.common.finder import Finder
from geometry_solver.common.utils import symbol


@tm.theoried(Perpendicular)
def perpendicular_angle(perpendicular: Perpendicular,
                       finder: Finder) -> None:
    line1 = perpendicular.line1
    line2 = perpendicular.line2
    # Extend line first.
    line1 = finder.extend_line(line1)
    line2 = finder.extend_line(line2)
    # Find intersection.
    intersection = finder.find_lines_intersection(line1, line2)
    if len(intersection) != 1:
        raise Exception('Perpendicular relationship is suppposed to include '
                        'two perpendicular line. Except 1, got {}.'
                        .format(len(intersection)))
    cross_p = intersection[0]
    for p1 in line1.ends:
        for p2 in line2.ends:
            if p1 == cross_p or p2 == cross_p:
                continue
            line1_ = finder.find_line_by_ends(p1, cross_p)
            line2_ = finder.find_line_by_ends(p2, cross_p)
            angle = finder.find_angle_by_sides(line1_, line2_)
            angle.angle = 90

