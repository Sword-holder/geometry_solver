from geometry_solver.entities import Point, Line, Angle

from quick_input.parser import Parser


parser = Parser()


def link(*points) -> Line:
    parser.link(*points)


def submit():
    parser.parse()
    parser.initialize()


def set_angle(angle_id, degree):
    parser.set_angle(angle_id, degree)


def get_angle(angle_id):
    parser.set_target(angle_id, Angle, 'angle')


def set_length(line_id, length):
    parser.set_length(line_id, length)


def get_length(line_id):
    parser.set_target(line_id, Line, 'length')


def split_angle(angle_id, line_id, ratio):
    parser.add_angle_split(angle_id, line_id, ratio)


def split_line(line_id, point_id, ratio):
    parser.add_line_split(line_id, point_id, ratio)


def set_common_vertex_angles(vertex_id, around_points):
    parser.add_common_vertex_angle(vertex_id, around_points)


def perpendicular(line_id1, line_id2):
    parser.add_perpendicular(line_id1, line_id2)
    
