import sys
from math import log

class TreeNode:
    def __init__(self, name = None, children = None):
        self.name = name
        self.children = children
    
    def __print_tree__(self):
        if self.children == None:
            return str(self.label)
        else:
            return str(self.label) + "-->" + str(self.children)

filename = "ldf"

with open(filename, "r") as f:
    count = 0
    for line in f:
        if count != 0:
            pass
        else:
            count += 1

def calc_entropy(cols):
    entropy = 0
    new_cols = [x[-1] for x in cols]
    categories = set(new_cols)
    for cat in categories:
        frac = new_cols.count(cat) / len(new_cols)
        entropy -= frac * log(frac, 2)
    return entropy

def calc_info_gain():
    pass
