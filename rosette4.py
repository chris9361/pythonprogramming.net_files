__author__ = 'cclif'

from turtle import *
canvas = Screen()
canvas.setup(400, 400)
t = turtle()
for x in range(4):
    t.circle(100)
    t.left(90)

canvas.exitonclick()