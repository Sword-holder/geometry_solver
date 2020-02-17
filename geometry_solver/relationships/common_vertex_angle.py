from typing import List

from geometry_solver.entities import Point, Line, Angle
from geometry_solver.relationships import Relationship


class CommonVertexAngle(Relationship):

    def __init__(self, id_: str, vertex: Point, lines: List[Point]):
        super(CommonVertexAngle, self).__init__(id_)
        self.vertex = vertex
        self.lines = lines
    
    def __str__(self):
        return '(' \
            + 'CommonVertexAngle relationship ' \
            + self.id \
            + ': ' \
            + 'vertex = [' \
            + str(self.vertex) \
            + ', lines: ' \
            + ','.join([p.id for p in self.lines]) \
            + ']' \
            + ')'

