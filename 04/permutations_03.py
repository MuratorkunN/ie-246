from itertools import permutations

my_items = (0, 1, 2)

orderings_2_element = permutations(my_items, 2)
print(orderings_2_element)
print(list(orderings_2_element))

print(list(permutations(my_items, 3)))
print(list(permutations(my_items)))