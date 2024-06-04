import art

def start():
    print(art.logo)

    symbol = ["+", "-", "*", "/"]

    def add(a, b):
        return a + b
    
    def minus(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        return a / b
    
    def calculate(first_number, operation, next_number):
        if operation == "+":
            return add(first_number, next_number)
        elif operation == "-":
            return minus(first_number, next_number)
        elif operation == "*":
            return multiply(first_number, next_number)
        elif operation == "/":
            return divide(first_number, next_number)

    
    more_calculation = True
    first_number = int(input("What is your first number?\n"))

    while more_calculation:
        for i in symbol:
            print(i)
        operation = input("Pick an operation.\n")

        if operation not in symbol:
            print("Please enter a valid operation")
            continue

        next_number = int(input("What's the next number?\n"))
        result = calculate(first_number, operation, next_number)
        print(f'{first_number} {operation} {next_number} = {result}')
        continue_calc = input(f"Type y to continue the calculation or n to exit\n")

        if continue_calc != 'y':
            more_calculation = False
        else:
            first_number = result

    print("See your again.")
start()
        



