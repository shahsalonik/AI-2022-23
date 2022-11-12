import sys
from time import perf_counter

start = perf_counter()

N, subblock_height, subblock_width = 0, 0, 0
symbol_set = set()
constraint_list = []
neighbors = []
state_dict = dict()
solved_indices = []

symbol_set = {'1'}
#sys.argv[1]
filename = "Unit 2/puzzles_3_standard_medium.txt"

with open(filename) as f:
    line_list = [line.strip() for line in f]

def generate_board(state):
    state_dict = dict()

    for x in range(len(state)):
        if state[x] != ".":
            state_dict[x] = state[x]
            solved_indices.append(x)
        else:
            state_dict[x] = ''.join(symbol_set)
    
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
   return list(state[ind])

def create_solved_indices(state):
    solved_list = []
    for key in state:
        if len(state[key]) == 1:
            solved_list.append(key)
        if len(state[key]) == 0:
            return None
    return solved_list

def new_forward_looking(state):
    #value_list is the list of all the values in the symbol set
    value_list = list(symbol_set)

    while(len(solved_indices)) > 0:
        for x in solved_indices:
            for y in neighbors[x]:
                for z in y:
                    if state[z] in value_list:
                        value_list.remove(state[z])
                        count += 1
                    if count >= len(neighbors[y]):
                        count = 0
                state_dict[y] = ''.join(value_list)
    
    return state

def forward_looking(state):
    solved_list = []
    removed_set = set()


    solved_list = create_solved_indices(state)

    while len(solved_list) > 0:
        for x in solved_list:
            neighbor_list = list(neighbors[x][0])
            neighbor_list += list(neighbors[x][1])
            neighbor_list += list(neighbors[x][2])
            neighbor_list = set(neighbor_list)
            neighbor_list = list(neighbor_list)
            for y in neighbor_list:
                state_list = list(state[y])
                if state[y] == state[x] and y != x:
                    state_list.remove(state[x])
                    state_string = ''.join(state_list)
                    state[y] = state_string
                    if len(state[y]) == 1 and y not in removed_set:
                        solved_list.append(y)
                if len(state[y]) == 0:
                    return None
            solved_list.remove(x)
            removed_set.add(x)

    return state
    

def csp_backtracking_with_forward_looking(state):
    if goal_test(state):
        return state
    var = get_most_constrained_var(state)
    for val in get_sorted_values(state, var):
        new_state = state.copy()
        new_state[var] = val
        checked_board = new_forward_looking(new_state)
        if checked_board is not None:
            result = csp_backtracking_with_forward_looking(checked_board)
            if result is not None:
                return result
    return None

x = ".2.....34.....4."
N, symbol_set, subblock_width, subblock_height, symbol_set, constraint_list, neighbors = board_setup(x)
board_dict = generate_board(x)
print(board_dict)
print()
print(neighbors)
result = csp_backtracking_with_forward_looking(board_dict)
print("Solution:", result)
solved_indices = []


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
