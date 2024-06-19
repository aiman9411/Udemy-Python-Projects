from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width= 500, height= 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Red, Green, Blue, Yellow")
colors = ["red", "green", "blue", "yellow"]
y_positions = [-70, -40, -10, 20]

finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(100,200)
finish_line.pendown()
finish_line.right(90)
finish_line.forward(400)
finish_line.penup()


turtle_list = []

for i in range(4):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x = -230, y = y_positions[i])
    turtle_list.append(tim)

def move_turtle(turtles):
    race_on = True
    while race_on:
        for turtle in turtles:
            random_distance = random.randint(0,10)
            turtle.forward(random_distance)
            if turtle.xcor() > 100:
                race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"{winning_color.capitalize()} turtle won the competition. You win")
                else:
                    print(f"{winning_color.capitalize()} turtle won the competition. You lose")
                
                word = Turtle()
                word.hideturtle()
                word.color("black")
                word.write(f"{winning_color.capitalize()} turtle wins!", align="center", font=("Arial", 16, "bold"))

move_turtle(turtle_list)

screen.exitonclick()
