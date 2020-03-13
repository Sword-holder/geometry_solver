import inspect

from sympy import Symbol, Number

from geometry_solver.entities.entity import Entity
from geometry_solver.relationships.relationship import Relationship
from geometry_solver.common.zh_lib import zh_theory


def _f_decorated(f):
    def decorator(**args):
        node = args['node']
        equation_pool = node.equation_pool
        new_objects = node.new_objects
        solving_path = node.solving_path

        equation_set = []
        group_key = '_'.join([f.__name__, args['object_'].id])

        if inspect.isgeneratorfunction(f):
            for item in f(args['object_'], args['node'].finder):
                if isinstance(item, Entity) or isinstance(item, Relationship):
                    # Deduction success if add a new object.
                    new_objects.add(item)
                    node.success = True
                else:
                    equation_set.append(item)
            equation_set = [eq for eq in equation_set if not isinstance(eq, Number)]
            if equation_set:
                if not equation_pool.has_key(group_key):
                    # Deduction success if add a new equation group.
                    node.success = True
                    for eq in equation_set:
                        if type(eq) != float and type(eq) != int:
                            solving_path.append_equation(zh_theory[f.__name__], eq)
                equation_pool.set_equation_group(group_key, equation_set)
        else:
            f(args['object_'], args['node'].finder)

    decorator.__name__ = f.__name__
    return decorator

