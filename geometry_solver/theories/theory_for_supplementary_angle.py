import math

from geometry_solver import theory_manager as tm
from geometry_solver.relationships.supplementary_angle import SupplementaryAngle
from geometry_solver.common.finder import Finder
from geometry_solver.common.utils import symbol


@tm.theoried(SupplementaryAngle)
def supplementary_angle_sum(supplementary_angle: SupplementaryAngle,
                            finder: Finder) -> None:
    angle1 = supplementary_angle.angle1
    angle2 = supplementary_angle.angle2
    yield symbol(angle1, 'angle') + symbol(angle2, 'angle') - 180

