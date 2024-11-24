
def func_name(*args, **kwargs):
    """Documentation"""
    # return result


# Ця функція повертає кортеж з трьох значень. При виклику функції можна "розпакувати" цей кортеж в окремі змінні.
def calculation(xa, xb):
    addition = xa + xb
    substruction = xa - xb
    multiplication = xa * xb
    return addition, substruction, multiplication

a, b, c = calculation(2, 2)
print(f"addiction: {a}, substruction: {b}, multiplication: {c}")