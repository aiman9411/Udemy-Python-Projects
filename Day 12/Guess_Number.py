import random

ART = '''
  ________ ____ ______________ _________ _________ ______________ ______________  _______   ____ ___  _____ _______________________________ 
 /  _____/|    |   \_   _____//   _____//   _____/ \__    ___/   |   \_   _____/  \      \ |    |   \/     \\______   \_   _____/\______   \
/   \  ___|    |   /|    __)_ \_____  \ \_____  \    |    | /    ~    \    __)_   /   |   \|    |   /  \ /  \|    |  _/|    __)_  |       _/
\    \_\  \    |  / |        \/        \/        \   |    | \    Y    /        \ /    |    \    |  /    Y    \    |   \|        \ |    |   \
 \______  /______/ /_______  /_______  /_______  /   |____|  \___|_  /_______  / \____|__  /______/\____|__  /______  /_______  / |____|_  /
        \/                 \/        \/        \/                  \/        \/          \/                \/       \/        \/         \/ 
'''

def print_everything():
    print(ART)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")


def start():
    print_everything()
    number = random.randint(1,100)
    level = input("Choose a difficulty level. Type 'easy' or 'hard\n")
    lives = 0

    if level == 'easy':
         lives = 10
    else:
         lives = 5
    

    keep_play = True
    while keep_play:
        guess = int(input("Make a guess\n"))
        if guess < number:
            lives -= 1
            print("Too low")
            print(f"You have {lives} attempts remaining to guess the number")
        elif guess > number:
            lives -= 1
            print("Too high")
            print(f"You have {lives} attempts remaining to guess the number")
        else:
            keep_play = False
            print(f"You got it right. The answer is {lives}")

        if lives > 0:
            continue
        else:
            keep_play = False
            print(f"Game over. The answer is {number}. Try again.")

start()




