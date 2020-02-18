import math

from geometry_solver import theory_manager as tm
from geometry_solver.relationships.vertical_angle import VerticalAngle
from geometry_solver.common.finder import Finder
from geometry_solver.common.utils import symbol


@tm.theoried(VerticalAngle)
def vertical_angle_equation(vertical_angle: VerticalAngle,
                       finder: Finder) -> None:
    angle1 = vertical_angle.angle1
    angle2 = vertical_angle.angle2
    yield symbol(angle1, 'angle') - symbol(angle2, 'angle')

