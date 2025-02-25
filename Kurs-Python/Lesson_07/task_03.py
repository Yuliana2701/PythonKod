"""
Напишите функцию, которой можно передать целое число.

Функция должна возвращать True, если число отрицательное или число чётное и одновременно положительное.
В остальных случаях функция должна возвращать False.

Вызовите функцию несколько раз, передав ей различные аргументы, и выведите результаты в консоль.
"""

def is_number_positive_even_or_negative(number):
    is_negative = number < 0
    is_positive = number > 0
    is_even = number % 2 == 0
    result = is_negative or is_positive and is_even
    return result


print(is_number_positive_even_or_negative(-4))
print(is_number_positive_even_or_negative(-9))
print(is_number_positive_even_or_negative(0))
print(is_number_positive_even_or_negative(8))
print(is_number_positive_even_or_negative(5))
