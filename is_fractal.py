import turtle as tl
tl.pensize(0.1)
tl.penup()
tl.pendown()
i = 750
tl.speed(100)

def triangle(x, y):
    if x >= 1 and y:
        triangle(x/(2**(1/2)), 1)
        tl.left(135)
        triangle(x, 0)
    else:
        tl.forward(x)


triangle(i, 1)
tl.done()
