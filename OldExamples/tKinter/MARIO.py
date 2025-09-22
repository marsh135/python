#MARIO

def move_right():
    #move right code
    print("moving right")

def move_left():
    #move_left
    print("moving left")

def jump():
    #jump code
    print("jumping")

def duck():
    #duck code
    print("ducking")

while True:
    controller =  input()

    while controller == "d":
        move_right()
    while controller == "a":
        move_left()
    while controller == "w":
        jump()
    while controller == "s":
        duck()

