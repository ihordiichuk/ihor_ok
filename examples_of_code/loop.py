"""
1. for loop
The for loop is used to iterate over a sequence (such as a list, tuple, string, or range). In each iteration,
it assigns the next value from the sequence to the loop variable and then executes the loop body.

### Syntax:

for element in iterable:
    # do something with element


### example:

numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)

Explanation: This for loop iterates over the list numbers and prints each element.


### Example using range():

for i in range(5):  # range generates numbers from 0 to 4
    print(i)

Explanation: Here, range(5) generates numbers from 0 to 4, and the loop prints each number.


2. while loop
The while loop repeatedly executes the loop body as long as the given condition is True.
It can potentially lead to infinite loops if the condition never becomes False.

### Syntax:

while condition:
    # loop body


### Example:

counter = 0
while counter < 5:
    print(counter)
    counter += 1  # increment counter to avoid infinite loop

Explanation: The while loop checks the condition counter < 5.
As long as the condition is true, it prints the value of counter and increments it by 1.


3. break statement
The break statement is used to exit a loop prematurely, even if the loop condition is still True.

### Example:

for i in range(10):
    if i == 5:
        break  # exit loop when i equals 5
    print(i)

Explanation: This for loop prints numbers from 0 to 4 and exits the loop when i becomes 5, skipping the remaining iterations.


4. continue statement
The continue statement is used to skip the current iteration of the loop and continue with the next iteration.

### Example:

for i in range(5):
    if i == 2:
        continue  # skip when i equals 2
    print(i)

Explanation: The for loop skips printing 2 and continues to the next iteration, printing 0, 1, 3, and 4.


5. else clause in loops
A for or while loop can have an else clause. The else block will execute if the loop completes normally without
encountering a break statement.

###Example:

for i in range(5):
    print(i)
else:
    print("Loop finished without break")

Explanation: The else block is executed after the loop completes its iterations because no break occurred.


###Example with break:

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will not print")

Explanation: The else block is skipped because the loop is terminated by a break.

6. nested loops
You can nest loops, meaning placing one loop inside another.
This is useful for working with multi-dimensional data or performing complex iteration patterns.

###Example:

for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

Explanation: This example uses two for loops.
The inner loop completes all its iterations for each iteration of the outer loop. It prints combinations of i and j.


7. pass statement
The pass statement is a placeholder used when a loop or code block is required syntactically,
but you do not want to execute any code within it.

###Example:

for i in range(5):
    if i == 3:
        pass  # no action is taken when i equals 3
    print(i)

Explanation: The pass statement does nothing and allows the loop to continue.
It is often used as a placeholder for future code.


8. infinite loop
An infinite loop occurs when the loop condition never becomes False or
if you deliberately omit the termination condition. Such loops can be exited using the break statement.

###Example:

while True:
    print("This will run forever unless we break out of it")
    break  # prevents infinite loop

Explanation: The loop will run indefinitely, but here the break statement is used to terminate the loop immediately after the first iteration.


9. Looping over dictionaries
You can iterate over keys, values, or key-value pairs in a dictionary.

###Example:

my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

Explanation: The for loop iterates over the key-value pairs in the dictionary using the .items() method.


10. Looping over a file
You can iterate over the lines of a file using a for loop.

###Example:

with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip removes leading/trailing whitespace

Explanation: This example reads a file line by line and prints each line after
removing any leading or trailing whitespace.

"""


# 1. Shopping List App
# Problem: You are building a simple shopping list app.
# Users can add items to their shopping list and view the list. Once they are done, they can stop adding items.
#
# Goal:
#
# Use a while loop to keep asking the user to input items for their shopping list.
# Stop the loop when the user types "done".
# Print the final shopping list after the loop ends.
# Example:
shopping_list = []

while True:
    item = input("Add an item to your shopping list (type 'done' to finish): ")
    if item.lower() == "done":
        break
    shopping_list.append(item)

print("Your shopping list:", shopping_list)
