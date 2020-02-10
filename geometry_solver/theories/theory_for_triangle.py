import math

from geometry_solver import theory_manager as tm
from geometry_solver.entities.triangle import Triangle


@tm.theoried(Triangle)
def triangle_angle_sum(triangle: Triangle) -> None:
    known_angles = triangle.known_angles
    unknown_angles = triangle.unknown_angles
    if len(known_angles) == 2:
        unknown_angles[0].angle = 180 \
                                  - known_angles[0].angle \
                                  - known_angles[1].angle


@tm.theoried(Triangle)
def the_law_of_cosines(triangle: Triangle) -> None:
    known_sides = triangle.known_sides
    unknown_angles = triangle.unknown_angles
    if len(known_sides) == 3:
        if unknown_angles:
            angle = unknown_angles[0]
            opposite_side = triangle.opposite_side(angle)
            adj_side1, adj_side2 = triangle.adjacent_sides(angle)
            a = adj_side1.length
            b = adj_side2.length
            c = opposite_side.length
            angle.angle = math.acos((a * a + b * b - c * c) / (2 * a * b))
            angle.angle = angle.angle * 180 / math.pi

