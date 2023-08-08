import ds_exception
import logg

class Order:
    def __init__(self):
        self.your_order = {}

    def add_item(self, item):
        self.your_order[item.name] = item.price

    def remove_item(self, item):
        del self.your_order[item]

    def calculate_total(self, discount):
        self.discount = discount
        summ = 0
        if discount.discount() >= 100 or discount.discount() <= 0:
            logg.logger.error(f"Wrong discount value, {100 - discount.discount()*100:.2f}%")
            raise ds_exception.DiscountException("Wrong discount!!")

        for item in self.your_order:
            summ += self.your_order[item]

        logg.logger.info(f"discount: {100 - discount.discount()*100:.2f}%, sum: {summ * discount.discount():.2f}")
        return summ * discount.discount()

    def __str__(self):
        res = ''
        for item in self.your_order:
            res += f'{str(item)} '
        return f"Your order: {res}\nTotal is {self.calculate_total(self.discount)} dollars"