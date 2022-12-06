import sys
from time import perf_counter
import time

directions = [-11, -10, -9, -1, 1, 9, 10, 11]

def game_over(board):
    if "." in board or (len(possible_moves(board, "x")) == 0 and len(possible_moves(board, "o")) == 0):
        return False
    return True

def convert_small_board(board):
    new_board_string = "??????????"
    for x in range(0, len(board), 8):
        new_board_string += "?" + board[x:x+8] + "?"
    new_board_string += "??????????"
    return new_board_string

def convert_big_board(board):
    return board.replace("?", "")

#convert index 10 -> 8 and 8 -> 10
def convert_ten_to_eight(index):
    index = int(index)
    row = index // 10
    col = index % 10
    return (row - 1) * 8 + (col - 1)

def convert_eight_to_ten(index):
    index = int(index)
    row = index // 8
    col = index % 8
    return (row + 1) * 10 + (col + 1)

def possible_moves(board, token):
    board = convert_small_board(board)
    opponent = "xo"["ox".index(token)]
    possible_move_list = set()
    
    for char in range(len(board)):
        if board[char] == token:
            for dir in directions:
                if board[char + dir] == opponent:
                    count = 2
                    while board[char + (count * dir)] == opponent:
                        index2 = char + (count * dir)
                        count += 1
                    index2 = char + (count * dir)
                    if board[index2] == ".":
                        possible_move_list.add(convert_ten_to_eight(index2))
    
    return list(possible_move_list)

def make_move(board, token, index):
    board = convert_small_board(board)
    index = convert_eight_to_ten(index)
    opponent = "xo"["ox".index(token)]
    board_list = [*board]
    flip_set = set()
    
    for dir in directions:
        if board_list[index + dir] == opponent:
            count = 1
            temp_flip_set = set()
            temp_flip_set.add(index + dir)
            while board_list[index + (count * dir)] == opponent:
                temp_flip_set.add(index + (count * dir))
                count += 1
            if board_list[index] == ".":
                temp_flip_set.add(index)
            if board_list[index + (count * dir)] == token:
                for i in temp_flip_set:
                    flip_set.add(i)

    for coin in flip_set:
        board_list[coin] = token
    
    return convert_big_board(''.join(board_list))

def score(board):
    score = 0
    x = "x"
    o = "o"

    score += 20 * (board.count(x)) - (board.count(o))
    corner_list = [board[0], board[7], board[56], board[63]]
    for corner in corner_list:
        if corner == x:
            score += 20
        elif corner == o:
            score -= 20
    
    score += 15 * (len(possible_moves(board, x)) - len(possible_moves(board, o)))

    if "." not in board:
        x_count = board.count(x)
        if x_count < 33:
            score += 1000000 + x_count
        elif x_count > 33:
            score += 1000000 - x_count

    return score

def mid_game(board):
    if board.count(".") < 12:
        score(board)
    
    mid_score = 0
    x = "x"
    o = "o"
    corner_list = [board[0], board[7], board[56], board[63]]

    for corner in corner_list:
        if corner == x:
            mid_score += 40
        elif corner == o:
            mid_score -= 40
    
    mid_score += 20 * (len(possible_moves(board, x)) - len(possible_moves(board, o)))
    mid_score += (board.count(x) - board.count(o))

    edge_list = [board[1], board[8], board[9], board[6], board[14], board[15],board[48], board[49], board[57], board[54], board[55], board[62]]
    mid_score += 2 * edge_list.count(o)
    mid_score += 2 * edge_list.count(x)

    return mid_score

def min_step(board, opponent, depth):
    if depth == 0 or game_over(board):
        return mid_game(board)
    
    children = []
    for child in possible_moves(board, "x"):
        new_board = make_move(board, "x", child)
        result = max_step(new_board, opponent, depth - 1)
        children.append(result)
    
    if len(children) == 0:
        return max_step(board, opponent, depth - 1)

    return min(children)
    
def max_step(board, opponent, depth):
    if depth == 0 or game_over(board):
        return mid_game(board)

    children = []
    for child in possible_moves(board, "o"):
        new_board = make_move(board, "o", child)
        result = min_step(new_board, opponent, depth - 1)
        children.append(result)
    
    if len(children) == 0:
        return min_step(board, opponent, depth - 1)

    return max(children)

'''
def min_move(board, depth):
    win_lose_check = 9999999
    min_index = -1
    for move in possible_moves(board, "o"):
        new_board = make_move(board, "o", move)
        result = max_step(new_board, "x", depth)
        if result < win_lose_check:
            win_lose_check = result
            min_index = move
    return min_index

def max_move(board, depth):
    win_lose_check = -9999999
    max_index = -1
    for move in possible_moves(board, "x"):
        new_board = make_move(board, "x", move)
        result = min_step(new_board, "o", depth)
        if result > win_lose_check:
            win_lose_check = result
            max_index = move
    return max_index
'''

def find_next_move(board, player, depth):
    for move in possible_moves(board, player):
        new_board = make_move(board, player, move)
        if player == "x":
            return min_step(new_board, "o", depth - 1) #min_step(new_board, opponent, depth - 1)
        elif player == "o":
            return max_step(new_board, "x", depth - 1) #max_step(new_board, opponent, depth - 1)

#FOR OTHELLO RED
'''
class Strategy():
    logging = True
    
    def best_strategy(self, board, player, best_move, still_running):
        depth = 1
        for count in range(board.count(".")):
            best_move.value = find_next_move(board, player, depth)
            depth += 1
'''

#FOR OTHELLO BLUE


board = sys.argv[1]
player = sys.argv[2]
#board = "...........................ox......xo..........................."
#player = "x"
depth = 1

for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all
   print(find_next_move(board, player, depth))
   depth += 1


'''
results = []
with open("Unit 3/Othello/boards_timing.txt") as f:
    for line in f:
        board, token = line.strip().split()
        temp_list = [board, token]
        print(temp_list)
        for count in range(1, 7):
            start = time.perf_counter()
            find_next_move(board, token, count)
            end = time.perf_counter()
            temp_list.append(str(end - start))
            print("depth", count)
        print(temp_list)
        print()
        results.append(temp_list)
'''

'''
with open("Unit 3/Othello/boards_timing_my_results.csv", "w") as g:
    for l in results:
        g.write(", ".join(1) + "\n")
'''