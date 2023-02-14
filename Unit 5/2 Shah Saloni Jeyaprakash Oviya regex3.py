import sys; args = sys.argv[1:]

idx = int(args[0])-50

myRegexLst = [
    r"/\b\w*(\w)\w*\1\w*\b/i",
    r"/\b\w*(\w)\w*(\1\w*){3}\b/i",
    r"/^([01]?|0[01]*0|1[01]*1)$/",
    r"/(?=\b\w{6}\b)\b\w*cat\w*\b/i",
    r"",
    r"",
    r"",
    r"",
    r"",
    r"",
]

if idx < len(myRegexLst):
    
    print(myRegexLst[idx])
    
#Saloni Shah, 2, 2023
