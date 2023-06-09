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
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}


def process_coins():
    total = int(input("number of 10c: ")) * 0.1
    total += int(input("number of 20c: ")) * 0.2
    total += int(input("number of 50c: ")) * 0.5
    total += int(input("number of 1€: ")) * 1.0
    total += int(input("number of 2€: ")) * 2.0
    return_money = input("return money(y/n): ")
    if return_money == "y":
        total = -1
    return total


def process_coffee(a_choice_ingredients):
    for item in a_choice_ingredients:
        resources[item] -= a_choice_ingredients[item]


def sufficient_money(required):
    an_amount = 0.0
    while (an_amount < required) & (an_amount > -1.0):
        print(f"input of coins, current {an_amount}€ of {required}€ ")
        an_amount += process_coins()
    return an_amount


def sufficient_ingredients(a_choice_ingredients):
    for item in a_choice_ingredients:
        if a_choice_ingredients[item] >= resources[item]:
            return False
    return True


def print_report():
    print(f"water: {resources.get('water')}ml")
    print(f"coffee: {resources.get('coffee')}g")
    print(f"milk: {resources.get('milk')}ml")
    print(f"money: {profit}€")


def make_coffee(a_choice):
    print(f"my choice: {a_choice}")
    if sufficient_ingredients(a_choice["ingredients"]):
        total = sufficient_money(a_choice["cost"])
        if total >= 0:
            print("starting process")
            process_coffee(a_choice["ingredients"])
            amount = total - a_choice["cost"]
            print(f"please take your {a_choice}")
            print(f"returning {amount}€")
        else:
            print("process cancelled by user")
    else:
        print("insufficient ingredients")


cont = True
while cont:
    choice = input("choose your desired drink (espresso, latte, cappuccino): ")
    match choice:
        case "off":
            cont = False
        case "report":
            print_report()
        case "cappuccino" | "latte" | "espresso":
            make_coffee(MENU[choice])
        case other:
            print("incorrect command")


def print_hi(name, resources):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}, {resources.get("water")}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm', resources)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
