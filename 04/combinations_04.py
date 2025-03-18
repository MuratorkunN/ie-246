from itertools import combinations

my_items = (0, 1, 2, 3)

subsets_2_element = combinations(my_items, 2)
print(subsets_2_element)
print(list(subsets_2_element))

subsets_3_element = list(combinations(my_items, 3))
print(subsets_3_element)