import random
import art

def game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def draw_first():
        two_cards = []
        sum_value = 0
        for i in range(2):
            random_number = random.randint(0, len(cards) - 1)
            two_cards.append(cards[random_number])
            sum_value += cards[random_number]
        return two_cards, sum_value

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n").lower()

    if play == 'y':
        continue_game = True
        while continue_game:
            print(art.logo)
            two_cards, sum_value = draw_first()
            print(f"Your cards: {two_cards}, current score: {sum_value}")
            play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n").lower()
            
            if play_again == 'n':
                continue_game = False
                print("Come again")

    else:
        print("Come again.")

game()








