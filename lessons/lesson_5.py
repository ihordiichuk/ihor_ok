# value_str = [0, "one", 2, 3, 4, 5, "SIX", 7, 8, 9]
from distutils.command.install import value

# for index in range(len(value_str)):
#     print(value_str)

## enumerate()
# for index, letter in enumerate(value_str):
#     print(index, letter)

###

# value_str = "HeLlo"
# value_str_1 = value_str.lower()
# value_str_2 = value_str.upper()
# value_str_3 = value_str.capitalize()
#
# print(value_str, id(value_str))


# value_float = "12w"
# value = " "
#
# # value_is_digit = value_float.isdigit()    --> only numberes
# # value_is = value_float.isalpha()          --> only letters
# # value_is = value_float.isspace()          --> only spaces
# print(value)
#
# for letter in value_float:
#     if letter.isdigit():
#         value += letter
#
# print(value)


# value_float = "hello"
#
# method = value_float.find("l")
# for letter in value_float[method:+1]:
#     pass
#
# method = value_float.rfind("l")
# print(method)


# split()

# value = "c/j09u/Documents/kkk.png"

# some_method = value.split(".")
# print(some_method)
# some_method[-1] = 'jpeg'
# print(some_method)

# join()

# result = ".".join(some_method)
# print(result)

# replace()

# print(value)
#
# result = value.replace(".png", ".jpeg", 1)
# index = result.find(".png")
#
# result_1 = result[:index]
# print(result_1 )

# strip() & rstrip() & lstrip()

# value = " Nick     "
# print(value)
#
# result = value.strip()
# # result = value.rstrip()
# # result = value.lstrip()
#
# print(result)

### ASCII ##

alphabet = ""
# print(ord(value))
# print(chr(100))

for index_of_character in range(ord("A"), ord("Z")+1):
    alphabet += chr(index_of_character)
    # print(chr(index_of_character), index_of_character)

print(alphabet )