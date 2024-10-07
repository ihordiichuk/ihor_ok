# Завдання 1 Найпростіший калькулятор
#
# Програма має виконувати прості математичні дії (+, -, *, /).
# Користувачеві пропонується по черзі ввести числа та дію над цими числами, а програма, виходячи з дії,
# обчислює та друкує результат.
#
# Зробити перевірку на те, що при діленні дільник не дорівнює 0!

## Оператору пропонується почергово ввести число, операцію, число. Після чого буде виконана дія над числами.
# number_1 = int(input("Enter your first number: "))
# oper_sign = input('Enter your operation ( +, -, *, /): ')
# number_2 = int(input("Enter your second number: "))

### Ці два вирази створені, щоб оператор вводив значення для розрахунку в одному рядку ##
# Цей вираз лише додає значення до значення 1 + 1 = 11
number_1, oper_sign, number_2 = input("Enter calculation (e.g., 5 + 3): ").split()
# Цей вираз виконує операцію над значеннями які були введені
number_1, number_2 = int(number_1), int(number_2)

# Addition
if oper_sign == "+":
    print(number_1 + number_2)

# Subtraction
elif oper_sign == "-":
    print(number_1 - number_2)

# Multiplication
elif oper_sign == "*":
    print(number_1 * number_2)

# Division
elif oper_sign == "/":
    if number_2 == 0:
        print("Error! Cannot divide by 0!!!")
    else:
        print("result: ", (number_1 / number_2))

else:
    print("You are trying to use unsupported operator!")
