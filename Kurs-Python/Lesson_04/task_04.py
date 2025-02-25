"""
Task 3
Исходные данные:
 есть длина, ширина
 и высота склада,
 а также длина,
  ширина и высота коробки.
Напишите программу, которая запрашивает эти данные у пользователя, сохраняет эти данные в переменных, вычисляет и выводит в консоль, сколько коробок поместится на склад.
"""

sklad_length = int(input("Введите длину склада: "))
sklad_width = int(input("Введите ширину склада: "))
sklad_heigth = int(input("Введите высоту склада: "))

box_length = int(input("Введите длину коробки: "))
box_width = int(input("Введите ширину коробки: "))
box_heigth = int(input("Введите высоту коробки: "))

storage_v = sklad_length * sklad_width * sklad_heigth
storage_b = box_length * box_width * box_heigth

boxing = storage_v // storage_b

print("На склад поместиться", int(boxing), "коробок" )

