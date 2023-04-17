def task1():
    # Подготовьте любой графический файл для выполнения практической работы.
    # Напишите программу, которая открывает и выводит этот файл на экран.
    # Получите и выведите в консоль информацию о размере изображения, его формате, его цветовой модели.

    from PIL import Image

    filename = "wave.jpg"
    with Image.open(filename) as img:
        img.load()
        img.show()
        width, height = img.size
        format = img.format
        mode = img.mode
        print("Ширина: ", width)
        print("Высота:  ", height)
        print("Формат: ", format)
        print("Цветовая модель:", mode)

pass


def task2():

    # Напишите программу, которая создаёт уменьшенную в три раза копию изображения.
    # Получите горизонтальный и вертикальный зеркальный образ изображения.
    # Сохраните изображения в текущую папку под новым именем.
        import PIL
        from PIL import Image, ImageFilter

        filename = "wave.jpg"
        with Image.open(filename) as img:
                img.load()

        new_img = img.resize((img.width // 3, img.height // 3))

        new_img.save("wave1.jpg")
        new_img = img.rotate(180)
        new_img.save("wave2.jpg")
        new_img = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        new_img.save("wave3.jpg")


pass


def task3():

    # Подготовьте 5 графических файлов с именами 1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg.
    # Напишите программу, которая применит ко всем этим файлам сразу любой фильтр
    # (кроме размытия, т.к. он рассматривался на лекции).
    # Сохраните изображения в новую папку под новыми именами.

    from PIL import Image, ImageFilter
    filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

    for file in filenames:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.CONTOUR)
            new_img.show()
            new_img.save("new_COUNTOUR" + file)


pass


def task4():
    # Напишите программу, которая добавляет на изображение водяной знак.
    # Можно тоже применять сразу к нескольким изображениям.

    from PIL import Image

    water = "watermark.png"
    with Image.open(water) as img_water:
        img_water.load()

    img_water = Image.open(water)
    img_water = img_water.resize((img_water.width // 2, img_water.height // 2))
    filename = "Wavehost.jpg"
    with Image.open(filename) as img:
        img.load()

    img.paste(img_water, (50, 50), img_water)
    img.save("watermark_Wavehost.jpg")


task1()
task2()
task3()
task4()
