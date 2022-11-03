import sys
from time import perf_counter

N, subblock_height, subblock_width = 0, 0, 0
symbol_set = set()

symbol_set = {'1'}
#sys.argv[1]
filename = "Sudoku Files/puzzles_2_variety_easy.txt"

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

    return N, symbol_set, subblock_width, subblock_height, symbol_set

def print_board(state):
    for x in range(0, N*N, N):
        i = x
        current_block = "| "
        while i < x + N:
            current_block += state[i] + " "
            i += 1
        current_block += "|"
        print(current_block)

for x in line_list:
    N, symbol_set, subblock_width, subblock_height, symbol_set = board_setup(x)
    print(subblock_width, " ", subblock_height)
    print_board(x)
    print(display_symbol_setup(x))
    print()