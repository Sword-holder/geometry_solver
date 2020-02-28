import math
from typing import Union

import sympy
from sympy import Symbol

from geometry_solver.entities.entity import Entity
from geometry_solver.entities.line import Line
from geometry_solver.entities.angle import Angle


def to_degree_measure(radian):
    return radian * 180 / math.pi


def to_radian_measure(degree):
    return degree * math.pi / 180


def symbol(entity: Entity, attr: str) -> Union[Symbol, float]:
    if getattr(entity, attr) is None:
        return Symbol('_'.join([type(entity).__name__, entity.id, attr]))
    return getattr(entity, attr)

