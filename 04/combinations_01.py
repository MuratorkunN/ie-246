def combinations(items, sort=False):
    """Assumes items as a tuple containing unique elements.
       Returns a list of all combinations (subsets) of items as tuples. If sort
           is True, subsets are listed from smallest to largest."""
    if len(items) == 0:
        subsets = [tuple()]
    else:
        item, rmn_items = items[0], items[1:]
        subsets_0 = combinations(rmn_items)
        subsets_1 = [(item,) + subset for subset in subsets_0]
        subsets = subsets_0 + subsets_1
        if sort:
            subsets = sorted(subsets, key = lambda x:len(x))
    return subsets

my_items = (0, 1, 2, 3)
my_subsets = combinations(my_items)
print(my_subsets, "\n")

my_subsets = combinations(my_items, sort=True)
print(my_subsets)