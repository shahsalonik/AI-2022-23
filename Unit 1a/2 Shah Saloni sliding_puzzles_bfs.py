from collections import deque
import queue
import sys
from time import perf_counter

#sys.argv[1]
filename = "AI-2022-23/Unit 1a/slide_puzzle_tests.txt"

with open(filename) as f:
    line_list = [line.strip() for line in f]

def find_goal(board):
    sorted_board = sorted(board)
    goal_state = sorted_board[1:]
    goal_state.append(".")
    return ''.join(goal_state)

def get_children(state):
    size = int(state[0])
    board = state[2:]
    blank_index = board.index(".")
    children = []
    if blank_index % size != 0: #blank swap right
        children.append(board[:blank_index - 1] + "." + board[blank_index - 1] + board[blank_index + 1:])
    if (blank_index + 1) % size != 0: #blank swap left
        children.append(board[:blank_index] + board[blank_index + 1] + "." + board[blank_index + 2:])
    if blank_index >= size: #blank swap up
        children.append(board[:blank_index - size] + "." + board[blank_index - size + 1:blank_index] + board[blank_index - size] + board[blank_index + 1:]) 
    if blank_index <= (size * (size - 1)): #blank swap down
        children.append(board[:blank_index] + board[blank_index + size] + board[blank_index + 1:blank_index + size] + "." + board[blank_index + size + 1:])
    return children

def BFS(start_node):
    fringe = deque()
    visited = set()
    fringe.append(start_node)
    visited.add(start_node)
    moves = 1
    while len(fringe) != 0:
        v = fringe.popleft()
        if find_goal(v):
            moves_list.append(moves)
            moves = 0
            return v
        else:
            for x in get_children(v):
                if x not in visited:
                    fringe.append(x)
                    visited.add(x)
                    moves += 1
    return None

count = 0
moves_list = []

for x in line_list:
    size = int(x[0])
    board = x[2:]
    start = perf_counter()
    solved_board = BFS(board)
    end = perf_counter()
    print("Line", count, ":", BFS(board),  ",",  moves_list[count], "moves", "found in", end - start)
    count += 1