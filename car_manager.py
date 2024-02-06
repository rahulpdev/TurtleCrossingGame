from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []

    def add_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.left(180)
        new_car.goto(300, random.randint(-250, 250))
        self.cars.append(new_car)

    def move_forward(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
