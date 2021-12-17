from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# import sys
import os

os_clear = "cls" if os.name == "nt" else "clear"

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_items = menu.get_items()

while True:
    choice = input(f"What would you like? ({menu_items}): ")
    if choice == "off":
        break
        # sys.exit()
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        found_drink = menu.find_drink(choice)
        print(found_drink)
        if found_drink:
            if coffee_maker.is_resource_sufficient(found_drink):
                coffee_maker.make_coffee(found_drink)
                money_machine.make_payment(found_drink.cost)
