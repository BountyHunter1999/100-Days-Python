# Imports
import time
from turtle import Screen
from ball import Ball
from players import Player
from score_board import ScoreBoard

# Constants
SCORE1_COR = (80, 250)
SCORE2_COR = (-80, 250)

PLAYER1_SIDE = (-300, 0)
PLAYER2_SIDE = (300, 0)

# Objects
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
# screen.screensize(canvwidth=600, canvheight=600)
# screen.screensize(canvwidth=200, canvheight=200)
screen.title("PONG")
screen.listen()
screen.tracer(0)

ball = Ball()


player1 = Player(player=0)
player2 = Player(player=1)


# player2 = Player(player=1)

score1 = ScoreBoard(SCORE1_COR)
score2 = ScoreBoard(SCORE2_COR)

# screen.tracer(1)
screen.onkey(fun=player1.move_up, key="Up")
screen.onkey(fun=player1.move_down, key="Down")

screen.onkey(fun=player2.move_up, key="w")
screen.onkey(fun=player2.move_down, key="s")

#  Game Logic

game_on = True
i = 0
print(screen.screensize())
while game_on:
    time.sleep(0.1)
    screen.update()

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:  # width of ball is 20px
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(player1) < 50 or ball.xcor() < -320 and ball.distance(player2) < 50:
        print("Made contact")
        ball.bounce_x()

    if ball.xcor() > 370 or ball.xcor() < -370:  # paddle goes from 340 to 360
        if ball.xcor() < 0:
            score1.increase_score()
        else:
            score2.increase_score()

        ball.ball_reset()


screen.exitonclick()
