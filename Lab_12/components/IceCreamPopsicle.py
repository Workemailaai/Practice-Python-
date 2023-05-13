from Lab_12.components.IceCream import IceCream


class IceCreamPopsicle(IceCream):
    name = "Мороженое на палочке"

    def __init__(self, flavor):
        super().__init__(flavor)

    def sell(self):
        print("Продавец берет за палочку мороженое и передает покупателю")