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
#
#
# number_1, oper_sign, number_2 = input("Enter calculation (e.g., 5 + 3): ").split()
# number_1, number_2 = int(number_1), int(number_2)
system_questions = [ 'Enter first number: ', 'Enter operator (+, -, *, or /): ', 'Enter second number: ']

def ask_user(system_questions):
    input_answers = {}
    for question in system_questions:
        input_answers[system_questions] = input(question + ": ")
    return input_answers

while True:
# check first number for a digit
    user_input = input(system_questions[0])
    if user_input.isdigit():
        break
    else:
        print("This is not a number!",)
        try_again = input('Do you want to try again? Type y if yes and n if no: ')
        if try_again.lower() != 'y':
            break

# check operator for a logic symbol
    system_operator = input(system_questions[1])
    valid_operators = ['+', '-', '*', '/']
    if system_operator in valid_operators:
        break  # Exit the loop if both inputs are valid
    else:
        print("Invalid operator. Please enter +, -, *, or /")

# check second number for a digit
    user_input = input(system_questions[2])
    if user_input.isdigit():
        break
    else:
        print("This is not a number!",)
        try_again = input('Do you want to try again? Type y if yes and n if no: ')
        if try_again.lower() != 'y':
            break

# user_answers = ask_user(system_questions)
# print('You typed: ', user_answers)

# Словник операторів з lambda функціями
operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b if b != 0 else "Division by zero error",
}

# Функція для виконання операції
def perform_operation(operation, a, b):
    return operations.get(operation, lambda a, b: "Unknown operation")(a, b)

# Виклик функції
# result = perform_operation("multiply", 10, 5)
# print(result)

end_question = input('Do you want to continue? YES or NO: ')
if end_question == 'YES':
    print("Good bye!")