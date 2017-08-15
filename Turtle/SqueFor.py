import turtle

i = turtle.Pen()
i.speed(1)

for x in range (1, 20):
    i.forward(100)
    i.left(95)

i.reset()

for x in range(1, 19):
    i.forward(100)
    if x % 2 == 0:
        i.left(175)
    else:
        i.left(225)