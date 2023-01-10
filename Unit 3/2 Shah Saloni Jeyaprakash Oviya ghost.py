import sys

filename = sys.argv[1]
min_length = int(sys.argv[2])
in_progress = ""
if len(sys.argv) == 4:
    in_progress = sys.argv[3]

line_list = []

with open(filename) as f:
    for line in f:
        line = line.strip().upper()
        if line.isalpha():
            if line[0:len(in_progress)] == in_progress and len(line) >= min_length:
                line_list.append(line)

def possible_char(word, possible_word_dictionary):
    letter_dict = {}
    word_ind = len(word)
    for w in possible_word_dictionary:
        letter_dict[w[word_ind]] = letter_dict.get(w[word_ind], []) + [w]
    return letter_dict

def min_step(word, possible_words, alpha, beta):
    if word in possible_words:
        return -1
    children = []
    possible_moves = possible_char(word, possible_words)
    for child in possible_moves.keys():
        new_word = word + child
        result = max_step(new_word, possible_moves[child], alpha, beta)
        if alpha >= result:
            return result
        if beta > result:
            beta = result
        children.append(result)
    return max(beta, min(children))
    
def max_step(word, possible_words, alpha, beta):
    if word in possible_words:
        return 1
    children = []
    possible_moves = possible_char(word, possible_words)
    for child in possible_moves.keys():
        new_word = word + child
        result = min_step(new_word, possible_moves[child], alpha, beta)
        children.append(result)
        #ALPHA/BETA PRUNING HERE
        if result >= beta:
            return result
        if result > alpha:
            alpha = result
        children.append(result)
    return min(alpha, max(children))

def find_next_move(word, possible_move_list):
    win_letters = []
    moves = possible_char(word, possible_move_list)
    for char in moves.keys():
        new_word = word + char
        result = min_step(new_word, moves[char], -1000000, 1000000)
        if result == 1:
            win_letters.append(char)
    if len(win_letters) > 0:
        print("Next player can guarantee victory by playing any of these letters: " + str(win_letters))
        
    else:
        print("Next player will lose!")

find_next_move(in_progress, line_list)
