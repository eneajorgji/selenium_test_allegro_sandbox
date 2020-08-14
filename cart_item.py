class CartItem:
    def __init__(self, name=None, index=0, count=0, price=0):
        self.name = name
        self.index = index
        self.count = count
        self.price = price

    def compute_total_price(self):
        return self.price * self.count
