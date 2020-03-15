from geometry_solver.relationships.n_angle_sector import NAngleSector
from geometry_solver import theory_manager as tm
from geometry_solver.common.finder import Finder
from geometry_solver.common.utils import symbol


@tm.theoried(NAngleSector)
def n_angle_sector_ratio(n_angle_sector: NAngleSector,
                         finder: Finder) -> None:
    angle = n_angle_sector.angle
    line = n_angle_sector.line
    ratio = n_angle_sector.ratio
    nearer_line = n_angle_sector.nearer_line
    if nearer_line is None:
        nearer_line = angle.sides[0]
    angle_mid = finder.find_angle_by_sides(line, nearer_line)
    yield symbol(angle, 'angle') * ratio - symbol(angle_mid, 'angle')

