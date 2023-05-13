from lab_12.components.IceCream import IceCream


class IceCreamSoft(IceCream):
    name = "Мягкое"

    def __init__(self, flavor):
        super().__init__(flavor)

    def sell(self):
        print("Продавец накручивает мороженое в рожок и передает покупателю")