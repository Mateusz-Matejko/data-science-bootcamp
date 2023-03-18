# 1. Write a Python program to sum all the items in a list. Go to the editor


sample_list = []
for i in range(1, 115):
    sample_list.append(i)


def task_1(sample_list: list) -> int:
    return sum(sample_list)

# print(task_1(sample_list))

# 2. Write a Python program to multiply all the items in a list. Go to the editor


def task_2(sample_list: list) -> int:
    result = sample_list[0]
    for i in sample_list:
        result = i * result
    return result

# print(task_2(sample_list))

# 3. Write a Python program to get the largest number from a list. Go to the editor


def task_3(sample_list: list) -> int:
    return sorted(sample_list, reverse=True)[0]

# print(task_3(sample_list))


# 4. Write a Python program to get the smallest number from a list. Go to the editor


def task_4(sample_list: list) -> int:
    return sorted(sample_list)[0]

# print(task_4(sample_list))


# 5. Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same. Go to the editor
sample_list = ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2


def task_5(sample_list: list) -> int:
    result = 0
    for i in sample_list:
        if len(i) > 2 and i[0] == i[-1]:
            result += 1
    return result

# print(task_5(sample_list))


# 6. Write a Python program to get a list, sorted in increasing order by the last element in each
# tuple from a given list of non-empty tuples. Go to the editor
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


def task_6(sample_list: list) -> list:
    ...


# 7. Write a Python program to remove duplicates from a list. Go to the editor


def task_7(sample_list: list) -> list:
    return sorted(set(sample_list))


# print(task_7([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1 ]))


# 8. Write a Python program to check if a list is empty or not. Go to the editor


sample_list = [[], [1, 2, 3], [1, 5, 556], [], ["as"], [14]]


# def task_8(sample_list: list) -> bool:
#     if not sample_list:
#         return "Empty"
#     return "Not empty"


# for i in sample_list:
#     print(task_9(i))

# 9. Write a Python program to clone or copy a list. Go to the editor


# def task_9(sample_list: list) -> list:
#     return sample_list.copy()


# sample_list_2 = task_10(sample_list)


# 10. Write a Python program to find the list of words that are longer than n from a given list of words. Go to the editor

sample_string = "Ala ma kota a kot ma pierdolca i downa bo to jest kot chory na glowe i na ryj generalnie jest dosc walniet na ryj ten kot"


def task_10(given_length: int, given_string: str) -> list:
    result = []
    txt = given_string.split(" ")
    for i in txt:
        if len(i) > given_length:
            result.append(i)
    return result


# print(task_10(5, sample_string))


# 11. Write a Python function that takes two lists and returns True if they have at least one common member. Go to the editor

samp_list_1 = [1, 2, 3, 4, 5]
samp_list_2 = [6, 7, 8, 9, 10]
samp_list_3 = [11, 12, 13, 14, 15, 1, 16, 17]
samp_list_4 = [1, 2, 3, 4, 5, 6, 7]


def task_11(sample_list_1: list, sample_list_2: list):
    for i in sample_list_1:
        if i in sample_list_2:
            return True
    return False


# print(task_11(samp_list_1, samp_list_2))
# print(task_11(samp_list_3, samp_list_4))

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']


def task_12(sample_list: list, remove_1 = 0, remove_2 = 4) -> list:
    return sample_list.pop(0).pop(4)


print(task_12(sample_list))
