import turtle

t = turtle.Pen()


def mycirclee(red, green, blue):
    t.speed(1)
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

mycirclee(0, 0.5, 0)
mycirclee(1, 0, 0)
mycirclee(0.5, 0, 0)
mycirclee(0, 0, 1)
mycirclee(0, 0, 0.5)
mycirclee(0.9, 0.75, 0)