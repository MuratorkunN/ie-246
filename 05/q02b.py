from math import inf, floor
from copy import deepcopy as dc

# The solution of a problem will be kept as a two element tuple, however, this
# time, at index 1, we will have a dictionary where keys are the items and 
# values are the number of collected units from each item.

def ksbnd_rec(items, capacity, vals, weights, units, results=None):
    if results == None:
        results = {}
    if capacity < 0:
        results[(items, capacity)] = (-inf, {})
    elif len(items) == 1:
        item = items[0]
        num_available = units[item]
        num_feasible = floor(capacity / weights[item])
        num_collected = min(num_available, num_feasible)
        results[(items, capacity)] = (num_collected * vals[item], {item: num_collected})
    else:
        item = items[0]
        rmn_items = items[1:]
        alternatives = {}
        for n in range(units[item]+1):
            rmn_capacity = capacity - n * weights[item]
            if (rmn_items, rmn_capacity) in results.keys():
                obj, sol = dc(results[(rmn_items, rmn_capacity)])
            else:
                obj, sol = dc(ksbnd_rec(rmn_items, rmn_capacity, vals, weights, units, results))
            obj += n * vals[item]
            sol[item] = n
            alternatives[n] = (obj, sol)
        n_star = sorted(alternatives.keys(), key = lambda alt:alternatives[alt][0], reverse=True)[0]
        results[(items, capacity)] = alternatives[n_star]
    return results[(items, capacity)]