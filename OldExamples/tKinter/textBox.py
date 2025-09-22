import tkinter as tk        #Classic Widgets


def submit():
    letters = text_box.get("1.0")
    return letters

window =  tk.Tk()  # MUST HAVE
window.geometry("600x400")
#window.destroy()

text_box =  tk.Text()
text_box.pack()

btn_sub = tk.Button(text="Submit", command = submit)
btn_sub.pack


print(submit())
window.mainloop() #MUST HAVE