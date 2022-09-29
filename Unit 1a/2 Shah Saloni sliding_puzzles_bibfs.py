from collections import deque
import queue
import sys
from time import perf_counter

total_start = perf_counter()

filename = sys.argv[1]

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

def BFS(start_node):
    fringe = deque()
    visited = set()
    solved_fringe = deque()
    solved_visited = set()
    
    fringe.append((0, start_node))
    fringe_dict = {start_node: 0}
    visited.add(start_node)

    size, end_node = start_node.split()
    end_node = size + " " + end_node
    end_node = find_goal(end_node)
    end_node = size + " " + end_node

    solved_fringe.append((0, end_node))
    solved_fringe_dict = {end_node: 0}
    solved_visited.add(end_node)

    while fringe and solved_fringe:
        v = fringe.popleft()
        s_v = solved_fringe.popleft()

        if v[1][2::] == find_goal(v[1]) or v[1] in solved_visited:
            moves = solved_fringe_dict[v[1]]
            return (v[0] + moves, v[1])

        if s_v[1][2::] == start_node[2::] or s_v[1] in visited:
            moves = fringe_dict[s_v[1]]
            return (s_v[0] + moves, s_v[1])
        
        for x in get_children(v[1]):
            if x not in visited:
                fringe.append((v[0] + 1, x))
                visited.add(x)
                fringe_dict[x] = (v[0] + 1)

        for y in get_children(s_v[1]):
            if y not in solved_visited:
                solved_fringe.append((s_v[0] + 1, y))
                solved_visited.add(y)
                solved_fringe_dict[y] = (s_v[0] + 1)
    return None

count = 0

for x in line_list:
    board = x
    start = perf_counter()
    solved_board = BFS(board)
    end = perf_counter()
    print("Line", count, ": %s" % x + ",",  solved_board[0], "moves", "found in", end - start)
    count += 1

total_end = perf_counter()
print("Total Time: %s" % (total_end - total_start))
