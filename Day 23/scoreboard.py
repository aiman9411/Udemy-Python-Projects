FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-260, 260)
        self.write_level()
    
    def write_level(self):
        self.write(f"Level: {self.level}", font = FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write_level()

    def game_over(self):
        self.goto(00,0)
        self.write("Game Over", align = "center", font = FONT)

