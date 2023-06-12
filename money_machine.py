class MoneyMachine:

    def __init__(self):
        self.total = 0.0
        self.amount = 0.0
        self.profit = 0.0

    def print_report(self):
        print(f"money: {self.profit}€")

    def sufficient_money(self, required):
        an_amount = 0.0
        while (an_amount < required) & (an_amount > -1.0):
            print(f"input of coins, current {an_amount}€ of {required}€ ")
            an_amount += self.process_coins()
        return an_amount

    def process_coins(self):
        self.total += int(input("number of 10c: ")) * 0.1
        self.total += int(input("number of 20c: ")) * 0.2
        self.total += int(input("number of 50c: ")) * 0.5
        self.total += int(input("number of 1€: ")) * 1.0
        self.total += int(input("number of 2€: ")) * 2.0
        return_money = input("return money(y/n): ")
        if return_money == "y":
            self.total = -1.0
        return self.total
