import sys

filename = sys.argv[1]
tests = sys.argv[2]

language = ''
states = 0
final_states = []
dfa_dict = {}

with open(filename) as f:
    file_string = f.read()
    file_string_list = file_string.split("\n\n")
    inputs = file_string_list[0].split("\n")
    language = str(inputs[0])
    states = inputs[1]
    final_states = inputs[2].split()
    for z in range(len(final_states)):
        final_states[z] = int(final_states[z])

    for x in range(1, len(file_string_list)):
        temp_list = file_string_list[x].split("\n")
        state_dict = {}
        #the name of the dictionary is temp[0] so 
        #key is the letter
        #value is where it's pointing to
        for y in range(1, len(temp_list)):
            letter_list = temp_list[y].split()
            state_dict[letter_list[0]] = int(letter_list[1])
        dfa_dict[int(temp_list[0])] = state_dict

def print_table(nested_dict):
    language_list = [x for x in language]
    print("*\t\t", "\t\t".join(language_list))
    for key in nested_dict.keys():
        print_list = [str(key)]
        for y in language_list:
            if y in nested_dict[key].keys():
                print_list.append(str(nested_dict[key][y]))
            else:
                print_list.append("_")
        print("\t\t".join(print_list))

print_table(dfa_dict)
print("Final nodes:", final_states)

def dfa_check_helper(current, character):
    if character in dfa_dict[current]:
        new_state = dfa_dict[current][character]
    else:
        new_state = None
    return new_state

def dfa_check(input_string, state):
    current_state = state
    for char in input_string:
        current_state = dfa_check_helper(current_state, char)
        if current_state == None:
            return False
    if current_state in final_states:
        return True

with open(tests) as t:
    for line in t:
        line = line.strip("\n")
        print(dfa_check(line, 0), line)
