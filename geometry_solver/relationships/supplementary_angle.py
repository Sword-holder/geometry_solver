from typing import List

from geometry_solver.entities.angle import Angle
from geometry_solver.relationships import Relationship


class SupplementaryAngle(Relationship):

    def __init__(self, id_: str,  angle1: Angle, angle2: Angle):
        super(SupplementaryAngle, self).__init__(id_)
        self.angle1 = angle1
        self.angle2 = angle2
    
    def __str__(self):
         return '(' \
            + 'SupplementaryAngle relationship ' \
            + self.id \
            + ': ' \
            + 'angle1 = ' \
            + str(self.angle1) \
            + ', angle2 = ' \
            + str(self.angle2) \
            + ')'

