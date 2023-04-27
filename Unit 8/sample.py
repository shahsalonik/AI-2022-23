import math
import csv
import sys

class TreeNode:
    def __init__(self, label=None, children=None):
        self.label = label
        self.children = children

    def __repr__(self):
        # for print()
        if self.children == None:
            return str(self.label)
        return str(self.label) + " --> " + str(self.children)


def load_csv(filename):
    # return separate list of headers and data
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    headers = dataset[0]
    dataset = dataset[1:]
    return headers, dataset


def entropy(dataset):
    # calculate the entropy of the data
    entropy = 0
    labels = [row[-1] for row in dataset]  # last column is entropy
    labelset = set(labels)
    for label in labelset:
        p = labels.count(label) / len(labels)
        entropy -= p * math.log(p, 2)
    return entropy


def split_dataset(labels, dataset, feature, value):
    # generate a new dataset by splitting on a feature with a value
    new_dataset = []
    for row in dataset: # iterates over the rows, which are lists
        if row[labels.index(feature)] == value:   # if the value of the feature is the value we want
            new_row = [thing for thing in row] # copy the row
            # new_row = row[: labels.index(feature)] + row[labels.index(feature) + 1 :]
            new_dataset.append(new_row)
    return new_dataset


def information_gain(labels, dataset, feature):
    # every value the feature can have
    values = set([row[labels.index(feature)] for row in dataset])
    # calculate the entropy of the data
    entropies = []
    occurences = []
    for value in values:
        new_dataset = split_dataset(labels, dataset, feature, value)
        entropies.append(entropy(new_dataset))
        occurences.append(len(new_dataset))
    # calculate the expected value of entropy
    expected_entropy = 0
    for i in range(len(entropies)):
        expected_entropy += (occurences[i] / len(dataset)) * entropies[i]
    # calculate the information gain
    return entropy(dataset) - expected_entropy


def generate_tree(labels, dataset):
    print(".", end="", flush=True)
    # consider each feature, calc information gain, choose best
    information_gains = {}
    for feature in labels[:-1]:
        information_gains[feature] = information_gain(labels, dataset, feature)
    # choose feature with highest information gain
    best_feature = max(information_gains, key=information_gains.get)# ; print(f"[DEBUG] best_feature: {best_feature}", end=" ")
    # create a tree node with the best feature as label
    tree = TreeNode(best_feature)
    # for each value the best feature can have
    values = set([row[labels.index(best_feature)] for row in dataset])# ; print(f"[DEBUG] values: {values}")
    # create a branch for that value
    tree.children = {}
    for value in values:
        # create a subtree for that branch
        new_dataset = split_dataset(labels, dataset, best_feature, value)
        # if the subtree is perfect (0 entropy), label it with the output
        if entropy(new_dataset) == 0:
            tree.children[value] = TreeNode(new_dataset[0][-1])
        # otherwise, repeat the process
        else:
            tree.children[value] = generate_tree(labels, new_dataset)
    return tree


def visualize_tree_helper(tree, indent=0, file=sys.stdout):
    # accepts a TreNode which is th root, prints it
    for key, value in tree.children.items():
        # input(f"DEBUG: {key} | {value} | {type(value)} | {value.children}")
        print("\t" * indent + "  * " + str(key), end="", file=file)
        if isinstance(value.children, dict):  # if not leaf node
            # print("?")
            print(file=file)
            print("\t" * (indent + 1) + "* " + str(value.label) + "?", file=file)
            visualize_tree_helper(value, indent + 1, file=file)
        else:
            print(" --> " + str(value), file=file)  # if leaf node, print the Yes/No

def visualize_tree(tree, file=sys.stdout):
    print("* "+tree.label+"?", file=file)
    visualize_tree_helper(tree, 1, file=file)

def graphviz_helper(tree, g, parent):
    for key, value in tree.children.items():
        if isinstance(value.children, dict):  # if not leaf node
            g.add_node(str(key))
            g.add_edge(parent, str(key))
            graphviz_helper(value, g, str(key))
        else:
            g.add_node(str(key) + " --> " + str(value))
            g.add_edge(parent, str(key) + " --> " + str(value))

def graph_visualization(tree):
    # requires networkx and matplotlib
    # produeces a graph visualization of the tree (very messy looking)
    try:
        import networkx as nx
        import matplotlib.pyplot as plt
    except ImportError:
        exit(1)
    g = nx.DiGraph()
    g.add_node(tree.label)
    graphviz_helper(tree, g, tree.label)
    nx.draw_networkx(g, with_labels=True, pos=nx.planar_layout(g), font_size=14)
    plt.show()


if __name__ == "__main__":
    headers, dataset = load_csv(sys.argv[1])
    # print(headers)
    # for row in dataset:
    #     print(row)

    print(headers, dataset)

    tree = generate_tree(headers, dataset)
    # for k, v in tree.children.items():
    #     print(k, "==>", v)

    visualize_tree(tree, file=open("treeout.txt", "w"))

    graph_visualization(tree)