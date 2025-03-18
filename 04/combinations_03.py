def combinations(items, k=None, sort=False):
    """Assumes items as tuple containing unique elements and k as an integer.
       Returns a list of all k-element subsets of items as tuples. If k is 
           None, returns a list of all subsets. If sort is True, subsets are
           listed from smallest cardinality to largest."""
    if k == None:                                                        # If the end-user wants all combinations.
        if len(items) == 0:                                              # BASE CASE: When the set is empty.
            subsets = [tuple()]
        else:                                                            # RECURSIVE STEP: When the set is non-empty. 
            item, rmn_items = items[0], items[1:]
            subsets_0 = combinations(rmn_items)
            subsets_1 = [(item,) + subset for subset in subsets_0]
            subsets = subsets_0 + subsets_1
            if sort:                                                     # Sorts subsets from smallest to largest in size. 
                subsets = sorted(subsets, key = lambda x:len(x))
    else:                                                                # If the end-user wants only k-element subsets.
        if k not in range(len(items) + 1):                               # BASE CASE 1: When there is no k-element subset.
            subsets = []
        elif k == 0:                                                     # BASE CASE 2: When we look for 0-element subsets.
            subsets = [tuple()]
        else:                                                            # RECURSIVE STEP: When there are k-element subsets.
            item, rmn_items = items[0], items[1:]
            subsets_0 = combinations(rmn_items, k)
            reduced_subsets = combinations(rmn_items, k-1)
            subsets_1 = [(item,) + subset for subset in reduced_subsets]
            subsets = subsets_0 + subsets_1
    return subsets                                                       # Return the result coming from one if block.

print(combinations((0, 1, 2), sort=True))
print(combinations((0, 1, 2), 0))
print(combinations((0, 1, 2), 1))
print(combinations((0, 1, 2), 2))
print(combinations((0, 1, 2), 3))
print(combinations((0, 1, 2), 4))