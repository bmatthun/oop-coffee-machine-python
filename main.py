import sys

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def make_summarized_report():
    money_machine.report()
    coffee_maker.report()

def operate():
    while True:
        user_input = input(f"What would you like to order? {menu.get_items()}")
        if user_input.lower() == "report":
            make_summarized_report()
        elif user_input.lower() == "off":
            break
        else:
            selected_menu_item = menu.find_drink(user_input)
            is_paid = money_machine.make_payment(selected_menu_item.cost)
            if is_paid:
                is_sufficient = coffee_maker.is_resource_sufficient(selected_menu_item)
                if is_sufficient:
                    coffee_maker.make_coffee(selected_menu_item)

operate()
