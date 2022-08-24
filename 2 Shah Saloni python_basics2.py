import sys

s = sys.argv[1]

print("#1", s[2])
print("#2", s[6])
print("#3", len(s))
print("#4", s[0])
print("#5", s[len(s) - 1])
print("#6", s[len(s) - 2])
print("#7", s[3:8])
print("#8", s[-5:])
print("#9", s[2:])
print("#10", s[::2])
print("#11", s[1::3])
print("#12", s[::-1])
print("#13", s.find(" "))
print("#14", s[0:-1])
print("#15", s[1:])
print("#16", s.lower())

#TODO: figure out how to remove the empty string from the list, 17, 18
print("#17", s.split(" "))
print("#18", len(s.split(" ")))

print("#19", list(s))

#TODO: ascii order, 20
#print("#20", ord(s))

print("#21", s[0:s.find(" ")])

#TODO: palindrome, 22
if(s == reverse(s)):
    print("#22", True)
else:
    print("#22", False)
