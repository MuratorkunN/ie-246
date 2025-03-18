import numpy as np # We will use a numpy matrix to introduce assignment costs in the test code.
from copy import deepcopy as dc # We will use deep copies of solutions collected from 'results'
                                # dictionary, so the dictionary values will not be affected.

def assgn_rec(workers, jobs, costs, results=None):
    """Assumes 'workers' as a tuple of unique workers (integer or string),
           'jobs' as a tuple of unique jobs (integer or string) of the same 
           size as 'workers', and 'costs' as a dictionary where keys are 
           two-element tuples representing worker-job couples and values are
           assignment costs.
       Guarantees an optimal solution for ``Assignment'' problem with an
           enhanced recursive approach. Returns a two-element tuple containing 
           the objective value and a list of assignments (as two-element 
           tuples)."""
    if results == None: # If the user does not pass any argument for results,
        results = {}    # it will automatically be set as an empty dictionary.
    if len(jobs) == 1:                       # BASE CASE: If there is only a single worker-job couple.
        added_couple = (workers[0], jobs[0]) # Create a two-element tuple from this single couple.
        obj_val = costs[added_couple]        # Objective value is the only assignment cost.
        results[(workers, jobs)] = (obj_val, [added_couple]) # Add the obvious solution of this problem to 'results'.
    else:                         # RECURSIVE CASE: If there are at least two items.
        worker = workers[0]       # Take the first worker in consideration.
        rmn_workers = workers[1:] # Create a sliced tuple from remaining workers.
        obj_vals = {}    # Create an empty dictionary 'obj_vals' to store all optimal objective values
        for job in jobs: # conditioned on that the first worker is assigned to each job, one by one.
            rmn_jobs = tuple(j for j in jobs if j != job) # Create a tuple from remaining jobs (except the assigned one).
            if (rmn_workers, rmn_jobs) in results.keys():       # If the sub-problem is in keys of 'results'.
                obj, sol = dc(results[(rmn_workers, rmn_jobs)]) # Retrieve a deepcopy of the solution.
            # If the problem is not in 'results', call assgn_rec() recursively, take a deepcopy of the solution.
            else:
                obj, sol = dc(assgn_rec(rmn_workers, rmn_jobs, costs, results))
            obj += costs[(worker, job)] # Increment the objective with the assignment cost of the couple in consideration.
            sol.append((worker, job))   # Append the couple in consideration to the solution of the sub-problem.
            obj_vals[job] = (obj, sol)  # Add the objective value and the solution to 'obj_vals' dictionary.
        # The minimum total assignment cost accross "assigned jobs to the first worker"  
        # is identified. 'job_star' is the optimal job assigned to the first worker.
        job_star = min(jobs, key = lambda job:obj_vals[job][0])
        results[(workers, jobs)] = obj_vals[job_star] # Update 'results' dictionary with the problem:solution pair
    return results[(workers, jobs)]                   # and return the solution from 'results' dictionary.

my_workers = (1, 2, 3, 4)
my_jobs = ("A", "B", "C", "D")
x = np.array([14, 5, 12, 7, 
              20, 7, 6, 3, 
              10, 3, 4, 5, 
              12, 8, 7, 12]).reshape(4, 4)
my_costs = {(worker, job):x[i, j] for i, worker in enumerate(my_workers) 
            for j, job in enumerate(my_jobs)}

my_result = assgn_rec(my_workers, my_jobs, my_costs)
print(my_result)