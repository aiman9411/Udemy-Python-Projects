#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_password():
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    password = ''

    len_letters = len(letters)
    for i in range(nr_letters):
        number = random.randint(0, len_letters - 1)
        password += letters[number]

    len_symbols = len(symbols)
    for i in range(nr_symbols):
        number = random.randint(0, len_symbols - 1)
        password += symbols[number]

    len_numbers = len(numbers)
    for i in range(nr_numbers):
        number = random.randint(0, len_numbers - 1)
        password += numbers[number]
    
    print(f'Your password is: {password}')

gen_password()
