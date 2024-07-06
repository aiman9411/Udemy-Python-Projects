import turtle
import pandas as pd

class Screen:
    def __init__(self):
        self.number = 0
        self.screen = turtle.Screen()
        self.screen.title("Guess State Game")
        self.image = "blank_states_img.gif"
        self.screen.addshape(self.image)
        turtle.shape(self.image)

    def run(self):
        self.screen.exitonclick()

    def ask_question(self):
        answer = self.screen.textinput(f"{self.number}/50 States Correct", "Guess the next state's name").title()
        return answer
    
    def create_label(self, x_loc, y_loc, word):
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.up()
        pen.goto(x_loc, y_loc)
        pen.write(word, font=("Arial", 10, "normal"))

    def total_score(self):
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.up()
        pen.goto(0, 270)
        pen.write(f"Your total score is {self.number} / 50", align = "center", font=("Arial", 30, "normal"))

