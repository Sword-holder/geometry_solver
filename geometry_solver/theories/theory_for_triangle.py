import math

import sympy

from geometry_solver import theory_manager as tm
from geometry_solver.entities.triangle import Triangle
from geometry_solver.common.utils import to_degree_measure, to_radian_measure, symbol
from geometry_solver import solving_path
from geometry_solver.common.zh_lib import zh_theory


@tm.theoried(Triangle)
def triangle_angle_sum(triangle: Triangle) -> None:
    angle0, angle1, angle2 = triangle.angles
    yield symbol(angle0, 'angle') \
        + symbol(angle1, 'angle') \
        + symbol(angle2, 'angle') \
        - 180


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
            angle.angle = to_degree_measure(angle.angle)
            solving_path.append_deduction(
                theory=zh_theory['the_law_of_cosines'], 
                eq='Angle_{0} = arccos((Line_{1}^2+Line_{2}^2-Line_{3}^2) / (2*Line_{1}*Line_{2}))'.format(angle.id, adj_side1.id, adj_side2.id, opposite_side.id),
                result=angle.angle)
    elif len(known_sides) == 2:
        unknown_side = triangle.unknown_sides[0]
        angle = triangle.opposite_angle(unknown_side)
        if angle.angle is not None:
            a = known_sides[0].length
            b = known_sides[1].length
            cos_c = math.cos(to_radian_measure(angle.angle))
            unknown_side.length = math.sqrt(a * a + b * b - 2 * a * b * cos_c)
            solving_path.append_deduction(
                theory=zh_theory['the_law_of_cosines'], 
                eq='Line_{0} = sqrt(Line_{1}^2 + Line_{2}^2 - 2*Line_{1}*Line_{2}*cos(Angle_{3}))'.format(unknown_side.id, known_sides[0].id, known_sides[1].id, angle.id),
                result=unknown_side.length)


@tm.theoried(Triangle)
def the_law_of_sines(triangle: Triangle) -> None:
    for angle in triangle.angles:
        side = triangle.opposite_side(angle)
        if angle.angle is not None:
            yield symbol(side, 'length') / sympy.sin(to_radian_measure(symbol(angle, 'angle'))) \
                - 2 * symbol(triangle, 'r_outer')

    # known_angles = triangle.known_angles
    # if len(known_angles) == 0:
    #     return
    # elif len(known_angles) == 1:
    #     angle = known_angles[0]
    #     opposite_side = triangle.opposite_side(angle)
    #     if opposite_side.length is not None:
    #         for side in triangle.adjacent_sides(angle):
    #             if side.length is not None:
    #                 unknown_angle = triangle.opposite_angle(side)
    #                 sin_angle = math.sin(to_radian_measure(angle.angle)) * \
    #                     (side.length / opposite_side.length)
    #                 unknown_angle.angle = to_degree_measure(
    #                     math.asin(sin_angle))
    #                 solving_path.append_deduction(
    #                     theory=zh_theory['the_law_of_sines'],
    #                     eq='Angle_{0} = arcsin(sin(Angle_{1}) * (Line_{2} / Line_{3}))'.format(unknown_angle.id, angle.id, side.id, opposite_side.id),
    #                     result=unknown_angle.angle)
    #                 return
    # elif len(known_angles) > 1:
    #     opposite_sides = \
    #         [triangle.opposite_side(angle) for angle in known_angles]
    #     for index1, side1 in enumerate(opposite_sides):
    #         for index2, side2 in enumerate(opposite_sides):
    #             if side1.length is None and side2.length is not None:
    #                 angle1 = to_radian_measure(known_angles[index1].angle)
    #                 angle2 = to_radian_measure(known_angles[index2].angle)
    #                 side1.length = side2.length * math.sin(angle1) / math.sin(angle2)
    #                 solving_path.append_deduction(
    #                     theory=zh_theory['the_law_of_sines'],
    #                     eq='Line_{0} = Line_{1} * sin({2}) / sin({3})'.format(side1.id, side2.id, known_angles[index1].id, known_angles[index2].id),
    #                     result=side1.length)
    #                 return


@tm.theoried(Triangle)
def helen_formula(triangle: Triangle) -> None:
    known_sides = triangle.known_sides
    if len(known_sides) == 3:
        a = known_sides[0].length
        b = known_sides[1].length
        c = known_sides[2].length
        p = (a + b + c) / 2
        triangle.area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        solving_path.append_deduction(
            theory=zh_theory['helen_formula'],
            eq='Triangle_{0}.area = sqrt(p * (p-Line_{1}) * (p-Line{2}) *(p-Line_{3}))'.format(triangle.id, known_sides[0].id, known_sides[1].id, known_sides[2].id),
            result=triangle.area
        )

