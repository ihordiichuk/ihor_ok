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
from traceback import print_tb

from lessons.lesson_2 import list_1
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

#### передивитися і доповнити до цього рядка ####

############# loop #############

# while for

value_int = 0
is_true = True

# while True:
#     value_int += 1
#     print(value_int)

# while value_int < 10:
#     value_int += 1
#     print(value_int)

# while is_true:
#     value_int += 1
#     print(value_int)
#     if value_int > 10:
#         is_true = False

####

# while True:
#     value_int += 1
#     print(value_int)
#     if value_int > 10:
#         break             ##<--- зробили break
# else:
#     print("888888")

##
# while is_true:
#     value_int += 1
#     print(value_int)
#     if value_int > 10:
#         is_true = False   ##<--- вийшли нормально\природньо
# else:
#     print("888888")
# print("end")

##
# while is_true:
#     value_int += 1
#     print(value_int)
#     if value_int == 5:
#         continue
#     if value_int > 10:
#         is_true = False
# else:
#     print("888888")
# print("end")

### for, for else, range()

# some_str = "hello"
#
# [1,2,3,4]
# (1,2,3,4)
# "hello"
# index = 0
#
# while index < len(some_str):
#     print(some_str[index])
#     index += 1
#
# for letter in some_str:
#     print(letter)

# range(5)        -   (0, 4)
# range(2, 5)     -   (2, 4)
# range(2, 5, 2)  -   (2, 4)
#
# list_1 = [1, 2, 3, 4, 5]
# print(list_1[::-1])         # синтаксичний цукор який робить reverse
# print(list_1["from" : "to" : "step"])
#
# for i in range(2, 5, 2)
#     print(i)
#     if i == 4
#        break
# else:
#     print(5555)
#
# print("end")


for number in range(5):
    for num_2 in range(5):
        print(number)
        if num_2 == 4:
            break
    print(number)

else:
    print(111111)

print("end")