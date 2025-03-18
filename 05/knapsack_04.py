from math import inf
from copy import deepcopy as dc

def ks01_rec(items, capacity, vals, weights, results=None):
    if results == None:
        results = {}
        
    if capacity < 0: 
        results[(items, capacity)] = (-inf, [])
        
    elif len(items) == 1:
        item = items[0]
        if weights[item] > capacity:
            results[(items, capacity)] = (0, [])
        else:
            results[(items, capacity)] = (vals[item], [item])
            
    else:
        item, rmn_items = items[0], items[1:]
        rmn_capacity = capacity-weights[item]
        if (rmn_items, capacity) in results.keys():
            obj_0, sol_0 = dc(results[(rmn_items, capacity)])
        else:
            obj_0, sol_0 = dc(ks01_rec(rmn_items, capacity, vals, weights, results))
        if (rmn_items, rmn_capacity) in results.keys():
            obj_1, sol_1 = dc(results[(rmn_items, rmn_capacity)])
        else:
            obj_1, sol_1 = dc(ks01_rec(rmn_items, rmn_capacity, vals, weights, results))
        obj_1 += vals[item]
        sol_1.append(item)
        results[(items, capacity)] = (obj_0, sol_0) if obj_0 > obj_1 else (obj_1, sol_1)
        
    return results[(items, capacity)]

my_items = ("book", "clock", "computer", "painting", "radio", "vase")
my_capacity = 20
my_vals = dict(zip(my_items, (9, 175, 200, 99, 20, 50)))
my_weights = dict(zip(my_items, (1, 10, 20, 9, 4, 2)))
all_results = {}

my_result = ks01_rec(my_items, my_capacity, my_vals, my_weights, all_results)
print(my_result)
print(all_results)