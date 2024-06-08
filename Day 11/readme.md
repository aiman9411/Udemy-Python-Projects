# Blackjack Game

Welcome to the Blackjack Game! This project is a simple command-line implementation of the classic card game Blackjack. The game allows you to play against the computer in an interactive manner.

## Game Rules

- Blackjack is a card game where the goal is to have a hand value closest to 21 without exceeding it.
- Number cards are worth their face value.
- Face cards (Jack, Queen, King) are worth 10.
- Aces worth 11.
- A hand with an Ace and a 10-value card (10, Jack, Queen, King) is called a Blackjack and is an automatic win unless the dealer also has a Blackjack.
- The dealer must draw cards until their hand value is 17 or higher.

## Features

- Draw cards to build your hand and try to get as close to 21 as possible.
- The computer acts as the dealer, drawing cards according to the rules.
- Interactive prompts guide you through each step of the game.
- ASCII art enhances the visual experience of the game.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/blackjack-game.git
    ```
2. Navigate to the project directory:
    ```bash
    cd blackjack-game
    ```

### Usage

To start the game, run the `blackjack.py` file:

```bash
python blackjack.py
```

Follow the on-screen prompts to play the game. You can choose to draw more cards or pass to let the dealer play.

### Example

```
Do you want to play a game of Blackjack? Type 'y' or 'n': y
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |
      `------'                           |__/

Your cards: [10, 7], current score: 17
Computer's first card: 6
Type 'y' to get another card, type 'n' to pass: n
Your final hand: [10, 7], final score: 17
Computer's final hand: [6, 10], final score: 16
You win 😃
```

## Acknowledgements

- ASCII art generated using [ascii.co.uk](https://ascii.co.uk) and modified for this game.

Enjoy the game and happy playing!
```

Feel free to adjust the repository URL, author details, and any other specifics to better suit your project.
