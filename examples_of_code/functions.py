
# def func_name(*args, **kwargs):
#     """Documentation"""
#     # return result
#
#
# # Ця функція повертає кортеж з трьох значень. При виклику функції можна "розпакувати" цей кортеж в окремі змінні.
# def calculation(xa, xb):
#     addition = xa + xb
#     substruction = xa - xb
#     multiplication = xa * xb
#     return addition, substruction, multiplication
#
# a, b, c = calculation(2, 2)
# print(f"addiction: {a}, substruction: {b}, multiplication: {c}")

########


# def say_hi(name, age):
#     """
#     Gether the information about the user (name, surname, age)
#     and enter greeting.
#     It uses sub-functions for verification and formatting the data.
#     """
#     first_name = input_and_check_name("Input your first name: ")
#     # last_name = input_and_check_name("Input your last name: ")
#     age = input_and_check_age("Input your age: ")
#
#     # if "Error" in first_name or "Error" in last_name or "Error" in age:
#     if "Error" in first_name or "Error" in age:
#         print(first_name)
#         # print(last_name)
#         print(age)
#     else:
#         # greeting = f"Hi! My name is {first_name} {last_name} and I am {age} years old."
#         greeting = f"Hi! My name is {first_name} and I am {age} years old."
#         print(greeting)
#         return greeting  # Додано для тестів
#
#
# def input_and_check_name(prompt):
#     """
#     Asks about the name and surname and checks it with check_name.
#     """
#     name = input(prompt)
#     return check_name(name)
#
#
# def input_and_check_age(prompt):
#     """
#     Asks about the age and checks it with check_age.
#     """
#     age = input(prompt)
#     return check_age(age)
#
#
# def check_name(name):
#     """
#     Check if name and surname contain only letters and format first letter to capital.
#     """
#     if not name.isalpha():
#         return "Error: The name must contain only letters."
#     else:
#         return name.capitalize()
#
#
# def check_age(age):
#     """
#     Check if the age contains only digits.
#     """
#     if not age.isdigit():
#         return "Error: The age must contain only numbers."
#     else:
#         return age
#
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')


