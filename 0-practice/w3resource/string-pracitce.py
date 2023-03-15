# 1. Write a Python program to calculate the length of a string. Go to the editor
import pprint

txt = "Ala ma kota."


def task_1(sample_txt):
    return len(sample_txt)


length_of_sting = len(txt)

# 2. Write a Python program to count the number of characters (character frequency) in a string. Go to the editor

sample_string = "google.com"
answer_dict = {}


def task_2(sample_string):
    for i in sample_string:
        if i in answer_dict.keys():
            answer_dict[i] += 1
        else:
            answer_dict[i] = 1

# print(answer_dict)


# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.


def task_3(sample_string):
    if len(sample_string) >= 2:
        return sample_string[0:2] + sample_string[-2:]
    return "Empty string"


sample_string_list = ["w3resource", "w3", "w"]

# for i in sample_string_list:
    # print(new_string(i))


# 4. Write a Python program to get a string from a given string where all occurrences
# of its first char have been changed to '$', except the first char itself. Go to the editor


def task_4(original_string):
    char = original_string[0]
    return char + original_string.replace(char, "$")[1:]


# print(change_to_dolar("restart"))


# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first
# two characters of each string. Go to the editor


def task_5(string_1, string_2):
    string_merged = (string_2[0] + string_1[1:] + " " + string_1[0] + string_2[1:])
    return string_merged


string_1 = "abcdefgh"
string_2 = "ijklmnop"

# print(task_5(string_1, string_2))


# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3,
# leave it unchanged. Go to the editor


def task_6(string_1):
    if len(string_1) < 3:
        return string_1
    if string_1[-3:] == "ing":
        return string_1 + "ly"
    return string_1 + "ing"


tests_list_x = ["doing", "ly", "why", "flying", "matyly", "karzel"]

# for i in tests_list_x:
#    print(task_6(i))


# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.


def task_7(string_1):
    string_1 = string_1.lower()
    if "not poor" in string_1:
        return string_1.replace("not poor", "good")
    elif "not" in string_1:
        return string_1.replace("not", "good")
    elif "poor" in string_1:
        return string_1.replace("poor", "good")
    elif "good" in string_1:
        return string_1.replace("good", "poor")


test_scenario = ["The lyrics is not that poor!", "The lyrics is good",
                 "This man is poor", "This is not poor behaviour from you"]

# for i in test_scenario:
#     print(task_7(i))


# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9


def task_8(list_of_words):
    record = 0
    longest_word = ""
    for i in list_of_words:
        if len(i) > record:
            record = len(i)
            longest_word = i
    return longest_word, record


list_of_words = ["tarala", "kolejorz", "trampki", "budynek", "wiezowiec", "maskotka", "dzieckiotko",
                 "jezusek", "maryja", "konstantynopolitaneczka", "konstantynopol"]

word, record = task_8(list_of_words)


# 9. Write a Python program to remove the nth index character from a nonempty string. Go to the editor


def task_9(string_1, index_of_character):
    return string_1[:(index_of_character)] + string_1[index_of_character+1:]


# print(task_9("konstantynopolitaneczka", 2))


# 10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged. Go to the editor


def task_10(string_1):
    fist = string_1[0]
    last = string_1[-1]
    return last + string_1[1:-1] + fist


# print(task_10("Konstantynopolitaneczka Calineczka!"))

# 11. Write a Python program to remove characters that have odd index values in a given string. Go to the editor


# 12. Write a Python program to count the occurrences of each word in a given sentence. Go to the editor


test_sentence = "Hello, world! world i am as usu as sal as you are wold hello hello hi hi yo yo YOYOOYOYOYOYOYO motherfucker"


def task_12(sample_sentence):
    answer_dict = {}
    list_of_words = []
    while True:
        try:
            x, z = sample_sentence.split(" ", 1)
        except ValueError:
            list_of_words.append(z)
            break
        sample_sentence = z
        list_of_words.append(x)
    for i in list_of_words:
        if i in answer_dict.keys():
            answer_dict[i] += 1
        else:
            answer_dict[i] = 1
    return answer_dict

sorted_d = task_12(test_sentence)
sorted_d = sorted(sorted_d.items(), key=lambda x: x[1], reverse=True)

pprint.pprint(sorted_d)


