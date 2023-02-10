import sys; args = sys.argv[1:]

idx = int(args[0])-40

#Q40 (DONE): Write a regular expression that will match on an Othello board represented as a string.
#Q41 (DONE): Given a string of length 8, determine whether it could represent an Othello edge with exactly one hole.
#Q42 (DONE): Given an Othello edge as a string, determine whether there is a hole such that if X plays to the hole (assuming it could), it will be connected to one of the corners through X tokens.  
        #Specifically, this means that one of the ends must be a hole, or starting from an end there is a sequence of at least one x followed immediately by a sequence (possibly empty) of o, immediately followed by a hole.
#Q43 (DONE): Match on all strings of odd length.
#Q44 (DONE): Match on all odd length binary strings starting with 0, and on even length binary strings starting with 1.
#Q45 (DONE): Match all words having two adjacent vowels that differ.
#Q46 (DONE): Match on all binary strings which DON’T contain the substring 110.
#Q47 (DONE): Match on all non-empty strings over the alphabet {a, b, c} that contain at most one a.
#Q48 (DONE): Match on all non-empty strings over the alphabet {a, b, c} that contain an even number of a's.
#Q49 (DONE): Match on all positive, even, base 3 integer strings. (even number of 1s)

myRegexLst = [
    #40
    r"/^[x.o]{64}$/i",
    #41
    r"/^[xo]*\.[xo]*$/i",
    #42
    r"/^\.|^(x+o*\.[ox.]*|[ox.]*\.o*x+)$|\.$/i",
    #43
    r"/^(..)*.$/s",
    #44
    r"/^((0|1[01])([01][01])*)$/",
    #45
    r"/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i",
    #46
    r"/^((0*(1?010)*)*1*|((10)(1?0)*)*1*|0*1*)$/",
    #47
    r"/^[bc]*a[bc]*$|^[bc]+$/",
    #48
    r"/^[bc]*(a[bc]*a[bc]*)+$|^[bc]+$/",
    #49
    r"/^(2([02]*1[02]*1)*[02]*|(1[02]*1[02]*)+)$/"
]

if idx < len(myRegexLst):

    print(myRegexLst[idx])

#Saloni Shah, 2, 2023
