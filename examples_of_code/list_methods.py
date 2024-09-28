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

# people_1: list[str] = ['Mario', 'Elon', 'Trump', 'Elon']        # to extend list need to create another one
# people_2: list[str] = ['apple', 'banana']                       # list to be extended to first
#
# people_1.extend(people_2)
## people_1.extend([people_2])                          <-----    # to put list inside list
# print(people_1)


#############
# 6 index()

# people: list[str] = ['Mario', 'Elon', 'Trump']
# print(people.index('Trump'))


#############
# 7 insert()

# people: list[str] = ['Mario', 'Elon', 'Trump']
# print(list(range(len(people))))                         # len to calculates the length,
#                                                         # range to create a sequence of numbers from 0
#                                                         # list converts the range object into an actual list.
#
# people.insert(1, 'Luigi')                       # ( _index: position, _object: what to insert
# print(people)


#############
# 8 pop()

# people: list[str] = ['Mario', 'Elon', 'Trump']
# popped = people.pop(0)
#
# print(people)
# print(popped)


#############
# 9 remove()

# people: list[str] = ['Mario', 'Elon', 'Trump']
# people.remove('Elon')
#
# print(people)


#############
# 10 reverse()

# people: list[str] = ['Mario', 'Elon', 'Trump']
# people.reverse()
#
# print(people)


#############
# 11 sort()

# people: list[str] = ['Mario', 'Elon', 'bob', 'Trump', 'yaser']
# # people.sort()  # (self, key, reverse)
# # people.sort(key=lambda name: len(name), reverse=True)
# people.sort(reverse=True)
#
# print(people)
