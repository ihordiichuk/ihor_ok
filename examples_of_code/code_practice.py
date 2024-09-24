# user_name = input("Enter name: ")
# user_name = user_name.title()
# print(f"Hello, {user_name}!  ")
from operator import index

# mess_qq = input(" \"Name\" of book 'QQQ' ")
# print(mess_qq)


# firs_name = input("Enter your First Name: ")
# # firs_name = firs_name.strip()
# second_name = input("Enter your Second Name: ")
# # second_name = second_name.strip()
# sur_name = input("Enter your Surame: ")
# # sur_name = sur_name.strip()
# message = f"Hello, {firs_name.capitalize().strip()} {second_name.capitalize().strip()} {sur_name.capitalize().strip()}"
# print(message)

# firend_list = ['Oleh', 'Vasya', 'Dmytro']
# for friend in firend_list:
#     print(friend)

# friend_list = ['Oleh', 'Vasya', 'Dmytro']
# friend_list_1 = friend_list.pop(-1)
# print(friend_list)
# print(friend_list_1)
# friend_list.append(friend_list_1)
# print(friend_list)


# friend_list = ['Oleh', 'Vasya', 'Dmytro']
# friend_list.remove('Vasya')
# print(friend_list)


people_list = ['Nadia', 'Ghandi', 'Odin']
# for people in people_list:
#     message = f"Hello, my friends {people.capitalize()}"
#     print(message)
# print(f'I was waiting you.The list of my guests is {people_list}')
people_list.remove("Ghandi")
people_list.extend(['vika', 'yulia', 'sasha'])
# new_list = ['vika'], ['yulia'], ['sasha']
# people_list.append(new_list)
print(people_list)
# for people in people_list:
#     message = f"Hello, my friends {people.capitalize()}! Ghandi left our party!"
#     print(message)

