
class CoffeeMachine:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 0
        self.drinks = {
            "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.50},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.50},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.00}
        }

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: ${self.money:.2f}")

    def sources(self, drink):
        water = self.drinks[drink]["water"]
        milk = self.drinks[drink]["milk"]
        coffee = self.drinks[drink]["coffee"]
        if self.water < water:
            print("Sorry, there is not enough water.")
            return False
        if self.milk < milk:
            print("Sorry, there is not enough milk.")
            return False
        if self.coffee < coffee:
            print("Sorry, there is not enough coffee.")
            return False
        return True

    def make_coffee(self, drink):
        water = self.drinks[drink]["water"]
        milk = self.drinks[drink]["milk"]
        coffee = self.drinks[drink]["coffee"]
        cost = self.drinks[drink]["cost"]
        self.water -= water
        self.milk -= milk
        self.coffee -= coffee
        self.money += cost
        print(f"Here is your {drink}. Enjoy!")

    def main(self):
        while True:
            user_input = input("What would you like? (espresso/latte/cappuccino): ")
            if user_input == "off":
                break
            elif user_input == "report":
                self.report()
            elif user_input in self.drinks:
                if self.sources(user_input):
                    self.make_coffee(user_input)
            else:
                print("Invalid input.")

if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.main()

