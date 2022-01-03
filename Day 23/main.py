import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()

screen.onkey(fun=player.move_up, key="Up")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars(level=scoreboard.level)

    for car in car_manager.all_cars:
        # car are 20px height and 40px in width
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.goal:
        print("GOAL REACHED")
        scoreboard.increase_level()
        player.goto_start()

screen.exitonclick()
