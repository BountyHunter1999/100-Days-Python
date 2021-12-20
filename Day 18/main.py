import turtle
from turtle import Turtle, Screen
import random

tom = Turtle()
tom.shape("classic")
turtle.colormode(255)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def draw_shape(sides):
    internal_angle = int(360 / sides)
    tom.color(change_color())
    for _ in range(sides):
        tom.forward(100)
        tom.left(internal_angle)

for side in range(3, 11):
    draw_shape(side)

screen = Screen()
screen.exitonclick()
