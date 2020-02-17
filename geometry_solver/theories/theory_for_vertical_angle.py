import math

from geometry_solver import theory_manager as tm
from geometry_solver.relationships.vertical_angle import VerticalAngle
from geometry_solver.common.finder import Finder
from geometry_solver import equation_solver
from geometry_solver.common.utils import to_symbol


@tm.theoried(VerticalAngle)
def vertical_angle_equation(vertical_angle: VerticalAngle,
                       finder: Finder) -> None:
    angle1 = vertical_angle.angle1
    angle2 = vertical_angle.angle2
    equation_set = [to_symbol(angle1, 'angle') - to_symbol(angle2, 'angle')]
    group_key = 'vertical_angle_equation_' + vertical_angle.id
    equation_solver.set_equation_group(group_key, equation_set)

