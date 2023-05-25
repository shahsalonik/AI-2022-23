import sys
import ast
import numpy as np
import math
import random

# challenge 2
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

def challenge_two(num_epochs):
    training_set = [(np.array([0, 0]), np.array([0, 0])), (np.array([0, 1]), np.array([0, 1])), (np.array([1, 0]), np.array([0, 1])), (np.array([1, 1]), np.array([1, 0]))]

    weights = [None, np.array([[random.uniform(-1, 1), random.uniform(-1, 1)], [random.uniform(-1, 1), random.uniform(-1, 1)]]), np.array([[random.uniform(-1, 1), random.uniform(-1, 1)], [random.uniform(-1, 1), random.uniform(-1, 1)]])]
    biases = [None,np.array([random.uniform(-1, 1), random.uniform(-1, 1)]), np.array([random.uniform(-1, 1), random.uniform(-1, 1)])]

    a = [0, 0, 0]
    dot = [0, 0, 0]
    delta = [np.array([0, 0])] * 3
    changes = [0, 0, 0, 0]

    learning_rate = 3.6

    print("Output Vector:")
    for epoch in range(num_epochs):
        changes = []
        for x, y in training_set:
            a[0] = x
            for l in range(1, len(weights)):
                dot[l] = (weights[l] @ a[l - 1]) + biases[l]
                a[l] = sigmoid(dot[l])
            delta[-1] = sigmoid_deriv(dot[-1]) * (y - a[-1])
            for l_n in range(1, -1, -1):
                delta[l_n] = sigmoid_deriv(dot[l_n]) * (delta[l_n + 1] @ weights[l_n + 1].T)
            for l_n2 in range(len(delta) - 1, 0, -1):
                biases[l_n2] = biases[l_n2] + (learning_rate * delta[l_n2])
                weights[l_n2] = weights[l_n2] + (learning_rate * (a[l_n2 - 1].T @ delta[l_n2]))
            print(a[-1])
            changes.append(a[-1])

    print("\nFinal Output:")
    for inp, out in training_set:
        print(inp, "-->", out)

# challenge 3

def circle(x, y):
    mag = math.sqrt((x**2) + (y**2))
    if mag < 1:
        return 1
    else:
        return 0

def challenge_three(num_epochs):
    training_set = []
    with open("10000_pairs.txt") as f:
        for line in f:
            line = line.strip()
            split_line = line.split()
            x = [float(split_line[0]), float(split_line[1])]
            y = circle(x[0], x[1])
            training_set.append((np.array([x]), [y]))
    
    MULT = math.sqrt(2) / 2

    weights = [None, np.array([[1, -1, -1, 1], [-1, -1, 1, 1]]), np.array([[1, 1, 1, 1]]).T]
    biases = [None, np.array([[MULT, 3 * MULT, MULT, -1 * MULT]]), np.array([[-3]])]

    step_vec = np.vectorize(step)

    a = [0, 0, 0]
    dot = [0, 0, 0]
    delta = [np.array([0, 0])] * 3

    learning_rate = 0.4
    
    for epoch in range(num_epochs):
        for x, y in training_set:
            a[0] = np.array(x)
            for l in range(1, len(weights)):
                dot[l] = (a[l - 1] @ weights[l]) + biases[l]
                a[l] = sigmoid(dot[l])
            delta[2] = sigmoid_deriv(dot[2]) * (y - a[2])
            for l_n in range(1, -1, -1):
                    delta[l_n] = sigmoid_deriv(dot[l_n]) * (delta[l_n + 1] @ weights[l_n + 1].T)
            for l_n2 in range(len(delta) - 1, 0, -1):
                biases[l_n2] = biases[l_n2] + (learning_rate * delta[l_n2])
                weights[l_n2] = weights[l_n2] + (learning_rate * (a[l_n2 - 1].T @ delta[l_n2]))

        num_misclassified = 0
        for x, y in training_set:
            a[0] = np.array(x)
            for i in range(1, len(weights)):
                dot[i] = (a[i - 1] @ weights[i]) + biases[i]
                a[i] = sigmoid(dot[i])
            a[-1] = step_vec(a[-1])
            if int(a[-1]) != int(y[0]):
                num_misclassified += 1
            #print(a[-1], y[0], num_misclassified)
            #input()
        print("Misclassified points in epoch", epoch, "-", num_misclassified)

# implement later
input_arg = sys.argv[1]

if input_arg == "S":
    challenge_two(1700)
elif input_arg == "C":
    challenge_three(100)
