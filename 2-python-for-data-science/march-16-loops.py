
data = [
    ("Adam", 750),
    ("Ewa", 250),
    ("Jakub", 200),
    ("Elżbieta", 1000),
    ("Adam", 400),
    ("Ewa", 300)
]


def homework(starting_list):
    result = {}
    for i in starting_list:
        if i[0] not in result.keys():
            result[i[0]] = i[1] / 50
    return result


# print(homework(data))

def task_1(given_int:int):
    for i in range(given_int+1):
        if i % 2 == 0:
            print(i)


def task_2():
    start_num = 2
    while start_num < 10:
        print(start_num ** 0.5)
        start_num += 1


def task_3(start_num, end_num):
    sum = 0
    for i in range(start_num, end_num+1):
        sum += i
