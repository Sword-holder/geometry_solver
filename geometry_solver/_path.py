from enum import Enum


class StepType(Enum):
    ADD_EQUATION_STEP = 1
    SOLVING_RESULT_STEP = 2
    DIRECT_DEDUCTION_STEP = 3


class Path(object):

    def __init__(self):
        self._path = []

    def append_equation(self, theory, eq) -> None:
        self._path.append((StepType.ADD_EQUATION_STEP, (theory, eq)))

    def append_results(self, results) -> None:
        self._path.append((StepType.SOLVING_RESULT_STEP, results))
    
    def append_deduction(self, theory, eq, result) -> None:
        self._path.append((StepType.DIRECT_DEDUCTION_STEP, (theory, eq, result)))

    def _gen_solving_path_str(self):
        path_str = []
        for type_, content in self._path:
            if type_ == StepType.ADD_EQUATION_STEP:
                theory, eq = content
                path_str.append('根据定理：{}，得到方程：{} = 0'.format(str(theory), str(eq)))
            elif type_ == StepType.SOLVING_RESULT_STEP:
                solving_log = '解得：\n'
                for entity, value in content:
                    solving_log += '\t{} = {}\n'.format(str(entity), str(round(value, 3)))
                path_str.append(solving_log)
            elif type_ == StepType.DIRECT_DEDUCTION_STEP:
                theory, eq, result = content
                path_str.append('根据定理：{}，推得：{} = {}'.format(str(theory), str(eq), str(round(result, 3))))
        return '\n'.join([s for s in path_str])


    def __str__(self):
        return self._gen_solving_path_str()

