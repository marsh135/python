import tkinter as tk        #Classic Widgets
import tkinter.ttk as ttk   #Themed Widgets

window =  tk.Tk()  # MUST HAVE

button =  tk.Button(
    text="Click Me!",
    width=25,
    height =  10,
    bg="green",
    fg="black"
)


button.pack() # If you make it, you must PACK it

window.mainloop() #MUST HAVE