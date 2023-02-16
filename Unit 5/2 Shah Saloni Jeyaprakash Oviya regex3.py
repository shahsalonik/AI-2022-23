import sys; args = sys.argv[1:]

idx = int(args[0])-50

#Q50 (DONE): Match all words where some letter appears twice in the same word.
#Q51 (DONE): Match all words where some letter appears four times in the same word.
#Q52 (DONE): Match all non-empty binary strings with the same number of 01 substrings as 10 substrings.
#Q53 (DONE): Match all six letter words containing the substring cat.
#Q54 (DONE): Match all 5 to 9 letter words containing both the substrings bri and ing.
#Q55 (DONE): Match all six letter words not containing the substring cat.
#Q56: Match all words with no repeated characters.
#Q57 (DONE): Match all binary strings not containing the forbidden substring 10011.
#Q58 (DONE): Match all words having two different adjacent vowels.
#Q59: Match all binary strings containing neither 101 nor 111 as substrings.

myRegexLst = [
    r"/\b\w*(\w)\w*\1\w*\b/i",
    r"/\b\w*(\w)\w*(\1\w*){3}\b/i",
    r"/^([01]?|0[01]*0|1[01]*1)$/",
    r"/(?=\b\w{6}\b)\b\w*cat\w*\b/i",
    r"/(?=\b\w{5,9}\b)(?=\w*bri\w*)\w*ing\w*\b/i",
    r"/\b(?!\w*cat\w*)\w{6}\b/i",
    r"/(?!\w*(\w)\w*\1\w*)\b\w+/i",
    r"/^(?![01]*10011)[01]*$/",
    r"/\b\w*([aeiou])(?!\1)[aeiou]\w*\b/i",
    r"/^(1(?!11)(?!01)|0)*$/"
]

if idx < len(myRegexLst):

    print(myRegexLst[idx])

#Saloni Shah, 2, 2023
