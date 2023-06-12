class CoffeeMaker:
    profit = 0

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def process_coffee(self, a_choice_ingredients):
        for item in a_choice_ingredients:
            self.resources[item] -= a_choice_ingredients[item]

    def sufficient_ingredients(self, a_choice_ingredients):
        for item in a_choice_ingredients:
            if a_choice_ingredients[item] > self.resources[item]:
                return False
        return True

    def refill_machine(self):
        self.resources["water"] = 1000
        self.resources["coffee"] = 300
        self.resources["milk"] = 500

    def print_report(self):
        print(f"water: {self.resources.get('water')}ml")
        print(f"coffee: {self.resources.get('coffee')}g")
        print(f"milk: {self.resources.get('milk')}ml")

