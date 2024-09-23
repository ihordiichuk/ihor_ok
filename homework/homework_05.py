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

# A variable cannot:
#     begin with a digit,
#     consist of only digits,
#     contain capital letters, spaces, and punctuation (you can get it here string.punctuation), except for the underscore "_".
#     be any of the registered words.

user_do = input("Enter your: ")
if user_do

    #     result = ("Restricted to begin with a digit")
    # elif user_do.isdigit(user_do):
    #     result = ("Restricted to have only digits")
    # elif user_do.capitalize()

print(result)








"""

Завдання 2 Модифікувати калькулятор

Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче

Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного 
обчислення - якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.

"""