import random
import tkinter as tk
from tkinter import messagebox
turn = "Player1"
p1 = 0
p2 = 0
total = 0
last_roll = None

DIE_ART = {
    1: (
        "+-------+\n"
        "|       |\n"
        "|   o   |\n"
        "|       |\n"
        "+-------+"
    ),
    2: (
        "+-------+\n"
        "| o     |\n"
        "|       |\n"
        "|     o |\n"
        "+-------+"
    ),
    3: (
        "+-------+\n"
        "| o     |\n"
        "|   o   |\n"
        "|     o |\n"
        "+-------+"
    ),
    4: (
        "+-------+\n"
        "| o   o |\n"
        "|       |\n"
        "| o   o |\n"
        "+-------+"
    ),
    5: (
        "+-------+\n"
        "| o   o |\n"
        "|   o   |\n"
        "| o   o |\n"
        "+-------+"
    ),
    6: (
        "+-------+\n"
        "| o   o |\n"
        "| o   o |\n"
        "| o   o |\n"
        "+-------+"
    ),
}

def ascii_die(n):
    return DIE_ART.get(n, "+-------+\n|       |\n|       |\n|       |\n+-------+")

def roll():
    global total, last_roll
    r = random.randint(1, 6)
    last_roll = r
    print(r)
    if r == 1:
        total = 0
        print(total)
    else:
        total += r
        print(total)

def reset():
    global total
    total = 0

def hold():
    global total, p1, p2, turn
    if turn == "Player1":
        p1 += total
        print("Player 1 holds. SCORE: ", p1)
        print("It's your turn, P2!)")
        turn = "Player2"
    else:
        p2 += total
        print("Player 2 holds. SCORE: ", p2)
        print("It's your turn, P1!")
        turn = "Player1"
    reset()

def play():
    print("\nPlayer 1 score:", p1, "Player 2 score:", p2, "Turn total:", total)
    choice = input(f"{turn}, would you like to (r)oll or (h)old? ").lower().strip()
    if choice == "r":
        roll()
    elif choice == "h":
        hold()
    else:
        print("INVALID choice.")

def end():
    if p1 >= 100:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

def update_ui():
    p1_var.set(f"Player 1: {p1}")
    p2_var.set(f"Player 2: {p2}")
    total_var.set(f"Turn total: {total}")
    turn_var.set(f"Turn: {turn}")
    if last_roll is not None:
        die_var.set(ascii_die(last_roll))
    else:
        die_var.set(ascii_die(0))

def check_win():
    if p1 >= 100:
        messagebox.showinfo("Game Over", "Player 1 wins!")
        disable_buttons()
    elif p2 >= 100:
        messagebox.showinfo("Game Over", "Player 2 wins!")
        disable_buttons()

def disable_buttons():
    roll_btn.config(state="disabled")
    hold_btn.config(state="disabled")

def enable_buttons():
    roll_btn.config(state="normal")
    hold_btn.config(state="normal")

def switch_turn_after_1():
    global turn
    if turn == "Player1":
        turn = "Player2"
    else:
        turn = "Player1"

def gui_roll():
    roll()
    if total == 0:
        switch_turn_after_1()
        messagebox.showinfo("Oops!", f"{turn} now has the turn (rolled a 1).")
    update_ui()
    check_win()

def gui_hold():
    hold()
    update_ui()
    check_win()

def new_game():
    global p1, p2, total, turn, last_roll
    p1 = 0
    p2 = 0
    total = 0
    turn = "Player1"
    last_roll = None
    enable_buttons()
    update_ui()

# Build GUI
root = tk.Tk()
root.title("Pig Game (GUI)")

p1_var = tk.StringVar()
p2_var = tk.StringVar()
total_var = tk.StringVar()
turn_var = tk.StringVar()
die_var = tk.StringVar()

tk.Label(root, textvariable=p1_var, font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, textvariable=p2_var, font=("Arial", 14)).grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, textvariable=total_var, font=("Arial", 12)).grid(row=1, column=0, columnspan=2, pady=5)
tk.Label(root, textvariable=turn_var, font=("Arial", 12)).grid(row=2, column=0, columnspan=2, pady=5)

# ASCII die display (monospace)
tk.Label(root, textvariable=die_var, font=("Courier", 14), justify="center").grid(row=3, column=0, columnspan=2, pady=5)

roll_btn = tk.Button(root, text="Roll", width=10, command=gui_roll)
roll_btn.grid(row=4, column=0, pady=8)
hold_btn = tk.Button(root, text="Hold", width=10, command=gui_hold)
hold_btn.grid(row=4, column=1, pady=8)

tk.Button(root, text="New Game", command=new_game).grid(row=5, column=0, columnspan=2, pady=10)

update_ui()
root.mainloop()