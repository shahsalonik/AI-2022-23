import sys

directions = [-11, -10, -9, -1, 1, 9, 10, 11]

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