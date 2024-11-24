# Завдання 1
#
# Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]
#
# а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.
#
# б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.
#
# в) Порахувати середню вік усіх людей із початкового списку.
#
#
##### option 1
# humans_list = [
#     {"name": "John", "age": 15},
#     {"name": "Doron", "age": 51},
#     {"name": "Ramachandra", "age": 45},
#     {"name": "Yoth-Sototh", "age": 100000}
# ]
#
# # a) Find the name of the youngest person (or people if tied)
# min_age = min(person["age"] for person in humans_list)
# youngest_people = [person["name"] for person in humans_list if person["age"] == min_age]
# print(f"Youngest person(s): {youngest_people}")
#
# # b) Find the longest name (or names if tied)
# max_name_length = max(len(person["name"]) for person in humans_list)
# longest_names = [person["name"] for person in humans_list if len(person["name"]) == max_name_length]
# print(f"Longest name(s): {longest_names}")
#
# # c) Calculate the average age
# average_age = sum(person["age"] for person in humans_list) / len(humans_list)
# # print(f"Average age: {average_age:.2f}")
# print(f"Average age: {str(round(average_age, 2))}")
#
#
##### option 2
# #
# humans_list = [
#     {"name": "John", "age": 15},
#     {"name": "Doron", "age": 51},
#     {"name": "Ramachandra", "age": 45},
#     {"name": "Yoth-Sototh", "age": 100000}
# ]
#
# min_age = None
# youngest_people = []
#
# max_name_len = 0
# longest_name = []
#
# average_age = 0
#
# total_age = 0
#
# for person in humans_list:
#     age = person["age"]
#     name = person["name"]
#
#     # Track the youngest person
#     if min_age is None or age < min_age:
#         min_age = age
#         youngest_people = [name]
#     elif age == min_age:
#         youngest_people.append(name)
#     # else:
#     #     continue
#     # result_1 = name
#
#     # Track the longest name
#     if len(name) > max_name_len:
#         max_name_len = len(name)
#         longest_name = [name]
#     elif len(name) == max_name_len:
#         longest_name.append(name)
#     # else:
#     #     continue
#     # result_2 = name
#
#     # Sum all ages to calculate the average later
#     total_age += age
#
#     # Calculate the average age
# average_age = total_age / len(humans_list)
#
# # Output results
# print("Youngest People:", youngest_people)
# print("Longest Name(s):", longest_name)
# print("Average Age:", average_age)
#
#
# Завдання 2
#
# Дано два словники my_dict_1 і my_dict_2.
#
# а) Створити список із ключів, які є в обох словниках.
#
# б) Створити список із ключів, які є у першому, але немає у другому словнику.
#
# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
#
# г) Об'єднати ці два словники у новий словник за правилом:
#
# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
#
# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},

#  code
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

###############################
#
# my_dict_1 = {1: 1, 2: 2}
# my_dict_2 = {11: 11, 2: 22}
#
# # a) List of keys common to both dictionaries
# common_keys = list(set(my_dict_1.keys()) & set(my_dict_2.keys()))
# print(f"Common keys: {common_keys}")
#
# # b) List of keys in the first dictionary but not in the second
# keys_in_first_only = list(set(my_dict_1.keys()) - set(my_dict_2.keys()))
# print(f"Keys in the first dictionary but not in the second: {keys_in_first_only}")
#
# # c) Dictionary with key-value pairs from the first dictionary for keys not in the second
# dict_first_not_in_second = {key: my_dict_1[key] for key in keys_in_first_only}
# print(f"Dictionary with keys from the first but not in the second: {dict_first_not_in_second}")
#
# # d) Merge dictionaries with the specified rules
# merged_dict = {}
# for key in set(my_dict_1.keys()).union(my_dict_2.keys()):
#     if key in my_dict_1 and key in my_dict_2:
#         merged_dict[key] = [my_dict_1[key], my_dict_2[key]]
#     elif key in my_dict_1:
#         merged_dict[key] = my_dict_1[key]
#     else:
#         merged_dict[key] = my_dict_2[key]
#
# print(f"Merged dictionary: {merged_dict}")