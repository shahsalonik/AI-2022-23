import sys; args = sys.argv[1:]

idx = int(args[0])-30

#30 (DONE): Determine whether a string is either 0, 100, or 101.
#31 (DONE): Determine whether a given string is a binary string (ie. composed only of  0 and 1 characters).
#32 (DONE): Given a binary integer string, what regular expression determines whether it is even?
#33 (DONE): What is a regular expression to determine (ie. match) those words in a text that have at least two vowels?
#34 (DONE): Given a string, determine whether it is a non-negative, even binary integer string.
#35 (DONE): Determine whether a given string is a binary string containing 110 as a substring.
#36 (DONE): Match on all strings of length at least two, but at most four.
#37 (DONE): Validate a social security number entered into a field (ie. recognize ddd-dd-dddd where the d represents digits and where the dash indicates an arbitrary number of spaces with at most one dash).  For example, 542786363,   542  786363, and 542 – 78-6263 are all considered valid.
#38 (DONE): Determine a regular expression to help you find the first word of each line of text with a  d  in it: Match through the end of the first word with a d on each line that has a d.
#39 (DONE): Determine whether a string is a binary string that has the same number of 01 substrings as 10 substrings.

myRegexLst = [
    r"/^0$|^100$|^101$/",
    r"/^[01]*$/",
    r"/0$/",
    r"/\w*[aeiou]\w*[aeiou]\w*/i",
    r"/^0$|^1[01]*[01]*0$/",
    r"/^[01]*110[01]*$/",
    r"/^.{2,4}$/s",
    r"/^\d{3} *-? *\d{2} *-? *\d{4}$/",
    r"/^.*?d\w*/im",
    r"/^[01]?|^0[01]*0$|^1[01]*1$/"
]

if idx < len(myRegexLst):

    print(myRegexLst[idx])

#Saloni Shah, 2, 2023
