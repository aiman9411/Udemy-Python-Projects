# Import os module to use operating system funtionality i.e. clear
import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


# Define function
def start_auction():

    bid_list = []
    # Flag variable to check while loop necessity
    other_bidder = True
    # Define function to append new dictionary into list
    def add_bid(name, bid):
        bid_list.append({'name': name, 'bid': bid})
    # Request for name and bid price
    while other_bidder:
        print(logo)
        name = input("Type your name\n")
        bid = input("Type your bid price\n")
        add_bid(name, bid)
        more_bidder = input("Is there any other bidder? Answer yes or no\n").lower()
        if more_bidder == 'yes':
            os.system('clear')
        else:
            other_bidder = False
    # If there is no more bidder
    highest_bid = max(bid_list, key = lambda x: x['bid'])
    print(f'The highest bidder is {highest_bid["name"]} with a bid of {highest_bid["bid"]}')

start_auction()
