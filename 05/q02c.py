from q02a import ksbnd_grd
from q02b import ksbnd_rec

my_items = tuple(range(3))
my_capacity = 410
my_vals = dict(zip(my_items, (5.13, 10.50, 4.00)))
my_weights = dict(zip(my_items, (27, 50, 20)))
my_units = dict(zip(my_items, (6, 10, 6)))
my_results = {}

print(ksbnd_grd(my_items, my_capacity, my_vals, my_weights, my_units))
print(ksbnd_rec(my_items, my_capacity, my_vals, my_weights, my_units, my_results))