import sys

#              0    1    2   3  4  5  6   7
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
    row = index // 10
    col = index % 10
    return (row - 1) * 8 + (col - 1)

def convert_eight_to_ten(index):
    row = index // 8
    col = index % 8
    return (row + 1) * 10 + (col + 1)

#I THINK:
#issue rn is that it's taking the index of the big board with the question marks
#need to figure out how to do the small board
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

    for char in range(len(board)):
        if board_list[char] == token:
            for dir in directions:
                if board_list[char + dir] == opponent:
                    count = 2
                    while char + (count * dir) != index and board[char + (count * dir)] == opponent:
                        board_list[char + (count * dir)] = token
    
    return ''.join(board_list)
