import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    is_on = True
    while is_on:
        choice = input("What would you like? (small/medium/large/off/report): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            for item, amount in resources.items():
                print(f"{item}: {amount}")
        elif choice in recipes:
            sandwich = recipes[choice]
            if not sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                print("Sorry, there is not enough ingredients to make this sandwich.")
                continue

            coins = cashier_instance.process_coins()
            if cashier_instance.transaction_result(coins, sandwich["cost"]):
                sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])

if __name__=="__main__":
    main()