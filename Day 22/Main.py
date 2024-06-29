from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

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
    time.sleep(0.01)
    screen.update()
    ball.move_ball()

    if (ball.ycor() > 290 or ball.ycor() < -290):
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

screen.exitonclick()
