from enum import Enum


class TargetType(Enum):
    EVALUATION = 1
    PROOF = 2


class Target(object):

    def __init__(self, type_: TargetType, **setting):
        self.type = type_
        if type_ == TargetType.EVALUATION:
            self.entity = setting['entity']
            self.attr = setting['attr']

    @property
    def solved(self) -> bool:
        if self.type == TargetType.EVALUATION:
            return self._evaluation_solved
        elif self.type == TargetType.PROOF:
            return self._PROOF_solved
        return True

    @property
    def _evaluation_solved(self):
        return getattr(self.entity, self.attr) is not None

    @property
    def _PROOF_solved(self):
        pass

    def __str__(self):
        if self.type == TargetType.EVALUATION and self.solved:
            value = ', ' \
                + str(self.entity.id) \
                + '.' \
                + str(self.attr) \
                + ' = ' \
                + str(getattr(self.entity, self.attr))
        else:
            value = ''

        return '(' \
            + 'Target: ' \
            + 'type = ' \
            + str(self.type) \
            + value \
            + ', status = ' \
            + ('solved' if self.solved else 'unsolved') \
            + '.)'

