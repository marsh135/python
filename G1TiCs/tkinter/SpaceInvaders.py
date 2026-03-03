import tkinter as tk

WIDTH = 600
HEIGHT = 450

CELL = 32
ROWS = 4
COLS = 8

root = tk.Tk()
root.title("Space Invaders - Tkinter")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# -----------------------------
# Sprite builders (no files)
# -----------------------------

def make_player_sprite():
    img = tk.PhotoImage(width=24, height=16)
    for y in range(16):
        for x in range(24):
            if 6 <= x <= 17 and y >= 6:
                img.put("lime", (x, y))
    return img

def make_enemy_sprite():
    # 11 x 8 classic alien shape
    pattern = [
        "00100000100",
        "00010001000",
        "00111111100",
        "01101111010",
        "11111111111",
        "10111111101",
        "10100000101",
        "00011011000"
    ]

    h = len(pattern)
    w = len(pattern[0])

    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("white", (x, y))

    return img

def make_bullet_sprite():
    img = tk.PhotoImage(width=4, height=10)
    for y in range(10):
        for x in range(4):
            img.put("yellow", (x, y))
    return img

player_img = make_player_sprite()
enemy_img = make_enemy_sprite()
bullet_img = make_bullet_sprite()

# -----------------------------
# Game state
# -----------------------------

player = None
enemies = []
bullets = []

enemy_dx = 4
alive = True

# -----------------------------
# Helpers
# -----------------------------

def overlap(a, b):
    ax1, ay1, ax2, ay2 = canvas.bbox(a)
    bx1, by1, bx2, by2 = canvas.bbox(b)
    return ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1

# -----------------------------
# Setup
# -----------------------------

def create_player():
    return canvas.create_image(
        WIDTH//2,
        HEIGHT - 40,
        image=player_img,
        anchor="center"
    )

def create_enemy_formation():
    enemies.clear()

    start_x = 100
    start_y = 60

    for r in range(ROWS):
        for c in range(COLS):
            x = start_x + c * CELL
            y = start_y + r * CELL

            e = canvas.create_image(
                x, y,
                image=enemy_img,
                anchor="nw"
            )
            enemies.append(e)

# -----------------------------
# Controls
# -----------------------------

def move_left(event):
    canvas.move(player, -15, 0)

def move_right(event):
    canvas.move(player, 15, 0)

def shoot(event):
    if len(bullets) > 0:
        return   # one bullet at a time (classic rule)

    px1, py1, px2, py2 = canvas.bbox(player)

    b = canvas.create_image(
        (px1 + px2)//2,
        py1,
        image=bullet_img,
        anchor="s"
    )

    bullets.append(b)

# -----------------------------
# Reset
# -----------------------------

def reset(event=None):
    global player, alive, enemy_dx

    canvas.delete("all")
    bullets.clear()
    alive = True
    enemy_dx = 4

    create_enemy_formation()
    start()

# -----------------------------
# Game loop
# -----------------------------

def move_enemies():
    global enemy_dx

    hit_wall = False

    for e in enemies:
        x1, y1, x2, y2 = canvas.bbox(e)

        if x2 >= WIDTH - 10 and enemy_dx > 0:
            hit_wall = True
        if x1 <= 10 and enemy_dx < 0:
            hit_wall = True

    if hit_wall:
        enemy_dx = -enemy_dx
        for e in enemies:
            canvas.move(e, 0, 15)
    else:
        for e in enemies:
            canvas.move(e, enemy_dx, 0)

def game_loop():
    global alive

    if not alive:
        canvas.create_text(
            WIDTH//2, HEIGHT//2,
            text="GAME OVER",
            fill="white",
            font=("Arial", 24)
        )
        canvas.create_text(
            WIDTH//2, HEIGHT//2 + 40,
            text="Press R to restart",
            fill="white"
        )
        return

    move_enemies()

    # move bullet
    for b in bullets[:]:
        canvas.move(b, 0, -12)

        x1, y1, x2, y2 = canvas.bbox(b)

        if y2 < 0:
            canvas.delete(b)
            bullets.remove(b)

    # bullet vs enemy
    for b in bullets[:]:
        for e in enemies[:]:
            if overlap(b, e):
                canvas.delete(b)
                canvas.delete(e)

                if b in bullets:
                    bullets.remove(b)
                if e in enemies:
                    enemies.remove(e)

                break

    # enemies reach player
    for e in enemies:
        ex1, ey1, ex2, ey2 = canvas.bbox(e)
        px1, py1, px2, py2 = canvas.bbox(player)

        if ey2 >= py1:
            alive = False

    root.after(40, game_loop)

# -----------------------------
# Start
# -----------------------------

def start():
    global player
    player = create_player()
    game_loop()

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<space>", shoot)
root.bind("r", reset)

reset()
root.mainloop()