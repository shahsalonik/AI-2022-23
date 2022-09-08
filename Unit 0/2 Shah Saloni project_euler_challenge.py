from math import prod
import sys
import time
import heapq
from time import perf_counter

start = perf_counter()

#Problem #2: write an is_prime(x) function
def is_prime(x):
    if x == 1:
        return False

    for i in range(int(x**0.5)):
        if x % (i+1) == 0:
            return False
        else:
            return True

#Project Euler Problems

#Problem #1: Sum of all multiples of 3 and 5 < 1000
print("#1: %s" % sum([num for num in range(1000) if num % 3 == 0 or num % 5 == 0]))

#Problem #2: Sum of all even Fibbonacci numbers < 4,000,000
a, b = 1, 2
even_fib_list = [b]
c = a + b

while c <= 4000000:
    c = a + b
    a = b
    b = c
    if c % 2 == 0:
        even_fib_list.append(c)

print("#2: %s" % sum(even_fib_list))

#TODO
#Problem #3: Largest prime factor of 600851475143
number = 600851475143
factor = 2
big_prime = 0

while factor != number:
    if number % factor == 0:
        number = number/factor
        big_prime = factor
        factor = 2
    else:
        factor += 1
print("#3: %s" % big_prime)

#Problem #4: Largest palindrome product from 2 three digit numbers
product = 0

for num1 in range(999, 1, -1):
    for num2 in range(999, 1, -1):
        s = str(num1*num2)
        if(s == s[::-1]):
            if int(s) > int(product):
                product = s
print("#4: %s" % product)

#TODO
#Problem #5: Universal GCD
def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

#Problem #6: Natural numbers 
print("#6:", (pow(sum(x for x in range(101)), 2)) - sum([pow(n, 2) for n in range(101)]))

#Problem #8: 13 digits in 1000 digit number with the greatest product 23514624000

num_string = "731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385" +\
            "861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689" +\
            "664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589" +\
            "072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333" +\
            "001053367881220235421809751254540594752243525849077116705560136048395864467063244157221553975369781797" +\
            "784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474821663704844" +\
            "031998900088952434506585412275886668811642717147992444292823086346567481391912316282458617866458359124" +\
            "566529476545682848912883142607690042242190226710556263211111093705442175069416589604080719840385096245" +\
            "544436298123098787992724428490918884580156166097919133875499200524063689912560717606058861164671094050" +\
            "7754100225698315520005593572972571636269561882670428252483600823257530420752963450"

index = 0
greatest_product = 0

while index < (len(num_string) - 12):
    product = 1
    for i in range(13):
        product *= int(num_string[index])
        index += 1
    if product > greatest_product:
        greatest_product = product
    index -= 12

print("#8: %s" % greatest_product)

#Problem #7: 10001st prime 104743
a, b, c = 0, 0, 0

for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            if (a + b + c ) == 1000 and ((a**2) + (b**2) + (c**2) == 1000):
                print("#9: %s" % a % b % c)


end = perf_counter()
print("Total time:", end - start)
