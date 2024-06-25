from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# Screen Setting
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")
screen.onkey(snake.snake_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_is_on = False
        score.game_over()

screen.exitonclick()
