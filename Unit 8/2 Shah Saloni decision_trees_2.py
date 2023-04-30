import sys
from math import log
import matplotlib.pyplot as pyplot
import random

class TreeNode:
    def __init__(self, name = None, children = None):
        self.name = name
        self.children = children
    
    def __repr__(self) -> str:
        if self.children == None:
            return str(self.name)
        return str(self.name) + " --> " + str(self.children)

#sys.argv[1]
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
    max_info_gain = calc_info_gain(cols, data_info, cols[0])
    max_key = cols[0]
    info_gain_sum = 0
    for key in cols:
        temp_gain = calc_info_gain(cols, data_info, key)
        info_gain_sum += temp_gain
        if temp_gain > max_info_gain:
            max_info_gain = temp_gain
            max_key = key
    tree_node = TreeNode(max_key)
    if info_gain_sum == 0:
        random_choice = random.choice([i[-1] for i in data_info])
        return TreeNode(random_choice)
    val = [x[cols.index(max_key)] for x in data_info]
    val = set(val)
    tree_node.children = {}
    for v in val:
        new_data_info = split_data(cols, data_info, max_key, v)
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
        new_data_info = split_data(cols, data_info, key, v)
        entropy_list.append(calc_entropy(new_data_info))
        freq_list.append(len(new_data_info))

    entropy_sum = 0

    for ent_ind in range(len(entropy_list)):
        entropy_sum += ((freq_list[ent_ind] / len(data_info)) * entropy_list[ent_ind])
    return orig_entropy - entropy_sum

def print_final_tree(tree):
    print("* " + tree.name + "?")
    print_final_tree_rec(tree, 1)

def print_final_tree_rec(tree, depth):
    #https://stackoverflow.com/questions/55648799/append-to-previous-line
    for key, val in tree.children.items():
        depth_print = "\t" * depth
        print(depth_print + "* " + str(key), end="")
        
        if val.children != None:
            depth_print = "\t" * depth
            print()
            print(depth_print + "  * " + str(val.name) + "?")
            print_final_tree_rec(val, depth + 1)
        else:
            print(" --> " + str(val))

# PART 2 METHODS

def drop_rows(data_info, symbol):
    new_data_info = []
    count = 0
    for i in data_info:
        if symbol not in i:
            count += 1
            row = [x for x in i]
            new_data_info.append(row)
    return new_data_info

def drop_cols(data_info, ind):
    new_data_info = []
    for i in data_info:
        drop_col = i[:ind] + i[ind + 1:]
        new_data_info.append(drop_col)
    return new_data_info

def classify_feature_vector(vector, tree, categories):
    if tree.children != None:
        f_vector = tree.name
        val = vector[categories.index(f_vector)]
        if val not in tree.children:
            val_list = list(tree.children.values())
            new_cat = random.choice(val_list)
        else:
            new_cat = tree.children[val]
        return classify_feature_vector(vector, new_cat, categories)
    elif tree.children == None:
        return tree.name

def fill_missing_info(data_info, symbol):
    new_data_info = []
    for i in data_info:
        new_point = []
        for x in i:
            if x != symbol:
                new_point.append(x)
            else:
                col = [z[i.index(x)] for z in data_info]
                col_set = set(col)
                max_freq = 0
                key = col[0]
                for val in col_set:
                    check = col.count(val)
                    if check > max_freq:
                        max_freq = check
                        key = val
                new_point.append(key)
        new_data_info.append(new_point)
    return new_data_info

def split_data(cols, data_info, vector, symbol):
    new_data_info = []
    for i in data_info:
        if i[cols.index(vector)] == symbol:
            new_data_info.append(i)
    return new_data_info


#dec_tree = make_tree(column_names[:-1], data)

# pt 1
'''
test_rows = 50

nonmissing = drop_rows(data, "?")
nonmissing = drop_cols(nonmissing, 0)
column_names.pop(0)

train = nonmissing[: len(nonmissing) - test_rows]
test = nonmissing[len(nonmissing) - test_rows:]

size_acc_list = []

for size in range(5, 182):
    random_rows = random.sample(train, size)
    check_party = set([x[-1] for x in random_rows])
    while len(check_party) < 2:
        random_rows = random.sample(train, size)
        check_party = set([x[-1] for x in random_rows])
    dec_tree = make_tree(column_names[:-1], random_rows)
    correct_class = 0
    for f in test:
        if classify_feature_vector(f, dec_tree, column_names) == f[-1]:
            correct_class += 1
    percent_accuracy = correct_class / len(test)
    size_acc_list.append((size, percent_accuracy))

x_values = [x[0] for x in size_acc_list]
y_values = [y[1] for y in size_acc_list]
'''

# pt 2
'''
nonmissing = fill_missing_info(data, "?")
nonmissing = drop_cols(nonmissing, 0)
column_names.pop(0)

train = nonmissing[: len(nonmissing) - test_rows]
test = nonmissing[len(nonmissing) - test_rows:]

size_acc_list = []

for size in range(5, 385):
    random_rows = random.sample(train, size)
    check_party = [x[-1] for x in random_rows]
    check_party = set(check_party)
    while len(check_party) < 2:
        if len(check_party) < 2:
            random_rows = random.sample(train, size)
            check_party.clear()
    dec_tree = make_tree(column_names[:-1], random_rows)
    correct_class = 0
    for f in test:
        if classify_feature_vector(f, dec_tree, column_names) == f[-1]:
            correct_class += 1
    percent_accuracy = correct_class / len(test)
    size_acc_list.append((size, percent_accuracy))
    

x_values = [x[0] for x in size_acc_list]
y_values = [y[1] for y in size_acc_list]
'''

# pt 3
'''
# nursery: 500
# connect 4: 7000
test_rows = 7000

random.shuffle(data)

train = data[: len(data) - test_rows]
test = data[len(data) - test_rows:]


size_acc_list = []

# nursery: 500, 12000, 500
# connect 4: 5000, 60000, 5000
for size in range(5000, 60000, 5000):
    random_rows = random.sample(train, size)
    check_party = [x[-1] for x in random_rows]
    check_party = set(check_party)
    while len(check_party) < 2:
        if len(check_party) < 2:
            random_rows = random.sample(train, size)
            check_party.clear()
    dec_tree = make_tree(column_names[:-1], random_rows)
    correct_class = 0
    for f in test:
        if classify_feature_vector(f, dec_tree, column_names) == f[-1]:
            correct_class += 1
    percent_accuracy = correct_class / len(test)
    size_acc_list.append((size, percent_accuracy))
'''

# formatting for submission

test_rows = sys.argv[2]

train = data[: len(data) - test_rows]
test = data[len(data) - test_rows:]

size_acc_list = []

for size in range(sys.argv[3], sys.argv[4], sys.argv[5]):
    random_rows = random.sample(train, size)
    check_party = [x[-1] for x in random_rows]
    check_party = set(check_party)
    while len(check_party) < 2:
        if len(check_party) < 2:
            random_rows = random.sample(train, size)
            check_party.clear()
    dec_tree = make_tree(column_names[:-1], random_rows)
    correct_class = 0
    for f in test:
        if classify_feature_vector(f, dec_tree, column_names) == f[-1]:
            correct_class += 1
    percent_accuracy = correct_class / len(test)
    size_acc_list.append((size, percent_accuracy))

x_values = [x[0] for x in size_acc_list]
y_values = [y[1] for y in size_acc_list]

pyplot.scatter(x_values, y_values)
pyplot.xlabel("Size")
pyplot.ylabel("Accuracy")
pyplot.title("Accuracy vs. Size")
pyplot.show()  

# from dec trees 1
'''
original_stout = sys.stdout
with open("treeout.txt", "w") as f:
    sys.stdout = f
    print_final_tree(dec_tree)
    sys.stdout = original_stout
'''

# for plotting
'''
pyplot.scatter(x_values, y_values)
pyplot.xlabel("Size")
pyplot.ylabel("Accuracy")
pyplot.title("Accuracy vs. Size")
pyplot.show()  
'''
