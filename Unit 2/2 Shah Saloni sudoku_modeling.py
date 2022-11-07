import sys
from time import perf_counter

N, subblock_height, subblock_width = 0, 0, 0
symbol_set = set()
constraint_list = []
neighbors = []

symbol_set = {'1'}
#sys.argv[1]
filename = sys.argv[1]

with open(filename) as f:
    line_list = [line.strip() for line in f]

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
    if "." in state:
        return False
    return True

def get_next_unassigned_var(state):
    blank_index = state.index(".")
    return blank_index

def get_sorted_values(state,  neighbor_dict, ind):
    value_list = list(symbol_set)
    count = 0
    for y in neighbor_dict[ind]:
        for x in neighbor_dict[ind][count]:
            if state[x] in value_list:
                value_list.remove(state[x])
        count += 1
    return value_list

def csp_backtracking(state, neighbor_dict):
    state_list = list(state)
    if goal_test(state):
        return ''.join(state)
    var = get_next_unassigned_var(state)

    for val in get_sorted_values(state, neighbor_dict, var):
        new_state = state_list.copy()
        new_state[var] = val
        result = csp_backtracking(new_state, neighbor_dict)
        if result is not None:
            return result
    return None

count = 0
for x in line_list:
    N, symbol_set, subblock_width, subblock_height, symbol_set, constraint_list, neighbors = board_setup(x)
    result = csp_backtracking(x, neighbors)
    print("Puzzle", count, ", Solution:", result)
    count += 1
