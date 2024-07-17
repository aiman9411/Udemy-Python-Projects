# Language Flash Card App

A simple language learning flashcard application built with Python and tkinter GUI framework. This application allows users to practice French-English translations interactively.

## Features

- Display flashcards with French words on the front and their English translations on the back.
- Buttons to mark cards as known or to skip to the next card.
- Automatically saves progress by updating a CSV file (`words_to_learn.csv`) with words the user wants to review further.

## Requirements

- Python 3.x
- Pandas library (for CSV handling)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your_username/language-flashcard-app.git
   cd language-flashcard-app
   ```

2. Install dependencies:

   ```
   pip install pandas
   ```

3. Run the application:

   ```
   python flashcard_app.py
   ```

## Usage

- Upon running the application, a tkinter window opens displaying a flashcard with a French word.
- Click on the green tick button (`✓`) if you know the English translation of the word.
- Click on the red cross button (`✗`) if you want to skip the current word.
- Progress is automatically saved to `words_to_learn.csv`. If the file doesn't exist, it will create one based on initial words (`french_words.csv`).

## File Structure

- `flashcard_app.py`: Main Python script containing the flashcard application logic.
- `card_front.png`: Image file for the front side of the flashcard.
- `card_back.png`: Image file for the back side of the flashcard.
- `wrong.png`: Image file for the cross (skip) button.
- `right.png`: Image file for the tick (known) button.
- `french_words.csv`: CSV file containing initial French words and their English translations.
- `words_to_learn.csv`: CSV file dynamically updated with words the user wants to review further.
