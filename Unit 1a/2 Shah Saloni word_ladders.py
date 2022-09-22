from collections import deque
import queue
import sys
from time import perf_counter

with open("words_06_letters.txt") as f:
    dict_list = [line.strip() for line in f]

with open("puzzles_normal.txt") as f:
    puzzle_list = [line.strip() for line in f]

#should take in each line and return both words (split)
def goal_test(one_line):
    input, goal = one_line.split()
    return input, goal

def get_children(node):
    print("no children yet")

def wordLadders(first, goal):
    fringe = deque()
    visited = set()
    fringe.append((0, first))
    visited.add(first)
    while fringe:
        v = fringe.popleft()
        if v[1] == goal:
            return v
        for x in get_children(v[1]):
            if x not in visited:
                fringe.append((v[0] + 1, x))
                visited.add(x)
    return "Cannot be solved!"

count = 0

for x in puzzle_list:
    initial, final = goal_test(x)
    ladder = wordLadders(initial, final)
    print("Line", count, ":\nLength is:", len(ladder), "\n%s" %initial, "\n%s" %ladder, "\n%s" %final, "\n")
    count += 1