# Higher Lower Game

## Overview

The Higher Lower Game is a fun, interactive command-line game where players compare the follower counts of different profiles and guess which one has more followers. The game uses a predefined dataset of profiles with their descriptions, countries, and follower counts.

## Features

- Compare follower counts of various profiles.
- Keep track of the score for correct guesses.
- Simple and intuitive command-line interface.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/higher-lower-game.git
   ```

2. Navigate to the project directory:
   ```bash
   cd higher-lower-game
   ```

3. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

## Usage

1. Make sure your `game_data.py` file contains a `data` list with the required structure for the game to work. Here is an example of the `game_data.py` file:

    ```python
    # game_data.py
    data = [
        {
            'name': 'Person A',
            'description': 'description of Person A',
            'country': 'Country A',
            'follower_count': 100
        },
        {
            'name': 'Person B',
            'description': 'description of Person B',
            'country': 'Country B',
            'follower_count': 150
        },
        # Add more entries as needed
    ]
    ```

2. Run the game:
   ```bash
   python main.py
   ```

3. Follow the on-screen instructions to play the game. You'll be prompted to guess which profile has more followers by typing 'A' or 'B'.

## Example

```
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Person A, a description of Person A from Country A
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Compare B: Person B, a description of Person B from Country B
Who has more followers? Type 'A' or 'B'
```
