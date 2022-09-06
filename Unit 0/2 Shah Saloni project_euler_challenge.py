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
        if x % i == 0:
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

#Problem #6: Natural numbers 25164150
print(sum([n**n for n in range(101)]) - sum([n for n in range(101)]))

end = perf_counter()
print("Total time:", end - start)
