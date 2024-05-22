import random


def get_player_choice():
    while True:
        try:
            player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors  "))
            if player in [0,1,2]:
                return player
            else:
                print("Invalid choice.Please enter 0, 1, 2")
        except:
            print("invalid input. Please enter a number (0, 1, 2) ")

def start_game(player):

    # Define game variables
    rock = '''

Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''

Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''

Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


    if player == 0:
        player_choice = rock
    elif player == 1:
        player_choice = paper
    else:
        player_choice = scissors

    print(f'''
You choose:
          
{player_choice}''')

    comp = random.randint(0,2)

    if comp == 0:
        comp_choice = rock
    elif comp == 1:
        comp_choice = paper
    else:
        comp_choice = scissors

    print(f'''
Computer choose:
          
{comp_choice}''')

    if player_choice == comp_choice:
        print("You draw")
    elif player_choice == rock and comp_choice == paper:
        print("You lose")
    elif player_choice == rock and comp_choice == scissors:
        print("You win")
    elif player_choice == paper and comp_choice == rock:
        print("You win")
    elif player_choice == paper and comp_choice == scissors:
        print("You lose")
    elif player_choice == scissors and comp_choice == rock:
        print("You lose")
    elif player_choice == scissors and comp_choice == paper:
        print("You win")

player = get_player_choice()
start_game(player)