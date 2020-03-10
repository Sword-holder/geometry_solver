from quick_input.abc import A, B, C, D, O
from quick_input import link, submit, set_angle, get_angle


def test_parser_example1():
    link(A, D)
    link(A, B)
    link(A, O, C)
    link(B, O, D)
    link(B, C)

    set_angle('BAC', 60)
    set_angle('ACB', 30)
    set_angle('ADB', 45)
    set_angle('ABD', 45)
    set_angle('BAD', 90)
    set_angle('ABC', 90)

    get_angle('AOB')

    submit()

