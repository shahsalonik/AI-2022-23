import sys
from math import log

class TreeNode:
    def __init__(self, name = None, children = None):
        self.name = name
        self.children = children
    
    def __repr__(self) -> str:
        if self.children == None:
            return str(self.name)
        return str(self.name) + " --> " + str(self.children)

filename = sys.argv[1]
column_names, data = [], []

with open(filename, "r") as f:
    count = 0
    for line in f:
        if count != 0:
            data.append(line.strip("\n").split(","))
        else:
            column_names = line.strip("\n").split(",")
            count += 1
    
#print(column_names, data)
#input()

def make_tree(cols, data_info):
    max_info_gain = 0
    max_key = cols[0]
    for key in cols:
        temp_gain = calc_info_gain(cols, data_info, key)
        if temp_gain > max_info_gain:
            max_info_gain = temp_gain
            max_key = key
    tree_node = TreeNode(max_key)
    val = [x[cols.index(max_key)] for x in data_info]
    val = set(val)
    tree_node.children = {}
    for v in val:
        new_data_info = new_data(cols, data_info, max_key, v)
        
        if calc_entropy(new_data_info) == 0:
            tree_node.children[v] = TreeNode(new_data_info[0][-1])
        else:
            tree_node.children[v] = make_tree(cols, new_data_info)
    return tree_node

def new_data(cols, data_info, key, val):
    n_data = []
    for i in data_info:
        if i[cols.index(key)] == val:
            data_point = [x for x in i]
            n_data.append(data_point)
    return n_data

def calc_entropy(cols):
    entropy = 0
    new_cols = [x[-1] for x in cols]
    categories = set(new_cols)
    for cat in categories:
        frac = new_cols.count(cat) / len(new_cols)
        entropy -= frac * log(frac, 2)
    return entropy

def calc_info_gain(cols, data_info, key):
    orig_entropy = calc_entropy(data_info)

    val = [x[cols.index(key)] for x in data_info]
    val = set(val)

    entropy_list, freq_list = [], []

    for v in val:
        new_data_info = new_data(cols, data_info, key, v)
        entropy_list.append(calc_entropy(new_data_info))
        freq_list.append(len(new_data_info))

    entropy_sum = 0

    for ent_ind in range(len(entropy_list)):
        entropy_sum += ((freq_list[ent_ind] / len(data_info)) * entropy_list[ent_ind])
    return orig_entropy - entropy_sum

def print_final_tree(tree):
    print("* " + tree.name + "?")
    print_final_tree_rec(tree, 1)

def print_final_tree_rec(tree, num_indents):
    #https://stackoverflow.com/questions/55648799/append-to-previous-line
    for key, val in tree.children.items():
        indent = "\t" * num_indents
        print(indent + "* " + str(key), end="")
        
        if val.children != None:
            indent = "\t" * num_indents
            print()
            print(indent + "  * " + str(val.name) + "?")
            print_final_tree_rec(val, num_indents + 1)
        else:
            print(" --> " + str(val))

dec_tree = make_tree(column_names[:-1], data)

original_stout = sys.stdout
with open("treeout.txt", "w") as f:
    sys.stdout = f
    print_final_tree(dec_tree)
    sys.stdout = original_stout
