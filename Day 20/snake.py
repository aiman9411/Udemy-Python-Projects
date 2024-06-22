from turtle import Turtle, Screen

# Screen Setting
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake_list = []
x_axis = [-20, 0, 20]
for i in range(3):
    snake = Turtle()
    snake.penup()
    snake.goto(x_axis[i], 0)
    snake.shape("square")
    snake.color("white")
    snake_list.append(snake)

moving = True
while moving:
    for snake in snake_list:                        
        snake.forward(5)
        
    head_snake = snake_list[2]
    if head_snake.xcor() == 280:
        moving = False

screen.exitonclick()
