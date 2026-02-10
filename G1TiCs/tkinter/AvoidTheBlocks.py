import tkinter as tk

import random

WIDTH = 400
HEIGHT = 300
PLAYER_SIZE = 30
BLOCK_SIZE = 20
multiplier = 1
score = 0
generate = 1
COLORS = ["red", "orange", "yellow", "purple", "cyan", "pink"]
root = tk.Tk()
root.title("Avoid the Blocks")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

root.geometry("400x400")

# Player
player = canvas.create_rectangle(
    180, 250, 180 + PLAYER_SIZE, 250 + PLAYER_SIZE,
    fill="lime"
)





blocks = []
bonuses = []
alive = True
def reset(event):
    global score, blocks, alive, player, canvas, bonuses, generate, multiplier
    canvas.delete("all")
    blocks = []
    bonuses = []
    generate = 1
    multiplier = 1
    alive =  True
    player = canvas.create_rectangle(
        180, 250, 180 + PLAYER_SIZE, 250 + PLAYER_SIZE,
        fill="lime" 
    )
    score = 0
    label.config(text=f"Score: {score}")
    game_loop()




# Movement
def move_left(event):
    px1, py1, px2, py2 = canvas.bbox(player)
    if px1<=0:
        canvas.move(player, WIDTH, 0)
    else:
        canvas.move(player, -20, 0)
    


def move_right(event):
    px1, py1, px2, py2 = canvas.bbox(player)
    if px2>=WIDTH:
        canvas.move(player, -WIDTH, 0)
    else:
        canvas.move(player, 20, 0)


#binds
root.bind("a", move_left)
root.bind("d", move_right)
root.bind("r", reset)
# Spawn blocks
def spawn_block():
    x = random.randint(0, WIDTH - BLOCK_SIZE)
    block = canvas.create_rectangle(
        x, 0, x + BLOCK_SIZE, BLOCK_SIZE,
        fill=random.choice(COLORS)
    )
    blocks.append(block)

def spawn_bonus():
    x = random.randint(0, WIDTH - BLOCK_SIZE)
    y=0
    size = 20
    bonus = canvas.create_oval(x,y, x+20, y+20, fill = "gold")
    bonuses.append(bonus)




label = tk.Label(root, text=score)
label.pack()
# Game loop
def game_loop():
    global score
    global alive, multiplier, generate
    label.config(text=f"Score: {score}   Multiplier: {multiplier}")


    if not alive:
        canvas.delete("all")
        canvas.create_text(
            WIDTH // 2, HEIGHT // 2,
            text="GAME OVER",
            fill="white",
            font=("Arial", 24)
        )
        canvas.create_text(
            WIDTH // 2, HEIGHT // 2 + 40,
            text="(r)estart",
            fill="white",
            font=("Arial", 14)
        )
        return
    if score > 20:
        generate+=1
    elif score > 50:
        generate+=2
    elif score > 100:
        generate +=10
    if random.randint(1, 20) == 1:
        for i in range(generate):
            spawn_block()
    if random.randint(1, 50) == 1:
        spawn_bonus()  
    for block in blocks[:]:
        canvas.move(block, 0, 10) #standard move
        
        ex1, ey1, ex2, ey2 = canvas.bbox(block)
        px1, py1, px2, py2 = canvas.bbox(player)
        

        if ey1 > HEIGHT:
            canvas.delete(block)
            blocks.remove(block)
            score = score+ (multiplier *1)
            label.config(text=f"Score: {score}   Multiplier: {multiplier}")
            continue
    
        if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
            alive = False
    for bonus in bonuses[:]:
        canvas.move(bonus, 0, 10) #standard move
        
        bx1, by1, bx2, by2 = canvas.bbox(bonus)
        px1, py1, px2, py2 = canvas.bbox(player)
        

        if by1 > HEIGHT:
            canvas.delete(bonus)
            bonuses.remove(bonus)
            label.config(text=f"Score: {score}   Multiplier: {multiplier}")

            continue
    
        if bx1 < px2 and bx2 > px1 and by1 < py2 and by2 > py1:
            multiplier +=1
            score+=5
            canvas.delete(bonus)
            bonuses.remove(bonus)

    root.after(50, game_loop)


game_loop()
root.mainloop()