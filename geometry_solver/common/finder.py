from geometry_solver.entities.entity import Entity
from geometry_solver.entities.point import Point
from geometry_solver.entities.line import Line
from geometry_solver.entities.angle import Angle


class Finder(object):

    class UnoderedEntities(object):

        def __init__(self, *entities):
            self._entities = set(entities)

        def __len__(self):
            return len(self._entities)

        def __hash__(self):
            h = sum([hash(e.id) for e in self._entities])
            return h
        
        def __eq__(self, other):
            return self._entities == other._entities


    def __init__(self, entity: Entity):
        self.entiy = entity
        self._init_maps()
        self._analyse_entity(entity)

    def _init_maps(self):
        self.ends_to_line_map = {}
        self.sides_to_angle_map = {}

    def _analyse_entity(self, entity: Entity) -> None:
        for e in entity.children:
            if type(e) == Line:
                ends = Finder.UnoderedEntities(*e.ends)
                self.ends_to_line_map[ends] = e
            elif type(e) == Angle:
                sides = Finder.UnoderedEntities(*e.sides)
                self.sides_to_angle_map[sides] = e

    def find_line_by_ends(self, *ends):
        return self._find_entity_by_unordered_components(ends, 
                                            self.ends_to_line_map)

    def find_angle_by_sides(self, *sides):
        return self._find_entity_by_unordered_components(sides,
                                            self.sides_to_angle_map)
    
    def _find_entity_by_unordered_components(self, components, map_):
        try:
            components = Finder.UnoderedEntities(*components)
            entity = map_[components]
        except KeyError:
            entity = None
        return entity

