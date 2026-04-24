import tkinter as tk

VIEW_SIZE = 400      # Size of the visible canvas area
WORLD_SIZE = 1200    # Size of the full world
PLAYER_SIZE = 30     # Size of the player square
STEP = 20            # Distance moved per key press

root = tk.Tk()
root.title("Scrolling Canvas Demo")

canvas = tk.Canvas(
    root,
    width=VIEW_SIZE,
    height=VIEW_SIZE,
    bg="white",
    scrollregion=(0, 0, WORLD_SIZE, WORLD_SIZE),  # Full scrollable area
    highlightthickness=2,                         # Border thickness around the canvas
    highlightbackground="black",                  # Border color
)
canvas.pack(padx=150, pady=150)

# Draw a grid so movement is easier to see
for line in range(0, WORLD_SIZE + 1, 100):
    canvas.create_line(line, 0, line, WORLD_SIZE, fill="#d9d9d9")
    canvas.create_line(0, line, WORLD_SIZE, line, fill="#d9d9d9")

# Draw the outer border of the world
canvas.create_rectangle(
    5, 5, WORLD_SIZE - 5, WORLD_SIZE - 5,
    outline="black",
    width=3
)

# Start the player near the middle of the visible area
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
    """Scroll the canvas so the player stays centered when possible."""
    x1, y1, x2, y2 = canvas.coords(player)
    player_center_x = (x1 + x2) / 2
    player_center_y = (y1 + y2) / 2

    # Prevent the viewport from scrolling past the world edges
    max_offset = WORLD_SIZE - VIEW_SIZE
    left = min(max(player_center_x - VIEW_SIZE / 2, 0), max_offset)
    top = min(max(player_center_y - VIEW_SIZE / 2, 0), max_offset)

    canvas.xview_moveto(left / WORLD_SIZE)
    canvas.yview_moveto(top / WORLD_SIZE)


def move_player(dx, dy):
    """Move the player, keeping it inside the world boundaries."""
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


# Arrow keys move the player
root.bind("<Left>", lambda _event: move_player(-STEP, 0))
root.bind("<Right>", lambda _event: move_player(STEP, 0))
root.bind("<Up>", lambda _event: move_player(0, -STEP))
root.bind("<Down>", lambda _event: move_player(0, STEP))

center_view_on_player()
canvas.focus_set()

root.mainloop()
