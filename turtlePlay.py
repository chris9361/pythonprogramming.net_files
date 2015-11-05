__author__ = 'cclif'

from turtle import *
canvas = Screen()
canvas.setup(400,400)
canvas.bgcolor("yellow")        # set the background color for the canvas
tess = Turtle()
tess.color("blue")
tess.pensize(5)                 # set the width of the turtle's pen

tess.forward(50)
tess.left(120)
tess.forward(50)
tess.penup()                    # pick up the pen (don't draw when you move)
tess.goto(10,10)                # go to a x and y location
tess.pendown()                  # put the pen down (draw again)
tess.forward(30)

canvas.exitonclick()            # wait for a user click on the canvas
