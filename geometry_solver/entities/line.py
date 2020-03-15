from typing import List

from geometry_solver.entities.entity import Entity
from geometry_solver.entities.point import Point


class Line(Entity):

    def __init__(self, id_: str, ends: List[Point], length: float):
        super(Line, self).__init__(id_)
        self.ends = ends
        self.length = length
        self.add_entity(*ends)

    def __str__(self):
        return '(' \
            + 'Line ' \
            + self.id \
            + ': ' \
            + 'from ' \
            + str(self.ends[0]) \
            + ', to ' \
            + str(self.ends[1]) \
            + ', length = ' \
            + str(self.length) \
            + ')'

