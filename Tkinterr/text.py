from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_text(150, 100, text='Был один хуибола из Кубы')
mainloop()