from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_text(150, 100, text='Был один хуибола из Кубы')
canvas.create_text(150, 120, text='Я торгую арбузами! Потому что я Лоха', fill='red')
canvas.create_text(180, 150, text='Сорри! Но ты все равно хуибОла!', fill='blue', font=('Arial', -20))
mainloop()