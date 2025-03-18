from math import inf
def ks01_rec_naive(items, capacity, vals, weights):
    if capacity < 0:
        obj_val = -inf
    elif len(items) == 1:
        item = items[0]
        obj_val = 0 if weights[item] > capacity else vals[item]
    else:
        item, rmn_items = items[0], items[1:]
        rmn_capacity = capacity - weights[item]
        obj_0 = ks01_rec_naive(rmn_items, capacity, vals, weights)
        obj_1 = vals[item] + ks01_rec_naive(rmn_items, rmn_capacity, vals, weights)
        obj_val = max(obj_0, obj_1)
    return obj_val

my_items = ("book", "clock", "computer", "painting", "radio", "vase")
my_capacity = 20
my_vals = dict(zip(my_items, (9, 175, 200, 99, 20, 50)))
my_weights = dict(zip(my_items, (1, 10, 20, 9, 4, 2)))

my_result = ks01_rec_naive(my_items, my_capacity, my_vals, my_weights)
print(my_result)