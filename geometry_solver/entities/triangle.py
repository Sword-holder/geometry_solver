from typing import List
import copy

from geometry_solver.entities.area import Area
from geometry_solver.entities.point import Point
from geometry_solver.entities.line import Line
from geometry_solver.entities.angle import Angle
from geometry_solver.state.triangle_state import TriangleState


class Triangle(Area):

    def __init__(self, id_, 
                 vertexes: List[Point], 
                 sides: List[Line], 
                 angles: List[Angle], 
                 area: float=None,
                 circumference: float=None,
                 r_inner: float=None,
                 r_outer: float=None):
        super(Triangle, self).__init__(id_, vertexes, sides, angles, area, circumference)
        self.r_inner = r_inner
        self.r_outer = r_outer
        self.state = TriangleState()
    
    @property
    def known_angles(self) -> List[Angle]:
        return [angle for angle in self.angles if angle.angle is not None]

    @property
    def unknown_angles(self) -> List[Angle]:
        return [angle for angle in self.angles if angle.angle is None]

    @property
    def known_sides(self) -> List[Line]:
        return [side for side in self.sides if side.length is not None]
    
    @property
    def unknown_sides(self) -> List[Line]:
        return [side for side in self.sides if side.length is None]

    def opposite_side(self, angle: Angle) -> Line:
        try:
            index = self.angles.index(angle)
        except:
            print('Error: Angle {} is not in triangle!'.format(angle.id))
        return self.sides[index]

    def adjacent_sides(self, angle: Angle) -> List[Line]:
        opposite_side = self.opposite_side(angle)
        return [side for side in self.sides if side is not opposite_side]

    def opposite_angle(self, side: Line) -> Angle:
        try:
            index = self.sides.index(side)
        except:
            print('Error: Side {} is not in triangle!'.format(side.id))
        return self.angles[index]

    def adjacent_angles(self, side: Line) -> List[Angle]:
        opposite_angle = self.opposite_angle(side)
        return [angle for angle in self.angles if angle is not opposite_angle]
    
    def to_rt(self, vertex=None):
        if vertex is None:
            print('Warning: the triangle is not right triangle.')
        self.state.to_rt()

    def to_isosceles(self, vertex=None):
        if vertex is None:
            print('Warning: the triangle is not isosceles.')
        self.to_isosceles(vertex)

    def to_equilateral(self):
        self.to_equilateral()

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

