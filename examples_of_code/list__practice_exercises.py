### Python List
# 1. Write a Python program to sum all the items in a list.
#
# for list in items_list:
#     sum_list = sum(items_list)
#
# print(sum_list)
## or ##
# results = 0
#
# for list in items_list:
#     results += list
#
# print(results)
#
#
# 2. Write a Python program to multiply all the items in a list.
#
# multiply_list = [2, 23, 2]
# results = 1                     # Ініціалізувати змінну 'results' для зберігання добутку чисел, починаючи з 1
#
# for list in multiply_list:
#     results *= list
#
# print(results)
#
#
# 3. Write a Python program to get the largest number from a list.
#
# list_of_numbers = [2, 4, 6, 1, 8, 0, 9]
# max = list_of_numbers[0]          # Ініціалізувати змінну 'max' першим елементом вхідного списку як початковий максимум
#
# for list in list_of_numbers:
#     if list > max:
#         max = list
#
# print(max)
#
#
# 4. Write a Python program to get the smallest number from a list.
#
# list_of_numbers = [2, 4, 6, 1, 8, 10, 9]
# min = list_of_numbers[0]
#
# for list in list_of_numbers:
#     if list < min:
#         min = list
#
# print(min)
#
#
# 5. Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
#
# sample_list = ['abc', 'xyz', 'aba', '1221']
#
# count = 0
#
# for list in sample_list:
#     if len(list) > 1 and list[0] == list[-1]:
#         count += 1
#
# print(count)
#
## or ##
#
# Count matching strings using a list comprehension
# count = len([s for s in sample_list if len(s) > 1 and s[0] == s[-1]])
#
# print(count)
#
#
# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple
# from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#
# sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# sample_list.sort(reverse=False, key=lambda x: x[1])
#
# print(sample_list)
#
#
# 7. Write a Python program to remove duplicates from a list.

some_list = []