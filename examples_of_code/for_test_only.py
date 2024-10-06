# зберегти 5 локацій
# перевірити на впорядкованість за алфавітом
#
#
# locations_list: list[str] = ['Rome', 'Milan', 'Berlin', 'London', 'Kyiv']
# locations_list.sort(reverse=False)
# print(locations_list)
#
# locations_list.reverse()
# print(locations_list)
#
# locations_list.sort(, reversed=True)
# print(locations_list)
#
#
# fav_pizza = ['marharita', 'meat', 'hawaii']
#
# for pizza in fav_pizza:
#     print(f'I like {pizza}.')
#
# print('I really love pizza')
#
# fav_pet = ['dog', 'cat', 'bird']
#
# for animal in fav_pet:
#     print(f'The {animal} like to eat and poo.')
#
# print('I really love animals')
#
#
# num_num = []
# for i in range(3, 31):
#     # num_num.append(i)
#     if i % 3 == 0:
#         num_num.append(i)
#     else:
#         continue
# print(num_num)
# print(min(num_num), max(num_num))
# print(sum(num_num))
#
# list_l = []
# for i in range(1, 6):
#     list_l.append(i**3)
# print(list_l, 'IIIII')
# #
# list_l1 = []
# for i in list_l:
#     list_l1.append(int(i ** (1/3)))
#
# print(list_l1)
#
#
# Take from dictionary fruits into the new list, one by one, with text "I've got a "
#
fruit_collection: dict = {1: 'apple', 2: 'pineapple', 3: 'peach', 4: 'banana', 5: 'melon'}
# print(fruit_collection)
fruit_list = []

for fruits in fruit_collection:
    taken_fruits = fruit_collection[fruits]
    if taken_fruits not in fruit_collection:
        fruit_list.append(f"I've got a {taken_fruits}")

print(fruit_list)

