import random
import sys
from math import log

encode = 'PF HACYHTTRQ VF N PBYYRPGVBA BS SERR YRNEAVAT NPGVIVGVRF GUNG GRNPU PBZCHGRE FPVRAPR GUEBHTU RATNTVAT TNZRF NAQ CHMMYRF GUNG HFR PNEQF, FGEVAT, PENLBAF NAQ YBGF BS EHAAVAT NEBHAQ. JR BEVTVANYYL QRIRYBCRQ GUVF FB GUNG LBHAT FGHQRAGF PBHYQ QVIR URNQ-SVEFG VAGB PBZCHGRE FPVRAPR, RKCREVRAPVAT GUR XVAQF BS DHRFGVBAF NAQ PUNYYRATRF GUNG PBZCHGRE FPVRAGVFGF RKCREVRAPR, OHG JVGUBHG UNIVAT GB YRNEA CEBTENZZVAT SVEFG. GUR PBYYRPGVBA JNF BEVTVANYYL VAGRAQRQ NF N ERFBHEPR SBE BHGERNPU NAQ RKGRAFVBA, OHG JVGU GUR NQBCGVBA BS PBZCHGVAT NAQ PBZCHGNGVBANY GUVAXVAT VAGB ZNAL PYNFFEBBZF NEBHAQ GUR JBEYQ, VG VF ABJ JVQRYL HFRQ SBE GRNPUVAT. GUR ZNGREVNY UNF ORRA HFRQ VA ZNAL PBAGRKGF BHGFVQR GUR PYNFFEBBZ NF JRYY, VAPYHQVAT FPVRAPR FUBJF, GNYXF SBE FRAVBE PVGVMRAF, NAQ FCRPVNY RIRAGF. GUNAXF GB TRAREBHF FCBAFBEFUVCF JR UNIR ORRA NOYR GB PERNGR NFFBPVNGRQ ERFBHEPRF FHPU NF GUR IVQRBF, JUVPU NER VAGRAQRQ GB URYC GRNPUREF FRR UBJ GUR NPGVIVGVRF JBEX (CYRNFR QBA’G FUBJ GURZ GB LBHE PYNFFRF – YRG GURZ RKCREVRAPR GUR NPGVIVGVRF GURZFRYIRF!). NYY BS GUR NPGVIVGVRF GUNG JR CEBIVQR NER BCRA FBHEPR – GURL NER ERYRNFRQ HAQRE N PERNGVIR PBZZBAF NGGEVOHGVBA-FUNERNYVXR YVPRAPR, FB LBH PNA PBCL, FUNER NAQ ZBQVSL GUR ZNGREVNY. SBE NA RKCYNANGVBA BA GUR PBAARPGVBAF ORGJRRA PF HACYHTTRQ NAQ PBZCHGNGVBANY GUVAXVAT FXVYYF, FRR BHE PBZCHGNGVBANY GUVAXVAT NAQ PF HACYHTTRQ CNTR. GB IVRJ GUR GRNZ BS PBAGEVOHGBEF JUB JBEX BA GUVF CEBWRPG, FRR BHE CRBCYR CNTR. SBE QRGNVYF BA UBJ GB PBAGNPG HF, FRR BHE PBAGNPG HF CNTR. SBE ZBER VASBEZNGVBA NOBHG GUR CEVAPVCYRF ORUVAQ PF HACYHTTRQ, FRR BHE CEVAPVCYRF CNTR.'
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_dict = {}
decipher_dict = {}
cipher_fitness_dict = {}
n_grams_file = "ngrams.txt"
n_grams_dict = {}

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
            if n_gram_word in n_grams_dict.keys():
                to_add = n_grams_dict[n_gram_word]
                if to_add > 0:
                    n_gram_sum += log(to_add, 2)

    cipher_fitness_dict[cipher_string] = n_gram_sum
    return n_gram_sum

def hill_climbing(message_string):
    alphabet_list = list(ALPHABET)
    random.shuffle(alphabet_list)
    cipher_string = ''.join(alphabet_list)

    message_string = decode_func(message_string, decipher_dict_func(cipher_string))

    score = fitness(3, message_string, cipher_string)

    while True:

        swap_index1, swap_index2 = random.sample(range(26),2)
        
        if swap_index1 > swap_index2:
            to_swap = swap_index1
            swap_index1 = swap_index2
            swap_index2 = to_swap
        
        new_cipher_code = cipher_string[0 : swap_index1] + cipher_string[swap_index2] + cipher_string[swap_index1 + 1 : swap_index2] + cipher_string[swap_index1] + cipher_string[swap_index2 + 1:]

        new_score = fitness(3, message_string, new_cipher_code)

        if new_score > score:
            score = new_score
            cipher_string = new_cipher_code
            print(score, cipher_string)
            print(decode_func(message_string, decipher_dict_func(new_cipher_code)))
            print()

#print(encode_func(encode))
#print(decode_func(encode_func(encode)))
#print(fitness(3, encode, new_cipher))
#print(fitness(4, encode, new_cipher))

hill_climbing(encode)
