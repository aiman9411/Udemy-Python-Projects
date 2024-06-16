import colorgram
import turtle as t
import random

# Set up turtle graphics
t.colormode(255)

screen = t.Screen()
timmy = t.Turtle()
timmy.speed(0)
timmy.penup()
timmy.hideturtle()

# Extract colors from an image
list_colors = []
colors = colorgram.extract("painting.jpg", 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    list_colors.append(new_color)

# Function to draw a grid of dots
def draw_dot(dot_size, spacing, rows, columns):
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)
    for row in range(rows):
        for col in range(columns):
            timmy.dot(dot_size, random.choice(list_colors))  # Use random.choice instead of random.choices
            timmy.forward(spacing)
        timmy.backward(spacing * columns)
        timmy.right(90)
        timmy.forward(spacing)
        timmy.left(90)

# Draw a grid of dots with specified size and spacing
draw_dot(dot_size=20, spacing=50, rows=10, columns=10)

# Set up the screen to close when clicked
screen.exitonclick()