from math import inf # We will use -inf as a penalty for infeasible solutions.
from copy import deepcopy as dc # We will use deep copies of solutions collected from 'results'
                                # dictionary, so the dictionary values will not be affected.

def ks01_rec(items, capacity, vals, weights, results=None):
    """Assumes 'items' as a tuple of unique collectibles (integer or string), 
           'capacity' as a numeric value representing the knapsack capacity,
           'vals' and 'weights' as dictionaries holding respectively the values 
           and the weights of collectibles. You can pass an empty dictionary to 
           'results' to see the optimal solutions for all solved problems.
       Guarantees an optimal solution for ``Knapsack 0-1'' problem with an 
           enhanced recursive approach. Returns a two-element tuple containing 
           the optimal objective value and a list of optimal items to be
           collected."""
    
    if results == None: # If the user does not pass any argument for results,
        results = {}    # it will automatically be set as an empty dictionary.
        
    # BASE CASE 1: If the capacity is negative, then the problem is infeasible.
    if capacity < 0:                            # We always store a solution to 'results'  
        results[(items, capacity)] = (-inf, []) # dictionary as a problem:solution pair.
    elif len(items) == 1: # BASE CASE 2: If there is only one item that can be collected.
        item = items[0]   # Take that one item in consideration.
        if weights[item] > capacity:             # If the weight is more than the capacity.
            results[(items, capacity)] = (0, []) # Leave the item. 
        else:                                                 # If it fits.
            results[(items, capacity)] = (vals[item], [item]) # Take the item.
    else:                                     # RECURSIVE CASE: If there are at least two items.
        item = items[0]                       # Take the first item in consideration.
        rmn_items = items[1:]                 # Create a sliced tuple from remaining items.
        rmn_capacity = capacity-weights[item] # Calculate the potential remaining capacity
                                              # assuming that we place the first item.
        if (rmn_items, capacity) in results.keys():           # If the problem is in keys of 'results'.
            obj_0, sol_0 = dc(results[(rmn_items, capacity)]) # Retrieve a deepcopy of the solution.
        # If the problem is not in 'results', call ks01_rec() recursively, take a deepcopy of the solution.
        else:
            obj_0, sol_0 = dc(ks01_rec(rmn_items, capacity, vals, weights, results))
        if (rmn_items, rmn_capacity) in results.keys():           # If the problem is in keys of 'results'.
            obj_1, sol_1 = dc(results[(rmn_items, rmn_capacity)]) # Retrieve a deepcopy of the solution.
        # If the problem is not in 'results', call ks01_rec() recursively, take a deepcopy of the solution.
        else:
            obj_1, sol_1 = dc(ks01_rec(rmn_items, rmn_capacity, vals, weights, results))
        obj_1 += vals[item] # Increment the optimal total value with the first item's value.
        sol_1.append(item)  # Since the first item is collected, append it to the collected items.
        if obj_0 > obj_1:   # Optimal total value is the maximum of these two values.   
            results[(items, capacity)] = (obj_0, sol_0) # Update 'results' dictionary with a 
        else:                                           # problem:solution pair, based on which
            results[(items, capacity)] = (obj_1, sol_1) # objective value is better.
    return results[(items, capacity)]                   # Return the solution from 'results' dictionary.

# TEST CODE

my_items = ("book", "clock", "computer", "painting", "radio", "vase")
my_capacity = 20
my_vals = dict(zip(my_items, (9, 175, 200, 99, 20, 50)))
my_weights = dict(zip(my_items, (1, 10, 20, 9, 4, 2)))
all_results = {}

my_result = ks01_rec(my_items, my_capacity, my_vals, my_weights, all_results)
print(my_result)
print(all_results) # Here, you can see all problem:solution pairs for all problems solved recursively.