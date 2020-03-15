from quick_input.abc import A, B, C, M, N
from quick_input import link, clear, set_length, get_length, perpendicular, split_line


def test_parser_example4():
    link(A, B)
    link(A, N, C)
    link(B, M, C)
    link(M, N)

    set_length('AB', 5)
    set_length('AC', 5)
    set_length('BC', 6)

    perpendicular('MN', 'AC')
    split_line('BC', 'M', 0.5)
    
    assert round(get_length('MN'), 6) == 2.4

    clear()

