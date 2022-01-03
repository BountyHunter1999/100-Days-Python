from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        # super().__init__()
        self.all_cars = []

    def create_car(self):
        if random.randint(0, 6) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_pos = random.randint(-230, 230)
            new_car.goto(290, y_pos)
            self.all_cars.append(new_car)

    def move_cars(self, level):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT)


