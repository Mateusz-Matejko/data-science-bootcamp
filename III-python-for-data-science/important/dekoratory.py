import datetime


def parent():
    def first():
        print("First")

    def second():
        print("Second")

    print("Parent")
    first()
    second()

# parent()


def my_add(a: float, b: float) -> float:
    return a + b


def my_sub(a: float, b: float) -> float:
    return a - b


def line_decorator(func):
    def wrapper():
        print("-" * 25)
        func()
        print("-" * 25)
    return wrapper


@line_decorator
def my_date() -> None:
    print(datetime.datetime.now())


@line_decorator
def my_course() -> None:
    print("Kurs to: ARPDataPL9")


"""
Dekoratory które warto znac: 
    -Class method
    -Property 
    -Setter
"""


# Dekorator dla funkcji, która nie przyjmuje argumentów i nic nie zwraca
def line_decorator(func):
    def wrapper():
        print(f"**********************************************")
        func()
        print(f"**********************************************")
    return wrapper


# Dekorator dla funkcji, która przyjmuje argumenty oraz niczego nie zwraca
def trigger_info_none(func):
    def wrapper(*args, **kwargs):
        print(f"Wywołano funkcję {func}")
        func(*args, **kwargs)
    return wrapper


# Dekorator dla funkcji, która przyjmuje argumenty oraz coś zwraca
def trigger_info_return(func):
    def wrapper(*args, **kwargs):
        print(f"Wywołano funkcję {func}")
        return func(*args, **kwargs)
    return wrapper


def sample_decorator(func):
    def wrapper():
        func()
        print("THE END")
    return wrapper


@sample_decorator
def sample_function():
    print("huehuehue")


sample_function()