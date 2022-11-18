import sys

distinct_games = []
distinct_wins = set()
check_num = list()

#sys.argv[1]
board = "........."

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
    possible_boards_dict = dict()
    for i in range(9):
        if board[i] == ".":
            temp_board = board[0:i] + current_player + board[i+1:]
            possible_boards.add(temp_board)
            possible_boards_dict[i] = temp_board
    return possible_boards, possible_boards_dict

def max_step(board):
    num, gameover = game_over(board)
    if gameover:
        return num
    results = []
    possible_set, possible_dict = possible_next_boards(board, "X")
    for next_board in possible_set:
        results.append(min_step(next_board))
    return max(results)

def max_move(board):
    win_lose_check = -9999999
    max_index = -1
    possible_set, possible_dict = possible_next_boards(board, "X")
    print()
    for key, val in possible_dict.items():
        result = min_step(val)
        if result == -1:
            print("Moving at", key, "results in a loss.")
        elif result == 0:
            print("Moving at", key, "results in a tie.")
        else:
            print("Moving at", key, "results in a win.")
        if result > win_lose_check:
            win_lose_check = result
            max_index = key
    print()
    print("I choose space", max_index)
    print()
    board = board[0:max_index] + "X" + board[max_index + 1:]
    print_board(board)
    return board

def min_step(board):
    num, gameover = game_over(board)
    if gameover:
        return num
    results = []
    possible_set, possible_dict = possible_next_boards(board, "O")
    for next_board in possible_set:
        results.append(max_step(next_board))
    return min(results)

def min_move(board):
    win_lose_check = 9999999
    min_index = -1
    possible_set, possible_dict = possible_next_boards(board, "O")
    print()
    for key, val in possible_dict.items():
        result = max_step(val)
        if result == -1:
            print("Moving at", key, "results in a win.")
        elif result == 0:
            print("Moving at", key, "results in a tie.")
        else:
            print("Moving at", key, "results in a loss.")
        if result < win_lose_check:
            win_lose_check = result
            min_index = key
    print()
    print("I choose space", min_index)
    print()
    board = board[0:min_index] + "O" + board[min_index + 1:]
    print_board(board)
    return board

def ai_turn(board):
    num, gameover = game_over(board)
    if gameover:
        return num, board
    start_state = ""
    if ai_player == "X":
        start_state = max_move(board)
    else:
        start_state = min_move(board)
    return user_turn(start_state)

def user_turn(board):
    num, gameover = game_over(board)
    if gameover:
        return num, board
    option_string = ""
    for y in range(9):
        if board[y] == ".":
            option_string += str(y) + ", "
    print()
    print("You can move to any of these spaces: " + option_string)
    print("Your choice?")
    move = input()
    board = board[0:int(move)] + user + board[int(move) + 1:]
    print_board(board)
    return ai_turn(board)

def print_board(board):
    for x in range(0, 9, 3):
        print(board[x:x + 3] + "\t" + str(x) + str(x+1) + str(x+2))

###INTERACTIVE PART###

num, gameover = game_over(board)
ai_player = ""
user = ""

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
        user = "O"
        result, final_board = ai_turn(board)
    elif ai_player == "O":
        print("Current Board:")
        print_board(board)
        user = "X"
        result, final_board = user_turn(board)
    else:
        print("Sorry, please enter either X or O")
    print()
    if (result == 1 and ai_player == "X") or (result == -1 and ai_player == "O"):
        winner = "I win!"
    elif (result == 1 and user == "X") or (result == -1 and user == "O"):
        winner = " You win!"
    else:
        winner = "We tied!"
    print(winner) 
else:
    if board.count("X") % 2 == 0:
        ai_player = "X"
        user = "O"
    else:
        user = "X"
        ai_player = "O"

winner = ""
