from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Turtle(shape="square")
snake.penup()
snake.turtlesize(stretch_len=3)
snake.color("white")


def move_forward():
    snake.forward(10)

def move_left():
    snake.left(90)


screen.onkey(fun=move_forward, key="f")
screen.onkey(fun=move_left, key="w")
print(snake.shapesize())

screen.listen()
screen.exitonclick()
