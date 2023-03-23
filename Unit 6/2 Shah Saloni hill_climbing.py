import random
import sys
from math import log

encode = sys.argv[1]
ALPHABET = "ETAOINSHRDLCUMWFGYPBVKXJQZ"
cipher_dict = {}
decipher_dict = {}
cipher_fitness_dict = {}
n_grams_file = "ngrams.txt"
n_grams_dict = {}

POPULATION_SIZE = 500
NUM_CLONES = 1
TOURNAMENT_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = 0.75
CROSSOVER_LOCATIONS = 5
MUTATION_RATE = 0.8
N = 3
ITERATIONS = 500

def decipher_dict_func(cipher):
    for x in range(len(cipher)):
        decipher_dict[cipher[x]] = ALPHABET[x]
    
    return decipher_dict

with open(n_grams_file) as f:
    for line in f:
        char, freq = line.split()
        n_grams_dict[char] = int(freq)

def encode_func(to_cipher_string):
    to_cipher_string = to_cipher_string.upper()
    new_string = ""
    for char in to_cipher_string:
        if char not in cipher_dict:
            new_string = new_string + char
        else:
            new_char = cipher_dict[char]
            new_string = new_string + new_char
    return new_string

def decode_func(to_decipher_string, decipher_dict_passed):
    to_decipher_string = to_decipher_string.upper()
    new_string = ""
    for char in to_decipher_string:
        if char in decipher_dict_passed:
            new_char = decipher_dict_passed[char]
            new_string += new_char
        else:
            new_string += char
    return new_string

def fitness(n_value, message_string, cipher_string):
    if cipher_string in cipher_fitness_dict.keys():
        return cipher_fitness_dict[cipher_string]

    n_gram_sum = 0

    decoded = decode_func(message_string, decipher_dict_func(cipher_string))

    word_list = decoded.split(" ")

    for word in word_list:
        n_gram_list = [word[char : char2] for char in range(len(word)) for char2 in range(char + 1, len(word) + 1) if len(word[char : char2]) == n_value]

        for n_gram_word in n_gram_list:
            if n_gram_word in n_grams_dict:
                to_add = n_grams_dict[n_gram_word]
                if to_add > 0:
                    n_gram_sum += log(to_add, 2)

    cipher_fitness_dict[cipher_string] = n_gram_sum
    return n_gram_sum

def generate_population():
    population_set = set()

    while len(population_set) < POPULATION_SIZE:
        alphabet_list = list(ALPHABET)
        random.shuffle(alphabet_list)
        cipher_string = ''.join(alphabet_list)
        population_set.add(cipher_string)
    
    return population_set

def tournament_genetic_algorithm(population, message_string, iteration_number):
    if iteration_number >= ITERATIONS:
        return
    
    new_population = set()
    population_list = []

    for cipher in population:
        score = fitness(N, message_string, cipher)
        population_list.append((score, cipher))
    
    population_list = sorted(population_list, reverse = True)

    for k in range(NUM_CLONES):
        new_population.add(population_list[k][1])
    
    tournament1, tournament2 = tournament_selection(population_list, message_string)

    while len(new_population) < POPULATION_SIZE:
        for c in tournament1:
            if random.random() < TOURNAMENT_WIN_PROBABILITY:
                parent1 = c
                break
        
        for c2 in tournament2:
            if random.random() < TOURNAMENT_WIN_PROBABILITY:
                parent2 = c2
                break
        
        child = breeding(parent1, parent2)

        new_population.add(mutate(child)) 

    print("Iteration " + str(iteration_number + 1) + ": " + decode_func(message_string, decipher_dict_func(population_list[0][1])) + "\n")
    return tournament_genetic_algorithm(new_population, message_string, iteration_number + 1)

def tournament_selection(population_list, message):
    temp_set = set(random.sample(population_list, 2 * TOURNAMENT_SIZE))
    competitors = set()
    tournament1, tournament2 = [], []

    for x in temp_set:
        competitors.add(x[1])

    for ciphers_1 in range(TOURNAMENT_SIZE):
        cipher_to_add = competitors.pop()
        score = fitness(N, message, cipher_to_add)
        tournament1.append((score, cipher_to_add))
    tournament1 = sorted(tournament1, reverse = True)

    for ciphers_2 in range(TOURNAMENT_SIZE):
        cipher_to_add2 = competitors.pop()
        score2 = fitness(N, message, cipher_to_add2)
        tournament2.append((score2, cipher_to_add2))
    tournament2 = sorted(tournament2, reverse = True)

    return tournament1, tournament2

def parents(tournament_list):
    for x in tournament_list:
        if random.random() < TOURNAMENT_WIN_PROBABILITY:
            return x

def mutate(child_cipher):
    if random.random() < MUTATION_RATE:
        swap_index1, swap_index2 = random.sample(range(26), 2)
        
        if swap_index1 > swap_index2:
            to_swap = swap_index1
            swap_index1 = swap_index2
            swap_index2 = to_swap
            
        new_cipher_code = child_cipher[0 : swap_index1] + child_cipher[swap_index2] + child_cipher[swap_index1 + 1 : swap_index2] + child_cipher[swap_index1] + child_cipher[swap_index2 + 1:]
        return new_cipher_code
    else:
        return child_cipher

def breeding(parent1, parent2):
    child = [-1] * 26
    crossover_points = random.sample(range(26), CROSSOVER_LOCATIONS)
    crossover_letters = []

    for n in crossover_points:
        #print(child, parent1)
        child[n] = parent1[1][n]
        crossover_letters.append(parent1[1][n])
    
    k = 0
    for i in range(26):
        if child[i] == -1:
            while (parent2[1][k] in crossover_letters or parent2[1][k] in child) and k < 26:
                k += 1
            child[i] = parent2[1][k]
            k += 1
    
    child = ''.join(child)

    return child

tournament_genetic_algorithm(generate_population(), encode, 0)
