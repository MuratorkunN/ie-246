import pandas as pd
from math import inf

def pack_items(item_weights, bag_capacity, tied=True):
    """Assumes item_weights as a list of weights of unique items and 
           bag_capacity as a positive numeric value representing constant bag 
           capacity, tied as a boolean.
       Places items following the order in item_weights. If tied is True, ties 
           a bag if the next item does not fit and adds another empty bag for 
           that item. Else, bags remain untied, we check all earlier bags to 
           fit the next item. If it does not fit to any slack capacity, we add 
           another empty bag for that item. Returns a nested list where inner 
           lists represent closed bags. Does not return the optimale placement 
           of bags."""
    
    all_bags = [[]]
    if tied:
        slack = bag_capacity
        for weight in item_weights:
            if weight <= slack:
                all_bags[-1].append(weight)
                slack -= weight
            else:
                all_bags.append([weight])
                slack = bag_capacity - weight
    else:
        bag_slacks = [bag_capacity]
        for weight in item_weights:
            placed = False
            for i, bag in enumerate(all_bags):
                if weight <= bag_slacks[i]: # Place item into the first bagthat it fits.
                    bag.append(weight)
                    bag_slacks[i] -= weight
                    placed = True
                    break # Terminates the second for loop if the item is placed in an earlier bag.
            if not placed: # Item is not placed to any earlier bag. Create a new bag.
                new_bag = [weight]
                all_bags.append(new_bag)
                bag_slacks.append(bag_capacity - weight)
    return all_bags

def choose_best_pack(item_weights, bag_capacity_options, tied=True, trace=False):
    """Assumes item_weights as a list of weights of unique items and 
           bag_capacity_options as a list of positive numeric values 
           representing alternative bag capacities, tied and trace as booleans.
       Based on the argument of "tied", uses either tied or untied version of 
           pack_items(). Returns the best bag capacity alternative under any 
           packaging policy. Shows results for all alternatives if trace is 
           True."""    
    
    minimum_slack = inf
    best_bag_list = None
    best_capacity_option = None
    total_weight = sum(item_weights)

    for bag_capacity in bag_capacity_options:
        bag_list = pack_items(item_weights, bag_capacity, tied=tied) # "tied" parameter of  pack_items() is assigned 
        total_capacity = bag_capacity * len(bag_list)                # as the argument passed to choose_best_pack().
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

best_bag_list, best_capacity, minimum_slack = choose_best_pack(my_item_weights, my_bag_capacity_options, trace=True)
print(best_capacity)
print(round(minimum_slack, 2))

best_bag_list, best_capacity, minimum_slack = choose_best_pack(my_item_weights, my_bag_capacity_options, False, True)
print(best_capacity)
print(round(minimum_slack, 2))