import random

words = ['jolly', 'mouse', 'lorry']

def start_game():
    choosen_word = random.choice(words)
    display = ['_' for i in choosen_word]
    num_of_life = len(choosen_word)


    while '_' in display and num_of_life > 0 :
        guess = input("Guess a letter: ").lower()
        
        if guess in choosen_word:
            index = [i for i,alphabet in enumerate(choosen_word) if guess == alphabet]
            for i in index:
                display[i] = guess
        else:
            num_of_life -= 1

        print(''.join(display))
        print(f'Remaining live: {num_of_life}')
    
    if '_' not in display:
        print("Congratulations. You won the game!")
    else:
        print("You lose. Play again.")

start_game()
