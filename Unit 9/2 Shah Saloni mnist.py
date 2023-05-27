import sys
import ast
import numpy as np
import math
import random
import csv

def step(n): 
    if n > 0.5:
        return 1
    return 0

def sigmoid(num):
    return 1 / (1 + pow(math.e, -num))

def sig_deriv_vec(num):
    sig = sigmoid(num)
    return sig * (1 - sig)

def sigmoid_deriv(num):
    A = np.vectorize(sig_deriv_vec)
    return A(num)

def create_network(dims):
    weights = [None]
    biases = [None]
    for d in range(1, len(dims)):
        weights.append(2 * np.random.rand(dims[d - 1], dims[d]) - 1)
        biases.append(2 * np.random.rand(1, dims[d]) - 1)
    return weights, biases

# TRAINING THE NETWORK
ep_count = 0

# network architecture
weights, biases = create_network([784, 300, 100, 10])
training_set = open("mnist_train.csv")
training_set = csv.reader(training_set)

weights_output_file = open("mnist_w.pkl", "w")
biases_output_file = open("mnist_b.pkl", "w")

for nums in training_set:
    classify_list = []
    for c in nums:
        classify_list.append(int(c))
    actual_num = classify_list.pop(0)
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y[actual_num] = 1

    a = [np.array([[0]])] * len(weights)
    dot = [np.array([[0]])] * len(weights)
    delta = [np.array([[0]])] * len(weights)
    
    learning_rate = 0.4

    # back propagation
    a[0] = np.array([classify_list]) / 255

    for l in range(1, len(weights)):
        dot[l] = (a[l - 1] @ weights[l]) + biases[l]
        a[l] = sigmoid(dot[l])
    delta[-1] = sigmoid_deriv(dot[-1]) * (y - a[-1])
    for l_n in range(len(weights) - 2, -1, -1):
        delta[l_n] = sigmoid_deriv(dot[l_n]) * (delta[l_n + 1] @ weights[l_n + 1].T)
    for l_n2 in range(len(delta) - 1, 0, -1):
        biases[l_n2] = biases[l_n2] + (learning_rate * delta[l_n2])
        weights[l_n2] = weights[l_n2] + (learning_rate * (a[l_n2 - 1].T @ delta[l_n2]))
    
    ep_count += 1
    #print(ep_count)
    if ep_count % 60000 == 0:
        weights_output_file.write(str(weights))         
        biases_output_file.write(str(biases)) 
        break


#TESTING NETWORK TRAINING ACCURACY
correct_classif = 0
total = 0

training_set = open("mnist_train.csv")
training_set = csv.reader(training_set)
load_file = open("mnist_w_b.pkl", "w")
output_file = open("to_write.txt", "w")


weights, biases = [], []
for line in load_file:
    line = line.split()
    weights = line[0]
    biases = line[1]

for vals in training_set:
    classify_list = []
    for c in vals:
        classify_list.append(int(c))
    actual_num = classify_list.pop(0)
    y = [0] * 10
    y[actual_num] = 1

    a = [np.array([[0]])] * len(weights)
    a[0] = np.array([classify_list]) / 255

    for l in range(1, len(weights)):
        dot = (a[l - 1] @ weights[l]) + biases[l]
        a[l] = sigmoid(dot)

    get_max_num_list = list(a[-1][0])
    max_num = get_max_num_list.index(max(get_max_num_list))

    if max_num == actual_num:
        correct_classif += 1
    total += 1
    print("Training Accuracy: " + str(correct_classif * 100 / total))
output_file.write("training classification:" + str(correct_classif * 100 / total) + "\n")

#TESTING OVERALL ACCURACY
testing_correct_classif = 0
test_total = 0

testing_set = open("mnist_test.csv")
testing_set = csv.reader(testing_set)

for vals in testing_set:
    classify_list = []
    for c in vals:
        classify_list.append(int(c))
    actual_num = classify_list.pop(0)

    a = [np.array([[0]])] * len(weights)
    a[0] = np.array([classify_list]) / 255

    for l in range(1, len(weights)):
        dot = (a[l - 1] @ weights[l]) + biases[l]
        a[l] = sigmoid(dot)

    get_max_num_list = list(a[-1][0])
    max_num = get_max_num_list.index(max(get_max_num_list))

    if max_num == actual_num:
        testing_correct_classif += 1
    test_total += 1
output_file.write("testing classification:" + str(testing_correct_classif * 100 / test_total))
