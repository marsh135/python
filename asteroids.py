import random
from SimpleGraphics import *

UNIT = round(get_width() / 100, 0)
DELAY = 40

laser = None
dx = get_width() / 2  # starting x position for laser endpoint

def start():
    setup()
    timer.set_interval(game, DELAY)
    add_key_down_handler(left_right)

def setup():
    canvas.style.backgroundColor = '#000000'
    for i in range(100):
        rand_x = random.randint(1, 99)
        rand_y = random.randint(1, 110)
        star = Circle(1)
        star.set_position(UNIT * rand_x, UNIT * rand_y)
        star.set_color('#f5ffff')
        add(star)

    global laser
    laser = Line(get_width() / 2, get_height(), get_width() / 2, 0)
    laser.set_color('#800000')
    add(laser)

    add_asteroid()

def game():
    laser.set_endpoint(dx, 0)

def add_asteroid():
    rand_int = random.randint(1, 5)
    asteroid = Circle(UNIT * rand_int)
    asteroid.set_position(get_width() - UNIT * rand_int - 5, UNIT * rand_int + 5)
    asteroid.set_color('#B0C4DE')
    add(asteroid)

def left_right(event):
    global dx
    if event.key == "ArrowLeft":
        dx -= UNIT
    if event.key == "ArrowRight":
        dx += UNIT

start()