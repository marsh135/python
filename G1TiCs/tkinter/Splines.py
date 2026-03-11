import tkinter as tk
import math

WIDTH = 600
HEIGHT = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

enemy = canvas.create_oval(0, 0, 20, 20, fill="red")

# Bezier control points
P0 = (50, -50)
P1 = (300, 200)
P2 = (150, 400)

t = 0
running = False


def move_enemy():
    global t, running

    if not running:
        return
    """
    if t <= 1:
        x = (1-t)**2 * P0[0] + 2*(1-t)*t * P1[0] + t**2 * P2[0]
        y = (1-t)**2 * P0[1] + 2*(1-t)*t * P1[1] + t**2 * P2[1]

        canvas.coords(enemy, x, y, x+20, y+20)

        t += 0.02
        root.after(20, move_enemy)
    """
    if t <= 1:
        # Base position along the Bezier curve
        bx = (1-t)**2 * P0[0] + 2*(1-t)*t * P1[0] + t**2 * P2[0]
        by = (1-t)**2 * P0[1] + 2*(1-t)*t * P1[1] + t**2 * P2[1]

        # Spiral offset: increasing angle with decreasing radius
        angle = t * 10 * math.pi  # number of rotations
        radius = 80 * (1 - t)     # radius shrinks over time
        x = bx + radius * math.cos(angle)
        y = by + radius * math.sin(angle)

        canvas.coords(enemy, x, y, x+20, y+20)

        t += 0.005
        root.after(10, move_enemy)



def start():
    global running
    running = True
    move_enemy()


def restart():
    global t, running

    running = False
    t = 0

    # reset enemy position
    canvas.coords(enemy, P0[0], P0[1], P0[0]+20, P0[1]+20)

    running = True
    move_enemy()


start_button = tk.Button(root, text="Start", command=start)
start_button.pack()

restart_button = tk.Button(root, text="Restart", command=restart)
restart_button.pack()

root.mainloop()