# my_list = [
#     1,
#     2,
#     3,
#     4,
#     5,
# ]
#
# my_tuple = (1, 44, 666, "List_of_some", [1,2,3])
# print(type(my_tuple))
# my_tuple_l = list(my_tuple)
# print(type(my_tuple_l), id(my_tuple_l))
# print(my_tuple_l)


# _ пишеться для ігнорування
value_tuple = (1, 4)
length, _ = value_tuple

print(length)
print(_)

for _ in range(5):
    print("Hello")