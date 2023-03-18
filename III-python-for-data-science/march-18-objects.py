# from math import sqrt


# print(sqrt(6))
# print(6 ** (1/2))
# print(6 ** 0.5)

class Car:
    def __init__(self, brand, v_max, weight, length, width, price, year_of_production, owner):
        self.brand = brand
        self.v_max = v_max
        self.weight = weight
        self.length = length
        self.width = width
        self.price = price
        self.year_of_production = year_of_production
        self.owner = owner
        self.running = False

