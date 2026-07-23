import tkinter as tk
import random

# ---------------- Window ----------------
root = tk.Tk()
root.title("Ping Pong Game")
root.configure(bg="black")
root.resizable(False, False)

WIDTH = 700
HEIGHT = 400

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
                   bg="black", highlightthickness=0)
canvas.pack()

# ---------------- Score ----------------
left_score = 0
right_score = 0

score = canvas.create_text(
    WIDTH//2,
    25,
    text="0 : 0",
    fill="white",
    font=("Arial", 22, "bold")
)

# Center Line
canvas.create_line(
    WIDTH//2, 0,
    WIDTH//2, HEIGHT,
    fill="gray",
    dash=(6, 6)
)

# ---------------- Paddles ----------------
left = canvas.create_rectangle(
    20, 150, 35, 250,
    fill="white",
    outline="white"
)

right = canvas.create_rectangle(
    665, 150, 680, 250,
    fill="white",
    outline="white"
)

# ---------------- Ball ----------------
ball = canvas.create_oval(
    340, 190, 360, 210,
    fill="white",
    outline="white"
)

# Ball speed (Normal)
dx = random.choice([-5, 5])
dy = random.choice([-5, 5])

PADDLE_SPEED = 25

# ---------------- Paddle Controls ----------------
def left_up(event):
    x1, y1, x2, y2 = canvas.coords(left)
    if y1 > 0:
        canvas.move(left, 0, -PADDLE_SPEED)

def left_down(event):
    x1, y1, x2, y2 = canvas.coords(left)
    if y2 < HEIGHT:
        canvas.move(left, 0, PADDLE_SPEED)

def right_up(event):
    x1, y1, x2, y2 = canvas.coords(right)
    if y1 > 0:
        canvas.move(right, 0, -PADDLE_SPEED)

def right_down(event):
    x1, y1, x2, y2 = canvas.coords(right)
    if y2 < HEIGHT:
        canvas.move(right, 0, PADDLE_SPEED)

# Controls
root.bind("<w>", left_up)
root.bind("<s>", left_down)

root.bind("<Up>", right_up)
root.bind("<Down>", right_down)

# ---------------- Reset Ball ----------------
def reset_ball():
    global dx, dy

    canvas.coords(ball, 340, 190, 360, 210)

    dx = random.choice([-5, 5])
    dy = random.choice([-5, 5])

# ---------------- Game Loop ----------------
def move_ball():
    global dx, dy, left_score, right_score

    canvas.move(ball, dx, dy)

    x1, y1, x2, y2 = canvas.coords(ball)

    # Top & Bottom Wall
    if y1 <= 0 or y2 >= HEIGHT:
        dy = -dy

    # Left Paddle Collision
    lx1, ly1, lx2, ly2 = canvas.coords(left)

    if x1 <= lx2 and y2 >= ly1 and y1 <= ly2 and dx < 0:
        dx = -dx

    # Right Paddle Collision
    rx1, ry1, rx2, ry2 = canvas.coords(right)

    if x2 >= rx1 and y2 >= ry1 and y1 <= ry2 and dx > 0:
        dx = -dx

    # Right Player Scores
    if x1 <= 0:
        right_score += 1
        canvas.itemconfig(score, text=f"{left_score} : {right_score}")
        reset_ball()

    # Left Player Scores
    if x2 >= WIDTH:
        left_score += 1
        canvas.itemconfig(score, text=f"{left_score} : {right_score}")
        reset_ball()

    root.after(12, move_ball)

move_ball()

# ---------------- Footer ----------------
footer = tk.Frame(root, bg="black")
footer.pack(pady=10)

tk.Label(
    footer,
    text="Built with Python & Tkinter",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="black"
).pack()

tk.Label(
    footer,
    text="@InternPe Summer Internship (Python Programming)",
    font=("Arial", 10),
    fg="deepskyblue",
    bg="black"
).pack()

tk.Label(
    footer,
    text="Developed by Saatvik Gupta (AIML Student)",
    font=("Arial", 10),
    fg="gray",
    bg="black"
).pack()

root.mainloop()