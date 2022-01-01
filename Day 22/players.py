from turtle import Turtle

MOVE_DISTANCE = 15
X_POS = 350
Y_POS = 0
UP = 270
DOWN = 180


class Player(Turtle):

    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.create_snake(player)

    def create_snake(self, player):
        x = X_POS if player == 0 else -1 * X_POS
        self.goto(x, Y_POS)
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        self.setposition(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.setposition(self.xcor(), self.ycor() - MOVE_DISTANCE)
