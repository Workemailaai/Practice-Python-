
import json
import os

from lab_12.components.Restaurant import Restaurant


class IceCreamStand(Restaurant):
    __flavors = []
    location = 'Санкт-Петербург'
    work_time = 'с 9 до 21'
    data_path = 'icecream.json'
    ice_creams = []

    def __init__(self, restaurant_name, cuisine_type, initial_rating=0):
        super().__init__(restaurant_name, cuisine_type, initial_rating)
        self.init_data()
        self.init_flavors()

    def init_data(self):
        self.data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'icecream.json')

    def get_location(self):
        return self.location

    def describe_restaurant(self):
        print(f"Название кафе мороженного -  {self.restaurant_name} \nВиды шариков мороженого:")

        print(*self.get_flavors(), sep="\n")

    def open_restaurant(self):
        print("Кафе сейчас открыто.")

    def get_flavors(self):
        return self.__flavors

    def init_flavors(self):
        flavors = self.get_data()["flavors"]
        for flavor in flavors:
            self.append_flavor(flavor["name"], flavor["available"], flavor["alcohol"])

    def append_flavor(self, name, available, alcohol):
        alcohol_text = " (18+)" if alcohol else ""
        if available:
            self.__flavors.append("* " + name + alcohol_text)
        else:
            self.__flavors.append("! " + name + alcohol_text + " - нет в наличии")

    def add_flavor(self):
        k = int(input("Введите количество видов мороженного для добавления: "))
        flavors = {"flavors": []}
        for i in range(k):
            name = input("Название: ")
            available = bool(input("В наличии 0/1: "))
            alcohol = bool(input("Алкогольное 0/1: "))
            flavors["flavors"].append({"name": name, "available": available, "alcohol": alcohol})
            self.append_flavor(name, available, alcohol)

        data = self.get_data()

        data["flavors"].extend(flavors["flavors"])

        # for i in data["flavors"]:
        #     print(i["name"], "- в наличии" if i["available"] else "- нет в наличии!")

        with open(self.data_path, "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def remove_flavor(self, flavor_type):
        if self.check_flavor(flavor_type):
            data = self.get_data()["flavors"]
            flavors = {"flavors": []}
            self.__flavors = []
            for flavor in data:
                if flavor_type not in flavor["name"]:
                    flavors["flavors"].append({"name": flavor["name"], "available": flavor["available"], "alcohol": flavor["alcohol"]})
                    self.append_flavor(flavor["name"], flavor["available"], flavor["alcohol"])
            with open(self.data_path, "w") as file:
                json.dump(flavors, file, indent=2, ensure_ascii=False)

    def check_flavor(self, flavor_type):
        flavors = self.get_data()["flavors"]
        for flavor in flavors:
            if flavor_type in flavor["name"]:
                return True
        return False

    def get_data(self):
        with open(self.data_path, "r") as file:
            return json.load(file)

    def add_ice_cream(self, ice_cream):
        self.ice_creams.append(ice_cream)

    def remove_ice_cream(self):
        ice_cream = self.ice_creams.pop()
        ice_cream.sell()

    def show_ice_creams(self):
        if len(self.ice_creams) == 0:
            print("Ожидаем поступления мороженого")
            return
        print("Доступное мороженное:")
        for ice_cream in self.ice_creams:
            print("- " + ice_cream.name + " - " + ice_cream.flavor)
