from geometry_solver.entities import Angle, Entity, Line, Point, Triangle
from geometry_solver.relationships import Collineation, OppositeVerticalAngle, SupplementaryAngle
from geometry_solver import Problem, Solver, Target, TargetType


class Parser(object):

    def __init__(self):
        self.entity_container = Entity('Entity container')
        self._points = set()
        self._lines = set()
        self._adj_table = {}
        self.angle_dict = {}
        self.target_dict = []
        self.line_alias = {}
        self._collineation_list = []

    def link(self, *points) -> Line:
        n = len(points)

        for p in points:
            self._points.add(p.id)
        
        if n >= 3:
            self._collineation_list.append([p.id for p in points])

        # Initialize line alias
        ends_str = points[0].id + points[-1].id
        for i in range(n):
            for j in range(i + 1, n):
                self.line_alias[points[i].id + points[j].id] = ends_str
                self.line_alias[points[j].id + points[i].id] = ends_str[::-1]


        for i in range(n):
            for j in range(i + 1, n):
                line_id = ''.join([points[i].id, points[j].id])
                self._lines.add(line_id)
        
        for p in points:
            if p.id not in self._adj_table:
                self._adj_table[p.id] = []
            for adj_p in points:
                if id(adj_p) == id(p):
                    continue
                self._adj_table[p.id].append(adj_p.id) 


    def parse(self) -> Problem:

        print('Using intelligent parser...')

        def sort_string(str_):
            return ''.join(sorted(str_))


        # Generate points.
        points = {pid: Point(pid) for pid in self._points}

        # Generate lines.
        lines = {}
        for lid in self._lines:
            lid = sort_string(lid)
            ends = [points[pid] for pid in lid]
            line = Line(lid, ends=ends, length=None)
            lines[lid] = line
        

        def find_line_by_ends(pid1, pid2):
            return lines[sort_string(''.join([pid1, pid2]))]

        # Generate angles.
        angles = {}
        for vertex, adj_nodes in self._adj_table.items():
            n_adj = len(adj_nodes)
            for i in range(n_adj):
                for j in range(i + 1, n_adj):
                    node1, node2 = adj_nodes[i], adj_nodes[j]
                    node1 = self.line_alias[node1 + vertex][0]
                    node2 = self.line_alias[vertex + node2][1]
                    # Angle with zero degree
                    if node1 == node2:
                        continue
                    # Flat angle
                    if self._is_collineation(node1, vertex, node2):
                        continue
                    node1, node2 = sorted([node1, node2])
                    aid = ''.join([node1, vertex, node2])
                    line1 = find_line_by_ends(node1, vertex)
                    line2 = find_line_by_ends(node2, vertex)
                    sides = [line1, line2]
                    degree = self._look_up_degree(aid)
                    angles[aid] = Angle(aid, sides=sides, vertex=points[vertex], angle=degree)


        def find_angle_by_points(pid1, vertex, pid2):
            pid1 = self.line_alias[pid1 + vertex][0]
            pid2 = self.line_alias[vertex + pid2][1]
            if pid1 > pid2:
                pid1, pid2 = pid2, pid1
            return angles[''.join([pid1, vertex, pid2])]


        # Generate triangle.
        triangles = {}
        triangle_ids = self._analyse_triangle()
        for tid in triangle_ids:
            t_vertexes = [points[v] for v in tid]
            t_side1 = find_line_by_ends(tid[0], tid[1])
            t_side2 = find_line_by_ends(tid[1], tid[2])
            t_side3 = find_line_by_ends(tid[0], tid[2])
            t_sides = [t_side1, t_side2, t_side3]
            t_angle1 = find_angle_by_points(tid[0], tid[2], tid[1])
            t_angle2 = find_angle_by_points(tid[1], tid[0], tid[2])
            t_angle3 = find_angle_by_points(tid[0], tid[1], tid[2])
            t_angles = [t_angle1, t_angle2, t_angle3]
            triangles[tid] = Triangle(tid, vertexes=t_vertexes, sides=t_sides, angles=t_angles, area=None)


        print('points: ', sorted(points.keys()))
        print('lines', sorted(lines.keys()))
        print('angles: ', sorted(angles.keys()))
        print('triangles: ', sorted(triangles.keys()))


        # Generate relationships.
        collineations = {}
        for col in self._collineation_list:
            col_id = 'Collineation ' + ''.join([p for p in col])
            collineations[col_id] = Collineation(col_id, points=col)

        # Generate opposite vertival angles.
        opposite_angles = {}
        n_cols = len(self._collineation_list)
        for i in range(n_cols):
            for j in range(i + 1, n_cols):
                col1 = self._collineation_list[i]
                col2 = self._collineation_list[j]
                common = list(set(col1) & set(col2))
                if len(common) != 1:
                    continue
                vertex = common[0]
                if vertex in [col1[0], col1[-1], col2[0], col2[-1]]:
                    continue

                angle1_1 = find_angle_by_points(col1[0], vertex, col2[0])
                angle1_2 = find_angle_by_points(col1[-1], vertex, col2[-1])
                rid = ' '.join(['OppositeAngle', angle1_1.id, angle1_2.id])
                opposite_angles[rid] = OppositeVerticalAngle(rid, 
                    angle1=angle1_1, angle2=angle1_2, vertex=vertex)

                angle2_1 = find_angle_by_points(col1[0], vertex, col2[-1])
                angle2_2 = find_angle_by_points(col1[-1], vertex, col2[0])
                rid = ' '.join(['OppositeAngle', angle2_1.id, angle2_2.id])
                opposite_angles[rid] = OppositeVerticalAngle(rid, 
                    angle1=angle2_1, angle2=angle2_2, vertex=vertex)


        # Generate supplementary angles.
        supplementary_angles = {}
        for col in self._collineation_list:
            for p in col[1:-1]:
                for adj_p in self._adj_table[p]:
                    if adj_p == col[0] or adj_p == col[-1]:
                        continue
                    angle1 = find_angle_by_points(col[0], p, adj_p)
                    angle2 = find_angle_by_points(col[-1], p, adj_p)
                    rid = ' '.join(['SupplementaryAngle', angle1.id, angle2.id])
                    supplementary_angles[rid] = \
                        SupplementaryAngle(rid, angle1=angle1, angle2=angle2)

        
        print('collineations: ', sorted(collineations.keys()))
        print('opposite angles: ', sorted(opposite_angles.keys()))
        print('supplementary angles: ', sorted(supplementary_angles.keys()))



        self.entity_container.add_entity(*(points.values()))
        self.entity_container.add_entity(*(lines.values()))
        self.entity_container.add_entity(*(angles.values()))
        self.entity_container.add_entity(*(triangles.values()))

        problem = Problem(entity=self.entity_container)
        
        solver = Solver(problem)
        
        print('Create a triangle successfully!')
        print(problem)

        # Add targets.
        for id_, type_, attr in self.target_dict:
            target = Target(TargetType.EVALUATION,
                    entity=problem.entity.find_child(id_, type_),
                    attr=attr)
            solver.add_target(target)
        
        solver.solve()
    
        # return problem


    def _is_collineation(self, *points):
        if len(points) < 3:
            return True
        for col in self._collineation_list:
            on_a_line = True
            for p in points:
                if p not in col:
                    on_a_line = False
                    break
            if on_a_line:
                return True
        return False


    def _analyse_triangle(self):
        all_triangles = set()
        for p in self._adj_table.keys():
            self._dfs_triangle([p], all_triangles)
        return {t for t in all_triangles if not self._is_collineation(*t)}


    def _dfs_triangle(self, trajectory, all_triangles):
        if len(trajectory) == 4:
            if trajectory[0] == trajectory[-1]:
                triangle_id = ''.join(sorted(trajectory[:3]))
                all_triangles.add(triangle_id)
            return
        node = trajectory[-1]
        for adj_node in self._adj_table[node]:
            if len(trajectory) < 3 and adj_node in trajectory:
                continue
            self._dfs_triangle(trajectory + [adj_node], all_triangles)


    def set_angle(self, angle_id, degree):
        self.angle_dict[angle_id] = degree


    def _look_up_degree(self, aid):
        if aid not in self.angle_dict:
            return None
        return self.angle_dict[aid]

    def set_target(self, id_, type_, attr):
        self.target_dict.append((id_, type_, attr))

