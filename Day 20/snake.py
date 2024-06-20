from turtle import Turtle, Screen

# Screen Setting
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")

turtle_list = []
moving = True

def create_turtle():
    x_axis = [-20, 0, 20]
    for i in range(3):
        turtle = Turtle()
        turtle.penup()
        turtle.goto(x_axis[i], 0)
        turtle.shape("square")
        turtle.color("white")
        turtle_list.append(turtle)

def move_turtle():
    while moving:
        for turtle in turtle_list:
            turtle.forward(5)

create_turtle()
move_turtle()

screen.exitonclick()