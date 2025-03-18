import pandas as pd
from math import inf

def pack_items(item_weights, bag_capacity):
    """Assumes item_weights as a list of weights of unique items and 
           bag_capacity as a positive numeric value representing constant bag 
           capacity.
       Places items following the order in item_weights. Ties a bag if the
           next item does not fit and adds another empty bag for that item. 
           Returns a nested list where inner lists represent closed bags. Does 
           not return the optimale placement of bags."""
    
    all_bags, slack = [[]], bag_capacity
    for weight in item_weights:
        if weight <= slack:
            all_bags[-1].append(weight)
            slack -= weight
        else:
            all_bags.append([weight])
            slack = bag_capacity - weight
    return all_bags

def choose_best_pack(item_weights, bag_capacity_options, trace=False):
    """Assumes item_weights as a list of weights of unique items and 
           bag_capacity_options as a list of positive numeric values 
           representing alternative bag capacities, trace as boolean.
       Uses pack_items(). Returns the best bag capacity alternative under this 
           packaging policy. Shows results for all alternatives if trace is 
           True."""      
    
    minimum_slack = inf
    best_bag_list = None
    best_capacity_option = None
    total_weight = sum(item_weights)

    for bag_capacity in bag_capacity_options:
        bag_list = pack_items(item_weights, bag_capacity)
        total_capacity = bag_capacity * len(bag_list)
        total_slack = total_capacity - total_weight
        if trace:
            print("capacity:", bag_capacity, 
                  ", bags count:", len(bag_list), 
                  ", total capacity:", total_capacity, 
                  ", total slack:", round(total_slack, 2))
        if total_slack < minimum_slack:
            minimum_slack = total_slack
            best_bag_list = bag_list
            best_capacity_option = bag_capacity
    
    return (best_bag_list, best_capacity_option, minimum_slack)

df = pd.read_csv('q05_items_data.csv')
my_item_weights = df['weights'].to_list()
my_bag_capacity_options = [90 + i for i in range(31)]

best_bag_list, best_capacity_option, minimum_slack = choose_best_pack(my_item_weights, my_bag_capacity_options, True)
print(best_capacity_option)
print(round(minimum_slack, 2))