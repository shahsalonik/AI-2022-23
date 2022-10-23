import sys
from time import perf_counter

start = perf_counter()

def generate_board(size):
    board = []
    for x in range(size):
        board.append(None)

    return board

def goal_test(state):
    if None not in state:
        return True
    return False

def get_next_unassigned_var(state):
    none_index = state.index(None)
    return none_index

def get_sorted_values(state, var):
    children = []
    size = len(state)
    is_valid = True

    for i in range(size):
        if i in state:
            is_valid = False
        if (i - 1) != 0:
            if (i - 1) in state:
                is_valid = False
        if (i + 1) < size:
            if (i + 1) in state:
                is_valid = False
        if is_valid:
            children.append(i)
    return children
            

def csp_backtracking(state):
    if goal_test(state):
        return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_state = state.copy()
        new_state[var] = val
        result = csp_backtracking(new_state)
        if result is not None:
            return result
    return None

end = perf_counter()

print(generate_board(4))
board = generate_board(4)
print(csp_backtracking(board))

print("Total time: %s" % (end - start))
