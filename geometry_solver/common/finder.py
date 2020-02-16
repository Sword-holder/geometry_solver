from geometry_solver.entities.entity import Entity
from geometry_solver.entities.point import Point
from geometry_solver.entities.line import Line


class Finder(object):

    class UnoderedEntities(object):

        def __init__(self, *entities):
            self._entities = set(entities)

        def __hash__(self):
            h = sum([hash(e.id) for e in self._entities])
            return h
        
        def __eq__(self, other):
            return self._entities == other._entities


    def __init__(self, entity: Entity):
        self.entiy = entity
        self.points_to_line_map = {}
        self._analyse_entity(entity)

    def _analyse_entity(self, entity: Entity) -> None:
        for e in entity.children:
            if type(e) == Line:
                ends = Finder.UnoderedEntities(*e.ends)
                self.points_to_line_map[ends] = e

    def find_line_by_ends(self, *ends):
        try:
            ends = Finder.UnoderedEntities(*ends)
            line = self.points_to_line_map[ends]
        except KeyError:
            line = None
        return line

