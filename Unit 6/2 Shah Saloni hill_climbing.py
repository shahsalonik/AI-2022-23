import sys
from math import log

#cipher = sys.argv[1].upper()
encode = sys.argv[1]
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_dict = {}
decipher_dict = {}
n_grams_file = "ngrams.txt"
n_grams_dict = {}

'''
for x in range(len(cipher)):
    cipher_dict[ALPHABET[x]] = cipher[x].upper()
    decipher_dict[cipher[x]] = ALPHABET[x]
'''
with open(n_grams_file) as f:
    for line in f:
        char, freq = line.split()
        n_grams_dict[char] = int(freq)

def encode_func(to_cipher_string):
    to_cipher_string = to_cipher_string.upper()
    new_string = ""
    for char in to_cipher_string:
        if char == "?" or char == "," or char == "." or char == "!" or char == " " or char == "\n":
            new_string = new_string + char
        else:
            new_char = cipher_dict[char]
            new_string = new_string + new_char
    return new_string

def decode_func(to_decipher_string):
    to_decipher_string = to_decipher_string.upper()
    new_string = ""
    for char in to_decipher_string:
        if char == "?" or char == "," or char == "." or char == "!" or char == " " or char == "\n":
            new_string = new_string + char
        else:
            new_char = decipher_dict[char]
            new_string = new_string + new_char
    return new_string

def fitness(n_value, encoded):
    n_gram_sum = 0
    decoded = encoded
    #decode_func(encoded)
    n_gram_list = []
    for x in range(0, len(decoded)):
        if x + n_value < len(decoded) + 1:
            n_gram_list.append(decoded[x : x + n_value])

    for gram in n_gram_list:
        if gram in n_grams_dict.keys():
            n_gram_sum += log(n_grams_dict[gram], 2)

    return n_gram_sum



#print(encode_func(encode))
#print(decode_func(encode_func(encode)))
print(fitness(3, encode))
print(fitness(4, encode))
