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
    for n in range(size):
        count = 0
        if n in state:
            is_valid = False
        while is_valid == True and var == n - count:
            if ((n - count) >= 0) :
                is_valid = False
            count += 1
    if is_valid:
        children.append(n)
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
