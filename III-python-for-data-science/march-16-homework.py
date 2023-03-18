# Zadanie 01
# Napisać funkcję, która zamienić stopnie Celsjusza na Kelwina. Funkcja przyjmuje jako argument temperaturę w C, a funkcja zwraca temperaturę w K. Więcej informacji o konwersji: https://www.rapidtables.org/pl/convert/temperature/how-celsius-to-kelvin.html

def temp_converter(temperature: float) -> float:
    return float(temperature-217.15)

# Obie wartości maja być typu float
#
# Zadanie 02
# Napisać funkcję, która jako argument przyjmuje dowolny łańcuch znakowy, a następnie zwraca słownik zliczający ilość
# wystąpień każdego słowa (kot =/= kota). Podpowiedź możemy użyć metody split(" ").


def word_counter(sample_string: str) -> dict:
    result = {}
    for i in sample_string.split(" "):
        if i in result.keys():
            result[i] += i
        else:
            result[i] = 1
    return result


# Zadanie 03
# Użytkownik podaje trzy liczby całkowite. Następnie program zwraca informację, która z podanych liczb jest największa
# (dla odważnych - możecie również weryfikować czy dane liczbą są takie same).


def number_compression(n_1, n_2, n_3):
    list_of_numbers = [n_1, n_2, n_3]
    if len(list_of_numbers) == len(set(list_of_numbers)):
        return sorted(list_of_numbers[-1])
    result = ""
    if n_1 in [n_2, n_3]:
        if n_1 == n_2:
            result += f"{n_1} and {n_2} are equal.\n"
        if n_1 == n_3:
            result += f"{n_1} and {n_3} are equal.\n"
    if n_2 == n_3:
        result += f"{n_3} and {n_3} are equal.\n"
    return result


# print(number_compression(1, 2, 2))

# Zadanie 04
# Napisać program, gdzie użytkownik podaje liczby całkowite i je sumuje. Program działa dopóki użytkownik nie poda
# liczby ujemnej. Po podaniu liczby ujemnej program wyświetla sumę podanych poprzednich liczb.


def numbers_summarize(list_of_numbers: list) -> int:
    result = 0
    for i in list_of_numbers:
        if i >= 0:
            result += i
        else:
            return result
    return result


# Zadanie 05
# Napisać funkcję, która konwertuje liczbę z systemu dziesiętnego na binarny (nie używamy funkcji wbudowanych w Pythonie)


def convert_from_system_to_system(casual_number: int) -> str:
    sample_result = ""
    while casual_number > 0:
        sample_result += str(casual_number % 2)
        casual_number = int(casual_number/2)
    return sample_result[::-1]


# print(convert_from_system_to_system(12))


# Zadanie 06
# Użytkownik podaje liczbe całkowitą. Następnie program zwraca sumę CYFR z których składa się podana liczba.
# Przykładowo: użytkownik podaje 1307, program zwraca 11 (1+3+0+7). Podpowiedź: konwersja na str

def number_converter_task(sample_number: int) -> int:
    result = 0
    for i in str(sample_number):
        result += int(i)
    return result


# print(number_converter_task(1307))


# Zadanie 07
# Napisać program, gdzie użytkownik podaje n łańcuchów znakowych (ilość n również definiuje wcześniej użytkownik).
# Następnie program zwraca informacje ile łańcuchów znakowych jest unikatowych. :)
#
# Przykładowo: użytkownik podał n = 3. Następnie podał trzy łańcuchy znakowe: Kot,
# Pies, Kot. Program zwróci informacje, że ilość UNIKATOWYCH łańuchów znakowych to: 2.


def homework_unique_strings(amount_of_strings):
    strings_container = []
    for i in range(amount_of_strings):
        strings_container.append(input("What's your word? "))
    print(f"Amount of unique words: {len(set(strings_container))}")


homework_unique_strings(3)
