from typing import Any, List

import sympy
from sympy import Symbol, Number


class EquationSolver(object):

    def __init__(self):
        self._equation_group = {}
        self._solved = set()
    
    def set_equation_group(self, key: Any, equation_set: List) -> None:
        self._equation_group[key] = equation_set

    def solve(self, solving_path):
        equation_set = []
        for _, value in self._equation_group.items():
            for eq in value:
                if not isinstance(eq, Number):
                    equation_set.append(eq)
        result = sympy.solvers.solve(equation_set)
        self._track_path(result, solving_path)
        return result

    def clear(self):
        self._equation_group = {}

    def has_key(self, key: str) -> bool:
        return key in self._equation_group

    def _track_path(self, result, solving_path):
        if not result:
            return
        solved_attrs = []
        for e_symb, value in result.items():
            if isinstance(value, Number) and e_symb not in self._solved:
                solved_attrs.append((e_symb, value))
                self._solved.add(e_symb)
        if solved_attrs:
            solving_path.append_results(solved_attrs)

    def __str__(self):
        eq_str = ''
        for key, equations in self._equation_group.items():
            eq_str += key + ':'
            for eq in equations:
                eq_str += '\n\t' + str(eq)
            eq_str += '\n'
        return '[Equation pool:\n' + eq_str + ']'

