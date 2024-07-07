
# NATO Phonetic Alphabet Converter

## Introduction
This Python script allows users to convert any word into its corresponding NATO phonetic alphabet representation. The project uses a CSV file that maps each letter of the alphabet to its NATO phonetic code. This tool is particularly useful for clear and precise verbal communications, especially in noisy environments or over the phone.

## Installation

### Prerequisites
Before you run the script, make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/). Additionally, you will need `pandas`, a powerful data manipulation library in Python.


## Usage
To use the script, follow these steps:
1. Ensure you have the `nato.csv` file in the same directory as the script. This CSV should contain two columns: `letter` and `code`, where `letter` represents a letter of the alphabet and `code` its corresponding NATO phonetic term.
2. Run the script with Python:
   ```bash
   python nato_converter.py
   ```
3. Follow the on-screen prompts to enter a word when requested.
4. The script will display the NATO phonetic alphabet codes corresponding to each letter of the input word.
