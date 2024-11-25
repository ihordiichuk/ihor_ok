import random
from faker import Faker


def say_hi(name, age):
    """
    Returns a greeting string with the given name and age.
    """
    return f"Hi. My name is {name} and I'm {age} years old"

# Your existing code
def input_and_check_age(prompt):
    """
    Asks about the age and checks it with check_age.
    """
    age = input(prompt)
    return check_age(age)


def check_name(name):
    """
    Check if name and surname contain only letters and format first letter to capital.
    """
    if not name.isalpha():
        return "Error: The name must contain only letters."
    else:
        return name.capitalize()


def check_age(age):
    """
    Check if the age contains only digits.
    """
    if not age.isdigit():
        return "Error: The age must contain only numbers."
    else:
        return age


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# assert say_hi(name=input("Enter name: "), age=input("Enter age: ")) == f"Hi, my name is {name} and I am {age} years old", 'Test3'
print('ОК')

# Dynamic tests
fake = Faker()

# Generate random tests
for _ in range(5):  # Run 5 tests dynamically
    name = fake.first_name()
    age = random.randint(1, 100)
    expected = f"Hi. My name is {name} and I'm {age} years old"

    result = say_hi(name, age)
    assert result == expected, f"Test failed for input: name={name}, age={age}"

print("All dynamic tests passed!")


# Dynamic test cases stored in a list
test_cases = [
    {"name": "Alex", "age": 32, "expected": "Hi. My name is Alex and I'm 32 years old"},
    {"name": "Frank", "age": 68, "expected": "Hi. My name is Frank and I'm 68 years old"}
]

# Loop through test cases
for test in test_cases:
    result = say_hi(test["name"], test["age"])
    assert result == test["expected"], f"Failed for input: {test}"

print("Dynamic Test Case", test_cases)