import turtle

t = turtle.Pen()
def mycircle(red, green, blue):
    t.speed(1)
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

mycircle(0, 0.5, 0)