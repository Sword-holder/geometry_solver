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
    angle = finder.find_angle_by_sides(line1, line2)
    angle.angle = 90

