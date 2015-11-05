__author__ = 'cclif'

from turtle import *
canvas = Screen()
canvas.setup(600,600)
canvas.bgcolor("white")        # set the background color for the canvas
t = Turtle()
t.hideturtle()
t.color("blue")
t.pensize(2)                 # set the width of the turtle's pen
t.penup()
t.forward(20)
t.pendown()

for x in range(20):
    t.circle(100)
    t.left(20)

canvas.exitonclick()            # wait for a user click on the canvas
