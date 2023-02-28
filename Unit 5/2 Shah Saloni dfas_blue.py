import sys

filename = sys.argv[1]
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

print(dfa_dict)
