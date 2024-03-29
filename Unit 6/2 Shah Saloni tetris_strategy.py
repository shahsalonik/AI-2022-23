import sys
import random
from time import perf_counter

board_input = sys.argv[1]

HEIGHT = 20
WIDTH = 10

POPULATION_SIZE = 100
NUM_CLONES = POPULATION_SIZE // 6
TOURNAMENT_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = 0.75
MUTATION_RATE = 0.2

GAME_OVER = "GAME OVER"

piece_dict = {
    "I": ["####N", "#N#N#N#N"],
    "O":["##N##N"],
    "T":["###N # N","# N##N# N"," # N###N"," #N##N #N"],
    "S":["## N ##N"," #N##N# N"],
    "Z":[" ##N## N","# N##N #N"],
    "J":["###N#  N","# N# N##N","  #N###N","##N #N #N"],
    "L":["###N  #N","##N# N# N","#  N###N"," #N #N##N"]
}

def eliminate_rows(board):
    elim_row_count = 0
    for x in range(HEIGHT):
        if board[x * WIDTH : x * WIDTH + 10] == "##########":
            board = "          " + board[: x * WIDTH] + board[x * WIDTH + WIDTH :]
            elim_row_count += 1
    if elim_row_count == 0:
        return board, 0
    elif elim_row_count == 1:
        return board, 40
    elif elim_row_count == 2:
        return board, 100
    elif elim_row_count == 3:
        return board, 300
    elif elim_row_count >= 4:
        return board, 1200

def place_piece_row(board, piece, col, last_row):
    # checks if edge is out
    if col + piece.index("N") > WIDTH:
        return GAME_OVER
    else:
        # finds the index to place the piece
        place_ind = last_row * WIDTH + col

        # go through all the orientations in the piece
        for orient in piece:
            # checks if it's out of column range
            if last_row < 0:
                return GAME_OVER
            
            # if it is a new line character
            if orient == "N":
                # then the last row is decreased by 1 because it goes to another line
                last_row = last_row - 1
                # change the place index based on that !
                place_ind = last_row * WIDTH + col
            # if where you want to place a piece is a # that is not good ! game is over
            # you literally don't have to check where else you want to put it (right now)
            # the code will do that later
            elif board[place_ind] == "#" and orient == "#":
                    return GAME_OVER
            # this means that the piece location is valid <3
            # place the piece block part not the whole thing
            else:
                if orient == "#":
                    board = board[0 : place_ind] + "#" + board[place_ind + 1:]
                # go up by 1 to continue placing pieces :)
                place_ind += 1

    # return the final board :)
    return board

def place_actual_piece(board, piece, col):
    # this is the best board case 
    # this is what you want.
    target_board = GAME_OVER
    # this checks the space between the possibly placed block and the top of the board
    for r in range(piece.count("N") - 1, HEIGHT):
        # places the piece according to the earlier method
        possible_location = place_piece_row(board, piece, col, r)
        # if it's game over, then return the current board
        if possible_location == GAME_OVER:
            return target_board
        # otherwise, you have the modified board
        else:
            target_board = possible_location

    # return the board at the very end
    return target_board

def print_board(board):
    if board == GAME_OVER:
        print(GAME_OVER)
    else:
        print("=======================")
        for count in range(20):
            print(' '.join(list(("|" + board[count * 10: (count + 1) * 10] + "|"))), " ", count)
        print("=======================")
        print()
        print("  0 1 2 3 4 5 6 7 8 9  ")
        print()

def play_game(strategy):
    board = " " * 200
    points = 0
    score_dict = {}
    while board != GAME_OVER:
        piece = list(random.choice(piece_dict.keys()))
        for orientation in piece:
            for col in range(11 - orientation.index("N")):
                poss_board = place_actual_piece(board, orientation, col)
                poss_score = heuristic(poss_board, strategy)
                score_dict[poss_score] = poss_board
        board = score_dict[max(score_dict.keys())]
        board, points_to_add = eliminate_rows(board)
        points += points_to_add
    return points

# TODO: write the heuristic
def heuristic(board, strategy):
    #come up with more variables
    ROW, EMPTY_SPACES = strategy
    if board == GAME_OVER:
        return -99999999
    value = 0
    return value

def fitness_function(strategy):
    game_scores_average = 0
    for count in range(5):
        game_scores_average += play_game(strategy)
    return (game_scores_average / 5)

def breeding(strategy, parent1, parent2):
    child = list(" " * 200)
    to_change = random.randint(1, len(strategy) - 1)
    indices_to_change = random.sample(range(1, len(strategy) - 1), to_change)
    for i in indices_to_change:
        child[i] = parent1[i]
    for x in child:
        if x not in indices_to_change:
            child[x] = parent2[x]
    
    if random.random() < MUTATION_RATE:
        return child
    else:
        return mutate(child)

def mutate(board):
    print("TODO")

'''
start_time = perf_counter()
print_board(board_input)
output_file = open("tetrisout.txt", "x")
output_list = []

# writing to file :)
for piece in piece_dict:
    for orientation in piece_dict[piece]:
        for c in range(11 - orientation.index("N")):
            to_print = place_actual_piece(board_input, orientation, c)
            to_print = eliminate_rows(to_print)[0]
            print_board(to_print)
            output_list.append(to_print)
            output_file.write(to_print)
            output_file.write("\n")

output_file.close()
print_board(board_input)
end_time = perf_counter()
print("Time taken: " + str(end_time - start_time))
'''
