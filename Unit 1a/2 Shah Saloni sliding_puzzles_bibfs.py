from collections import deque
import queue
import sys
from time import perf_counter

total_start = perf_counter()

filename = sys.argv[1]

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

'''
Part 2: 
1. Bidirectional BFS runs at a fraction of the time as BFS (0.6s compared to 2.5s)
2. The last puzzle I can solve in less than a minute is line 41, which almost double
the number of puzzles I could solve with BFS, when it could only solve until line 22.
3. BiBFS word ladders is only very slightly faster than normal word ladders
4. I stored the word ladder with 2 different dicts, one that tracked the path from the beginning and one that tracked it from
the end. Then, when the solution was found or either one of the words was in the other fringe, I returned a combination of both 
paths using two different methods: ```end_path``` and ```path```. ```path``` returned a reversed list of the dict's values, 
and ```end_path``` returned a non-reversed list of the dict's values. This is because when I was tracking the paths, the 
```end_path``` method already iterated through the dict and added the values to the dict in a reversed manner. 
5. BiBFS is more useful when you have the final goal state and the children of the start node (and any following nodes) 
grow at an exponential pace and are unknown. BiBFS was most useful for decreasing the time to solve sliding puzzles, because
we didn't know the children, but in word ladders, the children were all already generated and stored in a dict.
'''
