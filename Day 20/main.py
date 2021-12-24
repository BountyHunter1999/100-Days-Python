import time
from turtle import Screen

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # tracer is off, screen won't update

game_on = True

snake = Snake()
screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

while True:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
