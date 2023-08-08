import logg
class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        if not isinstance(name, str):
            logg.logger.error("Error in product name")
            raise TypeError("Error in product name")
        if not isinstance(description, str):
            logg.logger.error("Error in product description")
            raise TypeError("Error in product discription")
        if not isinstance(price, int | float) or price <= 0:
            logg.logger.error("Error in product value")
            raise ValueError("Error in product price")
        logg.logger.info(f"{self.name}, {self.description}, {self.price}")

    def __str__(self):
        return f"{self.name}{self.description}{self.price}"