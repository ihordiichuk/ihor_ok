# my_string = input("Input variable: ")
# result = False
#
# if my_string.isidentifier():
#     if my_string == "_" or my_string.islower():
#         result = True
#
# print(result)
#
# Створення словника
# student = {'name': 'Іван', 'age': 21, 'grade': 'A'}

# Отримання значення за ключем
# print(student.get('name'))  # Виведе: Іван

# Отримання всіх ключів
# print(student.keys())  # Виведе: dict_keys(['name', 'age', 'grade'])

# Отримання всіх значень
# print(student.values())  # Виведе: dict_values(['Іван', 21, 'A'])


# student = { 'name': 'Fred', 'age': 33, 'grade': 'A'}
# print(student.get('name'))
# print(student.keys())
# print(student.values())

# from collections import OrderedDict
#
# # Створення OrderedDict
# ordered_student = OrderedDict()
# ordered_student['name'] = 'Іван'
# ordered_student['age'] = 21
# ordered_student['grade'] = 'A'
#
# print(ordered_student)  # Виведе: OrderedDict([('name', 'Іван'), ('age', 21), ('grade', 'A')])
#
# # Переміщення елемента в кінець
# ordered_student.move_to_end('name')
# print(ordered_student)  # Виведе: OrderedDict([('age', 21), ('grade', 'A'), ('name', 'Іван')])


from collections import

ordered_student = ordereddict()
ordered_student['name'] = 'Fred'
ordered_student['age'] = 33
ordered_student['grade'] = 'A'

print(ordered_student)



