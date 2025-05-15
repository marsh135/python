import tkinter as tk


def submit():
    user_input = favAnimal.get()
    print(user_input)

window =  tk.Tk()
window.geometry("600x400")

m_label =  tk.Label(text = "Enter you favorite animal")
m_label.pack()
favAnimal = tk.Entry()
favAnimal.pack()




sub_btn =  tk.Button(text="Submit", command = submit)
sub_btn.pack()
window.mainloop()