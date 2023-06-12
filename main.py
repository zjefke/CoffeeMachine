from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu_item import MenuItemFactory

mm = MoneyMachine()
cm = CoffeeMaker()


def make_coffee(choice_as_string, a_choice):
    print(f"my choice: {a_choice.name}")
    if a_choice.ingredients["water"] > 0 & cm.sufficient_ingredients(a_choice.ingredients):
        mm.total = mm.sufficient_money(a_choice.cost)
        if mm.total >= 0:
            print("starting process")
            cm.process_coffee(a_choice.ingredients)
            mm.amount = mm.total - a_choice.cost
            print(f"please take your {choice_as_string} ☕")
            print(f"returning {mm.amount}€")
            mm.profit += a_choice.cost
        else:
            print("process cancelled by user")
            mm.total = 0
    else:
        print("insufficient ingredients")


cont = True
while cont:
    choice = input("choose your desired drink (espresso, latte, cappuccino): ")
    if choice == "off" or choice == "exit":
        cont = False
    elif choice == "report":
        cm.print_report()
        mm.print_report()
    elif choice == "refill":
        cm.refill_machine()
    elif choice in MenuItemFactory.get_all_menu_items():
        make_coffee(choice, MenuItemFactory.get_menu_item(choice))
    else:
        print("incorrect command")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
