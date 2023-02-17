MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
turn_off = False
while not turn_off:
    ask = str(input("What would you like? (espresso/latte/cappuccino)?: "))
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    if ask == 'espresso':
        if resources["water"] >= 50:
            if resources["coffee"] >= 18:
                resources["water"] = resources["water"] - 50
                resources["coffee"] = resources["coffee"] - 18
                print("Please insert coins")
                cquarters = float(input("How many quarters?: "))
                cdimes = float(input("How many dimes?: "))
                cnickles = float(input("How many nickles?: "))
                cpennies = float(input("How many pennies?: "))
                quarters = quarters * cquarters
                dimes = dimes * cdimes
                nickles = nickles * cnickles
                pennies = pennies * cpennies
                sum = pennies + nickles + dimes + quarters
                if sum < 1.5:
                    print("Sorry that's not enough money. Money refunded.")
                    sum = 0
                elif sum > 1.5:
                    sum = sum - 1.5
                    print(f"Here is ${sum} dollars in change")
                    print("Here is your espresso. Enjoy!")
                    sum = 0
                elif sum == 1.5:
                    print("Here is your espresso. Enjoy!")

            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")

    if ask == 'latte':
        if resources["water"] >= 200:
            if resources["coffee"] >= 25:
                if resources["milk"] >= 150:
                    print("Please insert coins")
                    resources["water"] = resources["water"] - 200
                    resources["coffee"] = resources["coffee"] - 24
                    resources["milk"] = resources["milk"] - 150
                    cquarters = float(input("How many quarters?: "))
                    cdimes = float(input("How many dimes?: "))
                    cnickles = float(input("How many nickles?: "))
                    cpennies = float(input("How many pennies?: "))
                    quarters = quarters * cquarters
                    dimes = dimes * cdimes
                    nickles = nickles * cnickles
                    pennies = pennies * cpennies
                    sum = pennies + nickles + dimes + quarters
                    if sum < 1.5:
                        print("Sorry that's not enough money. Money refunded.")
                        sum = 0
                    elif sum > 1.5:
                        sum = sum - 1.5
                        print(f"Here is ${sum} dollars in change")
                        print("Here is your espresso. Enjoy!")
                        sum = 0
                    elif sum == 1.5:
                        print("Here is your espresso. Enjoy!")

                else:
                    print("Sorry there is not enough coffee")
            else:
                print("Sorry there is not enough water")
        else:
            print("Sorry there is not enough water")

    if ask == 'cappuccino':
        if resources["water"] >= 250:
            if resources["coffee"] >= 24:
                if resources["milk"] >= 100:
                    resources["water"] = resources["water"] - 250
                    resources["coffee"] = resources["coffee"] - 24
                    resources["milk"] = resources["milk"] - 100
                    print("Please insert coins")
                    cquarters = float(input("How many quarters?: "))
                    cdimes = float(input("How many dimes?: "))
                    cnickles = float(input("How many nickles?: "))
                    cpennies = float(input("How many pennies?: "))
                    quarters = quarters * cquarters
                    dimes = dimes * cdimes
                    nickles = nickles * cnickles
                    pennies = pennies * cpennies
                    sum = pennies + nickles + dimes + quarters
                    if sum < 1.5:
                        print("Sorry that's not enough money. Money refunded.")
                        sum = 0
                    elif sum > 1.5:
                        sum = sum - 1.5
                        print(f"Here is ${sum} dollars in change")
                        print("Here is your espresso. Enjoy!")
                        sum = 0
                    elif sum == 1.5:
                        print("Here is your espresso. Enjoy!")

                else:
                    print("Sorry there is not enough coffee")
            else:
                print("Sorry there is not enough water")
        else:
            print("Sorry there is not enough water")

    if ask == 'report':
        print(f'Water: {resources["water"]}')
        print(f'Milk: {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(f'Money: {sum}')

    if ask == 'off':
        turn_off = True
