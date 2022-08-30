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

set1 = set()

for x in s1:
    if x not in set1:
        set1.add(x)
        print(x)







end = perf_counter()
print("Total time:", end - start)
