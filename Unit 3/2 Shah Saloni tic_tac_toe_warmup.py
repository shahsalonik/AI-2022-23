import sys

distinct_games = []
distinct_wins = set()
check_num = list()

#sys.argv[1]
board = sys.argv[1]

def game_over(board):
    for ind in range(0, 9, 3):
        check_solved = board[ind:ind + 3]
        if check_solved == "XXX":
            return 1, True
        if check_solved == "OOO":
            return -1, True
    for ind in range(0, 3):
        check_solved = board[ind] + board[ind + 3] + board[ind + 6]
        if check_solved == "XXX":
            return 1, True
        if check_solved == "OOO":
            return -1, True
    diagonal_1 = board[0] + board [4] + board [8]
    diagonal_2 = board[2] + board [4] + board [6]
    if diagonal_1 == "XXX" or diagonal_2 == "XXX":
        return 1, True
    if diagonal_1 == "OOO" or diagonal_2 == "OOO":
        return -1, True
    if "." not in board:
        return 0, True
    return None, False

def possible_next_boards(board, current_player):
    possible_boards = set()
    for i in range(9):
        if board[i] == ".":
            temp_board = board[0:i] + current_player + board[i+1:]
            possible_boards.add(temp_board)
    return possible_boards

def max_step(board):
    num, gameover = game_over(board)
    if gameover:
        distinct_games.append((num, board))
        return num
    results = []
    for next_board in possible_next_boards(board, "X"):
        results.append(min_step(next_board))
    return max(results)

def max_move(board, current_player):
    win_lose_check = -9999999
    max_index = -1
    index = 0
    for x in possible_next_boards(board, "X"):
        result = min_step(x)
        if result == -1:
            print("Moving at", index, "results in a loss.")
        elif result == 0:
            print("Moving at", index, "results in a tie.")
        else:
            print("Moving at", index, "results in a win.")
        if result > win_lose_check:
            win_lose_check = result
            max_index = index
        index += 1
    print()
    print("I choose space", max_index)
    print()
    board = board[0:max_index] + "X" + board[max_index + 1:]
    print_board(board)
    return board

def min_step(board):
    num, gameover = game_over(board)
    if gameover:
        distinct_games.append((num, board))
        return num
    results = []
    for next_board in possible_next_boards(board, "O"):
        results.append(max_step(next_board))
    return min(results)

def min_move(board):
    win_lose_check = -9999999
    min_index = -1
    index = 0
    for x in possible_next_boards(board, "X"):
        result = max_step(x)
        if result == -1:
            print("Moving at", index, "results in a win.")
        elif result == 0:
            print("Moving at", index, "results in a tie.")
        else:
            print("Moving at", index, "results in a loss.")
        if result < win_lose_check:
            win_lose_check = result
            min_index = index
        index += 1
    print()
    print("I choose space", min_index)
    print()
    board = board[0:min_index] + "O" + board[min_index + 1:]
    print_board(board)
    return board

def ai_turn(board):
    return "TODO"

def user_turn(board):
    return "TODO"

def print_board(board):
    for x in range(0, 9, 3):
        print(board[x:x + 3] + "\t" + str(x+1) + str(x+2) + str(x+3))

###INTERACTIVE PART###

num, gameover = game_over(board)

if gameover:
    winner = ""
    if num == 1:
        winner = "X won!"
    elif num == -1:
        winner = "O won!"
    else:
        winner = "We tied!"
    print("No moves possible!", winner)
elif board.count(".") == 9:
    print("Should I be X or O?")
    ai_player = input()
    print()
    if ai_player == "X":
        print("Current Board:")
        print_board(board)
    elif ai_player == "O":
        print("Current Board:")
        print_board(board)
    else:
        print("Sorry, please enter either X or O")
else:
    if board.count("X") % 2 == 0:
        #play as X
        print("X")
    else:
        #play as O
        print("O")
