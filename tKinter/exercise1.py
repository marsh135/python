

"""
Write a complete script that displays an Entry widget that’s 40 text units wide 
and has a white background and black text. Use .insert() to display text in the widget 
that reads What is your name?.
"""
import tkinter as tk

window = tk.Tk()

entry =  tk.Entry(width = 40, bg = "white",fg = "black")
entry.pack()

entry.insert(0,"what is your name?  ")


window.mainloop()




