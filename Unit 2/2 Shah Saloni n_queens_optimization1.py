import sys
from time import perf_counter
from heapq import heapify, heappop, heappush

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
    board = [None for x in range(size)]
    diagonal = [None for x in range(size * 2 - 1)]
    diagonal2 = diagonal.copy()
    return board, diagonal, diagonal2

def goal_test(state):
    if None not in state:
        return True
    return False

def get_next_unassigned_var(state):
    size = len(state)
    heap_values =[(abs(size // 2), index) for index in range(size) if state[index] == None]
    heapify(heap_values)
    return heappop(heap_values)[1]

def get_sorted_values(state, var, left_diag, right_diag):
    children = []
    size = len(state)
    index = 0

    #check above middle row first
    for i in range(size // 2):
        if state[i] == None and left_diag[var + i] == None and right_diag[var - 1 - i + size] == None:
            children.append(i)
    #check middle row and below 
    #need to check columns and diagonals
    for i in range(size // 2 - 1, -1, -1):
        if state[i] == None and left_diag[var + i] == None and right_diag[var - 1 - i + size] == None:
            children.insert(index, i)
            index += 2
    
    #initially gives me a reversed list, so reverse that
    return children[::-1]

def csp_backtracking(state, diagonal, diagonal2):
    size = len(state)
    if goal_test(state):
        return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var, diagonal, diagonal2):
        new_state = state.copy()
        new_diagonal = diagonal.copy()
        new_diagonal2 = diagonal2.copy()

        new_state[var] = val
        new_diagonal[var + val] = val
        new_diagonal2[var - 1 - val + size] = val

        result = csp_backtracking(new_state, new_diagonal, new_diagonal2)
        if result is not None:
            return result

        new_state[var] = None
        new_diagonal[var + val] = None
        new_diagonal2[var - 1 - val + size] = None
    return None

end = perf_counter()

board, diagonal, diagonal2 = generate_board(31)
print(csp_backtracking(board, diagonal, diagonal2))

print("Total time: %s" % (end - start))
