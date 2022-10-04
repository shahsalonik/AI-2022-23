import sys

#sys.argv[1]
filename = "slide_puzzle_tests.txt"

with open(filename) as f:
    line_list = [line.strip() for line in f]

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

        #find rows by splitting the board into its sizes
        return True
    return False

for puzzle in line_list:
    print(puzzle, is_solvable(puzzle))
