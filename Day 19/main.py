from turtle import Turtle, Screen
import random

colors = ["red", "green", "purple", "yellow", "orange", "blue"]

turtles = []
for i, color in enumerate(colors):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(color)
    turtles[i].penup()
    turtles[i].goto(-230, -40 + i * 30)


def steps():
    return random.choice(range(0, 20))


def move(player):
    player.forward(steps())


def check_end_reached(turtles, selected_color):
    for turtle in turtles:
        if turtle.xcor() >= 230:
            print(turtle.xcor())
            if turtle.pencolor() == selected_color:
                print("CONGRATS! Your Turtle Won!!")
            else:
                print(f"You Lost!!, {turtle.pencolor()} Turtle won ")
            return True

    return False


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="YOLO", prompt="Which turtle will win the race? Enter a color: ")

print(turtles[0].pencolor())
while True:
    player = random.choice(turtles)
    move(player)
    if check_end_reached(turtles, user_bet):
        break

screen.exitonclick()
