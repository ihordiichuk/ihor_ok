## modified calculator
#

while True:
    number_1 = input("Enter first number: ")
    oper_sign = input("Enter the operator: ")
    number_2 = input("Enter first number: ")

    if not number_1.isdigit() or number_2.isdigit():
        print("Undefined operation! Try again!")
        continue

    if not number_1.isdigit() and oper_sign not in ('+', '-', '*', '/') and not number_2.isdigit():
        print("Undefined operation! Try again!")
        continue


    number_1 = float(number_1)
    number_2 = float(number_2)


    result = float

    if oper_sign == '+':
        result = number_1 + number_2
        print(result)
    elif oper_sign == '-':
        result = number_1 - number_2
        print(result)
    elif oper_sign == '*':
        result = number_1 * number_2
        print(result)
    elif oper_sign == '/' and number_2 == 0:
        result = str("You cannot divide to zero!")
        print(result)
    else:
        result = number_1 / number_2
        print(result)

    end_question = input('Do you want to continue? YES or NO: ')
    if end_question != 'YES':
        print("Good bye!")
        break