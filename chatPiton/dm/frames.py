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


class IngredientFrame:
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name


# class PolyjuiceFrame(Frame):
#     name = 'polyjuice'
#
#     def __init__(self) -> None:
#         super().__init__()
#         self._ingredient1 = None
#         self._ingredient2 = None
#         self._ingredient3 = None
#         self._ingredient4 = None
#         self._ingredient5 = None
#         self._ingredient6 = None
#         self._ingredient7 = None
#
#
# class ArmadilloBileMixtureFrame(Frame):
#     name = 'armadillo bile mixture'
#
#     def __init__(self) -> None:
#         super().__init__()
#         self._ingredient1 = None
#         self._ingredient2 = None
#         self._ingredient3 = None
#         self._ingredient4 = None
#         self._ingredient5 = None
#         self._ingredient6 = None
#         self._ingredient7 = None
#
#
# class AnimagusFrame(Frame):
#     name = 'animagus'
#
#     def __init__(self) -> None:
#         super().__init__()
#         self._ingredient1 = None
#         self._ingredient2 = None
#         self._ingredient3 = None
#         self._ingredient4 = None

class AmortentiaFrame(Frame):
    name = 'amortentia'

    def __init__(self) -> None:
        super().__init__()
        self._ingredient1 = None
        self._ingredient2 = None
        self._ingredient3 = None
        self._ingredient4 = None


class ObliviousFrame(Frame):
    name = 'oblivious'

    def __init__(self) -> None:
        super().__init__()
        self._ingredient1 = None
        self._ingredient2 = None
        self._ingredient3 = None
        self._ingredient4 = None


class AgeingFrame(Frame):
    name = 'ageing'

    def __init__(self) -> None:
        super().__init__()
        self._ingredient1 = None
        self._ingredient2 = None
        self._ingredient3 = None
        self._ingredient4 = None


class FelixFelicisFrame(Frame):
    name = 'felix felicis'

    def __init__(self) -> None:
        super().__init__()
        self._ingredient1 = None
        self._ingredient2 = None
        self._ingredient3 = None
        self._ingredient4 = None
        self._ingredient5 = None
        self._ingredient6 = None



class LivingDeatchDistillateFrame(Frame):
    name = 'living death distillate'

    def __init__(self) -> None:
        super().__init__()
        self._ingredient1 = None
        self._ingredient2 = None
        self._ingredient3 = None
        self._ingredient4 = None
        self._ingredient5 = None
        self._ingredient6 = None
        self._ingredient7 = None
