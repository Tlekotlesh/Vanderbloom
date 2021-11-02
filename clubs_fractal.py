import turtle as tl

def draw_fractal(scale):
    if scale >= 10:
        draw_fractal(scale / 4.0)
        tl.left(90)
        draw_fractal(scale / 4.0)
        tl.right(90)
        draw_fractal(scale / 4.0)
        tl.right(90)
        draw_fractal(scale / 4.0)
        tl.left(90)
        draw_fractal(scale / 4.0)
    else:
        tl.forward(scale)



scale = 1400
tl.speed(10 ** 9)
tl.pensize(2)
tl.penup()
tl.goto(-scale/5, -scale/20)
tl.pendown()

draw_fractal(scale)
tl.done()
