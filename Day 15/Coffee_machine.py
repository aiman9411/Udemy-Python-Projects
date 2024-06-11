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



resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nProfit: {profit}")


def start():

    profit = 0
    
    drink = input("What would you like? (espresso, latte, cappucino):\n")

    def calculate_balance(total_money):
        balance = total_money - MENU[drink]["cost"]
        return balance
    
    def check_resource(water):
        for item in MENU:
            portion = MENU[water]["ingredients"]
            for sample in portion:
                if portion[sample] < MENU[water]["ingredients"][sample]:
                    print("Sorry we have insufficient resources. Kindly come back later")
        return True

    def update_resources():
        if check_resource(drink):
            for item in resources:
                resources[item] -= MENU[drink]["ingredients"][item]
    

    if drink == "report":
        report()

    else:
        print("Please insert coins.")
        quarters = int(input("How many quarters?\n"))
        dimes = int(input("How many dimes?\n"))
        nickles = int(input("How many nickles?\n"))
        pennies = int(input("How many pennies?\n"))

        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

        def check_money(water):
            if total >= MENU[water]["cost"]:
                return True
            else:
                return False

        
        sufficient_money = check_money(drink)

        if sufficient_money:
            balance = round(calculate_balance(total),2)
            check_resource(drink)
            update_resources()
            profit += MENU[drink]["cost"]
            print(profit)
            print(f"Here is your {balance} in change.")
            print(f"Here is your {drink}. Enjoy!")
        
        else:
            print("Insufficient money. Please come back later")


start()
