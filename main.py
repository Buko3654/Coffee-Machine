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

emoji = "☕"

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0
is_on = True


def report(resources, till):
    """Prints the amount of resources left in the machine."""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${till}")


def check_resources(order_ingredients):
    """Determines if enough ingredients on hand to make the order."""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def payment(menu, request):
    """Takes coins, determines if enough, and returns change."""
    print("Please insert coins.")
    cost = menu[request]["cost"]
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)
    if total >= cost:
        change = total - cost
        change = round(change, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


while is_on:
    order = input("What would you like? (espresso, latte, cappuccino): ")
    processed = False
    if order == "off":
        is_on = False
    elif order == "report":
        report(resources, money)
    else:
        if check_resources(order["ingredients"]):
            if payment(MENU, order):
                money += MENU[order]["cost"]
                for ingredient in MENU[order]["ingredients"]:
                    resources[ingredient] -= MENU[order]["ingredients"][ingredient]
                print(f"Here is your {order} {emoji}. Enjoy!")
