from typing import List

from geometry_solver.relationships.relationship import Relationship


class Collineation(Relationship):

    def __init__(self, id_: str, points: List):
        super(Collineation, self).__init__(id_)
        self.points = points

    def __str__(self):
        return '(' \
            + 'Collineation relationship ' \
            + self.id \
            + ': ' \
            + 'points = [' \
            + ', '.join([p.id for p in self.points]) \
            + ']' \
            + ')'

