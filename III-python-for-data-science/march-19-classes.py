# class WatchingPlaytime:
#     def __init__(self, start, playtime_seconds):
#         self.start = start
#         self.playtime_seconds = playtime_seconds
#         self.second_in_hour = 3600
#         self.seconds_in_minute = 60
#         self.playtime_left_after_first_hour = 0
#         self.seconds_in_first_hour = 0
#         self.result = {}
#         self.start_hour = 0
#         self.start_minute = 0
#         self.start_second = 0
#
#     def count_first_hours(self):
#         hour, minute, second = self.start.split(":")
#         self.start_hour, self.start_minute, self.start_second = int(hour), int(minute), int(second)
#         sum_of_second_in_this_hour = self.start_minute * 60 + self.start_second
#         if self.playtime_seconds >= self.second_in_hour - sum_of_second_in_this_hour:
#             self.seconds_in_first_hour = self.second_in_hour - sum_of_second_in_this_hour
#             self.result[hour] = self.seconds_in_first_hour
#             self.playtime_left_after_first_hour = self.playtime_seconds - (self.second_in_hour - sum_of_second_in_this_hour)
#         else:
#             self.result[hour] = self.playtime_seconds
#
#     def following_hours(self):
#         full_hours = int(self.playtime_left_after_first_hour/self.second_in_hour)
#         if full_hours > 0:
#             for i in range(self.start_hour + 1, self.start_hour + full_hours + 1):
#                 self.result[i] = self.second_in_hour
#         seconds_left_in_last_hour = self.playtime_seconds - \
#                                     ((self.second_in_hour * full_hours) + self.seconds_in_first_hour)
#         self.result[self.start_hour + full_hours + 1] = seconds_left_in_last_hour
#         print(self.result)
#
#
# task1 = WatchingPlaytime("15:50:33", 6000)
#
#
# task1.count_first_hours()
# task1.following_hours()

# class Person:
#     def __init__(self, f_name: str, l_name: str, age: int) -> None:
#         self.f_name = f_name
#         self.l_name = l_name
#         self.age = age
#
#
# p1 = Person("Jan", "Kowalski", 30)
# print(p1.age)


class Prodcut:
    def __init__(self, name: str, category: str, sn: str, price: float):
        self.name = name
        self.category = category
        self.__sn = sn
        self.price = price

    @property
    def sn(self):
        return self.__sn

    @sn.setter
    def sn(self, new_sn):
        self.__sn = new_sn

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            self._price = 0.01
        else:
            self._price = new_price


karton = Prodcut("Karton", "Pudelka", "f13513", 0)

print(karton.price)

karton.price = -1

print(karton.price)