import sys
from time import perf_counter

start = perf_counter()

N, subblock_height, subblock_width = 0, 0, 0
symbol_set = set()
constraint_list = []
neighbors = []
state_dict = dict()

symbol_set = {'1'}
#sys.argv[1]
filename = "Unit 2/Sudoku Files/puzzles_5_standard_hard.txt"

with open(filename) as f:
    line_list = [line.strip() for line in f]

def generate_board(state):
    state_dict = dict()
    solved_indices = []

    for x in range(len(state)):
        if state[x] != ".":
            state_dict[x] = state[x]
            solved_indices.append(x)
        else:
            state_dict[x] = ''.join(symbol_set)
    
    return state_dict, solved_indices

def display_symbol_setup(state):
    sorted_symbol_set = sorted(symbol_set)
    count_dict = {}
    for x in sorted_symbol_set:
        count_dict[x] = state.count(x)
    return count_dict

def board_setup(state):
    N = int(len(state) ** 0.5)
    symbols = "123456789ABCDEFGHIJKLMNOPQRSTUVQXYZ"
    symbols = symbols[:N]
    symbol_set = set(symbols)
    subblock_height = int(N ** 0.5)
    can_continue = True

    while subblock_height < N and can_continue:
        if N % subblock_height == 0:
            can_continue = False
        else:
            subblock_height += 1

    subblock_width = N // subblock_height

    temp = subblock_height

    if subblock_height > subblock_width:
        subblock_height = subblock_width
        subblock_width = temp

    row_set = [{i for i in range(row * N, (row + 1) * N)} for row in range(N)]
    col_set = [{i for i in range(col, col + len(state) - subblock_width * subblock_height + 1, subblock_width * subblock_height)} for col in range(N)]
    block_set = [{(row + subblock_col) + (subblock_row * N) + col for subblock_row in range(subblock_height) for col in range(subblock_width)} for row in range(0, len(state), subblock_height * N) for subblock_col in range(0, N, subblock_width)]

    constraint_list = row_set + col_set + block_set
    neighbors = dict()

    for n in range(len(state)):
        neighbors[n] = [num for num in constraint_list if n in num and num != n]
        neighbor_set = list(neighbors[n][0])
        neighbor_set += list(neighbors[n][1])
        neighbor_set += list(neighbors[n][2])
        neighbor_set = set(neighbor_set)
        neighbors[n] = neighbor_set

    return N, symbol_set, subblock_width, subblock_height, symbol_set, constraint_list, neighbors

def print_board(state):
    for x in range(0, N*N, N):
        i = x
        current_block = "| "
        while i < x + N:
            current_block += str(state[i]) + " "
            i += 1
        current_block += "|"
        print(current_block)

def goal_test(state):
    for key in state:
        if len(state[key]) > 1:
            return False
    return True

def get_most_constrained_var(state):
    min_length = -1
    min_index = 0

    for key in state:
        if (min_length == -1 and len(state[key]) != 1) or (len(state[key]) < min_length and len(state[key]) != 1):
            min_length = len(state[key])
            min_index = key

    return min_index

def get_sorted_values(state, ind):
   return list(state[ind])

#pass in solved indices
#forward looking should be able to solve the medium puzzles relatively easily
#might take some time for hard -- for this one you do constraint prop
def new_forward_looking(state, solved_indices):
    removed_set = set()
    size = len(state)

    while solved_indices and len(removed_set) != size:
        x = solved_indices.pop()
        for y in neighbors[x]:
            y_set = set(state[y])
            if x != y and state[x] in y_set:
                y_set.remove(state[x])
                state[y] = ''.join(y_set)
                if len(state[y]) == 1 and y not in removed_set:
                    solved_indices.append(y)
                if len(state[y]) == 0:
                    return None
        removed_set.add(x)
    return state

def constraint_propagation():
    return "TODO"
'''
#consider popping instead of looping (x)
    while solved_indices and len(removed_set) != size:
        for x in solved_indices:
            for y in neighbor_list:
                y_list = list(state[y])
                if state[x] in y_list and x != y:
                    y_list.remove(state[x])
                if len(y_list) == 1 and x != y and y not in removed_set:
                    solved_indices.append(y)
                if len(y_list) == 0:
                    return None
                state[y] = ''.join(y_list)
            removed_set.add(x)
'''

def csp_backtracking_with_forward_looking(state, solved_indices):
    if goal_test(state):
        return state
    var = get_most_constrained_var(state)
    for val in get_sorted_values(state, var):
        new_state = state.copy()
        new_state[var] = val
        checked_board = new_forward_looking(new_state, [var])
        if checked_board is not None:
            result = csp_backtracking_with_forward_looking(checked_board, solved_indices.copy())
            if result is not None:
                return result
    return None

'''
#4 x 4 3.....2..4.....1
x = "....8.4....2....1..6.......59....1.....6.2.......7.......5...6.4..1.....3...4...."
N, symbol_set, subblock_width, subblock_height, symbol_set, constraint_list, neighbors = board_setup(x)
board_dict, solved_indices = generate_board(x)
print(board_dict)
print()
print(neighbors)
result = new_forward_looking(board_dict.copy(), solved_indices.copy())
print(result)
print("moving on")
result = csp_backtracking_with_forward_looking(result, solved_indices)
solution = ""
for key in result:
    solution += result[key]
print("Solution:", solution)
solved_indices = []
'''
 
count = 0
for x in line_list:
    N, symbol_set, subblock_width, subblock_height, symbol_set, constraint_list, neighbors = board_setup(x)
    board_dict, solved_indices = generate_board(x)
    result = new_forward_looking(board_dict.copy(), solved_indices.copy())
    result = csp_backtracking_with_forward_looking(result, solved_indices)
    solution = ""
    for key in result:
        solution += result[key]
    print("Puzzle", count, "Solution:", solution)
    solved_indices = []
    count += 1

    
    
end = perf_counter()
print("Total Time: %s" % (end - start))
