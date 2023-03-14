# 1. Write a Python program to calculate the length of a string. Go to the editor
import pprint

txt = "Ala ma kota."
length_of_sting = len(txt)

# 2. Write a Python program to count the number of characters (character frequency) in a string. Go to the editor

sample_string = "google.com"
answer_dict = {}
for i in sample_string:
    if i in answer_dict.keys():
        answer_dict[i] += 1
    else:
        answer_dict[i] = 1
# print(answer_dict)

# expected result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1


# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.


# If the string length is less than 2, return the empty string instead. Go to the editor

sample_string = "w3resource"


def new_string(sample_string):
    if len(sample_string) >= 2:
        return sample_string[0:2] + sample_string[-2:]
    return "Empty string"


sample_string_list = ["w3resource", "w3", "w"]

# for i in sample_string_list:
    # print(new_string(i))

# Sample sting : 'w3 resouce'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String


# 4. Write a Python program to get a string from a given string where all occurrences
# of its first char have been changed to '$', except the first char itself. Go to the editor


def change_to_dolar(original_string):
    char = original_string[0]
    return char + original_string.replace(char, "$")[1:]


# print(change_to_dolar("restart"))

# Sample String : 'restart'
# Expected Result : 'resta$t'


# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

#
# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

#
# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

#
# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one. Go to the editor
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

#
# 9. Write a Python program to remove the nth index character from a nonempty string. Go to the editor

#
# 10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged. Go to the editor

#
# 11. Write a Python program to remove characters that have odd index values in a given string. Go to the editor

#
# 12. Write a Python program to count the occurrences of each word in a given sentence. Go to the editor


