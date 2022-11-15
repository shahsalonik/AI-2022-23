import sys

distinct_games = []
distinct_wins = set()
check_num = list()

#sys.argv[1]
board = "........."
print(board)

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

def min_step(board):
    num, gameover = game_over(board)
    if gameover:
        distinct_games.append((num, board))
        return num
    results = []
    for next_board in possible_next_boards(board, "O"):
        results.append(max_step(next_board))
    return min(results)

max_step(board)

print("Total number of distinct games:", len(distinct_games))
distinct_wins = set(distinct_games)
print("Total number of distinct wins:", len(distinct_wins))
print()

draw_count = 0
five_count = 0
seven_count = 0
nine_count = 0

six_count = 0
eight_count = 0

for x in distinct_wins:
    winner, board = x 
    if winner == 0:
        draw_count += 1
    if (board.count("X") + board.count("O") == 5) and winner == 1:
        five_count += 1
    elif (board.count("X") + board.count("O") == 7) and winner == 1:
        seven_count += 1
    elif (board.count("X") + board.count("O") == 9) and winner == 1:
        nine_count += 1
    elif (board.count("X") + board.count("O") == 6) and winner == -1:
        six_count += 1
    if (board.count("X") + board.count("O") == 8) and winner == -1:
        eight_count += 1

print("Draw:", draw_count)
print("X in 5:", five_count)
print("X in 7:", seven_count)
print("X in 9:", nine_count)

print("O in 6:", six_count)
print("O in 8:", eight_count)
