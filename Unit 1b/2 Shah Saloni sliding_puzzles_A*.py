import sys

#sys.argv[1]
filename = "15_puzzles.txt"

with open(filename) as f:
    line_list = [line.strip() for line in f]

def find_goal(board):
    sorted_board = sorted(board)
    goal_state = sorted_board[1:]
    goal_state.append(".")
    return ''.join(goal_state)

#parity check
def is_solvable(state):
    size, board = state.split()
    blank_index = int(board.index("."))
    board = board[:blank_index] + board[blank_index + 1:]
    size = int(size)

    out_of_order = 0

    if size % 2 != 0:
        for x in range(len(board) - 1):
            for y in board[x:]:
                if ord(board[x]) > ord(y):
                    out_of_order += 1
        
        if out_of_order % 2 == 0:
            return True
    else:
        for x in range(len(board) - 1):
            for y in board[x:]:
                if ord(board[x]) > ord(y):
                    out_of_order += 1
        
        row_count = 0
        #find rows by splitting the board into its sizes
        for row in range(size):
            size_set = set()
            size_set.add(board[row:row + size + 1])
            if "." in size_set:
                break
            else:
                row_count += 1
        
        if row_count % 2 == 0:
            if out_of_order % 2 != 0:
                return True
        else:
            if out_of_order % 2 == 0:
                return True
    return False

def taxicab(state):
    moves = 0
    goal = find_goal(state)
    size = int(4)
    for x in range(len(state)):
        if not state[x] == ".":
            x_point = goal.find(state[x]) // size
            y_point = goal.find(state[x]) % size
            x_distance = abs(x_point - x // size)
            y_distance = abs(y_point - x % size)
            moves += x_distance + y_distance
    return moves

for puzzle in line_list:
    print(puzzle, taxicab(puzzle))
