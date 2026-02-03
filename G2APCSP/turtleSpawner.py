import turtle
import random

#This function sets the background
def setScene():
    screen = turtle.Screen()
    screen.bgcolor('cyan')
    bgTurtle = turtle.Turtle()
    bgTurtle.speed(0)
    bgTurtle.penup()
    bgTurtle.goto(-360, 200)
    bgTurtle.pendown()
    bgTurtle.color("burlywood")
    bgTurtle.begin_fill()
    for i in range(4):
        bgTurtle.forward(400)
        bgTurtle.right(90)
    bgTurtle.end_fill()
    bgTurtle.hideturtle()

#This function spawns turtles in random locations.
#The number of turtles spawned is based on user input.

def createTurtles(numTurtles):
  turtles = []
  for i in range(numTurtles):
    x = random.randint(-300,300)
    y= random.randint(-150,150)
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.setposition(x,y)
    turtles.append(t)
  return turtles

def turtleSwim(turtles):
    for pat in turtles:
        while pat.xcor() < 300:
            pat.forward(5)
        pat.hideturtle()

setScene()
numTurtles = int(input("How many turtles? "))
turtles = createTurtles(numTurtles)
turtleSwim(turtles)