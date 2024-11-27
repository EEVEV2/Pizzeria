class Pizza:
    def __init__(self, size, ingredients):
        self.size = size
        self.ingredients = ingredients

    def __str__(self):
        return f"Pizza {self.size}, składniki: {', '.join(self.ingredients)}"

class PizzaBuilder:
    def __init__(self):
        self.size = None
        self.ingredients = []

    def set_size(self, size):
        self.size = size
        return self

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        return self

    def build(self):
        return Pizza(self.size, self.ingredients)
