from gui.IceCreamGUI import IceCreamGUI
from components.IceCreamStand import IceCreamStand
from components.IceCream import IceCream
from components.IceCreamSoft import IceCreamSoft
from components.IceCreamPopsicle import IceCreamPopsicle


def task1():
    print("\nЗадание 1 - вывод")
    ice_cream_stand = IceCreamStand("Тает лёд", "Грибы")
    ice_cream_stand.open_restaurant()
    ice_cream_stand.describe_restaurant()

    daily_ice_creams = [
        IceCream("Ванильное"),
        IceCreamSoft("Шоколадное"),
        IceCreamPopsicle("Коньячное")
    ]
    for ice_creams in daily_ice_creams:
        ice_cream_stand.add_ice_cream(ice_creams)
    ice_cream_stand.show_ice_creams()

    for ice_creams in daily_ice_creams:
        ice_cream_stand.remove_ice_cream()

    ice_cream_stand.show_ice_creams()



def task2():
    print("\nЗадание 2 - добавление")
    ice_cream_stand = IceCreamStand("Тает лёд", "Грибы")
    ice_cream_stand.add_flavor()
    ice_cream_stand.remove_flavor(input("Введите сорт мороженого для удаления: "))

    if ice_cream_stand.check_flavor(input("Введите сорт мороженого для проверки: ")):
        print("Содержится")
    else:
        print("Не содержится")



def task3():
    print("\nЗадание 3 - вывод окна")
    ice_cream_stand = IceCreamStand("Тает лёд", "Грибы")
    gui = IceCreamGUI(ice_cream_stand)


if __name__ == '__main__':
    task1()
    task2()
    task3()

