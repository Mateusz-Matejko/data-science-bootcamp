sample_dictionary = {
    "Marcin": 253,
    "Dorota": 531,
    "Kamil": 512,
    "Faustyna": 1435,
    "Gabriella": 13,
    "Grazyna": 73,
    "Mateusz": 999,
    }
# 1. Write a Python script to sort (ascending and descending) a dictionary by value. Go to the editor


def task_1(passed_dict: dict) -> dict:
    return dict(sorted(passed_dict.items(), key=lambda x: x[1]))


print(task_1(sample_dictionary))

# 2. Write a Python script to add a key to a dictionary. Go to the editor
#
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
#
#
#
# 3. Write a Python script to concatenate the following dictionaries to create a new one. Go to the editor
#
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
#
#
# 4. Write a Python script to check whether a given key already exists in a dictionary. Go to the editor
#
#
#
# 5. Write a Python program to iterate over dictionaries using for loops. Go to the editor
#
#
#
# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#
#
# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys. Go to the editor
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
#
#
# 8. Write a Python script to merge two Python dictionaries. Go to the editor
#
#
# 9. Write a Python program to iterate over dictionaries using for loops. Go to the editor
#
#
# 10. Write a Python program to sum all the items in a dictionary. Go to the editor
#
#
# 11. Write a Python program to multiply all the items in a dictionary. Go to the editor
#
#
# 12. Write a Python program to remove a key from a dictionary. Go to the editor