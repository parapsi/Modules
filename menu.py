class MenuCategory:
    def __init__(self):
        self.categories = {}

    def add_dishes(self, name, dish):
        if self.categories.get(name, False) is False:

            self.categories[name] = [[dish.name, dish.price]]
        else:
            self.categories[name].append([dish.name, dish.price])

    def __str__(self):
        res = ""
        for category in self.categories:
            res += f'{category.upper()}:\n'
            for dish in self.categories[category]:
                res += f"{dish[0]}: {dish[1]} dollars\n"

        return res
