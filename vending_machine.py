import os

class VendingMachine:
    def __init__(self, items, coin_price):
        self.items = items
        self.coin_price = coin_price

    def buy(self, req_items, req_coins):
        if req_items > self.items:
            return "Not enough items in the machine"
        elif req_coins < req_items * self.coin_price:
            return "Not enough coins"
        else:
            self.items -= req_items
            return req_coins - (req_items * self.coin_price)


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        # Initial vending machine setup
        num_items, item_price = map(int, input().split())
        machine = VendingMachine(num_items, item_price)

        # Number of transactions
        n = int(input())
        for _ in range(n):
            req_items, req_coins = map(int, input().split())
            change = machine.buy(req_items, req_coins)
            fptr.write(str(change) + "\n")
