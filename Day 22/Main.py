from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")


paddle = Paddle()

screen.exitonclick()