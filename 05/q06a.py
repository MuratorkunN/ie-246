import numpy as np # We will use a 2-D array to represent the cost matrix.

def assgn_grd(workers, jobs, costs):
    """Assumes 'workers' as a tuple of unique workers (integer or string),
           'jobs' as a tuple of unique jobs (integer or string) of the same 
           size as 'workers', and 'costs' as a dictionary where keys are 
           two-element tuples representing worker-job couples and values are
           assignment costs.
       Guarantees a sub-optimal solution for ``Assignment'' problem with a
           greedy approach based on an increasing order of assignment costs of
           workers to jobs. Returns a two-element tuple containing the 
           objective value and a list of two-tuples representing 
           assignments."""

    # INITIALIZATION
    # We create a list containing all possible one-to-one assignments of 
    # workers to jobs as two-element tuples.
    couples = [(worker, job) for worker in workers for job in jobs] 
    solution = [] # This list will contain assignments in our greedy solution. 
     
    # GREEDY HEURISTIC
    # We custom-sort couples based on an inreasing order of assignment costs. 
    grd_order = sorted(couples, key = lambda couple:costs[couple])
    while grd_order:                  # The loop will repeat until 'grd_order' becomes an empty list.
        added_couple = grd_order[0]   # The couple with the least assignment cost is to be added.
        worker, job = added_couple    # Index 0 of 'added_couple' is 'worker', index 1 is 'job'.
        solution.append(added_couple) # We add this couple to solution.
        # We re-create the 'grd_order' list but, this time, we exclude all couples
        # containing either the 'worker' or the 'job'.
        grd_order = [couple for couple in grd_order if couple[0] != worker and couple[1] != job]
        
    # RETURNING SOLUTION
    # This sums up assignment costs of couples in our solution.
    obj_val = sum(costs[couple] for couple in solution) 
    result = (obj_val, solution) # Index 0: The objective value of the solution.
    return result                # Index 1: A list of assignments as two-element tuples.

# TEST CODE

my_workers = (1, 2, 3, 4)
my_jobs = ("A", "B", "C", "D")
x = np.array([14, 5, 12, 7, 
              20, 7, 6, 3, 
              10, 3, 4, 5, 
              12, 8, 7, 12]).reshape(4, 4)
my_costs = {(worker, job):x[i, j] for i, worker in enumerate(my_workers) 
            for j, job in enumerate(my_jobs)}

my_result = assgn_grd(my_workers, my_jobs, my_costs)
print(my_result)