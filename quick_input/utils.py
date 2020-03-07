from geometry_solver.entities import Point, Line, Angle

from quick_input.parser import Parser


parser = Parser()


def link(*points) -> Line:
    parser.link(*points)


def submit():
    parser.parse()


def set_angle(angle_id, degree):
    parser.set_angle(angle_id, degree)


def get_angle(angle_id):
    parser.set_target(angle_id, Angle, 'angle')

