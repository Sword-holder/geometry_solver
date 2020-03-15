from quick_input.abc import A, B, C, D, F
from quick_input import link, clear, set_angle, get_angle, split_angle, set_common_vertex_angles, perpendicular


def test_parser_example3():
    link(A, B)
    link(A, F)
    link(A, D)
    link(A, C)
    link(B, F, D, C)

    set_angle('ABC', 36)
    set_angle('ACB', 76)

    split_angle('BAC', 'AF', ratio=0.5)
    set_common_vertex_angles('A', ['B', 'F', 'D', 'C'])
    perpendicular('AD', 'BC')

    assert round(get_angle('DAF'), 6) == 20

    clear()

