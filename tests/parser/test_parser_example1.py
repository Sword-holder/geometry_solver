from quick_input.abc import A, B, C, D, E
from quick_input import link, clear, set_angle, get_angle


def test_parser_example1():
    link(A, D)
    link(A, B)
    link(A, E, C)
    link(B, E, D)
    link(B, C)

    set_angle('BAC', 60)
    set_angle('ACB', 30)
    set_angle('ADB', 45)
    set_angle('ABD', 45)
    set_angle('BAD', 90)
    set_angle('ABC', 90)

    assert round(get_angle('AEB'), 6) == 75

    clear()

