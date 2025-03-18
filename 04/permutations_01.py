def permutations(items):
    """Assumes items as a tuple containing unique elements.
       Returns a list of all permutations (orderings) of items as tuples."""
    if len(items) == 0:
        orderings = [tuple()]
    else:
        orderings = []
        item, rmn_items = items[0], items[1:]
        reduced_orderings = permutations(rmn_items)
        for ordering in reduced_orderings:
            for i in range(len(ordering)+1):
                orderings.append(ordering[:i] + (item,) + ordering[i:])
    return orderings

my_items = (0, 1, 2, 3) 
my_orderings = permutations(my_items)               
print(my_orderings)