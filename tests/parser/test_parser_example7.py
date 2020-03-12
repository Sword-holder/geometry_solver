from quick_input.abc import A, B, C, D, E
from quick_input import link, clear, set_length, set_angle, split_angle, perpendicular, get_angle, set_common_vertex_angles, get_angle


def test_parser_example7():
    # link(A, B)
    # link(A, E, D)
    # link(B, D, C)
    # link(B, E)
    # link(C, E)

    # set_angle('ABC', 50)

    # split_angle('ABC', 'BE', 0.5)
    
    # perpendicular('AD', 'BC')

    # set_common_vertex_angles('E', ['B', 'D', 'C'])
    # set_common_vertex_angles('B', ['A', 'E', 'C'])

    # assert round(get_angle('AEC'), 6) == 59

    clear()
