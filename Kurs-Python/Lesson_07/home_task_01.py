"""
Task 1.
Напишите функцию, которой можно передать целое число.
Функция должна возвращать True, если число попадает в диапазон от 10 до 30 включительно.
В остальных случаях функция должна возвращать False.

Вызовите функцию несколько раз, передав ей различные аргументы, и выведите результаты в консоль.

"""

def check_number(num):
    return num >= 10 and  num <= 30


# True
num = 12
num1 = 26
# False
num2 = 8
num3 = 56

print(num, check_number(num))
print(num1, check_number(num1))
print(num2, check_number(num2))
print(num3, check_number(num3))