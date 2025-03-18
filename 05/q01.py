from math import inf
from copy import deepcopy as dc
import numpy as np

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
        item = items[0]
        rmn_items = items[1:]
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
        if obj_0 > obj_1: 
            results[(items, capacity)] = (obj_0, sol_0)
        else:
            results[(items, capacity)] = (obj_1, sol_1)     
    return results[(items, capacity)]

n_values = (50, 100, 150, 200)
for n in n_values:
    my_items, my_capacity = tuple(range(n)), 8 * n
    sub_opt_values = []
    for i in range(10):
        rng = np.random.default_rng()
        my_vals = dict(zip(my_items, rng.integers(50,151,n)))
        my_weights = dict(zip(my_items, rng.integers(10,51,n))) 
        obj_grd = ks01_grd(my_items, my_capacity, my_vals, my_weights)[0]
        obj_rec = ks01_rec(my_items, my_capacity, my_vals, my_weights)[0]
        sub_optimality = 100 * (obj_rec- obj_grd) / obj_rec
        sub_opt_values.append(sub_optimality)
    avg_sub_optimality = np.array(sub_opt_values).mean()
    print(f"Average sub-optimality for n={n}: {round(avg_sub_optimality, 4)} %")