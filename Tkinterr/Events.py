import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=200)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)


def movetriangle(event):
#canvas.bind_all('<KeyPress-Return>', movetriangle) движение по ENTER
    if event.keysym == 'Up':
        canvas.move(1, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(1, -5, 0)
    else:
        canvas.move(1, 5, 0)

canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)


mainloop()