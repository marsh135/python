# powerball.exe, a Powerball number generator
# Copyright (C) 2022  Chris Calderon

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from random import SystemRandom
import tkinter as tk
from tkinter import ttk
from tkinter import font
from idlelib.tooltip import Hovertip


def main():
	rng = SystemRandom()
	base_numbers = list(range(1, 70))
	base_number_count = 5
	powerball_numbers = list(range(1, 27))
	icon_data = (
        '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'
        '/wfkjsRv1nwQ2QAAAABJRU5ErkJggg=='
	)
	window = tk.Tk()
	window.title('Powerball number generator')
	screen_width = window.winfo_screenwidth()
	screen_height = window.winfo_screenheight()
	window.geometry(f"{330}x{100}+{(screen_width - 330)//2}+{(screen_height - 100)//2}")
	window.resizable(False, False)
	icon = tk.PhotoImage(data=icon_data)
	window.wm_iconphoto(False, icon)
	window.grid_rowconfigure(0, weight=1)
	window.grid_rowconfigure(1, weight=1)
	window.grid_columnconfigure(0, weight=1)

	number_font = font.nametofont('TkFixedFont')

	top_frame = ttk.Frame(window)
	top_frame.grid_rowconfigure(0, weight=1)
	top_frame.grid_columnconfigure(0, weight=1)
	top_frame.grid_columnconfigure(2*base_number_count+2, weight=1)
	top_frame.grid(row=0, column=0, sticky='news', padx=5, pady=5)

	bottom_frame = ttk.Frame(window)
	bottom_frame.grid_rowconfigure(0, weight=1)
	bottom_frame.grid_columnconfigure(0, weight=1)
	bottom_frame.grid(row=1, column=0, sticky='news', padx=5, pady=5)

	number_labels = [ttk.Label(top_frame, text="  ", font=number_font) for _ in range(base_number_count + 1)]
	seperator_labels = [ttk.Label(top_frame, text="   ", font=number_font)]
	seperator_labels.extend(ttk.Label(top_frame, text="-", font=number_font) for _ in range(base_number_count - 1))
	seperator_labels.append(ttk.Label(top_frame, text="|", font=number_font))
	seperator_labels.append(ttk.Label(top_frame, text="   ", font=number_font))
	generate_button = ttk.Button(bottom_frame, text="Generate!")
	tip = Hovertip(number_labels[-1], " Powerball number ")

	seperator_labels[0].grid(row=0, column=0, padx=5, pady=5)
	for i in range(base_number_count + 1):
		number_labels[i].grid(row=0, column=2*i+1, padx=5, pady=5)
		seperator_labels[i+1].grid(row=0, column=2*i+2, padx=5, pady=5)

	generate_button.grid(row=0, column=0, padx=5, pady=5)
	
	def genenerate_command():
		numbers = rng.sample(base_numbers, k=base_number_count)
		numbers.sort()
		powerball = rng.choice(powerball_numbers)
		for i, n in enumerate(numbers):
			number_labels[i]['text'] = str(n).rjust(2)
		number_labels[i + 1]['text'] = str(powerball).rjust(2)

	generate_button['command'] = genenerate_command

	window.mainloop()


if __name__ == '__main__':
	main()
