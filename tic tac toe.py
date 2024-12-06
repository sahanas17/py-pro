board  = [" " for x in range(9) ] #initialises a list containing 9 spaces represeting the 9 spaces on the tic tac toe board
def print_board():
    #used to print the board
    row1 = "|{:<10}|{:^10}|{:>10}|".format(board[0], board[1], board[2])
    row2 = "|{:<10}|{:^10}|{:>10}|".format(board[3], board[4], board[5])
    row3 = "|{:<10}|{:^10}|{:>10}|".format(board[6], board[7], board[8]) #The format() function in Python is a string method that allows you to format strings by inserting variables or expressions into placeholders {} within the string.
    print("Tic Tac Toe")
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == "X":
        number = 1 #decides which player has to play based on the icon
    elif icon == "O":
        number = 2
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move(1-9): ").strip()) #strip function used to remove any additional white spaces at the end or beginning of the entered choice
    if board[choice-1] == " ": #if space is empty
        board[choice-1] = icon #choice-1 since numbering of board starts from 1 not 0
    else: #if space is not empty
        print()
        print("Space is already taken!")

def is_victory(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or\
    (board[3] == icon and board[4] == icon and board[5] == icon) or\
    (board[6] == icon and board[7] == icon and board[8] == icon) or\
    (board[0] == icon and board[3] == icon and board[6] == icon) or\
    (board[1] == icon and board[4] == icon and board[7] == icon) or\
    (board[2] == icon and board[5] == icon and board[8] == icon) or\
    (board[0] == icon and board[4] == icon and board[8] == icon) or\
    (board[2] == icon and board[4] == icon and board[6] == icon) :
        return True
    else:
        return False

#to check if game is a draw, checks if all spaces are filled
def is_draw():
    if " " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print("O wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    
