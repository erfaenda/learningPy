import turtle

t = turtle.Pen()


def mysquear(size, filled):

    if filled == True:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()

mysquear(100, True)