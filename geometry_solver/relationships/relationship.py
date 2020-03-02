

class Relationship(object):

    def __init__(self, id_):
        self.id = id_

    def __eq__(self, other):
        return type(self) == type(other) \
               and self.id == other.id

    def __str__(self):
        return '(' \
            + 'Relationship ' \
            + self.id \
            + ')'

