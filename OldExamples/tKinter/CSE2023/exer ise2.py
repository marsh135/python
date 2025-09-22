#exercise 2:
#text input, return to user

#1. Import TKinter
import tkinter as tk

#2. Create a new window
window = tk.Tk()

#4. Write a funciton to update label with name
def display_text():
    global txt_name
    string =  txt_name.get("1.0")
    lbl_display.configure(text="Hello " + string)

#3. Create a button, label, and text box

btn_submit =  tk.Button(text="Submit", command = display_text)
lbl_display = tk.Label(text="")
txt_name =  tk.Entry(width=60)
txt_name.insert(0, "Please enter your name!")

lbl_display.pack()
txt_name.focus_set()
txt_name.pack()

btn_submit.pack()

#5. Bind it

#6. Show it
window.mainloop()