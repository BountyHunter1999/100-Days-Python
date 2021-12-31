from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self, place):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.hideturtle()
        self.score = 0
        self.goto(place)
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)



