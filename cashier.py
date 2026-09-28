class Cashier:
    def __init__(self):
        self.coins = 0

    def process_coins(self):
        large = int(input("how many large bills?: "))
        half_dollar = int(input("how many half dollars?: "))
        quarter = int(input("how many quarters?: "))    
        nickel = int(input("how many nickels?: "))

        total = large * 1.00 + half_dollar * 0.50 + quarter * 0.25 + nickel * 0.05
        return total


    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False