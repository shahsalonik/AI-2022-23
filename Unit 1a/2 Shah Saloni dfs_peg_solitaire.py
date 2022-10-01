from collections import deque
import queue
import sys
from time import perf_counter

total_start = perf_counter()

puzzle = "011111111111111"
peg_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#row 0, 5 spaces
#row 1, 4 spaces
#row 2, 3 spaces
#row 3, 2 spaces
#row 5, 1 space
def print_board(puzzle):
    index = 0
    space = 0
    string = ""

    for x in puzzle:
        if index == 0:
            if space == 0:
                string += "     "
                space += 1
            string += x + " "
            index += 1
        elif index <= 2:
            if space == 1:
                string += "\n" + "    "
                space += 1
            string += x + " "
            index += 1
        elif index <= 5:
            if space == 2:
                string += "\n" + "   "
                space += 1
            string += x + " "
            index += 1
        elif index <= 9:
            if space == 3:
                string += "\n" + "  "
                space += 1
            string += x + " "
            index += 1
        else:
            if space == 4:
                string += "\n" + " "
                space += 1
            string += x + " "
    print(string)

count = 0

def find_goal(board):
    if board == "100000000000000":
        return True
    else:
        return False

def get_moves(state):
    moves_list = [(0, 1, 3), (0, 2, 5), (1, 3, 6), (1, 4, 8), (2, 4, 7), (2, 5, 9), (3, 1, 0), (3, 4, 5), (3, 6, 10), 
    (3, 7, 12), (4, 7, 11), (4, 8, 13), (5, 2, 0), (5, 9, 14), (5, 8, 12), (5, 4, 3), (6, 7, 8), (6, 3, 1), (7, 8, 9), 
    (7, 4, 2), (8, 4, 1), (8, 7, 6), (9, 5, 2), (9, 8, 7), (10, 11, 12),  (10, 6, 3), (11, 12, 13), (11, 7, 4), (12, 13, 14), 
    (12, 7, 3), (12, 8, 5), (12, 11, 10), (13, 8, 4), (13, 12, 11), (14, 9, 5), (14, 13, 12)]

    puzzle = [*state]
    children = []

    for x in moves_list:
        if puzzle[x[0]] == "1" and puzzle[x[1]] == "1" and puzzle[x[2]] == "0":
            copy = [*state]
            children.append(make_move(x, copy))
    return children
    
def make_move(move, state):
    state[move[0]] = "0"
    state[move[1]] = "0"
    state[move[2]] = "1"
    return ''.join(state)

def path(node, tracked_path):
    path_list = [node]

    while tracked_path[node] != "s":
        path_list.append(tracked_path[node])
        node = tracked_path[node]

    return path_list[::-1]

def DFS(start_node):
    fringe = deque()
    visited = set()
    path_track_dict = {start_node: "s"}
    fringe.append((0, start_node))
    visited.add(start_node)
    while fringe:
        v = fringe.pop()
        if find_goal(v[1]) == True:
            return path(v[1], path_track_dict)
        for x in get_moves(v[1]):
            if x not in visited:
                fringe.append((v[0] + 1, x))
                visited.add(x)
                path_track_dict[x] = v[1]
    return None

def DFS(start_node):
    fringe = deque()
    visited = set()
    path_track_dict = {start_node: "s"}
    fringe.append((0, start_node))
    visited.add(start_node)
    while fringe:
        v = fringe.popleft()
        if find_goal(v[1]) == True:
            return path(v[1], path_track_dict)
        for x in get_moves(v[1]):
            if x not in visited:
                fringe.append((v[0] + 1, x))
                visited.add(x)
                path_track_dict[x] = v[1]
    return None


print("DFS Board:")

dfs_solved_board = DFS(puzzle)

for x in dfs_solved_board:
    print_board(x + "\n")

print("\nBFS Board:")

bfs_solved_board = DFS(puzzle)

for y in bfs_solved_board:
    print_board(y + "\n")

total_end = perf_counter()
print("Total Time: %s" % (total_end - total_start))

'''
Part 2 - DFS Questions:
1. Our goal for sliding puzzles was to find the shortest possible solution. DFS doesn't do that for sliding puzzles because
it has to iterate through so many different states and the number of moves is unknown. On the other hand, for sliding puzzles, 
DFS worked fine because we have a list of hardcoded moves, so DFS only has to iterate through those and its children.
2. Yes, there could be a time where DFS was preferable to BFS, especially in situations where the goal is to find the longest
possible path. DFS has to go through the longest path every time, so it would be an easier method to use.
'''
