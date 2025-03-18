def combinations_k(items, k):
    """Assumes items as tuple containing unique elements and k as an integer.
       Returns a list of all k-element subsets of items as tuples."""
    if k not in range(len(items) + 1):
        subsets = []
    elif k == 0:
        subsets = [tuple()]
    else:
        item, rmn_items = items[0], items[1:]
        subsets_0 = combinations_k(rmn_items, k)
        reduced_subsets = combinations_k(rmn_items, k-1)
        subsets_1 = [(item,) + subset for subset in reduced_subsets]
        subsets = subsets_0 + subsets_1
    return subsets

my_items = (0, 1, 2, 3)
subsets_0_element = combinations_k(my_items, 0)
print(subsets_0_element)

print(combinations_k(my_items, 1))
print(combinations_k(my_items, 2))
print(combinations_k(my_items, 3))
print(combinations_k(my_items, 4))
print(combinations_k(my_items, -1))
print(combinations_k(my_items, 5))