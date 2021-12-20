from turtle import Turtle, Screen

tom = Turtle()
tom.shape("classic")
tom.color("blue")

for _ in range(15):
    tom.forward(10)
    tom.penup()  # don't leave trail
    tom.forward(10)
    tom.pendown()  # Leave trail

screen = Screen()
screen.exitonclick()
