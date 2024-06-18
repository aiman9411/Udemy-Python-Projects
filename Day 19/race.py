from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width= 500, height= 400)
colors = ["red", "green", "blue", "yellow", "purple", "orange", "black", "pink", "brown", "cyan"]
y_positions = [-70, -40, -10, 20, 50, 80]

turtle_list = []

for i in range(4):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x = -230, y = y_positions[i])
    turtle_list.append(tim)

def move_turtle(turtles):
    for i in turtles:
        i.penup()
        i.goto(x = 200, y = y_positions[i for i in range(4)])


move_turtle(turtle_list)
screen.exitonclick()