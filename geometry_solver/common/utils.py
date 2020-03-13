import math
from typing import Union

import sympy
from sympy import Symbol

from geometry_solver.entities.entity import Entity
from geometry_solver.relationships.relationship import Relationship
from geometry_solver.entities.point import Point
from geometry_solver.entities.line import Line
from geometry_solver.entities.angle import Angle


def to_degree_measure(radian):
    return radian * 180 / math.pi


def to_radian_measure(degree):
    return degree * math.pi / 180


def symbol(object_: Union[Entity, Relationship], 
           attr: str) -> Union[Symbol, float]:
    if getattr(object_, attr) is None:
        return Symbol('_'.join([type(object_).__name__, object_.id, attr]))
    return getattr(object_, attr)


# def add_new_object(object_: Union[Entity, Relationship]) -> None:
#     new_objects.add(object_)


def points(*ids):
    """Create a seris of points"""
    ps = [Point(i) for i in ids]
    return ps
