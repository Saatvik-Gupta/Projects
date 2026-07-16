import tkinter as tk
from tkinter import messagebox

ROWS = 6
COLS = 7

board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
player = 1
root = tk.Tk()
root.title("Connect 4 Game using Python and Tkinter")
root.geometry("650x600")
root.configure(bg="lightblue")

cells = []

# Turn Label
turn = tk.Label(
    root,
    text="Player 1 Turn (Red)",
    font=("Arial", 16, "bold"),
    bg="lightgreen"
)
turn.pack(pady=10)


# Win Checking 
def check_win(p):

    # Horizontal
    for i in range(ROWS):
        for j in range(COLS - 3):
            if (board[i][j] == p and board[i][j+1] == p and
                board[i][j+2] == p and board[i][j+3] == p):
                return True

    # Vertical
    for i in range(ROWS - 3):
        for j in range(COLS):
            if (board[i][j] == p and board[i+1][j] == p and
                board[i+2][j] == p and board[i+3][j] == p):
                return True

    # Diagonal \
    for i in range(ROWS - 3):
        for j in range(COLS - 3):
            if (board[i][j] == p and board[i+1][j+1] == p and
                board[i+2][j+2] == p and board[i+3][j+3] == p):
                return True

    # Diagonal /
    for i in range(3, ROWS):
        for j in range(COLS - 3):
            if (board[i][j] == p and board[i-1][j+1] == p and
                board[i-2][j+2] == p and board[i-3][j+3] == p):
                return True

    return False


# Play Function 
def play(col):
    global player

    for row in range(ROWS - 1, -1, -1):

        if board[row][col] == 0:

            board[row][col] = player

            if player == 1:
                cells[row][col].config(bg="red")
            else:
                cells[row][col].config(bg="yellow")

            if check_win(player):
                messagebox.showinfo("Winner", f"Player {player} Wins!")
                root.destroy()
                return

            player = 2 if player == 1 else 1

            if player == 1:
                turn.config(text="Player 1 Turn (Red)")
            else:
                turn.config(text="Player 2 Turn (Yellow)")

            return

    messagebox.showwarning("Column Full", "This column is full!")


#  Game Board 
board_frame = tk.Frame(root, bg="blue")
board_frame.pack(expand=True)

for i in range(ROWS):

    row = []

    for j in range(COLS):

        label = tk.Label(
            board_frame,
            width=6,
            height=3,
            bg="white",
            relief="solid",
            borderwidth=2
        )

        label.grid(row=i, column=j, padx=3, pady=3)

        label.bind("<Button-1>", lambda event, col=j: play(col))

        row.append(label)

    cells.append(row)


# Footer 
footer = tk.Frame(root, bg="#1E1E1E")
footer.pack(side="bottom", fill="x")

tk.Label(
    footer,
    text="Built with Python & Tkinter",
    font=("Arial", 11),
    bg="#1E1E1E",
    fg="white"
).pack(pady=(8, 2))

tk.Label(
    footer,
    text="@InternPe Summer Internship (Python Programming)",
    font=("Arial", 11),
    bg="#1E1E1E",
    fg="white"
).pack()

tk.Label(
    footer,
    text="By: Saatvik Gupta (AIML Student)",
    font=("Arial", 11, "bold"),
    bg="#1E1E1E",
    fg="white"
).pack(pady=(2, 8))


root.mainloop()