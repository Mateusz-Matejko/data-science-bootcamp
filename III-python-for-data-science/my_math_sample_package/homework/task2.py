def square_function(x: float) -> float:
    try:
        x = float(x)
    except ValueError:
        print("Wrong argument passed, unable to convert to type: float")
        return
    return x ** 2


def second_degree_element(x: float) -> float:
    try:
        x = float(x)
    except ValueError:
        print("Wrong argument passed, unable to convert to type: float")
    return x ** 0.5


def harmonic_sequence(x: int) -> float:
    try:
        x = int(x)
    except ValueError:
        print("Wrong argument passed, unable to convert to type: float")
    sequence_itself = [1]
    denominator = 2
    for i in range(x - 1):
        sequence_itself.append(1/denominator)
        denominator += 1
    return sequence_itself[x - 1]

