from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    # move ball
    def move(self):
        self.setposition(self.xcor() + self.x_move, self.ycor() + self.y_move)

    # create collision with the wall
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def ball_reset(self):
        self.setposition(0, 0)
        # self.bounce_x()

