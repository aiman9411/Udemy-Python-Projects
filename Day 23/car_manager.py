COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

from turtle import Turtle
import random


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1,6)
        if chance > 3:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=0.5, stretch_len=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
            