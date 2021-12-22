from turtle import Turtle, Screen

tom = Turtle()


def move_forward():
    tom.forward(10)


def move_backward():
    tom.backward(10)


def move_left():
    new_heading = tom.heading() + 10
    tom.setheading(new_heading)
    # tom.left(90)
    # tom.forward(50)


def move_right():
    new_heading = tom.heading() - 10
    tom.setheading(new_heading)
    # tom.left(-90)
    # tom.forward(50)


def clr():
    # tom.clear()
    # tom.penup()
    # tom.home()
    # tom.pendown()
    screen.resetscreen()


screen = Screen()
screen.onkey(fun=move_forward, key='w')  # move forward
screen.onkey(fun=move_backward, key='s')  # move in backward
screen.onkey(fun=move_left, key='a')  # move left
screen.onkey(fun=move_right, key='d')  # move right
screen.onkey(fun=clr, key="c")

screen.listen()
screen.exitonclick()
