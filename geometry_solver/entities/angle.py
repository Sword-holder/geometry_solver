from typing import List

from geometry_solver.entities.entity import Entity
from geometry_solver.entities.line import Line


class Angle(Entity):

    def __init__(self, id_, sides: List[Line], angle: float):
        super(Angle, self).__init__(id_)
        self.sides = sides
        self.angle = angle
        self.add_entities(sides)

    def __str__(self):
        return '(' \
            + 'Angle ' \
            + self.id \
            + ': \n' \
            + '\tside1: ' \
            + str(self.sides[0]) \
            + '\n\tside2: ' \
            + str(self.sides[1]) \
            + '\n\tangle = ' \
            + str(self.angle) \
            + ')'

