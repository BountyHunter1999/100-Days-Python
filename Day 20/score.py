from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.show_score()

    def increase(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!", align=ALIGNMENT, font=FONT)

    def show_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
