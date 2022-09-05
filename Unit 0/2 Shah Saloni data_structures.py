from collections import deque
from multiprocessing import heap
from time import perf_counter
from heapq import heappush, heappop, heapify

import sys

start = perf_counter()

#code here

f1, f2, f3 = sys.argv[1], sys.argv[2], sys.argv[3]
s1, s2, s3 = [], [], []
set3 = set()

with open(f1) as f:
    s1 = [int(line.strip()) for line in f]

with open(f2) as f:
    s2 = [int(line.strip()) for line in f]

with open(f3) as f:
    s3 = [int(line.strip()) for line in f]

#convert list3 to set
set3 = set(s3)

#convert to dicts
dict1, dict2 = {}, {}

for x in s1:
    if x in dict1:
        dict1[x] += 1
    else:
        dict1[x] = 1

for i in s2:
    if i in dict2:
        dict2[i] += 1
    else:
        dict2[i] = 1

#Problem 1: Unique values files 1 & 2
count = 0

set1 = set(s1)
set2 = set(s2)

for i in set1:
    if(i in set2):
        count += 1

print("#1: %s" % count)

#Problem 2: Sum of every 100th unique value file 1
index = 99 
sum = 0
list1 = list(dict1.keys())

while index < len(list1):
    sum += list1[index]
    index += 100

print("#2: %s" % sum)

#Problem 3: Total number of times each unique value in file 3 appears in files 1/2
count_3 = 0

for key in set3:
    if key in dict1.keys():
        count_3 += dict1[key]
    if key in dict2.keys():
        count_3 += dict2[key]
        
print("#3: %s" % count_3)

#Problem 4: 10 smallest numbers in file 1 in increasing order
sorted_queue = deque(set1)
small_list = []

for y in range(10):
    small_list.append(sorted_queue.popleft()) 
print("#4: %s" % small_list)

#Problem 5: 10 largest numbers appearing 2+ times in file 2 in decreasing order
new_s2 = []
big_list = []

for key, val in dict2.items():
    if val > 1:
        new_s2.append(key)

sorted_s2 = sorted(new_s2)

for k in range(10):
    big_list.append(sorted_s2.pop())
print("#5: %s" % big_list)

#Problem 6: Read file 1 and get the smallest numbers before/including a multiple of 53 in a heap, then add them
sum_53 = 0
new_s1 = set()
heap_list = []

for x in s1:
    if x % 53 != 0:
        if x not in new_s1:
            heappush(heap_list, x)
    else:
        if x not in new_s1:
            heappush(heap_list, x)
        temp = heappop(heap_list)
        if temp in new_s1:
            while temp in new_s1:
                temp = temp = heappop(heap_list)
            new_s1.add(temp)
        else:
            new_s1.add(temp)
        
for y in new_s1:
    sum_53 += y

#31073
print("#6: %s" % sum_53)

end = perf_counter()
print("Total time:", end - start)
