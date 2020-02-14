

class Relationship(object):

    def __init__(self, id_):
        self.id = id_

    def __str__(self):
        return '(' \
            + 'Relationship ' \
            + self.id \
            + ')'

