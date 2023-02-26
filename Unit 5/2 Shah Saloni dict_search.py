import sys, re

#1 (DONE)
#2 (DONE)
#3
#4
#5 (DONE)
#6 (DONE)
#7 (DONE)
#8 (DONE)
#9 (DONE)
#10

filename = sys.argv[1]
word_list = []

with open(filename) as f:
    for line in f:
        word_list.append(line.lower().strip("\n"))

def re_func_1_5(word_dict, regexp):
    exp = regexp
    if len(exp.split("/")) > 2:
        exp, ad = exp.split("/")[1], exp.split("/")[2]
    else:
        exp, ad = exp.split("/")[1], ""
    if len(ad) == 0:
        reg = re.compile(r"{}".format(exp))
    elif len(ad) > 0:
        if ad == "i":
            reg = re.compile(r"{}".format(exp), re.I)
        elif ad == "s":
            reg = re.compile(r"{}".format(exp), re.S)
        elif ad == "m":
            reg = re.compile(r"{}".format(exp), re.M)
        elif ad == "is" or ad == "si":
            reg = re.compile(r"{}".format(exp), re.I | re.S)
        elif ad == "im" or ad == "mi":
            reg = re.compile(r"{}".format(exp), re.I | re.M)
        elif ad == "sm" or ad == "ms":
            reg = re.compile(r"{}".format(exp), re.S | re.M)
        elif ad == "ims" or ad == "ism" or ad == "mis" or ad == "msi" or ad == "sim" or ad == "smi":
            reg = re.compile(r"{}".format(exp), re.I | re.M | re.S)

    exp_list = []

    for result in word_dict:
        if reg.fullmatch(result):
            exp_list.append(result)

    return exp_list

def print_func(question, regexp, result):
    print("#" + str(question) + ": " + regexp)
    print(str(len(result)) + " total matches")
    if len(result) <= 5:
        for x in result:
            print(x)
    else:
        for x in range(0,5):
            print(result[x])

#QUESTION 1 (DONE):
my_regex = "/^(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w*$/"

final_list = re_func_1_5(word_list, my_regex)
min_length = len(final_list[0])
min_length_list = []
for x in final_list:
    if len(x) < min_length:
        min_length = len(x)
for y in final_list:
    if len(y) == min_length:
        min_length_list.append(y)
print_func(1, my_regex, min_length_list)

#QUESTION 2 (DONE):
my_regex = "/^([^aeiou]*[aeiou]){5}[^aeiou]*/"

final_list = re_func_1_5(word_list, my_regex)
max_length = len(final_list[0])
max_length_list = []
for x in final_list:
    if len(x) > max_length:
        max_length = len(x)
for y in final_list:
    if len(y) == max_length:
        max_length_list.append(y)
print_func(2, my_regex, max_length_list)

#QUESTION 3:
my_regex = "/^(\w)(?!\w*(\w*\1\w))(?=\w*\1)$/"

final_list = re_func_1_5(word_list, my_regex)
print_func(3, my_regex, final_list)

#QUESTION 4:
my_regex = "/^(\w)(\w)(\w)\w*$(?<=\3\2\1)/"

final_list = re_func_1_5(word_list, my_regex)
print_func(4, my_regex, final_list)

#QUESTION 5 (DONE):
my_regex = "/^[^bt]*(bt|tb)[^bt]*$/"

final_list = re_func_1_5(word_list, my_regex)
print_func(5, my_regex, final_list)

#HELPER FOR QUESTION 6
def longest_char_block(word):
    current_count = 1
    longest_count = 1
    prev_char = word[0]

    for x in range(1, len(word)):
        new_char = word[x]
        
        if new_char == prev_char:
            current_count += 1
        else:
            if current_count > longest_count:
                longest_count = current_count
            current_count = 1
        prev_char = new_char
    
    if current_count > longest_count:
        longest_count = current_count
    
    return longest_count

#QUESTION 6 (DONE):
my_regex = r"^\w*(\w)\1\w*$"
reg = re.compile(my_regex)

exp_list = []
final_list = []
act_longest = 0

for x in word_list:
    for result in reg.finditer(x):
        exp_list.append(x)
        longest_block = longest_char_block(x)
        if longest_block > act_longest:
            act_longest = longest_block
            

my_regex = r"^\w*(\w)\1{" + str(act_longest - 1) + r"}\w*$"
reg = re.compile(my_regex)
for y in exp_list:
    for result in reg.finditer(y):
        final_list.append(y)

print_func(6, "/" + my_regex + "/", final_list)

#HELPER FOR QUESTION 7
def max_chars(word):
    char_count = dict()
    max_count = 0
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for key in char_count.keys():
        if char_count[key] > max_count:
            max_count = char_count[key]

    return max_count

#QUESTION 7:
my_regex = r"^\w*(\w)\w*\1\w*$"
reg = re.compile(my_regex)

exp_list = []
final_list = []
max_char_length = 0

for x in word_list:
    for result in reg.finditer(x):
        exp_list.append(x)
        max_char = max_chars(x)
        if max_char > max_char_length:
            max_char_length = max_char

my_regex = r"^\w*(\w)(\w*\1){" + str(max_char_length - 1) + r"}\w*$"
reg = re.compile(my_regex)

for y in exp_list:
    for result in reg.finditer(y):
        final_list.append(y)

print_func(7, my_regex, final_list)

#HELPER FOR QUESTION 8
def max_adj_chars(word):
    adj_count = dict()
    max_count = 0

    for char in range(0, len(word) - 1):
        join = word[char] + word[char + 1]
        if join in adj_count:
            adj_count[join] += 1
        else:
            adj_count[join] = 1
    
    for key in adj_count.keys():
        if adj_count[key] > max_count:
            max_count = adj_count[key]

    return max_count

#QUESTION 8:
my_regex = r"^\w*(\w\w)\w*\1\w*$"
reg = re.compile(my_regex)

exp_list = []
final_list = []
max_adj_letters = 0

for x in word_list:
    for result in reg.finditer(x):
        exp_list.append(x)
        max_adj = max_adj_chars(x)
        if max_adj > max_adj_letters:
            max_adj_letters = max_adj

my_regex = r"^\w*(\w\w)(\w*\1){" + str(max_adj_letters - 1) + r"}\w*$"
reg = re.compile(my_regex)

for y in exp_list:
    for result in reg.finditer(y):
        final_list.append(y)

print_func(8, my_regex, final_list)

#HELPER FOR QUESTION 9:
def max_consonant_count(word):
    consonant_count = 0
    
    for x in word:
        if x != "a":
            if x != "e":
                if x != "i":
                    if x != "o":
                        if x != "u":
                            consonant_count += 1
    
    return consonant_count

#QUESTION 9:
my_regex = r"^\w*[bcdfghjklmnpqrstvwxyz]\w*$"
reg = re.compile(my_regex)

exp_list = []
final_list = []
max_consonants = 0

for x in word_list:
    for result in reg.finditer(x):
        exp_list.append(x)
        max_cons = max_consonant_count(x)
        if max_cons > max_consonants:
            max_consonants = max_cons

my_regex = r"^(\w*[bcdfghjklmnpqrstvwxyz]){" + str(max_consonants) + r"}\w*$"
reg = re.compile(my_regex)

for y in exp_list:
    for result in reg.finditer(y):
        final_list.append(y)

print_func(9, my_regex, final_list)

#QUESTION 10:
my_regex = "/^(?!\w*(\w)(\w*\1){2})\w*$/"

final_list = re_func_1_5(word_list, my_regex)
max_length = len(final_list[0])
max_length_list = []
for x in final_list:
    if len(x) > max_length:
        max_length = len(x)
for y in final_list:
    if len(y) == max_length:
        max_length_list.append(y)
print_func(10, my_regex, max_length_list)
