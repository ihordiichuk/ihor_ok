"""
Method	    Description

append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

"""
### EXAMPLES
"""
1. append()
Scenario: You're managing a shopping list, and after checking your fridge, you realize you need to buy eggs.

shopping_list = ["milk", "bread", "butter"]
shopping_list.append("eggs")
print(shopping_list)  # Output: ["milk", "bread", "butter", "eggs"]


2. clear()
Scenario: You just finished your shopping, so you want to reset the list for next time.

shopping_list = ["milk", "bread", "butter", "eggs"]
shopping_list.clear()
print(shopping_list)  # Output: []


3. copy()
Scenario: You want to make a backup copy of your current shopping list before adding more items.

original_list = ["milk", "bread", "butter"]
backup_list = original_list.copy()
print(backup_list)  # Output: ["milk", "bread", "butter"]


4. count()
Scenario: You’re counting how many times "apple" appears in your fruit basket.

fruit_basket = ["apple", "banana", "apple", "orange", "apple"]
apple_count = fruit_basket.count("apple")
print(apple_count)  # Output: 3


5. extend()
Scenario: You’re combining your grocery list with your friend's list before going to the supermarket.

my_list = ["milk", "bread"]
friend_list = ["eggs", "cheese"]
my_list.extend(friend_list)
print(my_list)  # Output: ["milk", "bread", "eggs", "cheese"]


6. index()
Scenario: You're looking for the position of "butter" in your shopping list to see where it is.

shopping_list = ["milk", "bread", "butter", "eggs"]
butter_index = shopping_list.index("butter")
print(butter_index)  # Output: 2


7. insert()
Scenario: You forgot to add "apples" to your shopping list, but you want to add it at the beginning.

shopping_list = ["milk", "bread", "butter"]
shopping_list.insert(0, "apples")
print(shopping_list)  # Output: ["apples", "milk", "bread", "butter"]


8. pop()
Scenario: You just finished using the last item from your list and want to remove it.

shopping_list = ["milk", "bread", "butter"]
last_item = shopping_list.pop()
print(last_item)  # Output: "butter"
print(shopping_list)  # Output: ["milk", "bread"]


9. remove()
Scenario: You realized you already have bread at home, so you want to remove it from your list.

shopping_list = ["milk", "bread", "butter"]
shopping_list.remove("bread")
print(shopping_list)  # Output: ["milk", "butter"]


10. reverse()
Scenario: You want to reverse the order of items in your to-do list for the day.

todo_list = ["do laundry", "buy groceries", "clean kitchen"]
todo_list.reverse()
print(todo_list)  # Output: ["clean kitchen", "buy groceries", "do laundry"]


11. sort()
Scenario: You're organizing your list of friends in alphabetical order for invitations.

friends = ["Charlie", "Alice", "Bob"]
friends.sort()
print(friends)  # Output: ["Alice", "Bob", "Charlie"]
"""