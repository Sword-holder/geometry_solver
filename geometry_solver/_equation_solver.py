from typing import Any, List

import sympy
from sympy import Symbol


class EquationSolver(object):

    def __init__(self):
        self.equation_group = {}
    
    def set_equation_group(self, key: Any, equation_set: List) -> None:
        self.equation_group[key] = equation_set

    def solve(self):
        equation_set = []
        for _, value in self.equation_group.items():
            equation_set += value
        return sympy.solvers.solve(equation_set)

