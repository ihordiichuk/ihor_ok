def say_hi(name, age):
    greeting = f"Hi. My name is {name} and I'm {age} years old."
    return greeting

    user_name = input("Your name is: ")
    user_age = input("Your age is: ")

    if not user_name.isalpha():
        print("Error: Name must contain only letters!")
    elif not user_age.isdigit():
        print("Error: Age must contain digits!")
    else:
        user_age = int(user_age)
        result = say_hi(user_name, user_age)
        print(result)

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('OK')
