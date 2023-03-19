# funkcja suma 2 argumentow

def summary_2(a: int, b: int):
    return a + b


# funkcja dla 3 argumentow
def summary_3(a: int, b: int, c:int):
    return a + b + c


def summary_ultimate(*args) -> None:
    print(f"Elements: {args}")
    print(sum(args))


# summary_ultimate(1, 2, 3, 4, 5)
# summary_ultimate(1, 2, 3, 4, 5, 6)
# summary_ultimate(3, 6, 7, 8)
# summary_ultimate(6, 5)


# kwargs

def fun_with_option(**kwargs):
    if kwargs.get("power", -1) == -1:
        print("Nie ma opcji potegi")
    else:
        print(2 ** kwargs.get("power", -1))

    if kwargs.get("sqrt", False):
        print("Chciałeś pierwiastkować?")
    else:
        print("Opcja sqrt jest na false")


def mathematical_operations(operation: str, *args) -> float:
    res = 0
    error_box = []
    operation = operation.lower()
    list_of_allowed_operations = ["addition", "subtraction", "multiplication", "division"]
    if operation not in list_of_allowed_operations:
        raise ValueError(f"Unknown operation passed!\n"
                         f"List of allowed operations: {list_of_allowed_operations}\n"
                         f"You passed: {operation}")
    elif operation == "addition":
        for i in args:
            try:
                i = int(i)
                res += i
            except ValueError:
                error_box.append(i)
                continue
        return res, error_box
    elif operation == "subtraction":
        for i in args:
            try:
                i = int(i)
                res -= i
            except ValueError:
                error_box.append(i)
                continue
        return res, error_box
    elif operation == "multiplication":
        res = args[0]
        for i in args[1:]:
            try:
                i = int(i)
                res *= i
            except ValueError:
                error_box.append(i)
                continue
        return res, error_box
    elif operation == "division":
        res = args[0]
        for i in args[1:]:
            try:
                i = int(i)
                res /= i
            except (ZeroDivisionError, ValueError):
                error_box.append(i)
                continue
        return res, error_box


print(mathematical_operations("addition", 3, 3, "ma", 4, 6))
print(mathematical_operations("multiplication", 3, 35, 4, "pieseł", 3, 3))
print(mathematical_operations("subtraction", 3, "kot", 6, 7, 8))
print(mathematical_operations("division", 3, 0, "dupa", 6, 7, 3))
