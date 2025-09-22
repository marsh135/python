import tkinter as tk

root =  tk.Tk()

f1 =  tk.Frame(master=root, width=100, height=100, bg="red")
#f1.pack(fill=tk.X)
#f1.pack(fill=tk.Y, side=tk.LEFT)
f1.pack(fill = tk.BOTH, side = tk.LEFT, expand= True)

f2 = tk.Frame(master=root, width=50, height=50, bg="yellow")
#f2.pack(fill=tk.X)
#f2.pack(fill=tk.Y, side=tk.LEFT)
f2.pack(fill = tk.BOTH, side = tk.LEFT, expand= True)

f3 = tk.Frame(master=root, width =  25, height=25, bg="green")
#f3.pack(fill=tk.X)
#f3.pack(fill=tk.Y, side=tk.LEFT)
f3.pack(fill = tk.BOTH, side = tk.LEFT, expand= True)

root.mainloop()
