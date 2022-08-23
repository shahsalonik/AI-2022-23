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
    x = int(sys.argv[2])
    a = 1
    b = 1
    if(x == 1):
        print(a)
    elif(x == 2):
        print(b)
    else:
        for i in range(0, x):
            c = a + b
            a = b
            b = c
            print(c)
        