from tkinter import *
from tkinter.colorchooser import *
import random

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_arc(10, 10, 200, 100, extent=350, style=ARC)
mainloop()