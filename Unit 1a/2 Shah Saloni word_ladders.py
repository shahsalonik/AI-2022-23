from collections import deque
import queue
import sys
from time import perf_counter

start = perf_counter()

with open("words_06_letters.txt") as f:
    dict_list = [line.strip() for line in f]

with open("puzzles_normal.txt") as f:
    puzzle_list = [line.strip() for line in f]

#initializing the dict with each possible letter variation of each of its keys
#need a dict where the values are lists and the keys are the root words
#check if word differs by only 1 letter???
#iterate through each index -> check if char is the same -> if yes do nothing
#if no add smth? -> add to a running count of different letters and then just return that
#should be called in the create word list func

def create_dict(word_list):
    word_dict = {}

    for w in dict_list:
        word_dict[w] = create_word_list(w, word_list)

    return word_dict

def create_word_list(word, dict):
    word_list = []

    for real_word in dict:
        if check_word_diff(word, real_word) == 1:
            word_list.append(real_word)
    
    return word_list

def check_word_diff(word1, word2):
    diff_letters = 0

    for x in range(len(word1)):
        if word1[x] != word2[x]:
            diff_letters += 1
    
    return diff_letters

#should take in each line and return both words (split)
def goal_test(one_line):
    input, goal = one_line.split()
    return input, goal

def path(node, tracked_path):
    path_list = [node]

    while tracked_path[node] != "s":
        path_list.append(tracked_path[node])
        node = tracked_path[node]

    return path_list[::-1]

def word_ladders(first, goal, dict):
    path_track_dict = {first: "s"}
    fringe = deque()
    visited = set()

    fringe.append(first)
    visited.add(first)

    while fringe:
        v = fringe.popleft()
        if v == goal:
            return path(v, path_track_dict)
        
        children = dict[v]

        for x in children:
            if x not in path_track_dict.keys():
                fringe.append(x)
                visited.add(x)
                path_track_dict[x] = v

    return "No Solution!"

count = 0
dict = create_dict(dict_list)

for x in puzzle_list:
    initial, final = goal_test(x)
    ladder = word_ladders(initial, final, dict)
    print(ladder)
    count += 1

end = perf_counter()
print("Total time: ", end - start)