# Написати програму, яка просить користувача ввести 4-х значне число з клавіатури, після чого друкує на екрані стовпчик
# цифр, з якого це число складається. Наприклад, користувач вводить 1234, а програма виводить:
#
# 1
#
# 2
#
# 3
#
# 4
#
# Завдання необхідно вирішити, використовуючи методи поділу (підказка // і % або divmod). Виведення в стовпчик можна зробити за допомогою 4-х функцій print.
#
# Користувач може ввести будь-яке 4 значне ціле число. Будь-яке 4-х значне число - це число, яке складається з 4-х цифр, де кожна цифра може бути від 0 до 9 включно.
#
# Ваше рішення має це враховувати! Якщо користувач ввів не ціле число, це проблема користувача, а не вашої програми.
#
# Створюйте рішення, виходячи з того, що число ЗАВЖДИ 4-хзначне.


######## Option 1 ########

# number = int(input("Please, enter a number of four numbers: "))

# thousands = number // 1000
# hundreds = (number % 1000) // 100
# tens = (number % 100) // 10
# units = number % 10

# print(thousands)
# print(hundreds)
# print(tens)
# print(units)


######## Option 2 ########

num = int(input("Please, enter a number of four numbers: "))

thousands, reminder = divmod(num, 1000)
hundreds, reminder = divmod(reminder, 100)
tens, units = divmod(reminder, 10)

print(f"{thousands}\n{hundreds}\n{tens}\n{units}")