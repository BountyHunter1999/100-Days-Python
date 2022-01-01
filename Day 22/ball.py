from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 6
        self.y_move = 6

    # move ball
    def move(self):
        self.setposition(self.xcor() + self.x_move, self.ycor() + self.y_move)

    # create collision with the wall
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.increase_speed()
        print(self.x_move, self.y_move)
        self.x_move *= -1

    def ball_reset(self):
        self.setposition(0, 0)
        self.x_move, self.y_move = (3, 3)
        self.bounce_x()

    def increase_speed(self):
        self.x_move *= 1.08
        self.y_move *= 1.08
