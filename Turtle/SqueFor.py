import turtle

i = turtle.Pen()
i.speed(0)

for x in range(1, 20):
    i.forward(100)
    i.left(95)

i.reset()

for x in range(1, 19):
    i.forward(100)
    if x % 2 == 0:
        i.left(175)
    else:
        i.left(225)

i.reset()


def mysquear(size):

    for x in range(1, 5):
        i.forward(size)
        i.left(90)

i.begin_fill()
mysquear(100)
i.end_fill()