# Colorama demo
from colorama import init, Back, Fore  # Note I have imported specific things here
import sys
import re

# Colorama first needs to be initalized so it works on any OS:
init()  # DO NOT FORGET TO DO THIS!!

s = "While inside they wined and dined, safe from the howling wind.\nAnd she whined, it seemed, for the 100th time, into the ear of her friend,\nWhy indeed should I wind the clocks up, if they all run down in the end?"
exp = sys.argv[1]
if len(exp.split("/")) > 2:
    exp, ad = exp.split("/")[1], exp.split("/")[2]
else:
    exp, ad = exp.split("/")[1], ""
if len(ad) == 0:
    reg = re.compile(r"{}".format(exp))
elif len(ad) > 0:
    if ad == "i":
        reg = re.compile(r"{}".format(exp), re.I)
    elif ad == "s":
        reg = re.compile(r"{}".format(exp), re.S)
    elif ad == "m":
        reg = re.compile(r"{}".format(exp), re.M)
    elif ad == "is" or ad == "si":
        reg = re.compile(r"{}".format(exp), re.I | re.S)
    elif ad == "im" or ad == "mi":
        reg = re.compile(r"{}".format(exp), re.I | re.M)
    elif ad == "sm" or ad == "ms":
        reg = re.compile(r"{}".format(exp), re.S | re.M)
    elif ad == "ims" or ad == "ism" or ad == "mis" or ad == "msi" or ad == "sim" or ad == "smi":
        reg = re.compile(r"{}".format(exp), re.I | re.M | re.S)

exp_list = []

for result in reg.finditer(s):
    exp_list.append(result.span())

temp = 0
orig = len(s)
running = 0
for x in exp_list:
    old = len(s)
    ind1 = x[0] + running
    ind2 = x[1] + running
    s = s[:ind1] + Back.LIGHTYELLOW_EX + s[ind1:ind2] + Back.RESET + s[ind2:]
    orig = len(s)
    temp = orig - old
    running += temp

s = s.replace(Back.RESET + Back.LIGHTYELLOW_EX, Back.RESET + Back.CYAN, 1)

print(s)
