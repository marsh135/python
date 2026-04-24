import tkinter as tk

VIEW_SIZE = 400  #size of the viewport
WORLD_SIZE = 1200 #size of the world
PLAYER_SIZE = 30 # size of the player
STEP = 20 #how much player moves per button press

root = tk.Tk()  #standard tk
root.title("Scrolling Canvas Demo") #lipstick

canvas = tk.Canvas(
    root,  #target
    width=VIEW_SIZE,  #size of the frame
    height=VIEW_SIZE,  # ""
    bg="white", # set bg color
    scrollregion=(0, 0, WORLD_SIZE, WORLD_SIZE), #set canvas extents, 0,0 -> 1200, 1200
    highlightthickness=2, # I actually have no idea
    highlightbackground="black", # edge boundary color
)
canvas.pack(padx=150, pady=150)  #border on the actual window

# Draw world
for line in range(0, WORLD_SIZE + 1, 100):  #draw a line ever4y 100 px jsut to show the canvas  "moving"
    canvas.create_line(line, 0, line, WORLD_SIZE, fill="#d9d9d9")  # one is horizontal
    canvas.create_line(0, line, WORLD_SIZE, line, fill="#d9d9d9") # one is vertical

canvas.create_rectangle(5, 5, WORLD_SIZE - 5, WORLD_SIZE - 5, outline="black", width=3) # this is the border on the world.  higher = thicker

start_x = VIEW_SIZE // 2  #start in the middle
start_y = VIEW_SIZE // 2 # start in the middle
player = canvas.create_rectangle(  # make our player - this is boiler plate
    start_x,  #600
    start_y, #600
    start_x + PLAYER_SIZE, #630
    start_y + PLAYER_SIZE, #630
    fill="royalblue",  #color
    outline="black", # outline color
)


def center_view_on_player():
    x1, y1, x2, y2 = canvas.coords(player)  #center the coords that the player starts at
    player_center_x = (x1 + x2) / 2
    player_center_y = (y1 + y2) / 2

    max_offset = WORLD_SIZE - VIEW_SIZE  #keeps the frame in view - essentially, makes sure that you always ahve the frame filled with world context
    left = min(max(player_center_x - VIEW_SIZE / 2, 0), max_offset)
    top = min(max(player_center_y - VIEW_SIZE / 2, 0), max_offset)

    canvas.xview_moveto(left / WORLD_SIZE)  #move the canvas
    canvas.yview_moveto(top / WORLD_SIZE) # move the canvas


def move_player(dx, dy): #move the player
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


root.bind("<Left>", lambda event: move_player(-STEP, 0)) # AH - LAMBDA Functions
root.bind("<Right>", lambda event: move_player(STEP, 0)) # A lambda funciton is a "ghost" or "phantom"
root.bind("<Up>", lambda event: move_player(0, -STEP)) # funciton - basically, a fucntion taht you do not think you will ever
root.bind("<Down>", lambda event: move_player(0, STEP)) # need again, but it allows you to ask a question and get an answer

center_view_on_player()
canvas.focus_set()

root.mainloop()
