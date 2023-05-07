
def task1():

    from PIL import Image, ImageFilter
    from pathlib import Path

    current_dir = ''
    filenames = Path(current_dir).glob('*')
    Path('new_images').mkdir(parents=True, exist_ok=True)

    for file in filenames:
        if file.suffix in ['.jpg', '.png']:
            with Image.open(file) as img:
                img.load()
                new_img = img.filter()
                new_img.save(Path("new_images", file))


# def task3():
#
#     # Имеется файл с данными в формате csv:
#     # Продукт,Количество,Цена
#     # Молоко,2,80
#     # Сыр,1,500
#     # Хлеб,2,70
#     # Напишите программу, которая считывает данные из этого файла,
#     # подсчитывает итоговую сумму расходов и выводит данные в виде:
#     # Нужно купить:
#     # Молоко - 2 шт. за 80 руб.
#     # Сыр - 1 шт. за 500 руб.
#     # Хлеб - 2 шт. за 70 руб.
#     # Итоговая сумма: 800 руб.
#
#
#     import csv
#     from pathlib import Path
#
#     file = open("data.csv," "r")
#     data = list(csv.reader(file, delimiter=", "))
#     print("Нужно купить: ")
#     for i in data:
#         print(f"{i[0]} - {i[1]} шт. за {i[2]} руб.")
#     print(f"Итоговая сумма: {sum([int(i[1])*int(i[2]) for i in data])} руб.")
#     file.close()

task1()