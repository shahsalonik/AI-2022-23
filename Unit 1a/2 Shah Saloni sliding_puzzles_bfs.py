import queue
import sys
from time import perf_counter

#sys.argv[1]
filename = "slide_puzzle_tests.txt"

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
        children.append(board[:blank_index - 1] + "." + board[blank_index - 1] + board[blank_index + 1:])
    if (blank_index + 1) % size != 0: #blank swap left
        children.append(board[:blank_index] + board[blank_index + 1] + "." + board[blank_index + 2:])
    if blank_index >= size: #blank swap up
        children.append(board[:blank_index - size] + "." + board[blank_index - size + 1:blank_index] + board[blank_index - size] + board[blank_index + 1:]) 
    if blank_index < (size * (size - 1)): #blank swap down
        children.append(board[:blank_index] + board[blank_index + size] + board[blank_index + 1:blank_index + size] + "." + board[blank_index + size + 1:])
    return children

def BFS(start_node):
    fringe = deque()
    visited = set()
    fringe.append((0, start_node))
    visited.add(start_node)
    while fringe:
        v = fringe.popleft()
        print(v[0])
        print(v[1])
        if v[1] == find_goal(v[1]):
            return v
        for x in get_children(v[1]):
            if x not in visited:
                fringe.append((v[0] + 1, x))
                visited.add(x)
    return None

count = 0

for x in line_list:
    board = x
    start = perf_counter()
    solved_board = BFS(board)
    end = perf_counter()
    print("Line", count, ":", solved_board,  ",",  solved_board[0], "moves", "found in", end - start)
    count += 1
