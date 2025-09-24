import random
import turtle
import tkinter as tk
#my_list = [1,2,3,4,5,6]
print(random.randint(1,6))

screen = turtle.Screen()
"""
caps ={
    "IN":"Indianapolis",
    "OH":"Columbus",
    "KY":"Frankfort",
    "IL":"Springfield",
    "WI":"Madison",
    "MI":"Lansing"
}
for key in caps:
    print(key)

choice = input("Enter a state abbreviation: ")
if(choice == "IN"):
    print(caps["IN"])
elif(choice == "OH"):
    print(caps["OH"])
elif(choice == "KY"):
    print(caps["KY"])
"""

def move():
    kurt.forward(10)
def stop():
    kurt.forward(0)
kurt= turtle.Turtle()
kurt.shape("turtle")
kurt.color("blue")
kurt.speed(10)
screen.onkeyrelease(move, "space")
screen.onkey(stop, "space")

screen.listen()