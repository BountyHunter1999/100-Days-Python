from turtle import Turtle

STARTING_SEGMENTS = [(0, 0), (-20, 0), (-40, 0), (-80,0)]
MOVE_DISTANCE = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_SEGMENTS:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for position in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[position - 1].xcor()
            new_y = self.segments[position - 1].ycor()
            # prev_pos = self.segments[position - 1].pos()
            self.segments[position].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            print("Inside Left")
            print(len(self.segments))
            # self.move()

    def right(self):
        print(self.head.heading(), "right")

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            print("Inside Right")
            # self.move()

    def down(self):
        print(self.head.heading(), "down")
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            print("Inside down")
        # self.move()

    def up(self):
        print(self.head.heading(), "up")
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            print("Inside up")
            # self.move()
