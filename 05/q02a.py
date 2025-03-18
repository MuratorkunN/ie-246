from math import inf, floor

# The solution of a problem will be kept as a two element tuple, however, this
# time, at index 1, we will have a dictionary where keys are the items and 
# values are the number of collected units from each item.

def ksbnd_grd(items, capacity, vals, weights, units):
    if capacity < 0:
        obj_val, solution = -inf, {}
    else:
        obj_val, solution, slack = 0, {}, capacity
        v2w_ratio = {item:vals[item]/weights[item] for item in items}
        grd_order = sorted(items, key=lambda item:v2w_ratio[item], reverse=True)  
        for item in grd_order:
            num_available = units[item]
            num_feasible = floor(slack / weights[item])      # This is where we use the floor function.
            num_collected = min(num_available, num_feasible)
            solution[item] = num_collected  
            slack -= num_collected * weights[item] 
            obj_val += num_collected * vals[item] 
    result = (obj_val, solution)
    return result