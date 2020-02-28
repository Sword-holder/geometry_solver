from enum import Enum


class TriangleState():


    class RT(Enum):
        plain = 1
        rt = 2


    class Isosceles(Enum):
        plain = 1
        isosceles = 2
        equilateral = 3

    
    def __init__(self):
        self.rt_state = TriangleState.RT.plain
        self.isosceles_state = TriangleState.Isosceles.plain
        self.rt_info = {'vertex': None}
        self.isosceles_info = {'vertex': None}

    def to_rt(self, vertex=None):
        """Alter the triangle state to right triangle.
        vertex represents the right angle.
        """
        self.rt_state = TriangleState.RT.rt
        self.rt_info['vertex'] = vertex

    def to_isosceles(self, vertex=None):
        """Alter the triangle state to isosceles triangle.
        vertex is the angle between two equivalent side.
        """
        self.isosceles_state = TriangleState.Isosceles.isosceles
        self.isosceles_info['vertex'] = vertex

    def to_equilateral(self):
        """Alter the triangle state to equilateral triagnle."""
        self.isosceles_state = TriangleState.Isosceles.equilateral

