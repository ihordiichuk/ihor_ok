## modified calculator
#

while True:
    number_1 = input("Enter first number: ")

    if not number_1.isdigit():
        print("Undefined number! Try again!")
        continue
    number_1 = float(number_1)

    action = input("Enter the operator: ")
    if action not in ('+', '-', '*', '/'):
        print("Undefined operator! Try again!")
        continue


    number_2 = input("Enter first number: ")

    if not number_2.isdigit():
        print("Undefined number! Try again!")
        continue
    number_2 = float(number_2)


    result = float

    if action == '+':
        result = number_1 + number_2
        print(result)
    elif action == '-':
        result = number_1 - number_2
        print(result)
    elif action == '*':
        result = number_1 * number_2
        print(result)
    elif action == '/' and number_2 == 0:
        result = str("You cannot divide to zero!")
        print(result)
    else:
        result = number_1 / number_2
        print(result)

    end_question = input('Do you want to continue? YES or NO: ')
    if end_question != 'YES':
        print("Good bye!")
        break