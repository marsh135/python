import tkinter as tk        #Classic Widgets
import tkinter.ttk as ttk   #Themed Widgets

window =  tk.Tk()

label = tk.Label(
    text="Hello, tKinter",
    foreground="white",  # can use colors, fg =  foreground
    background="black",  #can also use HexDecimal , bg =  background
    width =10,
    height =  10
    )
label.pack()

window.mainloop()