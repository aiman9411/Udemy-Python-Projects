MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nProfit: {profit}")


def start():
    drink = input("What would you like? (espresso, latte, cappucino):\n")

    def calculate_balance(total_money):
        balance = total_money - MENU[drink]["cost"]
        return balance
    
    # def check_resource():
    #     for item in MENU:

    

    if drink == "report":
        report()

    else:
        print("Please insert coins.")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))

        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        balance = calculate_balance(total)
        
        if balance >= 0:
            update_resource()
            profit += MENU[drink]["cost"]
            print(f"Here is your {balance} in change.")
            print(f"Here is your {drink}. Enjoy!")




