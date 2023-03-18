from math import pi


def rectangle_are(a: float, b: float) -> float:
    return a * b


def rectangle_circuit(a: float, b: float) -> float:
    return (2 * a) + (2 * b)


def is_square(a: float, b: float) -> float:
    return a == b


def circle_circuit(r: float) -> float:
    return pi * (r ** 2)


def circle_field(r: float) -> float:
    return 2 * pi * r