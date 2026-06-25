import random

board = ['-','-','-',
         '-','-','-',
         '-','-','-']

currentplayer = "X"
gamerun = True
winner = None


# Print board
def printing_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# Player input
def player_input(board):
    global currentplayer
    while True:
        play_inp = int(input("Choose a number from 1 to 9: "))

        if 1 <= play_inp <= 9 and board[play_inp - 1] == "-":
            board[play_inp - 1] = currentplayer
            break
        else:
            print("Invalid move! Try again.")


# Win conditions
def check_win_conditions(board):
    global winner

    # Horizontal
    if board[0]==board[1]==board[2] and board[0] != "-":
        winner = board[0]; return True
    if board[3]==board[4]==board[5] and board[3] != "-":
        winner = board[3]; return True
    if board[6]==board[7]==board[8] and board[6] != "-":
        winner = board[6]; return True

    # Vertical
    if board[0]==board[3]==board[6] and board[0] != "-":
        winner = board[0]; return True
    if board[1]==board[4]==board[7] and board[1] != "-":
        winner = board[1]; return True
    if board[2]==board[5]==board[8] and board[2] != "-":
        winner = board[2]; return True

    # Diagonal
    if board[0]==board[4]==board[8] and board[0] != "-":
        winner = board[0]; return True
    if board[2]==board[4]==board[6] and board[2] != "-":
        winner = board[2]; return True

    return False


# Check win
def check_win():
    global gamerun

    if check_win_conditions(board):
        print(f"The Winner is {winner}")
        gamerun = False


# Tie check
def tie(board):
    global gamerun

    if "-" not in board and gamerun:
        printing_board(board)
        print("It's a tie!")
        gamerun = False


# Switch player
def switch_player():
    global currentplayer
    currentplayer = "O" if currentplayer == "X" else "X"


# Computer move
def computer(board):
    global currentplayer

    if currentplayer == "O":
        while True:
            pos = random.randint(0, 8)
            if board[pos] == "-":
                board[pos] = "O"
                break

        switch_player()


# MAIN GAME LOOP
while gamerun:
    printing_board(board)

    player_input(board)
    check_win()
    tie(board)
    if not gamerun: # Someone i.e either player or computer won
        break

    switch_player()

    computer(board)
    check_win()
    tie(board)