from math import inf # We will use -inf as a penalty for infeasible solutions.

def ks01_rec_naive(items, capacity, vals, weights):
    """Assumes 'items' as a tuple of unique collectibles (integer or string), 
           'capacity' as a numeric value representing the knapsack capacity,
           'vals' and 'weights' as dictionaries holding respectively the values 
           and the weights of collectibles.
       Guarantees an optimal solution for ``Knapsack 0-1'' problem with a naive
           recursive approach. Returns only the optimal total value collected
           in the knapsack. Does not return the list of items collected in the 
           knapsack."""
    
    if capacity < 0:      # BASE CASE 1: If the capacity is negative, then the problem is infeasible.
        obj_val = -inf    # Worst objective value is returned.
    elif len(items) == 1:            # BASE CASE 2: If there is only one item that can be collected.
        item = items[0]              # Take that one item in consideration.
        if weights[item] > capacity: # If the weight is more than the knapsack capacity.
            obj_val = 0              # We do not take the item, thus the total value is zero.
        else:                        # If the weight is less than the knapsack capacity.
            obj_val = vals[item]     # We take the item, thus the total value is its value.
    else:                                       # RECURSIVE CASE: If there are at least two items.
        item = items[0]                         # Take the first item in consideration.
        rmn_items = items[1:]                   # Create a sliced tuple from remaining items.
        rmn_capacity = capacity - weights[item] # Calculate the potential remaining capacity
                                                # assuming that we place the first item.
        # Assume we do not take the first item and calculate the optimal total value achieved with
        # remaning items as obj_0.
        obj_0 = ks01_rec_naive(rmn_items, capacity, vals, weights)
        # Assume we take the first item, introduce its value, and calculate the optimal total value
        # achieved with remaning items and reduced capacity.
        obj_1 = vals[item] + ks01_rec_naive(rmn_items, rmn_capacity, vals, weights)
        obj_val = max(obj_0, obj_1) # Optimal total value is the maximum of these two values.
    return obj_val

# TEST CODE

my_items = ("book", "clock", "computer", "painting", "radio", "vase")
my_capacity = 20
my_vals = dict(zip(my_items, (9, 175, 200, 99, 20, 50)))
my_weights = dict(zip(my_items, (1, 10, 20, 9, 4, 2)))

my_result = ks01_rec_naive(my_items, my_capacity, my_vals, my_weights)
print(my_result)