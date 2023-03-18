# from math import sqrt


# print(sqrt(6))
# print(6 ** (1/2))
# print(6 ** 0.5)

class Car:
    def __init__(self, brand, v_max, weight, length, width, price, year_of_production, owner, color):
        self.brand = brand
        self.v_max = v_max
        self.weight = weight
        self.length = length
        self.width = width
        self.price = price
        self.year_of_production = year_of_production
        self.owner = owner
        self.color = color
        self.running = False

    def switch(self):
        if self.running:
            self.running = False
        else:
            self.running = True

    def __str__(self):
        return f"{self.brand}, {self.v_max}, {self.price}"


# tico = Car("Tico", 120, 400, 180, 70, 1500, 1999, "Mariusz", "yellow")
# seria_3 = Car("BMW", 250, 1600, 350, 130, 50000, 2012, "Mateusz", "blue")

# print(tico.color)
# print(seria_3.color)


class Student:
    def __init__(self, name, surname):
        self. name = name
        self.surname = surname
        self.list_of_grades = []
        self.average_grade = None

    def add_grade(self, grade):
        if grade in range(1, 6, 1):
            self.list_of_grades.append(grade)
            self.average_grade = sum(self.list_of_grades) / len(self.list_of_grades)

    def __str__(self):
        return f"{self.name} {self.surname}: {self.average_grade}"

    def __int__(self):
        print("__int__ // Sum of grades: ", end="")
        return int(sum(self.list_of_grades))

    def __float__(self):
        print("__float__ // Average grade: ", end="")
        return float(round(self.average_grade, 2))


class Animal:
    def __init__(self, name, legs_count, eyes_count):
        self.name = name
        self.legs_count = legs_count
        self.eyes_count = eyes_count
        self.is_alive = True

    def __str__(self):
        return f"Animal name: {self.name}"

    def change_alive_status(self):
        if self.is_alive:
            self.is_alive = False
        else:
            self.is_alive = True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise ValueError("Name of animal should be type: str")
        self._name = name

    @property
    def legs_count(self):
        return self._legs_count

    @legs_count.setter
    def legs_count(self, legs_count):
        if type(legs_count) != int:
            raise ValueError("Legs count should be type: int")
        self._legs_count = legs_count

    @property
    def eyes_count(self):
        return self._eyes_count

    @eyes_count.setter
    def eyes_count(self, eyes_count):
        if type(eyes_count) != int:
            raise ValueError("Eyes count should be type: int")
        self._eyes_count = eyes_count


class Dog(Animal):
    def __int__(self, name, legs_count, eyes_count):
        super().__init__(name=name, legs_count=legs_count, eyes_count=eyes_count)


class Cat(Animal):
    def __init__(self, name, legs_count, eyes_count, race):
        super().__init__(name, legs_count, eyes_count)
        self.race = race

    def __str__(self):
        print(super().__str__())
        return f"Race: {self.race}, Name: {self.name}"


cat1 = Cat("Fred", 4, 2, "Tygrys koci")


# print(cat1)

class Person:
    def __init__(self, name, surname, age, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name} \nSuranme: {self.surname}\n Adress: {self.address}"

    def check_is_adult(self):
        return self.age >= 18

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise ValueError("Name of person should be type: str")
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        if type(surname) != str:
            raise ValueError("Surname of person should be type: str")
        self._surname = surname

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if type(age) != int:
            raise ValueError("Age type of person should be type: int")
        self._age = age

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if type(address) != str:
            raise ValueError("Address of person should be type: str")
        self._surname = address


class Customer(Person):
    def __init__(self, name, surname, age, address, login):
        super().__init__(name, surname, age, address)
        self.login = login
        self.orders = []
        self.total_orders_cost = 0

    def __str__(self):
        return f"{super.__str__()}, login: {self.login}"

    def add_orders(self, product, cost):
        if self.check_is_adult():
            self.orders.append((product, cost))
            self.total_orders_cost += cost
        else:
            print("User isn't old enough to make purchase")

    def show_orders(self):
        return self.orders

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        if type(login) != str:
            raise ValueError("Surname of person should be type: str")
        self._login = login


c1 = Customer(name="Jan", surname="Kowalski", age=24, address="Sopot, Poland", login="kowal-jan01")

print(c1.show_orders())
c1.add_orders("Korniszon", 17)
print(c1.show_orders())
print(c1.total_orders_cost)


# c1 = Cat("Burek", 4, 2)
# print(c1.alive)
#
#
# an1 = Animal("Tygrys", 4, 4)
# print(an1)


#     @property
#     def average_grade(self):
#         return self._average_grade
#
#     @average_grade.setter
#     def average_grade(self, average_grade):
#         self._average_grade = sum(self.list_of_grades) / len(self.list_of_grades)
#


# ja = Student("Mateusz", "M")
#
# ja.add_grade(5)
# print(ja.average_grade)
#
# ja.add_grade(4)
# ja.add_grade(4)
#
# print(ja.list_of_grades)
#
# print(int(ja))
# print(float(ja))