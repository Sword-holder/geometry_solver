from quick_input.abc import A, B, C, D, E, F
from quick_input import link, clear, set_length, set_angle, split_angle, perpendicular, get_angle, set_common_vertex_angles, get_angle


def test_parser_example6():
    # link(A, E, C)
    # link(B, D, C)
    # link(A, B)
    # link(A, F, D)
    # link(B, F, E)

    # set_angle('ACB', 70)
    # set_angle('ABC', 48)

    # split_angle('BAC', 'AD', 0.5)
    
    # perpendicular('AC', 'BE')

    # set_common_vertex_angles('A', ['B', 'D', 'C'])
    # set_common_vertex_angles('B', ['A', 'E', 'C'])

    # assert round(get_angle('BFD'), 6) == 59

    clear()
