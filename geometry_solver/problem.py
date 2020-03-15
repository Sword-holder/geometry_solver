from typing import List

from geometry_solver.entities.entity import Entity
from geometry_solver.relationships.relationship import Relationship


class Problem(object):

    def __init__(self, 
            entity: Entity = None, 
            relationships: List[Relationship] = []) -> None:
        self.entity = entity
        self.relationships = relationships

    def set_entity(self, entity: Entity):
        self.entity = entity

    def set_relationships(self, 
            relationships: List[Relationship]) -> None:
        self.relationships = relationships
    
    def add_relationship(self, relationship: Relationship) -> None:
        self.relationships.append(relationship)

    def __str__(self):
        relationship_str = \
            '\n'.join([str(r) for r in self.relationships])
        return '(Problem: ' \
            + '\n\tentity: ' \
            + str(self.entity) \
            + '\n\trelationship: \n' \
            + str(relationship_str) \
            + ')'

