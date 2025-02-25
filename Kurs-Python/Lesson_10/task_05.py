"""
Напишите Функцию, которая принимает список чисел.

Функция должна вычислить и вернуть среднее арифметическое чисел, входящих в список.

Подсказка: среднее арифметическое чисел: Это сумма чисел, разделенная на их количество.

P.S. Реализовать защиту от деления на 0
"""


def calculate_average(numbers):
    # Код функции
    if len(numbers) == 0:
        return 0 # Защита от деления на 0

    total = 0
    for num in numbers:
        total += num # Считаем сумму

    print(f"Сумма {total}. Кол-во {len(numbers)}")
    # Сумму чисел разделить на количество
    return total / len(numbers)


print(calculate_average([1, 2, 3, 4, 5, 6]))
print(calculate_average([10, 15, 20, 25, 30]))
print(calculate_average([]))
