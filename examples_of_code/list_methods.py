# https://www.youtube.com/watch?v=0yySumZTxJ0

# append()
# clear()
# copy()
# count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()

#############
# 1 append()

# people: list[str] = ['Mario', 'Elon', 'Trump']
# people.append('Luigi')
# print(people)

#############
# 2 clear()

# people: list[str] = ['Mario', 'Elon', 'Trump']
# people.clear()
# print(people)

#############
# 3 copy()

# people: list[str] = ['Mario', ['Elon', 'Vladimir'], 'Trump']
# copy_people: list[str] = people.copy()
#
# copy_people.remove('Trump')
# print(people)
# print(copy_people)

#############
# 4 count()

# people: list[str] = ['Mario', 'Elon', 'Trump', 'Elon']
# elons = people.count('Elon')
#
# print(elons)


#############
# 5 extend() --> like append

people_1: list[str] = ['Mario', 'Elon', 'Trump', 'Elon']        # to extend list need to create another one
people_2: list[str] = ['apple', 'banana']                       # list to be extended to first

people_1.extend(people_2)
print(people_1)