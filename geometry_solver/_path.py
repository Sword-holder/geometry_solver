

class Path(object):

    def __init__(self):
        self.deduction_path = []

    def append_equation(self, theory, eq) -> None:
        self._append_step('根据定理：{}，得到方程：{} = 0'.format(str(theory), str(eq)))

    def append_results(self, results) -> None:
        solving_log = '解得：\n'
        for entity, value in results:
            solving_log += '\t{} = {}\n'.format(str(entity), str(round(value, 3)))
        self._append_step(solving_log)
    
    def append_deduction(self, theory, eq, result) -> None:
        self._append_step('根据定理：{}，推得：{} = {}'.format(str(theory), str(eq), str(round(result, 3))))

    def _append_step(self, step):
        self.deduction_path.append(step)

    def __str__(self):
        path_str = '\n'.join([s for s in self.deduction_path])
        return path_str

