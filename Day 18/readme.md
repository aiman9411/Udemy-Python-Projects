# Turtle Graphics Dot Grid

This project uses the `turtle` graphics library to create a grid of colored dots. The colors are extracted from an image using the `colorgram` library.

## Features

- Extracts colors from an image
- Draws a grid of colored dots using `turtle` graphics
- Uses random colors from the extracted palette for each dot

## Requirements

- Python 3.x
- `turtle` library (included with Python standard library)
- `colorgram.py` library

## Installation

1. Install the `colorgram.py` library:
    ```sh
    pip install colorgram.py
    ```

2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/turtle-dot-grid.git
    cd turtle-dot-grid
    ```

2. Add your image file (`painting.jpg`) to the project directory.

3. Run the script:
    ```sh
    python turtle_dot_grid.py
    ```

## Script Overview

The script performs the following steps:

1. Imports necessary libraries.
2. Sets up the `turtle` graphics environment.
3. Extracts colors from an image using `colorgram`.
4. Defines a function to draw a grid of dots.
5. Uses the extracted colors to draw the dots with random colors from the palette.

### Code

```python
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
```
