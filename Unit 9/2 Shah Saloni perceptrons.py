import sys
import ast

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

def check(n, w, b):
    truth_table_dict = truth_table(len(w), n)
    check_accuracy = 0
    for key, val in truth_table_dict.items():
        percept = perceptron(step, w, b, key)
        if percept == val:
            check_accuracy += 1
    return check_accuracy / len(truth_table_dict)

print(check(int(sys.argv[1]), ast.literal_eval(sys.argv[2]), float(sys.argv[3])))
