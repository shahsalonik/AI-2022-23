from collections import deque
import queue
import sys
from time import perf_counter

data_structure_start = perf_counter()

with open("words_06_letters.txt") as f:
    dict_list = [line.strip() for line in f]

with open("puzzles_normal.txt") as f:
    puzzle_list = [line.strip() for line in f]

dict_set = set(dict_list)
word_dict = {}
#build the dictionary one letter at a time
#pass in a word each time
#convert word to list -> swap letters
#check if new word is in the dict_list (convert to set for O(1) check) -> add to dict

def create_dict(word):
    word_list = []
    letter = [*word]
    letter2 = [*word]
    
    for x in range(len(letter)):
        for y in range(97, 123):
            char = letter2[x]
            letter2[x] = chr(y)
            letter2_string = ''.join(letter2)
            if letter2_string in dict_set and letter2_string != word:
                word_list.append(letter2_string)
            letter2[x] = char
    
    word_dict[word] = word_list

for w in dict_list:
    create_dict(w)
    

data_structure_end = perf_counter()
print("Total time to create the data structure was:", data_structure_end - data_structure_start)
print("There are %s" % len(dict_list), "words in this dict.")

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

start = perf_counter()

for x in puzzle_list:
    initial, final = goal_test(x)
    ladder = word_ladders(initial, final, word_dict)
    if ladder == "No Solution!":
        print("Line: %s" % count)
        print(ladder)
    else:
        print("Line: %s" % count)
        print("Length is: %s" % len(ladder))
        for y in ladder:
            print(y)
        print("\n")
    count += 1

end = perf_counter()
print("Time to solve all of these puzzles was: ", end - start)

'''
Part 2: Brainteasers
1. Number of singletons: 1568
2. Number of words in the biggest clump:  1625
3. Number of clumps: 450
4. Max path length: 28
['vaguer', 'valuer', 'values', 'valves', 'calves', 'carves', 'carver', 'carder', 'harder', 'herder', 'header', 'heaver', 'beaver', 'braver', 'braves', 'braces', 'traces', 'tracts', 'traits', 'trains', 'brains', 'braids', 'brands', 'grands', 'grants', 'grafts', 'crafts', 'crafty']
'''
