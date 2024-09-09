# a, b, *left_1 = (1, 2, 3, 4, 5)
# print(a)
# print(b)
# print(left_1)
#
#
# my_input = int(input("Please add 4 digits: "))
# thousands, left_1 = divmod(my_input, 1000)
# hundreds, left_2 = divmod(left_1, 100)
# tens, ones = divmod(left_2, 10)
#
# print(thousands)
# print(hundreds)
# print(tens)
# print(ones)
from lessons.lesson_3 import value_list

# action = " "
#
# if action == "+" or action == "-":      #якщо дія + чи - виводиться !!!! інакше &&&&
#     print("!!!!!!")
# else:
#     print("&&&&")


### match case

# weather = [1, 2]
#
# match weather:
#     case "cold":
#         print("It's cold")
#     case "hot":
#         print("It's hot")
#     case "raining":
#         print("It's raining")
#     case _:
#         print("Not weather")


########### LIST ###########

#value_list = [1, 2, 3, 4, 5, 6]
value_list = ['apple', 'red', 'true', 'aapple']

value_list.append("Hello")      # Метод append змінює список на місці та нічого не повертає
                                # додає до кінця списку зазначений в () елемент
print(value_list)

some_value = value_list.pop()

print(some_value)
print(value_list)


value_list.reverse()
print(value_list)
#value_list.sort(reverse=False, key=len) # sort змінює поточний list
value_list = sorted(value_list) # для sorted створити змінну -- sorted створює новий list -- працює з будь-яким list
print(value_list)

value_list.insert(0, "0000")# insert вставляє елементи в список
# print(value_list)
# print(len(value_list))
print(value_list[4])