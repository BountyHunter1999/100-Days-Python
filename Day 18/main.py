import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

tom = Turtle()
tom.pensize(10)
# tom.speed(10)

tom.speed("fastest")
tom.shape("classic")


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
#            "wheat", "SlateGray", "SeaGreen"]

# def change_color():
#     return random.choice(colours)


def move(ang):
    tom.color(change_color())

    tom.forward(50)
    tom.setheading(ang)
    # tom.left(direction)


angles = list(range(0, 271, 90))

for _ in range(200):
    direction = random.choice(angles)
    move(direction)

screen = Screen()
screen.exitonclick()
