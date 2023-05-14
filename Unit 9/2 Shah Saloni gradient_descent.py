import sys
import numpy as np

# 4x^2 - 3xy + 2y^2 + 24x - 20y
def gradA(x, y):
    return np.array((8*x - 3*y + 24, -3*x + 4*y - 20))

# (1 - y)^2 + (x - y^2)^2
def gradB(x, y):
    return np.array((2*(x - y**2), 2*(-2*x*y + 2*y**3 + y - 1)))

def gradient_descent(inp_function, learn_rate):
    #start at (0, 0)
    x, y = 0, 0

    if inp_function == "A":
        grad_func = gradA
    elif inp_function == "B":
        grad_func = gradB
    
    norm_grad = grad_func(x, y)

    while np.sqrt(norm_grad.dot(norm_grad)) > 0.0000001:
        norm_grad = grad_func(x, y)
        x = x - (learn_rate * norm_grad[0])
        y = y - (learn_rate * norm_grad[1])
        print(x, y, norm_grad)

input_function = sys.argv[1]

gradient_descent(input_function, 0.1)
