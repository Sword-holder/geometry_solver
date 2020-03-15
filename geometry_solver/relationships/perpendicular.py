from typing import List

from geometry_solver.entities.point import Point
from geometry_solver.entities.line import Line
from geometry_solver.relationships import Relationship


class Perpendicular(Relationship):

    def __init__(self, id_: str, line1: Line, line2: Line, foot_point: Point):
        super(Perpendicular, self).__init__(id_)
        self.line1 = line1
        self.line2 = line2
        self.foot_point = foot_point
    
    def __str__(self):
        return '(' \
            + 'Perpendicular relationship ' \
            + self.id \
            + ': ' \
            + 'line1: ' \
            + str(self.line1) \
            + ', line2: ' \
            + str(self.line2) \
            + ', foot_point: ' \
            + str(self.foot_point) \
            + ')'
