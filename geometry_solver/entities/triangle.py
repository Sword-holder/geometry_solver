from typing import List

from geometry_solver.entities.area import Area
from geometry_solver.entities.point import Point
from geometry_solver.entities.line import Line
from geometry_solver.entities.angle import Angle


class Triangle(Area):

    def __init__(self, id_, 
                 vertexes: List[Point], 
                 sides: List[Line], 
                 angles: List[Angle], 
                 area: float):
        super(Triangle, self).__init__(id_, vertexes, sides, angles, area)

    def __str__(self) -> str:
        return '(' \
            + 'Triangle ' \
            + self.id \
            + ': ' \
            + '\n\tvertexes: ' \
            + ' '.join(list(map(str, self.vertexes))) \
            + '\n\tside1: ' \
            + str(self.sides[0]) \
            + '\n\tside2: ' \
            + str(self.sides[1]) \
            + '\n\tside3: ' \
            + str(self.sides[2]) \
            + '\n\tangle1: ' \
            + '\n\t'.join(str(self.angles[0]).split('\n')) \
            + '\n\tangle2: ' \
            + '\n\t'.join(str(self.angles[1]).split('\n')) \
            + '\n\tangle3: ' \
            + '\n\t'.join(str(self.angles[2]).split('\n')) \
            + '\n\tarea = ' \
            + str(self.area) \
            + ')'

