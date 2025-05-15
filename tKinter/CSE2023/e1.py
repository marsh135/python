#exercise1


##modify to add blank label in beginning
#Create two buttons, two functions
#btn1  greets : Hello Students
#btn2 dismisses: Goodbye Students

#change colors for each


import tkinter as tk

def hello():
    font_tuple = ("Times", 100, "italic")
    greeting["text"] = "Hello, Students!"
    greeting["fg"] = "green"
    greeting["bg"] = "purple"

def goodbye():
    font_tuple = ("Comic Sans MS", 100, "bold")
    greeting["text"] = "Goodbye, Students!"
    greeting["fg"] = "red"
    greeting["bg"] = "black"


font_tuple = ("Comic Sans MS", 100, "italic")

window =  tk.Tk()
#window.destroy()
greeting = tk.Label(
    text="", 
    font=font_tuple,
    background = "tan",
    foreground =  "#556b2f"
    )

btn_greet =  tk.Button(
    text= "Greet!",
    width=25,
    height=5,
    bg= "yellow",
    fg = "red",
    command =  hello
)

btn_dismiss =  tk.Button(
    text= "Dismiss",
    width=25,
    height=5,
    bg= "yellow",
    fg = "red",
    command =  goodbye
)
greeting.pack()
btn_greet.pack()
btn_dismiss.pack()

window.mainloop()



