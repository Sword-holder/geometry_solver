from quick_input.abc import A, B, C, M, N, O
from quick_input import link, clear, set_length, get_length, split_angle, parallel, get_angle, set_common_vertex_angles, get_triangle_circumference


def test_parser_example5():
    link(A, M, B)
    link(A, N, C)
    link(B, C)
    link(B, O)
    link(C, O)
    link(M, O, N)

    set_length('AB', 12)
    set_length('AC', 18)
    set_length('BC', 24)

    split_angle('ABC', 'BO', 0.5)
    split_angle('ACB', 'CO', 0.5)
    
    parallel('MN', 'BC')

    set_common_vertex_angles('B', ['A', 'O', 'C'])
    set_common_vertex_angles('C', ['A', 'O', 'B'])

    assert round(get_triangle_circumference('AMN'), 6) == 30

    clear()
