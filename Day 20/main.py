import time
from turtle import Screen

from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # tracer is off, screen won't update

game_on = True

snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()

    # Detect collison with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.reset_game()
        snake.reset_snake()

    # Detect collison with its body
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            score.reset_game()
            snake.reset_snake()

screen.exitonclick()
