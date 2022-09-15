with open("slide_puzzle_tests.txt") as f:
    line_list = [line.strip() for line in f]

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
    blank_index = state.index(".")
    #print(blank_index)

#left right +1, -1
#up,down +size, -size

count = 0

for x in line_list:
    size = int(x[0])
    print("Line", count, "start state:")
    print_puzzle(size, x[2:])
    print("Line", count, "goal state:", find_goal(x[2:]))
    print("Line", count, "children:", get_children(x[2:]), "\n")
    count += 1
