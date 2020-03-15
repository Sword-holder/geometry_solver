from typing import List

from geometry_solver.entities.line import Line
from geometry_solver.entities.angle import Angle
from geometry_solver.relationships import Relationship


class NAngleSector(Relationship):

    def __init__(self, id_: str, angle: Angle, line: Line, ratio: float, nearer_line: Angle=None):
        super(NAngleSector, self).__init__(id_)
        self.angle = angle
        self.line = line
        self.ratio = ratio
        self.nearer_line = nearer_line
    
    def __str__(self):
        return '(' \
            + 'NAngleSector relationship ' \
            + self.id \
            + ': ' \
            + 'angle: ' \
            + str(self.angle) \
            + ', line: ' \
            + str(self.line) \
            + ', near_line = ' \
            + str(self.nearer_line) \
            + ')'

