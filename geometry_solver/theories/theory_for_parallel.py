import math
import itertools

from geometry_solver import theory_manager as tm
from geometry_solver.entities.point import Point
from geometry_solver.relationships.collineation import Collineation
from geometry_solver.relationships.parallel import Parallel
from geometry_solver.common.finder import Finder
from geometry_solver.common.utils import symbol


def _get_angles_fixed_ends(col1: Collineation, 
                           col2: Collineation,
                           end1: Point,
                           end2: Point,
                           finder: Finder):
    for top_p in col1.points:
        if id(top_p) == id(end1):
            continue
        for bottom_p in col2.points:
            if id(bottom_p) == id(end2):
                continue
            top_line = finder.find_line_by_ends(end1, top_p)
            middle_line = finder.find_line_by_ends(top_p, bottom_p)
            bottom_line = finder.find_line_by_ends(bottom_p, end2)
            # print('top line=============', top_line)
            # print('middle line============', middle_line)
            # print('bottom line============', bottom_line)
            if top_line is None \
                    or middle_line is None \
                    or bottom_line is None:
                continue
            top_angle = finder.find_angle_by_sides(top_line, middle_line)
            bottom_angle = finder.find_angle_by_sides(bottom_line, middle_line)
            # print('top angle==============', top_angle)
            # print('bottom angle==============', bottom_angle)
            if top_angle is not None and bottom_angle is not None:
                yield top_angle, bottom_angle


def _find_alternate_angels(col1: Collineation, 
                           col2: Collineation, 
                           finder: Finder):
    top_left = col1.points[0]
    top_right = col1.points[-1]
    bottom_left = col2.points[0]
    bottom_right = col2.points[-1]

    g1 = _get_angles_fixed_ends(col1, col2, top_left, bottom_right, finder)
    g2 = _get_angles_fixed_ends(col1, col2, top_right, bottom_left, finder)
    return itertools.chain(g1, g2)


@tm.theoried(Parallel)
def perpendicular_angle(parallel: Parallel,
                       finder: Finder) -> None:
    col1 = parallel.colllineation1
    col2 = parallel.colllineation2
    if col1 is None:
        col1 = Collineation(parallel.line1.id, parallel.line1.ends)
    if col2 is None:
        col2 = Collineation(parallel.line2.id, parallel.line2.ends)

    for angle1, angle2 in _find_alternate_angels(col1, col2, finder):
        yield symbol(angle1, 'angle') - symbol(angle2, 'angle')

    

