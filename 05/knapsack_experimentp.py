from math import inf
from copy import deepcopy as dc
import numpy as np
from time import time as ts # ts stands for time stamp.
from gurobipy import GRB, Model, quicksum

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

def ks01_ip(items, capacity, vals, weights):
    m = Model()
    m.Params.LogToConsole = 0
    x = m.addVars(items, vtype=GRB.BINARY)
    m.setObjective(quicksum(vals[j] * x[j] for j in items), sense=GRB.MAXIMIZE)
    m.addConstr(quicksum(weights[j] * x[j] for j in items) <= capacity)
    m.optimize()
    optimum = m.getAttr("x")
    solution = [items[j] for j in range(len(items)) if optimum[j] == 1]
    result = (m.getAttr("objVal"), list(solution))
    return result

########
# EXPERIMENTS
########

rng = np.random.default_rng(seed=1234) 
# The seed parameter with a fixed argument will generate the same random data, independent of the computer 
# on which this experiment is executed.
n_values = (50, 100, 150, 200)                 # The size of instances will vary from 50 to 200.                                          
test_functions = (ks01_grd, ks01_rec, ks01_ip) # A tuple containing names of the functions to be tested.
for n in n_values:
    my_items, my_capacity = tuple(range(n)), 8 * n          # Items are labeled with integers. Total capacity is 8 times the number of items.
    my_vals = dict(zip(my_items, rng.integers(50,151,n)))   # Values are randomly selected integers from 50 to 150.
    my_weights = dict(zip(my_items, rng.integers(10,51,n))) # Weights are randomly selected integers from 10 to 50.
    for test_function in test_functions:                    # We will test both the greedy heuristic and the recursive approach.
        start = ts()                                                   # Take a time stamp before execution starts.
        my_result = test_function(my_items, my_capacity, my_vals, my_weights) # Call the function with random data.
        finish = ts()                                                  # Take another time stamp after execution is complete.
        print(f"Total value: {my_result[0]}")                        # Report the total value of collected items.          
        print(f"Collected items are: {sorted(my_result[1])}.")       # Print the list of collected items.
        used_capacity = sum(my_weights[item] for item in my_items    # Calculate the total weight of collected items. 
                            if item in my_result[1])  
        print(f"Used capacity is {used_capacity}/{my_capacity}.")    # Report the used capacity.
        print(f"Solution time: {round(finish-start, 3)} seconds.\n") # Report the solution time in seconds.