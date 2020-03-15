import time
import queue
import copy

import numpy as np
from tqdm import tqdm

from geometry_solver.target import Target, TargetType
from geometry_solver._equation_solver import EquationSolver
from geometry_solver._path import Path
from geometry_solver.node import Node
# Import theories.
import geometry_solver.theories.theory_for_triangle
import geometry_solver.theories.theory_for_collineation
import geometry_solver.theories.theory_for_common_vertex_angle
import geometry_solver.theories.theory_for_opposite_vertical_angle
import geometry_solver.theories.theory_for_supplementary_angle
import geometry_solver.theories.theory_for_perpendicular
import geometry_solver.theories.theory_for_n_line_sector
import geometry_solver.theories.theory_for_n_angle_sector
import geometry_solver.theories.theory_for_parallel
import geometry_solver.theories.theory_for_similar_triangle

from geometry_solver.common.debug_utils import getsize


class Solver(object):


    def __init__(self, problem):
        self._targets_info = []
        equation_pool = EquationSolver()
        solving_path = Path()
        new_objects = set()
        self.root = Node(problem=problem, 
                         equation_pool=equation_pool, 
                         solving_path=solving_path, 
                         new_objects=new_objects)


    def add_target(self, target) -> None:
        tg_dict = {}
        tg_dict['target_type'] = target.type
        tg_dict['entity_id'] = target.entity.id
        tg_dict['entity_type'] = type(target.entity)
        tg_dict['attr'] = target.attr
        if target.type == TargetType.PROOF:
            tg_dict['value'] = target.value
        self._targets_info.append(tg_dict)


    def solve(self, policy='beam'):

        policy = policy.lower()
        print('solving problem....')
        print('Using policy: {}'.format(policy))

         # Set target.
        self.root.targets_info = self._targets_info

        start_time = time.time()

        if policy == 'random':
            final_node = self._random_search()
        elif policy == 'bfs':
            final_node = self._bfs()
        elif policy == 'dfs':
            final_node = self._dfs()
        elif policy == 'beam':
            final_node = self._beam_search()

        if final_node is not None and final_node.solved:
            print('Solve problem successfully! Here are results:')
            for target in final_node.targets:
                print(target)
        else:
            print('The problem has no solution!')

        print(final_node.solving_path)
        
        end_time = time.time()
        print('Use time: {} s'.format(end_time - start_time))
        return final_node.problem


    def _bfs(self) -> Node:
        final_node = None
        q = queue.Queue()
        q.put(self.root)
        next_step_num = 1
        current_step = 0
        step = 0
        while not q.empty():
            acc_num = 0
            for _ in tqdm(range(next_step_num), desc='Step {}'.format(current_step)):
                step += 1
                node = q.get()
                if node.solved:
                    final_node = node
                    break
                for node_copy in self._next_step_nodes(node):
                    acc_num += 1
                    q.put(node_copy)
            else:
                next_step_num = acc_num
                current_step += 1
                continue
            break

        print('Use step: {}'.format(current_step))
        return final_node
    

    def _dfs(self) -> Node:

        def _dfs_recursively(node):
            if node.solved:
                return node
            actions = node.valid_actions
            for action in actions:
                node_copy = copy.deepcopy(node)
                success = node_copy.take_action(action)
                if success:
                    final_node = _dfs_recursively(node_copy)
                    if final_node is not None:
                        return final_node
            return None
        
        return _dfs_recursively(self.root)


    def _random_search(self) -> Node:
        print('Make {} entity-theory pairs.'.format(len(self.root._theory_obj_pairs)))
        epoch = 0
        while not self.root.solved:
            valid_actions = self.root.valid_actions
            if not valid_actions:
                break
            pair = np.random.choice(valid_actions)
            self.root.take_action(pair)
            print('epoch {}: chose {} to search.'.format(epoch, pair))
            epoch += 1
        return self.root


    def _beam_search(self, beam=20, max_step=None):
        final_node = None
        beam_nodes = [self.root]
        step = 0
        while max_step is None or step < max_step:
            # Check termination.
            for node in beam_nodes:
                if node.solved:
                    final_node = node
                    break
            else:
                # Search next step.
                step += 1
                next_nodes = []
                for node in tqdm(beam_nodes,  desc='Step {}'.format(step)):
                    next_nodes += self._next_step_nodes(node)
                np.random.shuffle(next_nodes)
                beam_nodes = next_nodes[:beam]
                continue
            break
        return final_node


    def _next_step_nodes(self, node):
        nodes = []
        actions = node.valid_actions
        for action in actions:
            node_copy = copy.deepcopy(node)
            success = node_copy.take_action(action)
            if success:
                nodes.append(node_copy)
        return nodes
    
