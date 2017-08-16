from tkinter import *

root = Tk()
root.geometry('700x700')
root.title('Root')

def new_window(event):
    window = Toplevel(root)

lab = Label(root, text='Press here')
but = Button(root, text='Ok')
but.bind('<Button->', new_window)

lab.pack()
but.pack()

root.mainloop()