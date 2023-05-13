from datetime import date, datetime


def task1():
    # Напишите функцию, которая проверяет, делится ли введенное число на 3, или нет.
    x = int(input("Введите число: "))
    if x % 3 ==0:
        print("Делится")
    else:
        print ("Не делится")
def task2():
    # Напишите программу деления числа 100 на введенное пользователем число. Деление реализуйте с помощью функции.
    # Предусмотрите возможные исключения (ValueError, возникающее в случае,
    # если пользователь введет не число, а строку, и ZeroDivisionError – если будет введено число 0 и остальные).

    try:
        x = int(input("Введите число: "))
    except ValueError:
        print("Введите число!")
        task2()
        return
    try:
        x/x
    except ZeroDivisionError:
        print("Число не делится!")
        task2()
        return
    if x % 100 == 0:
        print("Делится")
    else:
        print("Не делится")
def task3():

    # Напишите функцию, которая возвращает True, если введенная пользователем дата является магической,
    # и False в обратном случае. Магической считается дата,
    # в которой произведение дня и месяца равно двум последним цифрам года, например: 02.11.2022.
    x = datetime.strptime(input("Введите дату: "), "%d.%m.%Y")
    if str(x.day * x.month) == str(x.year)[2:]:
        print("Магическая дата")
    else:
        print("Сосём лапу")

def task4():
    # "Счастливым" называют билет с номером, в котором сумма первой половины цифр
    # равна сумме второй половины цифр. Номера могут быть произвольной длины,
    # с единственным условием, что количество цифр всегда чётно, например: 33 или 2341 и так далее.
    # Билет с номером 385916 — счастливый, так как 3 + 8 + 5 == 9 + 1 + 6.
    # Билет с номером 231002 не является счастливым, так как 2 + 3 + 1 != 0 + 0 + 2
    # Реализуйте функцию, проверяющую является ли номер счастливым (номер — всегда строка).
    print("Введите номер билета: ")
    a = [int(i) for i in input()]
    if len(a)% 2 != 0:
        print("Введите четное кол-во чисел: ")
        task4()
        return
    if sum(a[:int(len(a)/2)]) == sum(a[int(len(a)/2):]):
        print("Счастливый билет!")
    else:
        print("Не является счастливым билетом:(")

task1()
task2()
task3()
task4()