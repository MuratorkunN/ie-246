from gurobipy import GRB, Model, quicksum

def ks01_ip(items, capacity, vals, weights):
    m = Model()
    x = m.addVars(items, vtype=GRB.BINARY)
    m.setObjective(quicksum(vals[j] * x[j] for j in items), sense=GRB.MAXIMIZE)
    m.addConstr(quicksum(weights[j] * x[j] for j in items) <= capacity)
    m.optimize()
    optimum = m.getAttr("x")
    solution = [items[j] for j in range(len(items)) if optimum[j] == 1]
    result = (m.getAttr("objVal"), list(solution))
    return result

# TEST CODE

my_items = ("book", "clock", "computer", "painting", "radio", "vase")
my_capacity = 20
my_vals = dict(zip(my_items, (9, 175, 200, 99, 20, 50)))
my_weights = dict(zip(my_items, (1, 10, 20, 9, 4, 2)))
    
my_result = ks01_ip(my_items, my_capacity, my_vals, my_weights)  
print(my_result)
        