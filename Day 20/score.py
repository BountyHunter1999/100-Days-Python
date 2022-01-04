from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


def get_hs():
    with open('data.txt') as f:
        highscore = f.read()

    if highscore:
        return int(highscore)

    return 0


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.highscore = get_hs()
        self.show_score()

    def increase(self):
        self.score += 1
        self.show_score()

    def update_hs(self):
        with open('data.txt', mode="w") as f:
            f.write(str(self.highscore))

    def reset_game(self):
        # self.goto(0, 0)
        if self.score > self.highscore:
            self.highscore = self.score
            self.update_hs()

        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
