import turtle

class Screen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("U.S. States Game")
        self.image = "blank_states_img.gif"
        self.screen.addshape(self.image)
        turtle.shape(self.image)

    def run(self):
        self.screen.exitonclick()