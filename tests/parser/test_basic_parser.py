from quick_input.abc import A, B, C
from quick_input import link, submit, set_angle, get_angle


def test_basic_parser():
    link(A, B)
    link(A, C)
    link(B, C)

    set_angle('ABC', 90)
    set_angle('ACB', 30)

    get_angle('BAC')

    submit()

