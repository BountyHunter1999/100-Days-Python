import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

tom = Turtle()
tom.pensize(3)
# tom.speed(10)

tom.speed("fastest")
tom.shape("classic")


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def draw_spirograph(gap_size):
    steps = int(360 / gap_size)
    for _ in range(steps):
        tom.circle(100)
        tom.color(change_color())
        # tom.left(10)
        tom.setheading(tom.heading() + gap_size)


draw_spirograph(10)

screen = Screen()
screen.exitonclick()
