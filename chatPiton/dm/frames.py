class Frame:
    def __init__(self) -> None:
        super().__init__()

    def set_ingredient(self, ingredient):
        for attribute, value in self.__dict__.items():
            if value is None:
                setattr(self, attribute, ingredient)
                break

    def get_ingredients(self):
        ingredients = []
        for attribute, value in self.__dict__.items():
            if value is not None:
                ingredients.append(value.name)
        return ingredients

    def is_complete(self):
        ing = 0
        for attribute, value in self.__dict__.items():
            if value is not None:
                ing += 1
        return float(ing * 100 / len(self.__dict__.items()))

    def show_attributes(self):
        for attribute, value in self.__dict__.items():
            if value is not None:
                print(attribute, '=', value.name)
            else:
                print(attribute, '=', value)


class PotionFrame(Frame):
    def __init__(self, name, ingredients: list):
        super().__init__()
        self.name = name
        self._ingredients = ingredients

    def set_ingredient(self, ingredient):
        self._ingredients.append(ingredient)

    def get_ingredients(self):
        return [ingredient for ingredient in self._ingredients]

    def is_complete(self):
        return float(len(self._ingredients) * 100 / len(self._ingredients))

    def show_attributes(self):
        for attribute, value in self.__dict__.items():
            if value is not None:
                print(attribute, '=', value)
            else:
                print(attribute, '=', value)


class IngredientFrame:
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
