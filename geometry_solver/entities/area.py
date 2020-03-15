from typing import List

from geometry_solver.entities.entity import Entity
from geometry_solver.entities.point import Point
from geometry_solver.entities.line import Line
from geometry_solver.entities.angle import Angle


class Area(Entity):

    def __init__(self, 
                 id_, 
                 vertexes: List[Point], 
                 sides: List[Line], 
                 angles: List[Angle], 
                 area: float=None,
                 circumference: float=None):
        super(Area, self).__init__(id_)
        self.vertexes = vertexes
        self.sides = sides
        self.angles = angles
        self.area = area
        self.circumference = circumference
        children = vertexes + sides + angles
        self.add_entity(*children)

