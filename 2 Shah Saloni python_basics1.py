import sys

if(sys.argv[1] == 'A'):
    print(int(sys.argv[2]) + int(sys.argv[3]) + int(sys.argv[4]))
elif(sys.argv[1] == 'B'):
    x = 0
    for index, value in enumerate(sys.argv):
        if(index > 1):
            x = x + int(value)
    print(x)
elif(sys.argv[1] == 'C'):
    list = []
    for index, value in enumerate(sys.argv):
        if(index > 1 and int(value) % 3 == 0):
            list.append(value)
    print(list)
elif(sys.argv[1] == 'D'):
    x, a, b = int(sys.argv[2]), 1, 1
    if(x >= 1):
        print(a)
    else:
        print("no fibonacci sequence available for that number :(")
    if(x >= 2):
        print(b)
    if(x > 2):
        for i in range(2, x):
            c = a + b
            a = b
            b = c
            print(c)
elif(sys.argv[1] == 'E'):
    x, y = int(sys.argv[2]), int(sys.argv[3])
    for k in range(x, y+1):
        value = pow(k, 2) - (3*k) + 2
        print(value)
elif(sys.argv[1] == 'F'):
    a, b, c = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
    if(a + b > c and b + c > a and a + c > b):
        p = (a + b + c)/2
        area = p * (p - a) * (p - b) * (p - c)
        t_area = pow(area, 0.5)
        print("The area of the triangle is", t_area)
    else:
        print("sorry, that's not a valid triangle")
elif(sys.argv[1] == 'G'):
    word = sys.argv[2]
    count = {n:sum([1 for letter in word if letter == n]) for n in 'AEIOUaeiou'}
    print(count)

