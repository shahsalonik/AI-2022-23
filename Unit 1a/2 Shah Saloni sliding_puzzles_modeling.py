with open("slide_puzzle_tests.txt") as f:
    line_list = [line.strip() for line in f]

def print_puzzle(size, board):
    for num in range(size):
        print((" ").join(board[:size]))
        board = board[size:]
    print(board)

def find_goal(board):
    sorted_board = sorted(board)
    goal_state = sorted_board[1:]
    goal_state.append(".")
    return ''.join(goal_state)

def get_children(state):
    size = int(state[0])
    board = state[2:]
    blank_index = board.index(".")
    children = []
    if blank_index % size != 0: #blank swap right
        children.append(board[:blank_index - 1] + "." + board[blank_index - 1] + board[blank_index + 1:])
    if (blank_index + 1) % size != 0: #blank swap left
        children.append(board[:blank_index] + board[blank_index + 1] + "." + board[blank_index + 2:])
    if blank_index >= size: #blank swap up
        children.append(board[:blank_index - size] + "." + board[blank_index - size + 1:blank_index] + board[blank_index - size] + board[blank_index + 1:]) 
    if blank_index <= (size * (size - 1)): #blank swap down
        children.append(board[:blank_index] + board[blank_index + size] + board[blank_index + 1:blank_index + size] + "." + board[blank_index + size + 1:])
    return children

count = 0

for x in line_list:
    size = int(x[0])
    print("Line", count, "start state:")
    print_puzzle(size, x[2:]) 
    print("Line", count, "goal state:", find_goal(x[2:]))
    print("Line", count, "children:", get_children(x), "\n")
    count += 1
