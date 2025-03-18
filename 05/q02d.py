from q02a import ksbnd_grd
from q02b import ksbnd_rec
import pandas as pd

stock_df = pd.read_csv("q02_bonds_data.csv")

my_items = tuple(range(len(stock_df)))
my_capacity = 3000
my_vals = dict(zip(my_items, stock_df["profit"]))
my_weights = dict(zip(my_items, stock_df["price"]))
my_units = dict(zip(my_items, stock_df["quantity"]))
my_results = {}

my_result = ksbnd_grd(my_items, my_capacity, my_vals, my_weights, my_units)
used_capacity = sum(my_weights[item] * my_result[1][item] for item in my_items) 
print(my_result)
print(used_capacity)

my_result = ksbnd_rec(my_items, my_capacity, my_vals, my_weights, my_units, my_results)
used_capacity = sum(my_weights[item] * my_result[1][item] for item in my_items) 
print(my_result)
print(used_capacity)