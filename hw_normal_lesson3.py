__author__ = 'Екатерина Гольдфингер'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    l = [1, 1]
    for i in range(2, m):
        l.append(l[i-1] + l[i-2])
    part_fibonacci = l[n-1:m]
    return part_fibonacci




#Задача 2 (альтернативная):
#Напишите пожалуйста программу, которая открыват файл на запись, записывает туда N случайных чисел от -100 до 100
#после этого, закрывает файл.
#открывает файл снова для чтения, читает оттуда числа, и все числа, которые больше 0 записывает в новый файл.

import random
n = int(input('Введите число элементов в итоговом списке'))
random_list = []

line = ''
for i in range(n-1):
    line=line+str(random.randint(-100, 100))+','
line = line + str(random.randint(-100, 100))


with open("numbers.txt", "w", encoding="utf-8") as ft:
    ft.write (line)
    ft.close

with open("numbers.txt", "r", encoding="utf-8") as ft:
   list_from_file = ft.readline()
   list_from_file = [int(x) for x in list_from_file.split(',')]
   new_list = list(filter(lambda x: x > 0, list_from_file))
   with open("numbers2.txt", "w", encoding="utf-8") as ft:
       ft.write(str(new_list))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter(condition, list):
    """

    :param condition: условие исключения элемента из списка
    :param list: Исходный список
    :return: конечный список, без исключенных элементов
    """
    list2 = []
    for x in list:
        if condition(x):
            list2.append(x)

    return list2


#Задача 4 (альтернативная):
#Напишите функцию, которая считает сумму квадратов от своих аргументов.
#Кол-во аргументов функции может быть любым.

def squares(*args):
    """ Вычисляет сумму квадратов от своих аргументов

    :param args: числа
    :return: число, сумма квадратов для аргументов
    """
    summa = 0
    for i in args:
        i = i**2
        summa = summa + i

    return summa

