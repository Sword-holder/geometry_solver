from typing import List

from geometry_solver.entities.entity import Entity
from geometry_solver.entities.point import Point
from geometry_solver.entities.line import Line
from geometry_solver.entities.angle import Angle
from geometry_solver.entities.triangle import Triangle
from geometry_solver.relationships.relationship import Relationship
from geometry_solver.relationships.collineation import Collineation


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


    def __init__(self, entity: Entity, relationships: List[Relationship]):
        self._init_container()
        self._analyse_entity(entity)
        self._analyse_relationship(relationships)
        self._analyse_link()

    def _init_container(self):
        self._point_name_map = {}
        self._ends_to_line_map = {}
        self._sides_to_angle_map = {}
        self._triangle_set = set()
        self._relationship_map = {}
        self._entity_map = {}
        self._line_alias = {}
        self._link = []

    def _analyse_entity(self, entity: Entity) -> None:
        for e in entity.children:
            type_ = type(e)
            if type_ not in self._entity_map:
                self._entity_map[type_] = []
            self._entity_map[type_].append(e)

            if type_ == Point:
                self._point_name_map[e.id] = e
            elif type_ == Line:
                ends = e.ends
                ends_str = tuple(sorted([ends[0].id, ends[1].id]))
                self._line_alias[tuple(ends_str)] = ends_str
                self._line_alias[tuple(ends_str[::-1])] = ends_str
                unordered_ends = Finder.UnoderedEntities(*e.ends)
                self._ends_to_line_map[unordered_ends] = e
            elif type_ == Angle:
                sides = Finder.UnoderedEntities(*e.sides)
                self._sides_to_angle_map[sides] = e
            elif type_ == Triangle:
                self._triangle_set.add(e)

    def _analyse_relationship(self, relationships: List[Relationship]) -> None:
        self._relationship_map = self._relationship_classify(relationships)
        if Collineation in self._relationship_map:
            cols = self._relationship_map[Collineation]
            for col in cols:
                points = col.points
                two_ends = tuple(sorted([points[0].id, points[-1].id]))
                for p1 in points:
                    for p2 in points:
                        self._line_alias[tuple([p1.id, p2.id])] = two_ends
                        self._line_alias[tuple([p2.id, p1.id])] = two_ends

    def _relationship_classify(self, relationships: List[Relationship]) -> None:
        _relationship_map = {}
        for r in relationships:
            type_ = type(r)
            if type_ not in _relationship_map:
                _relationship_map[type_] = []
            _relationship_map[type_].append(r)
        return _relationship_map

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

    def extend_line(self, line: Line):
        ends = line.ends
        end_str1, end_str2 = self._extend_pid(ends[0].id, ends[1].id)
        end1 = self._point_name_map[end_str1]
        end2 = self._point_name_map[end_str2]
        return self.find_line_by_ends(end1, end2)

    def find_link_by_ends(self, end1, end2):
        for lk in self._link:
            if (lk[0] == end1.id and lk[-1] == end2.id) or \
                    (lk[0] == end2.id and lk[-1] == end1.id):
                return [self._point_name_map[pid] for pid in lk]
        return []

    def _extend_pid(self, pid1, pid2):
        return self._line_alias[tuple([pid1, pid2])]

    def _analyse_link(self):
        if Collineation in self._relationship_map:
            for col in self._relationship_map[Collineation]:
                self._link.append([p.id for p in col.points])

        def _line_in_col(line: Point) -> bool:
            pid1, pid2 = line.ends[0].id, line.ends[1].id
            for lk in self._link:
                if pid1 in lk and pid2 in lk:
                    return True
            return False

        line_link = []
        if Line in self._entity_map:
            for line in self._entity_map[Line]:
                if not _line_in_col(line):
                    line_link.append([line.ends[0].id, line.ends[1].id])
        self._link += line_link

    def find_lines_intersection(self, line1: Line, line2: Line) -> List[Point]:
        def _find_line_in_link(line: Line):
            pid1, pid2 = line.ends[0].id, line.ends[1].id
            for lk in self._link:
                try:
                    ind1 = lk.index(pid1)
                    ind2 = lk.index(pid2)
                except ValueError:
                    continue
                return lk[ind1:ind2+1]
            raise ValueError('Cannot find line in link!')

        lk1 = _find_line_in_link(line1)
        lk2 = _find_line_in_link(line2)
        intersection = list(set(lk1) & set(lk2))
        intersection_p = [self._point_name_map[i] for i in intersection]
        return intersection_p
