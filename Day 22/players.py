from turtle import Turtle

MOVE_DISTANCE = 20
WIDTH = 20
HEIGHT = 100
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
    #     self.segments = []
        self.create_snake(player)
    #     self.head = self.segments[0]

    def create_snake(self, player):
        x = X_POS if player == 0 else -1 * X_POS
        self.goto(x, Y_POS)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        # starting_segments = SEGMENTS_1 if player == 0 else SEGMENTS_2
        # for position in starting_segments:
        #     self.add_segment(position)
    #
    # def add_segment(self, position):
    #     segment = Turtle(shape="square")
    #     segment.color("white")
    #     segment.penup()
    #     segment.shapesize(stretch_len=0.5)
    #     segment.goto(position)
    #     self.segments.append(segment)
    #
    # #  move paddle

    def move_up(self):
        self.setposition(self.xcor(), self.ycor() + 15)

    def move_down(self):
        self.setposition(self.xcor(), self.ycor() - 15)



