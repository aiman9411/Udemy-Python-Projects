
# Silent Auction

This is a simple command-line based silent auction program written in Python. Participants can enter their names and bid amounts, and the program will determine the highest bidder at the end of the auction.

## Features

- Accepts multiple bids from different participants.
- Clears the screen between each bid to keep the bids private.
- Determines and displays the highest bidder at the end of the auction.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/silent-auction.git
    ```
2. Navigate to the project directory:
    ```bash
    cd silent-auction
    ```
3. Run the auction program:
    ```bash
    python auction.py
    ```

## Example

```bash
Type your name:
Alice
Type your bid price:
100
Is there any other bidder? Answer yes or no
yes

Type your name:
Bob
Type your bid price:
150
Is there any other bidder? Answer yes or no
no
```

Output:
```bash
The highest bidder is Bob with a bid of 150.0
```
