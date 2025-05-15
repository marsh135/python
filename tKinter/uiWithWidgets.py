import tkinter as tk        #Classic Widgets

window =  tk.Tk()  # MUST HAVE
window.destroy()

entry = tk.Entry()
label =  tk.Label(text="Name")


label.pack() # MUST HAVE
entry.pack()

name=entry.get()
name
entry.delete(0)


window.mainloop() #MUST HAVE