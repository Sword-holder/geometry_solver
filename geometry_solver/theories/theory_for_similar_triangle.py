import math

import sympy

from geometry_solver import theory_manager as tm
from geometry_solver.entities.triangle import Triangle
from geometry_solver.relationships.similar_triangle import SimilarTriangle
from geometry_solver.common.utils import to_degree_measure, to_radian_measure, symbol, add_new_object
from geometry_solver.common.finder import Finder
from geometry_solver import solving_path
from geometry_solver.common.zh_lib import zh_theory


@tm.theoried(SimilarTriangle)
def similar_triangle_ratio(similar_triangle: SimilarTriangle,
                           finder: Finder) -> None:
    ratio = symbol(similar_triangle, 'ratio')
    triangle1 = similar_triangle.triangle1
    triangle2 = similar_triangle.triangle2
    for angle1, angle2 in similar_triangle.corresponding:
        line1 = triangle1.opposite_side(angle1)
        line2 = triangle2.opposite_side(angle2)
        yield symbol(line1, 'length') - ratio*symbol(line2, 'length')


@tm.theoried(SimilarTriangle)
def similar_triangle_angle_equality(similar_triangle: SimilarTriangle,
                                    finder: Finder) -> None:
    for angle1, angle2 in similar_triangle.corresponding:
        yield symbol(angle1, 'angle') - symbol(angle2, 'angle')


@tm.theoried(Triangle)
def similar_triangle_determination(triangle: Triangle,
                                   finder: Finder) -> None:
    known_angles = triangle.known_angles
    if len(known_angles) < 3:
        return
    triangle_set = finder.find_all_triangles()
    for t in triangle_set:
        if id(t) == id(triangle) or len(t.known_angles) < 3:
            continue
        angles1 = [known_angles[0].angle, \
                   known_angles[1].angle, \
                   known_angles[2].angle]
        angles2 = [t.known_angles[0].angle, \
                   t.known_angles[1].angle, \
                   t.known_angles[2].angle]
        if set(angles1) == set(angles2):
            corresponding = []
            for a1 in known_angles:
                for a2 in t.known_angles:
                    if a1.angle == a2.angle:
                        corresponding.append((a1, a2))
            ratio = None
            for a1, a2 in corresponding:
                line1 = triangle.opposite_side(a1)
                line2 = t.opposite_side(a2)
                if line1.length is not None and line2.length is not None:
                    ratio = line1.length / line2.length
            r = SimilarTriangle(
                '_'.join(['similar_triangle', triangle.id, t.id]),
                triangle1=triangle,
                triangle2=t,
                corresponding=corresponding,
                ratio=ratio)
            add_new_object(r)

