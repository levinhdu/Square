import turtle
t = turtle.Turtle()
t.pensize(5)
t.rt(90)
def square():
    t.fd(100)
    for i in range(3):
        t.lt(90)
        t.fd(200)
    t.lt(90)
    t.fd(100)
for i in range(5):
    square()
    t.lt(72)
turtle.done()