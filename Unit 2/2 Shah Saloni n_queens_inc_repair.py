import sys
import random
from time import perf_counter
from heapq import heapify, heappop, heappush

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
    board = [i for i in range(size)]
    for i in range(len(board)):
        board[i] = random.choice(board)
    return board

def goal_test(conflicts_sum):
    if conflicts_sum == 0:
        return True
    return False

#pick from middle bc it's more efficient
#use a min heap 
def get_next_unassigned_var(state):
    size = len(state)
    heap_values =[(abs(size // 2 - index), index) for index in range(size) if state[index] == None]
    heapify(heap_values)
    return heappop(heap_values)[1]

def get_sorted_values(state, var, column, left_diag, right_diag):
    children = []
    size = len(state)
    index = 0

    #check above middle row first
    for i in range(size // 2, size):
        if (i not in state) and (column[i] == None) and (left_diag[var + i] == None) and (right_diag[var - i - 1 + size] == None):
            children.append(i)
    #check middle row and below 
    #need to check columns and diagonals
    for i in range(size // 2 - 1, -1, -1):
        if (i not in state) and (column[i] == None) and (left_diag[var + i] == None) and (right_diag[var - i - 1 + size] == None):
            children.insert(index, i)
            index += 2
    
    #reversed list works better
    return children[::-1]

def csp_backtracking(state, conflicts):
    size = len(state)
    total_conflicts = sum(conflicts)

    if goal_test(total_conflicts):
        return state

    print("Current board state: ", state)
    print("Conflicts: ", total_conflicts)

    var = get_next_unassigned_var(state, conflicts)

    for conf, val in get_sorted_values(state, conflicts):
        new_state = state.copy()
        new_state[var] = val

        result = csp_backtracking(new_state, [**SOME CONDITION** for i in range(len(state))])

        if result is not None:
            return result
    return None


start = perf_counter()

'''
#31x31
board, column, diagonal, diagonal2 = generate_board(31)
print(csp_backtracking(board, column, diagonal, diagonal2))
print(test_solution(csp_backtracking(board, column, diagonal, diagonal2)))

#35x35
board, column, diagonal, diagonal2 = generate_board(35)
print(csp_backtracking(board, column, diagonal, diagonal2))
print(test_solution(csp_backtracking(board, column, diagonal, diagonal2)))
'''
end = perf_counter()

print("Total time: %s" % (end - start))