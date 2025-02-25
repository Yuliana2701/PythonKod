"""
Напишите программу, которая определяет минимальное значение из списка и выводит его в консоль.
"""

numbers = [8, 4, 7, 3, 9, 2, 5]
min = numbers[0]
for n in numbers :
    if n < min:
        min = n

print("Минимальное значение списка:", min)

# Перебираем индексы от 1 до len - 1.
min = numbers[0]
for idx in range(1, len(numbers)):
    if numbers[idx] < min :
        min = numbers[idx]

print("Минимальное значение списка 2:", min)

# Перебираем индексы от 1 до len - 1.
min = numbers[0]
for idx in range(1, len(numbers)) :
    num = numbers[idx]
    if num < min :
        min = num

print("Минимальное значение списка 3:", min)
