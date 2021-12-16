import sys
import os

from menu import MENU
from units import R_M, MONEY

os_clear = "cls" if os.name == "nt" else "clear"

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# Check resources sufficient
def resources_sufficient(coffee):
    """
    :param coffee:
    :return: True if resources are sufficient
             False if resources are insufficient
    """
    coffee_requirement = MENU[coffee]["ingredients"]
    for i in coffee_requirement.keys():
        if coffee_requirement[i] > resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    # print("Sufficient")
    return True

def change_resource(choice):
    """
    updates the existing resources
    """
    coffee_requirement = MENU[choice]["ingredients"]
    for i in coffee_requirement.keys():
        resources[i] -= coffee_requirement[i]

    resources["money"] += MENU[choice]["cost"]

# Process coins
def coin_sufficient(quarters, dimes, nickles, pennies, choice):
    """
    Takes the coins and process them against choice
    :return:  change if coins add up to become enough
              else change= -1
    """
    cash = quarters * MONEY["quarters"] + dimes * MONEY["dimes"] + \
           nickles * MONEY["nickles"] + pennies * MONEY["pennies"]

    cost = MENU[choice]["cost"]

    if cash >= cost:
        change = cash - cost
        change_resource(choice)
        return change
    else:
        return -1

def coffee_order():
    # Prompt user by asking for the order
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        sys.exit()
    elif choice == "report":
        for item, quantity in resources.items():
            # Print report
            if item == "money":
                print(f"\t {item.capitalize():>7}: {R_M[item]}{quantity}")
                continue
            print(f"\t {item.capitalize():>7}: {quantity}{R_M[item]}")

    else:
        if resources_sufficient(choice):
            print("Please insert coins.")
            quarters = int(input("\t How many quarters?: "))
            dimes = int(input("\t How many dimes?: "))
            nickles = int(input("\t How many nickles?: "))
            pennies = int(input("\t How many pennies?: "))

            change = coin_sufficient(quarters, dimes, nickles, pennies, choice)
            if not change == -1:
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {choice} ☕ .Enjoy!")
            else:
                print("Not Enough Cash")
        else:
            print("Fuck resource was not sufficient")




while True:
    coffee_order()
    os.system(os_clear)
