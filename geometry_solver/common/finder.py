from geometry_solver.entities.entity import Entity
from geometry_solver.entities.point import Point
from geometry_solver.entities.line import Line
from geometry_solver.entities.angle import Angle
from geometry_solver.entities.triangle import Triangle


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
        self._init_container()
        self._analyse_entity(entity)

    def _init_container(self):
        self._ends_to_line_map = {}
        self._sides_to_angle_map = {}
        self._triangle_set = set()

    def _analyse_entity(self, entity: Entity) -> None:
        for e in entity.children:
            if type(e) == Line:
                ends = Finder.UnoderedEntities(*e.ends)
                self._ends_to_line_map[ends] = e
            elif type(e) == Angle:
                sides = Finder.UnoderedEntities(*e.sides)
                self._sides_to_angle_map[sides] = e
            elif type(e) == Triangle:
                self._triangle_set.add(e)

    def find_line_by_ends(self, *ends):
        return self._find_entity_by_unordered_components(ends, 
                                            self._ends_to_line_map)

    def find_angle_by_sides(self, *sides):
        return self._find_entity_by_unordered_components(sides,
                                            self._sides_to_angle_map)
                            
    def find_all_triangles(self):
        return self._triangle_set
    
    def _find_entity_by_unordered_components(self, components, map_):
        try:
            components = Finder.UnoderedEntities(*components)
            entity = map_[components]
        except KeyError:
            entity = None
        return entity

