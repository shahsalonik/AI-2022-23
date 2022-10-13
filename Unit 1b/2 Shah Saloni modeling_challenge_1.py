#use get children whether the cube can move
#use blank index to find where the cube is and see which way it can move

#cube has front, back, top, bottom, left, and right
#when it moves, bottom of the cube swaps with current tile.
    #if current tile is empty, bottom face is also empty
    #if current tile is blue, bottom face turns blue
#swaps in a loop
    #if swapping up: top --> back --> bottom --> front --> top

#new index of the cube is the current position - size

from curses.panel import top_panel


filename = "cube_puzzles.txt"

with open(filename) as f:
    line_list = [line.strip() for line in f]

def print_board(state):
    size, board, cube = state.split()
    size = int(size)

    for x in range(0, len(board), size):
        print(board[x : x + size])

def find_goal(state):
    size, board, cube = state.split()
    if cube == {1, 1, 1, 1, 1, 1}:
        return True
    return False    

def swap(board, cube_index, swap_index, cube):
    new_cube_index = swap_index
    board2 = ""

    for x in range(len(board)):
        if x == cube_index:
            board2 += board[swap_index]
        elif x == swap_index:
            board2 += board[cube_index]
        else:
            board2 += board[x]
    return board2, new_cube_index, cube

def is_swappable(state):
    size, board, cube = state.split()
    size = int(size)
    cube_index = int(cube)
    top, bottom, left, right, front, back = cube[0], cube[1], cube[2], cube[3], cube[4], cube[5]
    children = []
    if cube_index % size != 0: #blank swap right
        new_cube = (right, left, top, bottom, front, back)
        children.append(swap(board, cube_index, cube_index + 1, new_cube))
    if (cube_index + 1) % size != 0: #blank swap lefts
        new_cube = (left, right, bottom, top, front, back)
        children.append(swap(board, cube_index, cube_index - 1, new_cube))
    if cube_index >= size: #blank swap up
        new_cube = (front, back, left, right, bottom, top)
        children.append(swap(board, cube_index, cube_index - size, new_cube))
    if cube_index < (size * (size - 1)): #blank swap down
        new_cube = (back, front, left, right, top, bottom)
        children.append(swap(board, cube_index, cube_index + size, new_cube))
    return children

def pls_do(to_do):
    moves = 0
        goal = find_goal(state)
        size, state = state.split()
        size = int(size)
        for x in range(len(state)):
            if not state[x] == ".":
                x_point = goal.find(state[x]) // size
                y_point = goal.find(state[x]) % size
                x_distance = abs(x_point - x // size)
                y_distance = abs(y_point - x % size)
                moves += x_distance + y_distance
        return moves

def taxicab(state):
    #check how many moves it takes to cover all the blue squares (dont pay attention to side)
    #check which blue square is closest and keep repeating until no blue squares left
        #maybe do normal taxicab? and keep doing it until all @s are .s
    
    size, board, cube = state.split()
    board_list = [*board]
    board_set = set(board_list)
    moves = 0
    size = int(size)
    cube = int(cube)

    while "@" in board_set:
        for x in range(len(board)):
            if x != cube:

    return bruh



    print("TODO")

def a_star(state):
    print("TODO")

for x in line_list:
    size, board, cube, link = x.split()
    game = size + " " + board + " " + cube
    print_board(game)
    print("\n")
