from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

right_paddle = Paddle(position = (350,0))
left_paddle = Paddle(position = (-350,0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()
    ball.move_ball()

    if (ball.ycor() > 290 or ball.ycor() < -290):
        ball.bounce()

screen.exitonclick()
