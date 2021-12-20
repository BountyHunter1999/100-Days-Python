from turtle import Turtle, Screen

tom = Turtle()
tom.shape("classic")
tom.color("blue")

for _ in range(4):
    tom.forward(100)
    tom.left(90)

# tom.forward("100")


screen = Screen()
screen.exitonclick()
