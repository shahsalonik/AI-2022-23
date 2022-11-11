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
filename = "Unit 2/puzzles_3_standard_medium.txt"

with open(filename) as f:
    line_list = [line.strip() for line in f]

def generate_board(state, neighbor_dict):
    state_dict = dict()
    new_state = list(state)
    state_list = list(state)
    ind_count = 0

    for x in state:
        if x != ".":
            state_dict[ind_count] = str(x)
            ind_count += 1
        else:
            value_list = list(symbol_set)
            count = 0
            ind = new_state.index(x)
            for y in neighbor_dict[ind]:
                for z in neighbor_dict[ind][count]:
                    if state[z] in value_list:
                        value_list.remove(state[z])
                    count += 1
                if count >= len(neighbor_dict[ind]):
                    count = 0
            state_dict[ind] = ''.join(value_list)
            new_state[ind] = ""
            ind_count += 1
    return state_dict

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
    min_length = len(state[0])
    min_index = 0

    for key in state:
        if len(state[key]) < min_length and len(state[key]) != 1:
            min_length = len(state[key])
            min_index = key

    return min_index

def get_sorted_values(state, ind):
   return state[ind]

def forward_looking(state):
    solved_list = []

    for key in state:
        if len(state[key]) == 1:
            solved_list.append(key)
        if len(state[key]) == 0:
            return None

    while len(solved_list) > 0:
        count = 0
        for x in solved_list:
            solved_value = state[x]
            for y in neighbors[x][count]:
                if solved_value in state[y]:
                    state[y].replace(solved_value, "")
                if len(state[y]) == 1:
                    solved_list.append(y)
                if len(state[y]) == 0:
                    return None
            count += 1
        count = 0

    return state
    

def csp_backtracking_with_forward_looking(state):
    if goal_test(state):
        return state
    var = get_most_constrained_var(state)
    for val in get_sorted_values(state, var):
        new_state = state.copy()
        new_state[var] = val
        checked_board = forward_looking(new_state)
        if checked_board is not None:
            result = csp_backtracking_with_forward_looking(checked_board)
            if result is not None:
                return result
    return None

x = "....42..41...."
N, symbol_set, subblock_width, subblock_height, symbol_set, constraint_list, neighbors = board_setup(x)
board_dict = generate_board(x, neighbors)
print(board_dict)
print()
print(neighbors)
result = csp_backtracking_with_forward_looking(board_dict)
print("Solution:", result)


'''    
count = 0
for x in line_list:
    N, symbol_set, subblock_width, subblock_height, symbol_set, constraint_list, neighbors = board_setup(x)
    board_dict = generate_board(x, neighbors)
    #print(board_dict)
    #print()
    #print(neighbors)
    result = csp_backtracking_with_forward_looking(board_dict)
    print("Puzzle", count, "Solution:", result)
    count += 1
'''
    
    
end = perf_counter()
print("Total Time: %s" % (end - start))
