import random

guess = input("Guess a letter: ").lower()

words = ['computer', 'mouse', 'chair']

def start_game(guess):
    display = ''
    choosen_word = random.choice(words)
    while len(display) != len(choosen_word):
        display += '_'
    

start_game(guess)

# if guess.isalpha() and len(guess) == 1:
#     start_game(guess)
# else:
#     print("Start Again")