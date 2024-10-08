# Питання для користувача на початку
#
system_questions = [ 'Enter first number: ', 'Enter operator (+, -, *, or /): ', 'Enter second number: ']
#
# Словник операторів з lambda функціями
operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b if b != 0 else "Division by zero error",
}

def ask_user(system_questions):
    input_answers = {}
    for question in system_questions:
        input_answers[system_questions] = input(system_questions + ": ")
    return input_answers

# Перевірка відповідей користувача на правильність
while True:
# check first number for a digit
    user_input = input(system_questions[0])
    if user_input.isdigit():
        break
    else:
        print("This is not a number!",)
        try_again = input('Do you want to try again? Type y if yes and n if no: ')
        if try_again.lower() != 'y' or 'yes':
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



# Функція для виконання операції
def perform_operation(operation, a, b):
    return operations.get(operation, lambda a, b: "Unknown operation")(a, b)

# Виклик функції
# result = perform_operation("multiply", 10, 5)
# print(result)

end_question = input('Do you want to continue? YES or NO: ')
if end_question == 'YES':
    print("Good bye!")