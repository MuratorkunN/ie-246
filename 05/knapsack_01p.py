from math import inf # We will use -inf as a penalty for infeasible solutions.

def ks01_grd(items, capacity, vals, weights):
    """Assumes 'items' as a tuple of unique collectibles (integer or string), 
           'capacity' as a numeric value representing the knapsack capacity,
           'vals' and 'weights' as dictionaries holding respectively the values 
           and the weights of collectibles.
       Guarantees a sub-optimal solution for ``Knapsack 0-1'' problem with a
           greedy approach based on a decreasing order of value-to-weight 
           ratios. Returns a two-element tuple containing the objective value 
           and a list of collected items."""
    
    # CHECKING OVERALL FEASIBILITY
    if capacity < 0:   # If the capacity is negative, then the problem is infeasible.
        solution = []  # No items can be collected at an infeasible situation.
        obj_val = -inf # Infeasibility indicated by the worst objective value.
    else:
        # INITIALIZATION       
        solution = []    # At current solution, no item is collected.
        obj_val = 0      # Current objective value is zero.  
        slack = capacity # Currently, the whole capacity remains.

        # We create a dictionary that holds value-to-weight ratios of items.
        v2w_ratio = {item:vals[item]/weights[item] for item in items}
        
        # GREEDY HEURISTIC
        # We custom-sort items based on a decreasing order of value-to-weight ratios. 
        grd_order = sorted(items, key=lambda item:v2w_ratio[item], reverse=True)
        
        for item in grd_order:         # We test if we can collect each next item.
            if weights[item] <= slack: # If slack capacity is enough for the next item:
                solution.append(item)  # Add the item to the knapsack. Consider it as collected.
                slack -= weights[item] # Reduce the slack (remaining) capacity.
                obj_val += vals[item]  # Increase the objective value by item's value. 
        
    # RETURNING SOLUTION         # Index 0: The objective value of the solution.
    result = (obj_val, solution) # Index 1: A list of collected items.
    return result

# TEST CODE

my_items = ("book", "clock", "computer", "painting", "radio", "vase")
my_capacity = 20
my_vals = dict(zip(my_items, (9, 175, 200, 99, 20, 50)))
my_weights = dict(zip(my_items, (1, 10, 20, 9, 4, 2)))
    
my_result = ks01_grd(my_items, my_capacity, my_vals, my_weights)  
print(my_result)