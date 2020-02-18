import math

from geometry_solver import theory_manager as tm
from geometry_solver.relationships.supplementary_angle import SupplementaryAngle
from geometry_solver.common.finder import Finder
from geometry_solver import equation_solver
from geometry_solver.common.utils import to_symbol


@tm.theoried(SupplementaryAngle)
def vertical_angle_equation(supplementary_angle: SupplementaryAngle,
                            finder: Finder) -> None:
    angle1 = supplementary_angle.angle1
    angle2 = supplementary_angle.angle2
    equation_set = [to_symbol(angle1, 'angle') 
                    + to_symbol(angle2, 'angle') 
                    - 180]
    group_key = 'vertical_angle_equation_' + supplementary_angle.id
    equation_solver.set_equation_group(group_key, equation_set)

