import tkinter as tk
import random

WIDTH = 400
HEIGHT = 300
PLAYER_SIZE = 30
BLOCK_SIZE = 20

root = tk.Tk()
root.title("Avoid the Blocks")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Player
player = canvas.create_rectangle(
    180, 250, 180 + PLAYER_SIZE, 250 + PLAYER_SIZE,
    fill="lime"
)

blocks = []
alive = True

# Movement
def move_left(event):
    canvas.move(player, -20, 0)

def move_right(event):
    canvas.move(player, 20, 0)

root.bind("a", move_left)
root.bind("d", move_right)

# Spawn blocks
def spawn_block():
    x = random.randint(0, WIDTH - BLOCK_SIZE)
    block = canvas.create_rectangle(
        x, 0, x + BLOCK_SIZE, BLOCK_SIZE,
        fill="red"
    )
    blocks.append(block)

# Game loop
def game_loop():
    global alive

    if not alive:
        canvas.create_text(
            WIDTH // 2, HEIGHT // 2,
            text="GAME OVER",
            fill="white",
            font=("Arial", 24)
        )
        return

    if random.randint(1, 20) == 1:
        spawn_block()

    for block in blocks:
        canvas.move(block, 0, 10)

        # Collision check
        if canvas.bbox(block) and canvas.bbox(player):
            bx1, by1, bx2, by2 = canvas.bbox(block)
            px1, py1, px2, py2 = canvas.bbox(player)

            if bx1 < px2 and bx2 > px1 and by1 < py2 and by2 > py1:
                alive = False

    root.after(50, game_loop)

game_loop()
root.mainloop()