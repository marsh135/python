import tkinter as tk

border_fx = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove":tk.GROOVE,
    "ridge":tk.RIDGE
}

window =  tk.Tk()
font_tuple = ("Comic Sans MS", 50, "italic")
#DO NOT TYPE THIS PART YET!!!!!!

for relief_name, relief, in border_fx.items():
    frame =  tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name,font=font_tuple)
    label.pack()

window.mainloop()