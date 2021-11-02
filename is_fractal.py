import turtle as tl
tl.pensize(0.1)
tl.penup()
tl.pendown()
i = 750
tl.speed(100)

def Triangle(x, y):
    if x >= 1 and y:
        Triangle(x/(2**(1/2)), 1)
        tl.left(135)
        Triangle(x, 0)
    else:
        tl.forward(x)


Triangle(i, 1)
tl.done()