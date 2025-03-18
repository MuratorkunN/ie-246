from math import inf
def ks01_grd(items, capacity, vals, weights):
    if capacity < 0:
        obj_val, solution = -inf, []
    else:
        obj_val, solution, slack = 0, [], capacity
        v2w_ratio = {item:vals[item]/weights[item] for item in items}
        grd_order = sorted(items, key=lambda item:v2w_ratio[item], reverse=True)  
        for item in grd_order:         
            if weights[item] <= slack:
                solution.append(item)  
                slack -= weights[item] 
                obj_val += vals[item] 
    result = (obj_val, solution)
    return result

my_items = ("book", "clock", "computer", "painting", "radio", "vase")
my_capacity = 20
my_vals = dict(zip(my_items, (9, 175, 200, 99, 20, 50)))
my_weights = dict(zip(my_items, (1, 10, 20, 9, 4, 2)))
    
my_result = ks01_grd(my_items, my_capacity, my_vals, my_weights)  
print(my_result)