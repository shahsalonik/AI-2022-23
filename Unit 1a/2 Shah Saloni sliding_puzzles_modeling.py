with open("slide_puzzles_tests.txt") as f:
    line_list = [line.strip() for line in f]

def print_puzzle(size, puzzle_rep):
    print(size, puzzle_rep)
