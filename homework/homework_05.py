"""
Завдання 1 Ім'я змінної

Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.

Змінна не може:

    починатися з цифри,
    складатися тільки з цифр,
    містити великі літери, пропуск і знаки пунктуації (взяти можна тут string.punctuation),
    окрім нижнього підкреслення "_".
    бути жодним із зареєстрованих слів.
При цьому ім'я змінної може складатися тільки з одного нижнього підкреслення "_".

Список зареєстрованих слів можна взяти із keyword.kwlist.

У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.

Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно )

_ => True
x => True
get_value => True
get value => False
get!value => False
some_super_puper_value => True
Get_value => False
get_Value => False
getValue => False
3m => False
m3 => True

"""
# variant 1
#
# user_do = input("Enter your: ")
# for user_input in user_do:
#     if user_do[0].isdigit():
#         result = ("Can not begin from a number!")
#     elif user_do.isnumeric():
#         result = ("Can not be numeric only")
#     elif user_do.isupper():
#         result = ("Can not contain capital letters")
#     elif user_do.isspace():
#         result = ("Can not have spaces")
#    # elif user_do # re.search() or find()
#     else:
#         result = (print("You entered: ", user_do))
#
#     #     result = ("Restricted to begin with a digit")
#     # elif user_do.isdigit(user_do):
#     #     result = ("Restricted to have only digits")
#     # elif user_do.capitalize()
#
# print(result)
#
#
# version 2
#
# user_do = input("Enter your: ")
#
# result = user_do.isidentifier() and (user_do == '_' or user_do.islower())
#
# print(result)
####
#
"""

Завдання 2 Модифікувати калькулятор

Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче

Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного 
обчислення - якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.

"""

def perform_calculations(first_number, operator_list, last_number):
    if operator_list == "+":
        return first_number + last_number
    elif operator_list == "-":
        return first_number - last_number
    elif operator_list == "*":
        return first_number * last_number
    elif operator_list == "/":
        if last_number == 0:
            return "Error! Cannot divide by 0!"
        else:
            return first_number / last_number

while True:
    first_number = input("Enter first number: ")
    operator_list = input("Enter operator from a list (+, -, *, /): ")
    last_number = input("Enter last number: ")

    if not first_number.isdigit() or not last_number.isdigit():
        print("Error: You are typing not a number! Please try again.")
        continue

    first_number = int(first_number)
    last_number = int(last_number)

    result = perform_calculations(first_number, operator_list, last_number)
    print(f"Result: {result}")

    user_choice = input("Enter 'q' to quit or 'p' to proceed: ").strip().lower()
    if user_choice == 'q':
        print("Good Bye!")
        break



