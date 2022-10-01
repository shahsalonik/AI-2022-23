from collections import deque
import queue
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
        children.append(str(size) + " " + board[:blank_index - 1] + "." + board[blank_index - 1] + board[blank_index + 1:])
    if (blank_index + 1) % size != 0: #blank swap left
        children.append(str(size) + " " + board[:blank_index] + board[blank_index + 1] + "." + board[blank_index + 2:])
    if blank_index >= size: #blank swap up
        children.append(str(size) + " " + board[:blank_index - size] + "." + board[blank_index - size + 1:blank_index] + board[blank_index - size] + board[blank_index + 1:]) 
    if blank_index < (size * (size - 1)): #blank swap down
        children.append(str(size) + " " + board[:blank_index] + board[blank_index + size] + board[blank_index + 1:blank_index + size] + "." + board[blank_index + size + 1:])
    return children

def k_DFS(start_state, k):
    fringe = []
    init_node = []
    init_node.append(start_state)
    init_node.append(0)
    init_node.append(set())
    init_node[2] = start_state
    start_node = tuple(init_node)
    fringe.append((start_node[0], start_node[1], start_node[2]))
    
    while fringe:
        v = fringe.pop()

        if v[0] == find_goal(v[0]):
            return v
        if v.depth < k:
            for c in get_children(v[0]):
                temp = []
                temp[0] = c
                temp[1] = v[1] + 1
                temp[2] = v[2].copy()
                temp[2].add(c)
                temp = tuple(temp)
                fringe.append(temp)
    return None

def ID_DFS(start_state):
    max_depth = 0
    result = None
    while result is None:
        result = k_DFS(start_state, max_depth)
        max_depth += 1
    return result

def BFS(start_node):
    fringe = deque()
    visited = set()
    fringe.append((0, start_node))
    visited.add(start_node)
    while fringe:
        v = fringe.popleft()
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
    bfs_start = perf_counter()
    bfs_solved_board = BFS(board)
    bfs_end = perf_counter()
    print("Line", count, ": %s" % bfs_solved_board[1] + ", BFS - ",  bfs_solved_board[0], "moves found in", bfs_end - bfs_start)

    dfs_start = perf_counter()
    dfs_solved_board = ID_DFS(board)
    dfs_end = perf_counter()
    print("Line", count, ": %s" % dfs_solved_board[1] + ", ID-DFS - ",  dfs_solved_board[0], "moves found in", dfs_end - dfs_start)
    count += 1
