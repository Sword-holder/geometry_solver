import math

from geometry_solver import theory_manager as tm
from geometry_solver.relationships.opposite_vertical_angle import OppositeVerticalAngle
from geometry_solver.common.finder import Finder
from geometry_solver.common.utils import symbol


@tm.theoried(OppositeVerticalAngle)
def vertical_angle_equality(opposite_vertical_angle: OppositeVerticalAngle,
                            finder: Finder) -> None:
    angle1 = opposite_vertical_angle.angle1
    angle2 = opposite_vertical_angle.angle2
    yield symbol(angle1, 'angle') - symbol(angle2, 'angle')

