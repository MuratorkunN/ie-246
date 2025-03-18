def combinations(items, k=None, sort=False):
    """Assumes items as tuple containing unique elements and k as an integer.
       Returns a list of all k-element subsets of items as tuples. If k is 
           None, returns a list of all subsets. If sort is True, subsets are
           listed from smallest cardinality to largest."""
    if k == None:
        if len(items) == 0:
            subsets = [tuple()]
        else:
            item, rmn_items = items[0], items[1:]
            subsets = combinations(rmn_items)
            for subset in subsets[:]:
                subsets.append((item,) + subset)
            if sort:
                subsets = sorted(subsets, key = lambda x:len(x))
    else:
        if k not in range(len(items) + 1):
            subsets = []
        elif k == 0:
            subsets = [tuple()]
        else:
            item, rmn_items = items[0], items[1:]
            subsets = combinations(rmn_items, k)
            other_subsets = combinations(rmn_items, k-1)
            for subset in other_subsets:
                subsets.append((item,) + subset)
    return subsets

def permutations(items, k=None):
    """Assumes items as tuple containing unique elements and k as an integer.
       Returns a list of all k-element permutations of items as tuples. If k 
           is None, returns a list of whole-set permutations."""
    if k == None or k == len(items):       
        if len(items) == 0:
            orderings = [tuple()]
        else:
            item, rmn_items, orderings = items[0], items[1:], []
            reduced_orderings = permutations(rmn_items)
            for ordering in reduced_orderings:
                for i in range(len(ordering)+1):
                    orderings.append(ordering[:i] + (item,) + ordering[i:])
    else:
        subsets, orderings = combinations(items, k), []
        for subset in subsets:
            orderings.extend(permutations(subset))
    return orderings

my_items = (0, 1, 2)                
my_orderings = permutations(my_items)
print(my_orderings)

print(permutations(my_items, 0))
print(permutations(my_items, 1))
print(permutations(my_items, 2))
print(permutations(my_items, 3))

print(permutations(my_items, -1))
print(permutations(my_items, 4))

