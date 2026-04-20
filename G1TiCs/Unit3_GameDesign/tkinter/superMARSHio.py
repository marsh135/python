import tkinter as tk
import random

WIDTH, HEIGHT = 600, 400
PLAYER_SIZE = 30
GRAVITY = 1
JUMP = -15
SPEED = 5

root = tk.Tk()
root.title("Mini Side-Scroller")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="skyblue")
canvas.pack()

# Player
player = canvas.create_rectangle(50, HEIGHT-50-PLAYER_SIZE, 50+PLAYER_SIZE, HEIGHT-50, fill="red")
vy = 0
on_ground = False
score = 0

# Platforms
platforms = [
    canvas.create_rectangle(0, HEIGHT-20, WIDTH*2, HEIGHT, fill="green"),  # Ground
    canvas.create_rectangle(150, 300, 300, 320, fill="brown"),
    canvas.create_rectangle(400, 250, 550, 270, fill="brown"),
]

# Coins
coins = [
    canvas.create_oval(180, 270, 200, 290, fill="gold"),
    canvas.create_oval(450, 220, 470, 240, fill="gold")
]

# Enemies
enemies = [
    {"id": canvas.create_rectangle(200, 280, 230, 310, fill="purple"), "dir": 2, "range": (150, 300)},
    {"id": canvas.create_rectangle(420, 230, 450, 260, fill="purple"), "dir": 3, "range": (400, 550)},
]

# Input
keys = {"left": False, "right": False, "jump": False}

def key_press(event):
    if event.keysym.lower() == "a":
        keys["left"] = True
    elif event.keysym.lower() == "d":
        keys["right"] = True
    elif event.keysym.lower() == "w":
        keys["jump"] = True

def key_release(event):
    if event.keysym.lower() == "a":
        keys["left"] = False
    elif event.keysym.lower() == "d":
        keys["right"] = False
    elif event.keysym.lower() == "w":
        keys["jump"] = False

root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

# Game loop
def game_loop():
    global vy, on_ground, score

    px1, py1, px2, py2 = canvas.bbox(player)

    # Horizontal movement
    if keys["left"]:
        if px1 > WIDTH//3:  # Player moves left until center
            canvas.move(player, -SPEED, 0)
        else:  # Scroll world right
            for plat in platforms:
                canvas.move(plat, SPEED, 0)
            for c in coins:
                canvas.move(c, SPEED, 0)
            for e in enemies:
                canvas.move(e["id"], SPEED, 0)

    if keys["right"]:
        if px2 < WIDTH*2//3:  # Player moves right until center
            canvas.move(player, SPEED, 0)
        else:  # Scroll world left
            for plat in platforms:
                canvas.move(plat, -SPEED, 0)
            for c in coins:
                canvas.move(c, -SPEED, 0)
            for e in enemies:
                canvas.move(e["id"], -SPEED, 0)

    # Jump
    if keys["jump"] and on_ground:
        vy = JUMP
        on_ground = False

    # Gravity
    vy += GRAVITY
    canvas.move(player, 0, vy)

    # Collision with platforms
    px1, py1, px2, py2 = canvas.bbox(player)
    on_ground = False
    for plat in platforms:
        x1, y1, x2, y2 = canvas.bbox(plat)
        if px2 > x1 and px1 < x2 and py2 > y1 and py1 < y2:
            if vy > 0:  # falling
                canvas.move(player, 0, y1 - py2)
                vy = 0
                on_ground = True

    # Collect coins
    for coin in coins[:]:
        cx1, cy1, cx2, cy2 = canvas.bbox(coin)
        if px2 > cx1 and px1 < cx2 and py2 > cy1 and py1 < cy2:
            canvas.delete(coin)
            coins.remove(coin)
            score += 1
            print("Score:", score)

    # Move enemies
    for e in enemies:
        canvas.move(e["id"], e["dir"], 0)
        ex1, ey1, ex2, ey2 = canvas.bbox(e["id"])
        r1, r2 = e["range"]
        if ex1 < r1 or ex2 > r2:
            e["dir"] *= -1  # Reverse direction

        # Collision with player
        if px2 > ex1 and px1 < ex2 and py2 > ey1 and py1 < ey2:
            print("GAME OVER! Final score:", score)
            return  # Stop the game loop

    root.after(20, game_loop)

game_loop()
root.mainloop()