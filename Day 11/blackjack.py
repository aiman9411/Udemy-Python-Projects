from typing import List
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
    
    def draw_more_card(the_cards):
        random_number = random.randint(0, len(cards) - 1)
        the_cards.append(cards[random_number])
        total = sum(the_cards)
        return the_cards, total


    def gen_comp_card():
        one_card = []
        random_number = random.randint(0, len(cards) - 1)
        one_card.append(cards[random_number])
        sum_com_card = sum(one_card)
        return one_card, sum_com_card
    
    
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n").lower()

    if play == 'y':
        print(art.logo)
        two_cards, sum_value = draw_first()
        comp_card, sum_com_card = gen_comp_card()
        print(f"Your cards: {two_cards}, current score: {sum_value}")
        print(f"Computer's first card: {comp_card}, current score: {sum_com_card}")

        if sum_value == 21:
            print("Win with a blackjack 😎")

        more_card = True
        
        while more_card:
            play_again = input("Type 'y' to get another card, type 'n' to pass\n").lower()
            if play_again == 'y':
                added_cards, total = draw_more_card(two_cards)
                print(f"Your cards {added_cards}, current score: {total}")
                two_cards = added_cards
                sum_value = total

                if sum_value > 21:
                    more_card = False
                    print("You went over. You lose 😤")
                elif sum_value == 21:
                    more_card = False
                    print("Win with a blackjack 😎")
            else:
                more_card = False
                print(f"Your final hand: {two_cards}, final_score: {sum_value}")
                while sum_com_card < 17:
                    new_comp_cards, sum_com_card = draw_more_card(comp_card)
                print(f"Computer's final hand: {new_comp_cards}, final score: {sum_com_card}")

                if sum_com_card > 21:
                    print("Opponent went over. You win 😁")
                elif sum_com_card == 21:
                    print("Lose, opponent has Blackjack 😱")
                elif sum_value > sum_com_card:
                    print("You win 😃")
                elif sum_value < sum_com_card:
                    print("You lose 😤")
                elif sum_value == sum_com_card:
                    print("Draw 🙃")

    else:
        print("Come again.")

game()
