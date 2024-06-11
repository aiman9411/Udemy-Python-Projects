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

def check_zero():
    for item in resources:
        if resources[item] <= 0:
            return False
    return True



def start():
    profit = 0
    start_mode = True

    def report():
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nProfit: {profit}")

    def check_resource(drink):
        for item in MENU[drink]["ingredients"]:
            if resources[item] < MENU[drink]["ingredients"][item]:
                print("Insufficient resource. Please choose another drink")
                return False
        return True
    
    while start_mode:
        drink = input("What would you like? (espresso, latte, cappuccino):\n")
        
        if drink == "off":
            print("Turning off the coffee machine...")
            break
        elif drink == "report":
            report()
            continue
        elif drink not in MENU:
            print("Please chooese a valid drink")
            continue

        
        if not check_resource(drink):
            continue

        def calculate_balance(total_money):
            balance = total_money - MENU[drink]["cost"]
            return balance

        def update_resources():
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
                update_resources()
                profit += MENU[drink]["cost"]
                print(f"Here is your {balance} in change.")
                print(f"Here is your {drink} \u2615. Enjoy!")
                start_mode = check_zero()
            
            elif sufficient_money == False:
                print("Insufficient money. Please come back later.")
                break


start()
