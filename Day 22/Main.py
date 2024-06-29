from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

right_paddle = Paddle(position = (350,0))
left_paddle = Paddle(position = (-350,0))
ball = Ball()
right_score = Score((200,250))
left_score = Score((-300, 250))

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    if (ball.ycor() > 240 or ball.ycor() < -290):
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 400:
        left_score.increase_score()
        ball.restart_ball()
        ball.x_move = -1
        ball.y_move = -1
    elif ball.xcor() < -400:
        right_score.increase_score()
        ball.restart_ball()
        ball.x_move = 1
        ball.y_move = 1

screen.exitonclick()
