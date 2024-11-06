class DiscountStrategy:
    def get_discount(self, price):
        raise NotImplementedError

class DefaultDiscount(DiscountStrategy):
    def get_discount(self, price):
        return price * 0.1

class VolumeDiscount(DiscountStrategy):
    def get_discount(self, price):
        if price > 100:
            return price * 0.2
        return 0

class Product:
    def __init__(self, name, price, discount_strategy=DefaultDiscount()):
        self.name = name
        self.price = price
        self.discount_strategy = discount_strategy

    def get_final_price(self):
        return self.price - self.discount_strategy.get_discount(self.price)