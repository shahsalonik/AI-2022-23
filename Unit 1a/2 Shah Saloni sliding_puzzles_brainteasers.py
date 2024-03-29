from collections import deque
import queue
import sys
from time import perf_counter

total_start = perf_counter()

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
    size, board = start_node.split()
    print(size)

    found = find_goal(start_node)
    print(found)
    found = size + " " + found
    print(found)
    fringe.append((0, found))
    visited.add(found)
    while fringe:
        v = fringe.popleft()
        if v[0] == 10:
            ten_list.append("s")
            return v
        for x in get_children(v[1]):
            if x not in visited:
                fringe.append((v[0] + 1, x))
                visited.add(x)
    return None

count = 0
ten_list = []

for x in line_list:
    board = x
    start = perf_counter()
    solved_board = BFS(board)
    end = perf_counter()
    #print("Line", count, ": %s" % solved_board[1][2::] + ",",  solved_board[0], "moves", "found in", end - start)
    count += 1

print(len(ten_list))


total_end = perf_counter()
print("Total time: ", total_end - total_start)

#Part 2: BFS Brainteasers
'''
1. 2x2 - 12, 3x3 - 181440
2. 12345687. When you plug it into the BFS method, it returns a NoneType, which means that it went through the length of the queue and visited, and couldn't find a solution to it.
3. 286
4. 2 hardest 3x3 puzzles - each have 31 moves to solve them
HFGBEDC.A path - ['HFGBEDC.A', 'HFGB.DCEA', 'H.GBFDCEA', '.HGBFDCEA', 'BHG.FDCEA', 'BHGCFD.EA', 'BHGCFDE.A', 'BHGCFDEA.', 'BHGCF.EAD', 'BH.CFGEAD', 'B.HCFGEAD', 'BFHC.GEAD', 'BFH.CGEAD', 'BFHECG.AD', 'BFHECGA.D', 'BFHECGAD.', 'BFHEC.ADG', 'BF.ECHADG', 'B.FECHADG', 'BCFE.HADG', 'BCF.EHADG', 'BCFAEH.DG', 'BCFAEHD.G', 'BCFAEHDG.', 'BCFAE.DGH', 'BC.AEFDGH', 'B.CAEFDGH', '.BCAEFDGH', 'ABC.EFDGH', 'ABCDEF.GH', 'ABCDEFG.H', 'ABCDEFGH.']
FDGHE.CBA path - ['FDGHE.CBA', 'FD.HEGCBA', 'F.DHEGCBA', 'FEDH.GCBA', 'FED.HGCBA', 'FEDCHG.BA', 'FEDCHGB.A', 'FEDC.GBHA', 'FEDCG.BHA', 'FEDCGABH.', 'FEDCGAB.H', 'FEDC.ABGH', '.FDCEABGH', 'CFD.EABGH', 'CFDBEA.GH', 'CFDBEAG.H', 'CFDB.AGEH', 'CFDBA.GEH', 'CF.BADGEH', 'C.FBADGEH', '.CFBADGEH', 'BCF.ADGEH', 'BCFA.DGEH', 'BCFAD.GEH', 'BC.ADFGEH', 'BC.ADFGEH', 'B.CADFGEH', '.BCADFGEH', 'ABC.DFGEH', 'ABCD.FGEH', 'ABCDEFG.H', 'ABCDEFGH.']
5. My program gets bogged down at around line 22.
'''
