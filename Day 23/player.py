from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goal = 0  # 1 when goal is reached
        self.goto_start()

    def move_up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)
        else:
            self.goal = 1

    def goto_start(self):
        self.goto(STARTING_POSITION)
        self.goal = 0


