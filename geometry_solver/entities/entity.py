from typing import List


class Entity(object):
    
    def __init__(self, id_):
        self.id = id_
        self.children = set()
    
    def add_entity(self, entity):
        # Add children recursively.
        for e in entity.children:
            self.add_entity(e)
        self.children.add(entity)
    
    def add_entities(self, entities: List):
        for entity in entities:
            self.add_entity(entity)
    
    def __str__(self):
        return '(' \
            + 'Entity: ' \
            + self.id \
            + ', has ' \
            + str(len(self.children)) \
            + ' children)'

