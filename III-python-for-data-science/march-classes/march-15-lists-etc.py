def manage_list(functionality, object_x, change):
    functionality = functionality.lower()
    if functionality not in ["add", "remove"]:
        raise ValueError("Wrong functionality passed")
    if functionality == "add":
        object_x.append(change)
        return
    object_x.pop()


list_x = ["Cat", "Dog", "Frog"]
manage_list("remove", list_x, "")
# print(list_x)

phone_list = {
    "Marek": 573-235-211,
    "Darek": 609-133-100
}


def add_contacts(dictionary_sample, key_name, phone_number):
    if key_name in dictionary_sample:
        print("Kontakt istnieje w słowniku.")
        return
    dictionary_sample[str(key_name)] = str(phone_number)
    print("Klucz dodano.")


# TUPLE

metadata_tuple = ("Python w DS", "3.11", "2022-07-11")
metadata_list = list(metadata_tuple)

# print(metadata_tuple, type(metadata_tuple))
# print(metadata_list, type(metadata_list))

# SET

numbers = {1, 2, 3, 5, 6, 6, 8, 9, 9, 10, 1, 2, 3, 4}
print(numbers)

wowowo = frozenset(numbers)
print(wowowo)

