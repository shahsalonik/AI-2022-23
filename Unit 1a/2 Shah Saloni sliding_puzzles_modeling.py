with open("slide_puzzle_tests.txt") as f:
    line_list = [line.strip() for line in f]

def print_puzzle(size, board):
    for num in range(size):
        print((" ").join(board[:size]))
        board = board[size:]

def find_goal(board):
    sorted_board = sorted(board)
    goal_state = sorted_board[1:]
    goal_state.append(".")
    return goal_state

print_puzzle(2, "A.CB")
find_goal("A.CB")
