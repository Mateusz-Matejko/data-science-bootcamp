from math import pi


def cuboid_volume(base_a: float, base_b: float, base_c: float) -> float:
    return base_a * base_b * base_c


def roller_volume(r: float, height: float) -> float:
    return (2 * pi * r) * height


