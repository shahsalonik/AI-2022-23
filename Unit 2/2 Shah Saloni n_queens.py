import sys
from time import perf_counter

start = perf_counter()

def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True

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

    for i in range(size):
        is_valid = True
        index = 0

        if i in state:
            is_valid = False

        while is_valid and (var - index) >= 0:
            if (state[var - index] == i - index):
                is_valid = False
            if (state[var - index] == i + index):
                is_valid = False
            index += 1

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

print(generate_board(8))
board = generate_board(8)
print(csp_backtracking(board))

print(generate_board(9))
board = generate_board(9)
print(csp_backtracking(board))

print(generate_board(10))
board = generate_board(10)
print(csp_backtracking(board))

print("Total time: %s" % (end - start))
