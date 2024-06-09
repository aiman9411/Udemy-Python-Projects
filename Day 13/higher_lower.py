import game_data
import random

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     


"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

"""

def compare(number):
    first_follower_count = game_data.data[number]['follower_count']
    second_follower_count = game_data.data[number + 1]['follower_count']
    if first_follower_count > second_follower_count:
        return 'a'
    else:
        return 'b'



def start():
    print(logo)
    score = 0
    random_number = random.randint(0, len(game_data.data) - 2)

    while True:
        first_profile = game_data.data[random_number]
        second_profile = game_data.data[random_number + 1]
        print(f"Compare A: {first_profile['name']}, a {first_profile['description']} from {first_profile['country']}")
        print(vs)
        print(f"Compare B: {second_profile['name']}, a {second_profile['description']} from {second_profile['country']}")
        correct_answer = compare(random_number)
        guess = input("Who has more followers? Type 'A' or 'B'\n").lower()
        if correct_answer == guess:
            score += 1
            print(f"You are right. Current score: {score}")
            random_number += 1

            if random_number >= len(game_data.data) -1 :
                random_number = 0
        else:
            correct_answer = False
            print(f"Sorry, that's is wrong. Final score: {score}")
            print(f"{first_profile['name']} : {first_profile['follower_count']}")
            print(f"{second_profile['name']} : {second_profile['follower_count']}")
            break


start()


