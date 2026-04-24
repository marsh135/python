import tkinter as tk

VIEW_SIZE = 400
WORLD_SIZE = 1200
PLAYER_SIZE = 30
STEP = 20

root = tk.Tk()
root.title("Scrolling Canvas Demo")

canvas = tk.Canvas(
    root,
    width=VIEW_SIZE,
    height=VIEW_SIZE,
    bg="white",
    scrollregion=(0, 0, WORLD_SIZE, WORLD_SIZE),
    highlightthickness=2,
    highlightbackground="black",
)
canvas.pack(padx=12, pady=12)

# Draw world
for line in range(0, WORLD_SIZE + 1, 100):
    canvas.create_line(line, 0, line, WORLD_SIZE, fill="#d9d9d9")
    canvas.create_line(0, line, WORLD_SIZE, line, fill="#d9d9d9")

canvas.create_rectangle(5, 5, WORLD_SIZE - 5, WORLD_SIZE - 5, outline="black", width=3)

start_x = VIEW_SIZE // 2
start_y = VIEW_SIZE // 2
player = canvas.create_rectangle(
    start_x,
    start_y,
    start_x + PLAYER_SIZE,
    start_y + PLAYER_SIZE,
    fill="royalblue",
    outline="black",
)


def center_view_on_player():
    x1, y1, x2, y2 = canvas.coords(player)
    player_center_x = (x1 + x2) / 2
    player_center_y = (y1 + y2) / 2

    max_offset = WORLD_SIZE - VIEW_SIZE
    left = min(max(player_center_x - VIEW_SIZE / 2, 0), max_offset)
    top = min(max(player_center_y - VIEW_SIZE / 2, 0), max_offset)

    canvas.xview_moveto(left / WORLD_SIZE)
    canvas.yview_moveto(top / WORLD_SIZE)


def move_player(dx, dy):
    x1, y1, x2, y2 = canvas.coords(player)

    if x1 + dx < 0:
        dx = -x1
    elif x2 + dx > WORLD_SIZE:
        dx = WORLD_SIZE - x2

    if y1 + dy < 0:
        dy = -y1
    elif y2 + dy > WORLD_SIZE:
        dy = WORLD_SIZE - y2

    canvas.move(player, dx, dy)
    center_view_on_player()


root.bind("<Left>", lambda event: move_player(-STEP, 0))
root.bind("<Right>", lambda event: move_player(STEP, 0))
root.bind("<Up>", lambda event: move_player(0, -STEP))
root.bind("<Down>", lambda event: move_player(0, STEP))

center_view_on_player()
canvas.focus_set()

root.mainloop()
