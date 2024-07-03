# Snake Game

This project is a simple implementation of the classic Snake game using Python's `turtle` graphics library. The game includes a snake that the player controls, food that the snake eats to grow longer, and a score system that tracks the current and high scores.

## Features

- Classic Snake game mechanics
- Simple and intuitive controls
- Persistent high score tracking

## Getting Started

### Prerequisites

- Python 3.x installed on your system
- `turtle` graphics library (included with Python's standard library)

### Installation

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/your-username/snake-game.git
    ```
2. Navigate to the project directory:
    ```sh
    cd snake-game
    ```

### Running the Game

To start the game, run the `main.py` file:
```sh
python main.py
```

## Controls

- **Up Arrow**: Move up
- **Down Arrow**: Move down
- **Left Arrow**: Move left
- **Right Arrow**: Move right

## Project Structure

- `main.py`: Main script to run the game.
- `snake.py`: Contains the `Snake` class, which handles the snake's behavior.
- `food.py`: Contains the `Food` class, which handles the food's behavior.
- `score.py`: Contains the `Score` class, which handles the score display and tracking.
- `data.txt`: A text file used to store the high score.

## Classes

### Snake

- Manages the snake's segments and movements.
- Handles the snake's growth when food is eaten.
- Detects collisions with itself and the walls.

### Food

- Manages the food's position on the screen.
- Randomly places food on the screen when it is eaten.

### Score

- Tracks and displays the current score and high score.
- Resets the score when the snake collides with itself or the walls.
