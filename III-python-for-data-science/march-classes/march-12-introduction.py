x = 10


def grade_counter(number_of_correct, amount_of_questions):
    percent = number_of_correct/amount_of_questions
    if percent > 0.89:
        print(5.0)
    elif percent > 0.75:
        print(4.5)
    elif percent > 0.69:
        print(4.0)
    elif percent > 0.59:
        print(3.5)
    elif percent > 0.49:
        print(3.0)
    else:
        print(2.0)


def grade_counter_fixed(number_of_correct, amount_of_questions):
    percent = number_of_correct/amount_of_questions
    box_levels = [0.89, 0.75, 0.69, 0.59, 0.49, 0]
    box_grade = [5.0, 4.5, 4.0, 3.5, 3,0, 2.0]
    counter = 0
    for i in box_levels:
        if percent > i:
            print(box_grade[counter])
        counter += 1
        break


def show_temp_status(temperature):
    if temperature < 36.4:
        return "Wychlodzenie"
    elif temperature < 36.8:
        return "W normie"
    elif temperature < 37:
        return "Stan podgorączkowy"
    return 'Gorączka'


for i in range(35, 38, 2):
    print(show_temp_status(i))
