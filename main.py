from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

game_is_on = True
game_loop = 0
game_speed = 0.1

# Setup game components on screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Passing Game')
screen.tracer(0)
turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Setup player control of turtle movement on screen
screen.listen()
screen.onkey(turtle.move_forward, 'Up')


while game_is_on:
    game_loop += 1

    # Add another car to the road
    if game_loop % 6 == 0:
        cars.add_car()
    cars.move_forward()

    # Update speed of cars
    time.sleep(game_speed)
    screen.update()

    # Stop game if turtle collides with car
    for car in cars.cars:
        if turtle.distance(car) <= 20:
            scoreboard.game_over()
            game_is_on = False

    # Restart turtle and increase level if turtle crosses road
    if turtle.finish_line():
        turtle.restart()
        scoreboard.increase_level()
        game_speed *= 0.5

screen.exitonclick()
