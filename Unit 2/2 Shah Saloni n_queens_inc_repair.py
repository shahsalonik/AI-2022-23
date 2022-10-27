import random
from time import perf_counter
from heapq import heapify

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

def inc_repair_generate_board(size):
    board = [i for i in range(size)]
    for i in range(len(board)):
        board[i] = random.choice(board)
    return board

def inc_repair_goal_test(conflicts_sum):
    if conflicts_sum == 0:
        return True
    return False

def inc_repair_conflicts(state, index):
    size = len(state)

    conf = state.count(state[index]) - 1
    conf_diff = index - state[index]

    diff = [i - state[i] for i in range(size)]

    conf += diff.count(conf_diff) - 1
    conf_sum = index + state[index]

    sum_diff = [i + state[i] for i in range(size) if state[i] != None]

    conf += sum_diff.count(conf_sum) - 1

    return conf

#pick from middle bc it's more efficient
#use a min heap 
def inc_repair_get_next_unassigned_var(state, conflict):
    size = len(state)
    most_conflicts = max(conflict)
    calc_conflict = [x for x in range(size) if conflict[x] == most_conflicts]
    return random.choice(calc_conflict)

def inc_repair_get_sorted_values(state, var):
    index = state[var]
    children = []
    
    size = len(state)

    for i in range(size):
        if index != i:
            new_state = state.copy()
            new_state[var] = i
            
            conflict = inc_repair_conflicts(new_state, var)
            children.append((conflict, i))
    
    heapify(children)
    return children

def inc_repair_backtracking(state, conflicts):
    size = len(state)
    total_conflicts = sum(conflicts)

    if inc_repair_goal_test(total_conflicts):
        return state

    print("Current board state: ", state)
    print("Conflicts: ", total_conflicts, "\n")

    var = inc_repair_get_next_unassigned_var(state, conflicts)

    for conf, val in inc_repair_get_sorted_values(state, var):
        new_state = state.copy()
        new_state[var] = val

        conf_sum = [inc_repair_conflicts(new_state, x) for x in range(size)]
        result = inc_repair_backtracking(new_state, conf_sum)

        if result is not None:
            return result
    return None

start = perf_counter()

board = inc_repair_generate_board(31)
conflict = [inc_repair_conflicts(board, x) for x in range(len(board))]
solved = inc_repair_backtracking(board, conflict)
print(solved)
print(test_solution(solved))

print("\n***NEXT BOARD***")
board = inc_repair_generate_board(35)
conflict = [inc_repair_conflicts(board, x) for x in range(len(board))]
solved = inc_repair_backtracking(board, conflict)
print("Solved board state: ", solved)
print(test_solution(solved))

end = perf_counter()

print("Total time: %s" % (end - start))
