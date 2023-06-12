class MenuItemFactory:

    @staticmethod
    def get_all_menu_items():
        return ["cappuccino", "latte", "espresso"]

    @staticmethod
    def get_menu_item(choice):
        a_menu_item = MenuItem()
        a_menu_item.set_name(choice)
        match choice:
            case "cappuccino":
                a_menu_item.set_ingredients(250, 100, 25)
                a_menu_item.set_cost(3.0)
                return a_menu_item
            case "latte":
                a_menu_item.set_ingredients(200, 150, 25)
                a_menu_item.set_cost(2.5)
                return a_menu_item
            case "espresso":
                a_menu_item.set_ingredients(50, 0, 15)
                a_menu_item.set_cost(1.5)
                return a_menu_item
            case other:
                print("no such menu item")
                a_menu_item.set_ingredients(-1, -1, -1)
                return a_menu_item


class MenuItem:

    def __init__(self):
        self.name = ""
        self.ingredients = {}
        self.cost = 0.0

    def set_name(self, name):
        self.name = name

    def set_cost(self, cost):
        self.cost = cost

    def set_ingredients(self, water, milk, coffee):
        self.ingredients["water"] = water
        self.ingredients["milk"] = milk
        self.ingredients["coffee"] = coffee
