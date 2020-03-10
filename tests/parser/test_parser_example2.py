from quick_input.abc import A, B, C, D, E
from quick_input import link, submit, set_angle, get_angle, set_length, get_length


def test_parser_example2():
    link(A, B, C, E)
    link(B, D)
    link(D, E)

    set_angle('ABD', 120)
    set_angle('BDE', 30)

    set_length('BD', 210)

    get_length('DE')

    submit()
