import  tkinter as tk


win = tk.Tk()

f1 =  tk.Frame(master=win, width=200, height = 100, bg="red")
f1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

f2 = tk.Frame(master=win, width=100,  bg="yellow")
f2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

label1 = tk.Label(master=f2, text="I'm at (0,0)", fg="black")
label1.place(x=-50,y=-10)


f3 =  tk.Frame(master=win, width=50, bg="blue")
f3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

win.mainloop()