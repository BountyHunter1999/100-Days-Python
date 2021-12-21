import turtle
from turtle import Turtle, Screen
import colorgram
import random

turtle.colormode(255)

tom = Turtle()
tom.hideturtle()
# tom.pensize(3)

tom.speed("fastest")
# tom.shape("classic")

rgb_colors = []

colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


tom.penup()
tom.goto(-600, -300)

for _ in range(10):
    tom.sety(tom.ycor() + 50)
    tom.goto(-200, tom.ycor())
    for _ in range(10):
        color = random.choice(rgb_colors)
        tom.dot(20, color)
        tom.forward(50)

screen = Screen()
screen.exitonclick()
