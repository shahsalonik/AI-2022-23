from collections import deque
from time import perf_counter

start = perf_counter()

#code here

f1, f2, f3 = "10kfile1.txt", "10kfile2.txt", "10kfile3.txt"
s1, s2, s3 = [], [], []

with open(f1) as f:
    s1 = [int(line.strip()) for line in f]

with open(f2) as f:
    s2 = [int(line.strip()) for line in f]

with open(f3) as f:
    s3 = [int(line.strip()) for line in f]

#Problem 1: Uniue values files 1 & 2
count = 0

set1 = set(s1)
set2 = set(s2)

for i in set1:
    if(i in set2):
        count += 1

print("#1: %s" % count)

#Problem 2: Sum of every 100th unique value file 1

list1 = list(set1)
sum = 0

for x in range(int(len(list1)/100)):
    print(s1[(x+1)*100])
    sum += s1[(x+1)*100]
print(sum)
print("\n")

#Problem 3: Total number of times each unique value in file 3 appears in files 1/2


#Problem 4: 10 smallest numbers in file 1 in increasing order
sorted_set = set(s1)
small_list = []

for y in range(10):
    small_list.append(sorted_set.pop()) 
print(small_list)

#Problem 5: 10 largest numbers appearing 2+ times in file 2 in decreasing order

ss2 = sorted(s2)
new_s2 = []
big_list = []
index = 0

for x in ss2:
    if index != len(ss2) - 1:
        if (ss2[index + 1] == x):
            new_s2.append(ss2[index])
    index += 1       

st2 = sorted(set(new_s2))
queue2 = deque(st2)
print(queue2)

for k in range(10):
    big_list.append(queue2.pop())
print(big_list)

end = perf_counter()
print("Total time:", end - start)
