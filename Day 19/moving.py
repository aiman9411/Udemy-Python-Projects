from turtle import Turtle, Screen

timmy = Turtle()

screen = Screen()

def forward():
    timmy.forward(10)

def backward():
    timmy.forward(-10)

def anticlockwise():
    timmy.left(30)

def clockwise():
    timmy.left(-30)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=anticlockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()