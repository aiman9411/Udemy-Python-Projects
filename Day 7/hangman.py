import random
import hangman_art
import hangman_word

print(hangman_art.logo)

def start_game():
    choosen_word = random.choice(hangman_word.word_list)
    display = ['_' for i in choosen_word]
    num_of_life = 6
    print(f'Total letters are: {len(choosen_word)}')


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
        print(f'{hangman_art.stages[num_of_life]}')
    
    if '_' not in display:
        print("Congratulations. You won the game!")
    else:
        print(f'The answer is: {choosen_word}')
        print("You lose. Play again.")

start_game()
