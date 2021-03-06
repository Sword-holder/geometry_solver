from quick_input.abc import A, B, C, D, E, F
from quick_input import link, clear, set_angle, get_angle


def test_advanced_parser():
    link(A, D, B)
    link(A, E, C)
    link(D, F, C)
    link(B, F, E)
    link(B, C)

    set_angle('BAC', 45)
    set_angle('ABE', 40)
    set_angle('ACD', 20)

    assert round(get_angle('EFC'), 6) == 75

    clear()

