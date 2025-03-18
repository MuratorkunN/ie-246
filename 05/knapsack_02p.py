from math import inf # We will use -inf as a penalty for infeasible solutions.
from enumeration import combinations # We will use combinations to create a list 
                                     # of all subsets of our items.

def ks01_exh(items, capacity, vals, weights):
    """Assumes 'items' as a tuple of unique collectibles (integer or string), 
           'capacity' as a numeric value representing the knapsack capacity,
           'vals' and 'weights' as dictionaries holding respectively the values 
           and the weights of collectibles.
       Guarantees an optimal solution for ``Knapsack 0-1'' problem with the
           exhaustive enumeration approach. Returns a two-element tuple 
           containing the optimal objective value and a list of optimal items
           to be collected."""
    
    # CHECKING OVERALL FEASIBILITY
    if capacity < 0:   # If the capacity is negative, then the problem is infeasible.
        solution = []  # No items can be collected at an infeasible situation.
        obj_val = -inf # Infeasibility indicated by the worst objective value.
    else:
        # GENERATION OF ALL SOLUTIONS
        all_subsets = combinations(items) # A list of all 2**n subsets (feasible or not).
        
        # FILTERING FEASIBLE SUBSETS
        is_feasible = lambda subset:(sum(weights[i] for i in subset) <= capacity)
        # is_feasible is a function that checks whether a given subset of items 
        # satisfies the capacity constraint or not. Returns a True or False.
        feasible_subsets = [subset for subset in all_subsets if is_feasible(subset)]
        # This list contains elements from all_subsets if only they are feasible.
        
        # IDENTIFYING THE BEST FEASIBLE SOLUTION
        total_value = lambda subset:sum(vals[i] for i in subset)
        # total_value is a function that evaluates and returns the total value 
        # for a given subset of items.
        solution = list(max(feasible_subsets, key = total_value))
        # max() custom-sorts feasible_subsets with respect to a descending order 
        # of their total value. Returns the subset with maximal total value.
        # The list format is chosen to stay consistent with ks01_grd() output format.
        obj_val = total_value(solution) # We re-evaluate the total value of the 
                                        # optimal solution.
                                        
    # RETURNING SOLUTION         # Index 0: The objective value of the solution.
    result = (obj_val, solution) # Index 1: A list of collected items. 
    return result

# TEST CODE

my_items = ("book", "clock", "computer", "painting", "radio", "vase")
my_capacity = 20
my_vals = dict(zip(my_items, (9, 175, 200, 99, 20, 50)))
my_weights = dict(zip(my_items, (1, 10, 20, 9, 4, 2)))
    
my_result = ks01_exh(my_items, my_capacity, my_vals, my_weights)  
print(my_result)   