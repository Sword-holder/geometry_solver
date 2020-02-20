from typing import List

from geometry_solver.entities.point import Point
from geometry_solver.entities.line import Line
from geometry_solver.relationships import Relationship


class NLineSector(Relationship):

    def __init__(self, id_: str, line: Line, point: Point, ratio: float, nearer_point: Point=None):
        super(NLineSector, self).__init__(id_)
        self.line = line
        self.point = point
        self.ratio = ratio
        self.nearer_point = nearer_point
    
    def __str__(self):
        return '(' \
            + 'NLineSector relationship ' \
            + self.id \
            + ': ' \
            + 'line: ' \
            + str(self.line) \
            + ', point: ' \
            + str(self.point) \
            + ', near_point = ' \
            + str(self.nearer_point) \
            + ')'

