#more dice
#Write a program that simulates rolling a six-sided die. There should be one 
#button with the text Roll. When the user clicks the button, a random integer 
#from 1 to 6 should be displayed.

import tkinter as tk
import random

font_tuple = ("Times New Roman", 20, "bold")
def rng():
    lbl_result1["text"] =  str(random.randint(1,6))
    lbl_result2["text"] =  str(random.randint(1,6))


root =  tk.Tk()
root.columnconfigure([0,1], minsize=150)
root.rowconfigure([0,1], minsize=50, weight=1)


btn_roll = tk.Button( text="Roll",  command= rng)
#btn_roll.pack()
 
lbl_result1 =  tk.Label( text="", relief="groove", width=10, height=5,font=font_tuple)
lbl_result2 =  tk.Label( text="", relief="groove", width=10, height=5, font=font_tuple)
#lbl_result.pack()

btn_roll.grid(row = 0, columnspan=2, sticky="nsew")
lbl_result1.grid(row=1, column= 0)
lbl_result2.grid(row=1, column= 1)


root.mainloop()
