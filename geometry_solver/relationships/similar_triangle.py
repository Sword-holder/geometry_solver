from typing import List, Tuple

from geometry_solver.entities.triangle import Triangle
from geometry_solver.entities.angle import Angle
from geometry_solver.relationships import Relationship


class SimilarTriangle(Relationship):

    def __init__(self, 
                 id_: str, 
                 triangle1: Triangle, 
                 triangle2: Triangle, 
                 corresponding: List[Tuple[Angle, Angle]],
                 ratio: float,):
        super(SimilarTriangle, self).__init__(id_)
        self.triangle1 = triangle1
        self.triangle2 = triangle2
        self.ratio = ratio
        self.corresponding = corresponding
    
    def __eq__(self, other):
        return \
            ( \
                self.triangle1 == other.triangle1 \
                and \
                self.triangle2 == other.triangle2 \
            ) \
            or \
            ( \
                self.triangle1 == other.triangle2 \
                and \
                self.triangle2 == other.triangle1 \
            )
    
    def __hash__(self):
        tid1, tid2 = self.triangle1.id, self.triangle2.id
        tid1, tid2 = sorted([tid1, tid2])
        return hash('_'.join(['SimilarTriangle', tid1, tid2]))
    
    def __str__(self):
        return '(' \
            + 'SimilarTriangle relationship ' \
            + self.id \
            + ': ' \
            + 'triangle1: ' \
            + str(self.triangle1.id) \
            + ', triangle2: ' \
            + str(self.triangle2.id) \
            + ', ratio: ' \
            + str(self.ratio) \
            + ')'
