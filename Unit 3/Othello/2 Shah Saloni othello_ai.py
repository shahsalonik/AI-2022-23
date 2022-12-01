import sys

directions = [-11, -10, -9, -1, 1, 9, 10, 11]

def game_over(board):
    if "." in board:
        return False
    return False

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
    
    return "TODO"

def min_step(board, opponent, depth):
    player = "xo"["ox".index(opponent)]

    if depth == 0:
        return score(board)
    
    children = []
    for child in possible_moves(board, "x"):
        new_board = make_move(board, "x", child)
        result = max_step(new_board, opponent, depth - 1)
        children.append(result)
    
    if len(children) == 0:
        return max_step(board, opponent, depth - 1)

    return min(children)
    
def max_step(board, opponent, depth):
    player = "xo"["ox".index(opponent)]

    if depth == 0:
        return score(board)

    children = []
    for child in possible_moves(board, "o"):
        new_board = make_move(board, "o", child)
        result = min_step(new_board, opponent, depth - 1)
        children.append(result)
    
    if len(children) == 0:
        return min_step(board, opponent, depth - 1)

    return max(children)

def min_move(board, depth):
    win_lose_check = 9999999
    min_index = -1
    for move in possible_moves(board, "o"):
        new_board = make_move(board, "o", move)
        result = max_step(new_board, depth)
        if result < win_lose_check:
            win_lose_check = result
            min_index = move
    return min_index

def max_move(board, depth):
    win_lose_check = -9999999
    max_index = -1
    for move in possible_moves(board, "x"):
        new_board = make_move(board, "x", move)
        result = min_step(new_board, depth)
        if result > win_lose_check:
            win_lose_check = result
            max_index = move
    return max_index

def find_next_move(board, player, depth):
    opponent = "xo"["ox".index(player)]
    for move in possible_moves(board, player):
        new_board = make_move(board, player, move)
        if player == "x":
            return max_move(new_board, depth) #min_step(new_board, opponent, depth - 1)
        elif player == "o":
            return min_move(new_board, opponent) #max_step(new_board, opponent, depth - 1)

#FOR OTHELLO RED
class Strategy():
    logging = True
    
    def best_strategy(self, board, player, best_move, still_running):
        depth = 1
        for count in range(board.count(".")):
            best_move.value = find_next_move(board, player, depth)
            depth += 1


#FOR OTHELLO BLUE
'''
board = sys.argv[1]
player = sys.argv[2]
depth = 1

for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all
   print(find_next_move(board, player, depth))
   depth += 1
'''