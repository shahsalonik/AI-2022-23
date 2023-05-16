import sys
import ast
import numpy as np
import math

def binary_func(num):
    convert = []
    while num > 0:
        convert.append(num % 2)
        num = num // 2
    #FIX: originally gives a reversed input -- must reverse it
    convert.reverse()
    if len(convert) == 0:
        convert.append(0)
    return convert

def truth_table(bits, n):
    #convert int to binary
    # bin() won't work since you need the commas between the values
    new_n = binary_func(n)
    input_list = []

    for i in range(2 ** bits):
        input_list.append(binary_func(i))
    
    for x in range(len(input_list)):
        while len(input_list[x]) < bits:
            #add a 0 to the beginning
            input_list[x].insert(0, 0)

    # needs to print in a descending order, so reverse list
    input_list.reverse()

    output_list = binary_func(n)
    for x in range(len(output_list)):
        while len(output_list) < 2 ** bits:
            #add a 0 to the beginning
            output_list.insert(0, 0)
    
    print_dict = {}
    for y in range(len(input_list)):
        print_dict[tuple(input_list[y])] = output_list[y]

    return print_dict

# scuffed formatting -- maybe fix later
def pretty_print_tt(table):
    print("Inputs | Outputs")
    print("-------|--------")
    for key, val in table.items():
        print(str(key) + " |    " + str(val))

def step(n): 
    if n > 0:
        return 1
    return 0

def dot_product(x, y):
    dot_product_result = 0
    for d in range(len(x)):
        dot_product_result += x[d] * y[d]
    return dot_product_result

def perceptron(A, w, b, x):
    return step(dot_product(w, x) + b)

def check(n, w, b, t_t):
    truth_table_dict = t_t
    check_accuracy = 0
    for key, val in truth_table_dict.items():
        #print("truth table", key, val)
        #print("weight", w, "bias", b)
        percept = perceptron(step, w, b, key)
        #print("perceptron", percept)
        if percept == val:
            check_accuracy += 1
        #print("accuracy count", check_accuracy)
        #input()
    #print("finished going through table")
    return check_accuracy / len(t_t)

def gen_all_truth_tables(bits):
    truth_list = []
    for n in range(2 ** (2 ** bits)):
        truth_list.append(truth_table(bits, n))
    return truth_list

def training(A, w, t_t, b, learn_rate, num_epochs):
    final_epochs = []
    #print("truth table", t_t)
    for i in range(num_epochs):
        for key, val in t_t.items():
            #print("KEY", key, "w is", w)
            perceps = perceptron(A, w, b, key)
            diff = val - perceps 
            for elem in range(len(w)):
                w[elem] += key[elem] * diff * learn_rate 
            b += diff * learn_rate
        final_epochs.append((tuple(w), b))
        if len(final_epochs) > 1:
            if final_epochs[-1] == final_epochs[-2]:
                return final_epochs[-1]
    return final_epochs[-1]

def run_sample(truth_table_inp, bit):
    perceptron = training(step, [0] * bit, truth_table_inp, 0, 1, 100)
    percent_accurate = check(bit, perceptron[0], perceptron[1], truth_table_inp)
    return perceptron, percent_accurate

# PERCEPTRONS 4

def p_net(A, weight_arg, bias_arg, input_arg):
    A_vec_arg = np.vectorize(A)
    a = []
    a.append(input_arg)
    for i in range(1, len(weight_arg)):
        comp = a[i-1] @ weight_arg[i]
        comp += bias_arg[i]
        a.append(A_vec_arg(comp))
    return a[len(a) - 1]

# challenge 1
def challenge_one(inp):
    weights = [None, np.array([[-1, 1], [1, -1]]), np.array([[1],[1]])]
    biases = [None, np.array([[0, 0]]), np.array([[0]])]

    #XOR HAPPENS HERE
    inp_arg1, inp_arg2 = inp
    print(p_net(step, weights, biases, [[inp_arg1, inp_arg2]])[0][0])

# challenge 2
def challenge_two(inp1, inp2):
    weights2 = [None, np.array([[1, -1, 1, -1], [1, 1, -1, -1]]), np.array([[1], [1], [1], [1]])]
    biases2 = [None, np.array([[1, 1, 1, 1]]), np.array([[-3]])]

    output = p_net(step, weights2, biases2, [[inp1, inp2]])[0][0]

    if output == 0:
        print("outside")
    else:
        print("inside")

# challenge 3
def sigmoid(num):
    return 1 / (1 + pow(math.e, -num))

def circle(x, y):
    mag = math.sqrt((x**2) + (y**2))
    if mag < 1:
        return 1
    else:
        return 0

def challenge_three():
    weights3 = [None, np.array([[1, -1, 1, -1], [1, 1, -1, -1]]), np.array([[1], [1], [1], [1]])]
    
    bias = 1.457
    biases3 = [None, np.array([[bias, bias, bias, bias]]), np.array([[-3]])]

    points = []

    for i in range(500):
        points.append([[np.random.uniform(-1,1), np.random.uniform(-1,1)]])

    accuracy_count = 0

    for p in points:
        output = p_net(sigmoid, weights3, biases3, p)
        if output[0][0] >= 0.05:
            p_val = 1
        else:
            p_val = 0
        real_val = circle(p[0][0], p[0][1])
        if real_val == 1:
            print("INSIDE")
        else:
            print( "outside")
        if p_val == real_val:
            accuracy_count += 1

    print("Accuracy:", (accuracy_count * 100 / 500))

#input_tuple = ast.literal_eval(sys.argv[1])
#challenge_one(input_tuple)
#challenge_two(0.2304, 0.93098630)
challenge_three()

#output = p_net(A_vec, weights, biases, input)
