import sys
import ast

input_bits = int(sys.argv[1])
input_n = int(sys.argv[2])

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

def step(num):
    if num > 0:
        return 1
    else:
        return 0

def dot_product(x, y):
    dot_product_result = 0
    for d in range(len(x)):
        dot_product_result += x[d] * y[d]
    return dot_product_result

def perceptron(A, w, b, x):
    return A(dot_product(w, x) + b)

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

def run_sample(truth_table_inp, bit):
    perceptron = epoch_algorithm(step, [0] * bit, truth_table_inp, 0, 1, 100)
    percent_accurate = check(bit, perceptron[0], perceptron[1], truth_table_inp)
    return perceptron, percent_accurate

def part_one(n):
    truth_list = gen_all_truth_tables(n)
    count = 0
    for t in truth_list:
        percep, acc_count = run_sample(t, n)
        #print(acc_count)
        if acc_count == 1:
            count += 1
    return len(truth_list), count

def epoch_algorithm(A, w, t_t, b, learn_rate, num_epochs):
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

#number_modeled, correct_number_modeled = part_one(input_n)
#print(number_modeled, "possible functions;", correct_number_modeled, "can be correctly modeled.")

first_truth_table = truth_table(input_bits, input_n)
perceptron_run, acc_percent = run_sample(first_truth_table, input_bits)
print("Final weight vector:", perceptron_run[0])
print("Final bias:", perceptron_run[1])
print("Accuracy:", acc_percent)
