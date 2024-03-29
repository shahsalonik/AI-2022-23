from heapq import heapify, heappush, heappop
import sys
from time import perf_counter

#sys.argv[1]
filename = "15_puzzles.txt"

with open(filename) as f:
    line_list = [line.strip() for line in f]

def find_goal(board):
    sorted_board = sorted(board)
    goal_state = sorted_board[1:]
    goal_state.append(".")
    return ''.join(goal_state)

def get_children(state):
    board = state
    size = int(4)
    blank_index = int(board.index("."))
    children = []
    if blank_index % size != 0: #blank swap right
        children.append(board[:blank_index - 1] + "." + board[blank_index - 1] + board[blank_index + 1:])
    if (blank_index + 1) % size != 0: #blank swap left
        children.append(board[:blank_index] + board[blank_index + 1] + "." + board[blank_index + 2:])
    if blank_index >= size: #blank swap up
        children.append(board[:blank_index - size] + "." + board[blank_index - size + 1:blank_index] + board[blank_index - size] + board[blank_index + 1:]) 
    if blank_index < (size * (size - 1)): #blank swap down
        children.append(board[:blank_index] + board[blank_index + size] + board[blank_index + 1:blank_index + size] + "." + board[blank_index + size + 1:])
    return children


#parity check
def is_solvable(state):
    board = state
    blank_index = int(board.index("."))
    other_board = board[:blank_index] + board[blank_index + 1:]
    size = int(4)

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
            for x in range(row, row + size):
                size_set.add(board[x])
            if "." in size_set or row_count + 1 == size:
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
    size = int(4)
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
    start_node = ((taxicab(puzzle), 0, puzzle))
    fringe = []
    heapify(fringe)
    heappush(fringe, start_node)

    while len(fringe) > 0:
        v = heappop(fringe)

        if v[2] == find_goal(v[2]):
            return v
        if v[2] not in closed:
            closed.add(v[2])
            for c in get_children(v[2]):
                if c not in closed:
                    temp = ((v[1] + 1 + taxicab(c), v[1] + 1, c))
                    heappush(fringe, temp)
    return None


count = 0

for puzzle in line_list:
    start = perf_counter()
    can_solve = is_solvable(puzzle)
    end = perf_counter()

    if can_solve:
        a_start = perf_counter()
        solved_board = a_star(puzzle)
        a_end = perf_counter()
        print("Line", count, ":", puzzle, ", A* -", solved_board[1], "moves in", a_end - a_start, "seconds")
    else:
        print("Line", count, ":", puzzle, ", no solution determined in", end - start, "seconds")
    
    count += 1
