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

def possible_moves(board, token):
    board = convert_small_board(board)
    opponent = "xo"["ox".index(token)]
    possible_move_list = []

    for i, char in board:
        if char == token:
            for dir in directions:
                if board[i + dir] == opponent:
                    count = 2
                    while board[i + (dir * count)] == opponent:
                        end_index = i + (count * dir)
                        count += 1
                    if board[(end_index := (i + (count * dir)))]:
                        possible_move_list.append((i, end_index, dir))
                        
    return possible_move_list

def make_move(board, token, index):
    return "TODO"
