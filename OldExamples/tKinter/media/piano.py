import tkinter as tk
import pygame



pygame.mixer.init()
root =  tk.Tk()

gSound = "tKinter/media/g.mp3"
c3Sound = "tKinter/media/c3.mp3"

def gNote(event):
    pygame.mixer.music.load(gSound)
    pygame.mixer.music.play()

def c3Note(event):
    pygame.mixer.music.load(c3Sound)
    pygame.mixer.music.play()

root.bind("<a>", gNote)
root.bind("<s>", c3Note)
root.bind("<d>", gNote)
root.bind("<f>", gNote)
root.bind("<g>", gNote)




root.mainloop()
