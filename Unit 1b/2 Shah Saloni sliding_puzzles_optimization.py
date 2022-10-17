from heapq import heapify, heappush, heappop
import sys
from time import perf_counter

#sys.argv[1]
filename = "15_puzzles.txt"

with open(filename) as f:
    line_list = [line.strip() for line in f]

goal_state = "ABCDEFGHIJKLMNO."

def make_dict(board):
    size = int(4)
    board = find_goal(board)
    coord_dict = dict()

    for x in board:
        row = board.find(x) // size
        col = board.find(x) % size
        coord_dict[x] = (row, col)

    return coord_dict

def find_goal(board):
    sorted_board = sorted(board)
    goal_state = sorted_board[1:]
    goal_state.append(".")
    return ''.join(goal_state)

def get_children(state, goal_dict):
    board = state
    size = int(4)
    blank_index = int(board.index("."))
    children = []
    if blank_index % size != 0: #blank swap right
        x_coord, y_coord = goal_dict[board[blank_index - 1]]
        swap_loc = blank_index % size
        if abs(swap_loc - 1 - y_coord) > abs(swap_loc - y_coord):
            children.append((-1, board[:blank_index - 1] + "." + board[blank_index - 1] + board[blank_index + 1:]))
        else:
            children.append((1, board[:blank_index - 1] + "." + board[blank_index - 1] + board[blank_index + 1:]))

    if (blank_index + 1) % size != 0: #blank swap left
        x_coord, y_coord = goal_dict[board[blank_index + 1]]
        swap_loc = blank_index % size

        if abs(swap_loc + 1 - y_coord) > abs(swap_loc - y_coord):
            children.append((-1, board[:blank_index] + board[blank_index + 1] + "." + board[blank_index + 2:]))
        else:
            children.append((1, board[:blank_index] + board[blank_index + 1] + "." + board[blank_index + 2:]))

    if blank_index >= size: #blank swap up
        x_coord, y_coord = goal_dict[board[blank_index - size]]
        swap_loc = blank_index // size

        if abs(swap_loc - 1 - x_coord) > abs(swap_loc - x_coord):
            children.append((-1, board[:blank_index - size] + "." + board[blank_index - size + 1:blank_index] + board[blank_index - size] + board[blank_index + 1:]))
        else:
            children.append((1, board[:blank_index - size] + "." + board[blank_index - size + 1:blank_index] + board[blank_index - size] + board[blank_index + 1:]))

    if blank_index < (size * (size - 1)): #blank swap down
        x_coord, y_coord = goal_dict[board[blank_index + size]]
        swap_loc = blank_index // size

        if abs(swap_loc + 1 - x_coord) > abs(swap_loc - x_coord):
            children.append((-1, board[:blank_index] + board[blank_index + size] + board[blank_index + 1:blank_index + size] + "." + board[blank_index + size + 1:]))
        else:
            children.append((1, board[:blank_index] + board[blank_index + size] + board[blank_index + 1:blank_index + size] + "." + board[blank_index + size + 1:]))

    return children

def taxicab(state, goal_dict):
    moves = 0
    size = int(4)
    for x in range(len(state)):
        if not state[x] == ".":
            print(goal_dict)
            input()
            x_point, y_point = goal_dict[state[x]]
            x_distance = abs(x_point - x // size)
            y_distance = abs(y_point - x % size)
            moves += x_distance + y_distance
    return moves

def a_star(puzzle, goal_dict):
    closed = set()
    start_node = ((taxicab(puzzle,goal_dict), 0, puzzle))
    fringe = []
    heapify(fringe)
    heappush(fringe, start_node)

    while len(fringe) > 0:
        v = heappop(fringe)

        if v[2] == find_goal(v[2]):
            return v
        if v[2] not in closed:
            closed.add(v[2])
            for c in get_children(v[2], goal_dict):
                taxi_add, board = c
                if board not in closed:
                    temp = ((v[1] + 1 + taxi_add, v[1] + 1, board))
                    heappush(fringe, temp)
    return None


count = 0
coord_dict = make_dict(goal_state)

for puzzle in line_list:
    a_start = perf_counter()
    solved_board = a_star(puzzle, coord_dict)
    a_end = perf_counter()
    print("Line", count, ":", puzzle, ", A* -", solved_board[0], "moves in", a_end - a_start, "seconds")
    count += 1
