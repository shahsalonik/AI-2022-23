
import sys
from time import perf_counter

start = perf_counter()

def goal_test(state):
    if None not in state:
        return True
    return False

def get_next_unassigned_var(state):
    none_index = state.index(None)
    return none_index

def get_sorted_values(state, var):
    return ""

def csp_backtracking(state):
    if goal_test(state):
        return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        val = var
        result = csp_backtracking(val)
        if result is not None:
            return result
    return None

end = perf_counter()
print("Total time: %s" % (end - start))
