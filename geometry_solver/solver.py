from geometry_solver.entities.entity import Entity


class Solver(object):

    def __init__(self, problem: Entity):
        self._problem = problem

    def solve(self):
        print('solving problem....')

