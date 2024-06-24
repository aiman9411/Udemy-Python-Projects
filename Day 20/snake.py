from turtle import Turtle
import time

X_AXIS = [20, 0, -20]
STEP = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in X_AXIS:
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(position, 0)
            self.segments.append(segment)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)
        self.head.forward(STEP)

    def snake_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def snake_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def snake_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def snake_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

