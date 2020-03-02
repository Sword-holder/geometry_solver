from geometry_solver.relationships.n_line_sector import NLineSector
from geometry_solver import theory_manager as tm
from geometry_solver.common.finder import Finder
from geometry_solver.common.utils import symbol


@tm.theoried(NLineSector)
def n_line_sector_ratio(n_line_sector: NLineSector,
                        finder: Finder) -> None:
    line = n_line_sector.line
    ratio = n_line_sector.ratio
    A = n_line_sector.nearer_point
    if A is None:
        A = line.ends[0]
    B = n_line_sector.point
    AB = finder.find_line_by_ends(A, B)
    yield symbol(line, 'length') * ratio - symbol(AB, 'length')

