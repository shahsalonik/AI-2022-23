from collections import deque
import queue
import sys
from time import perf_counter

data_structure_start = perf_counter()

dictionary = sys.argv[1]
puzzles = sys.argv[2]

with open(dictionary) as f:
    dict_list = [line.strip() for line in f]

with open(puzzles) as f:
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

def end_path(last_node, tracked_path):
    path_list = [last_node]

    while tracked_path[last_node] != "e":
        path_list.append(tracked_path[last_node])
        last_node = tracked_path[last_node]

    return path_list

def word_ladders(first, goal, dict):
    path_track_dict = {first: "s"}
    end_track_dict = {goal: "e"}
    fringe = deque()
    visited = set()
    solved_fringe = deque()
    solved_visited = set()

    fringe.append(first)
    visited.add(first)

    solved_fringe.append(goal)
    solved_visited.add(goal)

    while fringe and solved_fringe:
        v = fringe.popleft()
        s_v = solved_fringe.popleft()

        if v == goal or v in solved_fringe:
            return path(v, path_track_dict) + end_path(v, end_track_dict)
        
        if s_v == first or s_v in fringe:
            return end_path(s_v, end_track_dict) + path(s_v, path_track_dict) 
        
        children = dict[v]
        end_children = dict[s_v]

        for x in children:
            if x not in path_track_dict.keys():
                fringe.append(x)
                visited.add(x)
                path_track_dict[x] = v
        
        for y in end_children:
            if y not in end_track_dict.keys():
                solved_fringe.append(y)
                solved_visited.add(x)
                end_track_dict[y] = s_v

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
