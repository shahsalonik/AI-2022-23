from heapq import heapify, heappush, heappop
import sys
from time import perf_counter

#sys.argv[1]
filename = "slide_puzzle_tests_2.txt"

with open(filename) as f:
    line_list = [line.strip() for line in f]

def find_goal(board):
    size, board = board.split()
    sorted_board = sorted(board)
    goal_state = sorted_board[1:]
    goal_state.append(".")
    return ''.join(goal_state)

def get_children(state):
    size, board = state.split()
    size = int(size)
    blank_index = int(board.index("."))
    children = []
    if blank_index % size != 0: #blank swap right
        children.append(str(size) + " " + board[:blank_index - 1] + "." + board[blank_index - 1] + board[blank_index + 1:])
    if (blank_index + 1) % size != 0: #blank swap left
        children.append(str(size) + " " + board[:blank_index] + board[blank_index + 1] + "." + board[blank_index + 2:])
    if blank_index >= size: #blank swap up
        children.append(str(size) + " " + board[:blank_index - size] + "." + board[blank_index - size + 1:blank_index] + board[blank_index - size] + board[blank_index + 1:]) 
    if blank_index < (size * (size - 1)): #blank swap down
        children.append(str(size) + " " + board[:blank_index] + board[blank_index + size] + board[blank_index + 1:blank_index + size] + "." + board[blank_index + size + 1:])
    return children


#parity check
def is_solvable(state):
    size, board = state.split()
    blank_index = int(board.index("."))
    other_board = board[:blank_index] + board[blank_index + 1:]
    size = int(size)

    out_of_order = 0

    if size % 2 != 0:
        for x in range(len(other_board) - 1):
            for y in other_board[x:]:
                if ord(other_board[x]) > ord(y):
                    out_of_order += 1
        
        if out_of_order % 2 == 0:
            return True
    else:
        for x in range(len(other_board) - 1):
            letter = other_board[x]
            for y in other_board[x:]:
                if ord(other_board[x]) > ord(y):
                    out_of_order += 1
        
        row_count = 0
        #find rows by splitting the board into its sizes
        for row in range(0, size*size, size):
            size_set = set()
            for x in range(row, row + size + 1):
                size_set.add(board[x])
            if "." in size_set:
                break
            else:
                row_count += 1
        
        if row_count % 2 == 0:
            if out_of_order % 2 != 0:
                return True
        else:
            if out_of_order % 2 == 0:
                return True
    return False

def taxicab(state):
    moves = 0
    goal = find_goal(state)
    size, state = state.split()
    size = int(size)
    for x in range(len(state)):
        if not state[x] == ".":
            x_point = goal.find(state[x]) // size
            y_point = goal.find(state[x]) % size
            x_distance = abs(x_point - x // size)
            y_distance = abs(y_point - x % size)
            moves += x_distance + y_distance
    return moves

def a_star(puzzle):
    closed = set()
    start_node = (puzzle, 0, taxicab(puzzle))
    fringe = [start_node]
    heapify(fringe)

    while fringe:
        v = heappop(fringe)
        if v[0][2::] == find_goal(v[0]):
            return v
        if v[0] not in closed:
            closed.add(v[0])
            for c in get_children(v[0]):
                if c not in closed:
                    temp = (c, v[1] + 1, v[1] + 1 + taxicab(c))
                    heappush(fringe, temp)
    return None



count = 0

for puzzle in line_list:
    print(puzzle, is_solvable(puzzle))

'''
for puzzle in line_list:
    start = perf_counter()
    can_solve = is_solvable(puzzle)
    end = perf_counter()
    if can_solve == False:
        print("Line", count, ":", puzzle, ", no solution determined in ", end - start, "seconds")
    else:
        a_start = perf_counter()
        solved = a_star(puzzle)
        a_end = perf_counter()
        print("Line", count, ":", puzzle, ", A* - ", solved, "moves in ", a_end - a_start, "seconds")
    count += 1
'''
