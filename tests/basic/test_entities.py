import pytest

from geometry_solver.entities import Angle, Entity, Line, Point, Triangle


def test_line():
    p1 = Point('A')
    p2 = Point('B')
    line = Line('AB', ends=[p1, p2], length=34.5)
    print(line)


def test_angle():
    p1 = Point('A')
    p2 = Point('B')
    p3 = Point('C')
    line1 = Line('AB', ends=[p1, p2], length=34.5)
    line2 = Line('BC', ends=[p2, p3], length=13.2)
    angle = Angle('ABC', sides=[line1, line2], angle=60)
    print(angle)


def test_entity():
    entity_a = Entity('a')
    entity_b = Entity('b')
    entity_c = Entity('c')
    entity_d = Entity('d')
    entity_b.add_entity(entity_c)
    entity_b.add_entity(entity_d)
    entity_a.add_entity(entity_b)
    print(entity_a)


def test_triangle():
    pa = Point('A')
    pb = Point('B')
    pc = Point('C')
    
    line_ab = Line('AB', ends=[pa, pb], length=None)
    line_bc = Line('BC', ends=[pb, pc], length=None)
    line_ac = Line('AC', ends=[pa, pc], length=None)
    
    angle_abc = Angle('ABC', sides=[line_ab, line_bc], angle=90)
    angle_acb = Angle('ACB', sides=[line_ac, line_bc], angle=40)
    angle_bac = Angle('BAC', sides=[line_ab, line_ac], angle=None)

    triangle = Triangle('ABC', 
                        vertexes=[pa, pb, pc],
                        sides=[line_ab, line_ac, line_bc], 
                        angles=[angle_abc, angle_acb, angle_bac], 
                        area=6)

    print(triangle)


if __name__ == '__main__':
    test_line()
    test_angle()
    test_entity()
    test_triangle()
