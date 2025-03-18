from math import inf
from enumeration import combinations
def ks01_exh(items, capacity, vals, weights):
    if capacity < 0:
        obj_val, solution = -inf, []
    else:
        all_subsets = combinations(items)
        is_feasible = lambda subset:(sum(weights[i] for i in subset) <= capacity)
        feasible_subsets = [subset for subset in all_subsets if is_feasible(subset)]
        total_value = lambda subset:sum(vals[i] for i in subset)
        solution = list(max(feasible_subsets, key = total_value))
        obj_val = total_value(solution)
    result = (obj_val, solution)
    return result

# TEST CODE

my_items = ("book", "clock", "computer", "painting", "radio", "vase")
my_capacity = 20
my_vals = dict(zip(my_items, (9, 175, 200, 99, 20, 50)))
my_weights = dict(zip(my_items, (1, 10, 20, 9, 4, 2)))
    
my_result = ks01_exh(my_items, my_capacity, my_vals, my_weights)  
print(my_result)
        