import turtle

t = turtle.Pen()
t.speed(1)


def mnogomer(dlina, storona):
    t.begin_fill()
    for x in range(1,5):
        t.color(0, 0.5, 0)
        t.forward(dlina)
        t.left(45)
        t.forward(storona)
        t.left(45)
    t.end_fill()

mnogomer(100, 50)