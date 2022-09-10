import sys
import time
import heapq
from time import perf_counter

start = perf_counter()

#Problem #2: write an is_prime(x) function
def is_prime(x):
    if x == 1:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
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

#Problem #3: Largest prime factor of 600851475143
number, big_prime = 600851475143, 0

for num in range(2, int(number**0.5)):
    if number % num == 0:
        big_prime = num
        number /= num
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

#Problem #5: Universal GCD
def gcd(x, y):
    while y != 0:
        t = y
        y = x % y
        x = t
    return x

def lcm(a, b):
    return a // gcd(a, b) * b

def range_lcm(start, end):
    lcm_num = 1
    for x in range(start, end + 1):
        lcm_num = lcm(x, lcm_num)
    return lcm_num

print("#5: %s" % range_lcm(1, 20))

#Problem #6: Natural numbers 
print("#6:", (pow(sum(x for x in range(101)), 2)) - sum([pow(n, 2) for n in range(101)]))

#Problem #7: 1000st prime 104743
prime_count, prime_num = 1, 3

while prime_count < 10001:
    if is_prime(prime_num):
        prime_count += 1
        if prime_count == 10001:
            break
        prime_num += 2
    else:
        prime_num += 2
print("#7: %s" % prime_num)

#Problem #8: 13 digits in 1000 digit number with the greatest product 
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

index, greatest_product = 0, 0

while index < (len(num_string) - 12):
    product = 1
    for i in range(13):
        product *= int(num_string[index])
        index += 1
    if product > greatest_product:
        greatest_product = product
    index -= 12

print("#8: %s" % greatest_product)

#Problem 9: Special Pythagorean Triplet
product = 0

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b
        if (a**2 + b**2) == c**2:
            if a + b + c == 1000:
                product = a*b*c
print("#9: %s" % product)

#Problem 11: Largest product in a grid
data = [[ 8,  2, 22, 97, 38, 15,  0, 40,  0, 75,  4,  5,  7, 78, 52, 12, 50, 77, 91,  8],
       [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48,  4, 56, 62,  0],
       [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30,  3, 49, 13, 36, 65],
       [52, 70, 95, 23,  4, 60, 11, 42, 69, 24, 68, 56,  1, 32, 56, 71, 37,  2, 36, 91],
       [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
       [24, 47, 32, 60, 99,  3, 45,  2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
       [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
       [67, 26, 20, 68,  2, 62, 12, 20, 95, 63, 94, 39, 63,  8, 40, 91, 66, 49, 94, 21],
       [24, 55, 58,  5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
       [21, 36, 23,  9, 75,  0, 76, 44, 20, 45, 35, 14,  0, 61, 33, 97, 34, 31, 33, 95],
       [78, 17, 53, 28, 22, 75, 31, 67, 15, 94,  3, 80,  4, 62, 16, 14,  9, 53, 56, 92],
       [16, 39,  5, 42, 96, 35, 31, 47, 55, 58, 88, 24,  0, 17, 54, 24, 36, 29, 85, 57],
       [86, 56,  0, 48, 35, 71, 89,  7,  5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
       [19, 80, 81, 68,  5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77,  4, 89, 55, 40],
       [ 4, 52,  8, 83, 97, 35, 99, 16,  7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
       [88, 36, 68, 87, 57, 62, 20, 72,  3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
       [ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18,  8, 46, 29, 32, 40, 62, 76, 36],
       [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74,  4, 36, 16],
       [20, 73, 35, 29, 78, 31, 90,  1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57,  5, 54],
       [ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52,  1, 89, 19, 67, 48]]

max_product = 0

for row in range(16):
    for col in range(20):
        x_row = data[row][col] * data[row + 1][col] * data[row + 2][col] * data[row + 3][col]
        if x_row > max_product:
            max_product = x_row
for row in range(20):
    for col in range(16):
        y_col = data[row][col] * data[row][col + 1] * data[row][col + 2] * data[row][col + 3]
        if y_col > max_product:
            max_product = y_col
for row in range(16):
    for col in range(16):
        diag1 = data[row][col] * data[row + 1][col + 1] * data[row + 2][col + 2] * data[row + 3][col + 3]
        if diag1 > max_product:
            max_product = diag1
for row in range(16):
    for col in range(16):
        diag2 = data[row][col + 4] * data[row + 1][col + 3] * data[row + 2][col + 2] * data[row + 3][col + 1]
        if diag2 > max_product:
            max_product = diag2
print("#11: %s" % max_product)

#Problem 14: Longest Collatz sequence by a number under 1 million
solved = {1: 1}
max_length, seq_len, seq_num = 1, 0, 0

def generate_seq(num):
    length = 0
    seq_num = num

    while seq_num not in solved:
        if seq_num % 2 == 0:
            seq_num /= 2
        else:
            seq_num = (3 * seq_num) + 1
        length += 1

    solved[num] = length + solved[seq_num]

for col in range(2, 1000000):
    if col not in solved.keys():
        generate_seq(col)
    if solved[max_length] < solved[col]:
        max_length = col

print("#14: %s" % max_length)

#Problem 18: max path sum
data = [[75],
       [95, 64],
       [17, 47, 82],
       [18, 35, 87, 10],
       [20,  4, 82, 47, 65],
       [19,  1, 23, 75,  3, 34],
       [88,  2, 77, 73,  7, 63, 67],
       [99, 65,  4, 28,  6, 16, 70, 92],
       [41, 41, 26, 56, 83, 40, 80, 70, 33],
       [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
       [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
       [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
       [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
       [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
       [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]

max_sums = set()

def find_max(grid, x, y, sum):
    sum += grid[x][y]
    if x == 14:
        max_sums.add(sum)
    else:
        find_max(grid, x + 1, y + 1, sum)
        find_max(grid, x + 1, y, sum)

find_max(data, 0, 0, 0)

max_sum = 0

for n in max_sums:
    if n > max_sum:
        max_sum = n

print("#18: %s" % max_sum)

#Problem 28: Sum of the diagonals of a 1001 x 1001 spiral
corner_nums = list(range(1, 1002002))
index, sum, step = 0, 1, 2

while corner_nums[index] != 1002001:
    for corner_num in range(4):
        index += step
        sum += corner_nums[index]
    step += 2

print("#28: %s" % sum)

#Problem 29: a^b
print("#29: %s" % len({a**b for a in range(2, 101) for b in range(2, 101)}))

end = perf_counter()
print("Total time:", end - start)
