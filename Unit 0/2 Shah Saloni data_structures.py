from time import perf_counter

start = perf_counter()

#code here

f1, f2, f3 = "10kfile1.txt", "10kfile2.txt", "10kfile3.txt"
s1, s2, s3 = set(), set(), set()

with open(f1) as f:
    s1.add(line.strip() for line in f)

with open(f2) as f:
    s2.add(line.strip() for line in f)

with open(f3) as f:
    s3.add(line.strip() for line in f)

count = 0

for i in s1:
    if(i in s2):
        count += 1

print(count)

end = perf_counter()
print("Total time:", end - start)