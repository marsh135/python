import tkinter as tk

root =  tk.Tk()

def handle_keypress(event):
    print(event.char)

root.bind("<a>", handle_keypress)

def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")
button.pack()

button.bind("<Button-1>", handle_click)

root.mainloop()
