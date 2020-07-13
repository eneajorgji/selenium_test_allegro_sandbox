class CartItem:
    def __init__(self, name, index, count, price):
        self.name = name
        self.index = index
        self.count = count
        self.price = price

    def compute_total_price(self):
        return self.price * self.count
