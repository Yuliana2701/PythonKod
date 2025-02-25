# Цикл, это конструкция, которая позволяет повторять определенное действие /-я

# while - цикл с условием
# for - цикл, перебирающий элементы

# Цикл while выполняется до тех пор, пока условие остается истинным (возвращает True)

"""
while условия :
    # Тело цикла
    # Код, который выполняется, пока условие истинно
"""

# Вывести фразу "Hello world!" на экран 10 раз

# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")

# Счетчик цикла
counter = 0  # Начальное значение
while counter < 10:
    print("Hello world!")
    # Увеличиваю счетчик цикл на 1
    counter = counter + 1

print("Строка после цикла")

print("===============\n")
# Вывести на экран числа от 0 до 9 включительно

# Счетчик цикла
i = 0
while i <= 9:
    print(i)  # Выводим текущее значение
    i += 1  # i = i + 1

print("Цикл завешен")

# Что будет, если забыть увеличить счетчик цикла
# Бесконечный цикл

"""
j = 0
while j < 5 :
    print("Hello", j)
    # Ошибка: счетчик не увеличивается
    # Программа будет бесконечное кол-во раз выводить слово hello
"""

# Напишите программу, которая выводит все нечетные числа в диапазоне от 6 до 55 включительно в консоль
# Напишите программу, которая выводит все нечетные числа в диапазоне от a до b включительно в консоль
counter = 6
while counter < 55:
    if counter % 2 != 0:
        print(counter)
    counter += 1

print("===================\n")
i = 9
while i <= 29:
    print(i)
    i += 2
print("===================\n")


def print_numbers(num1, num2):
    counter = num1
    while counter <= num2:
        if counter % 2 != 0:
            print(counter)
            counter += 2
        else:
            counter += 1

print("===================\n")

def print_numbers2(num1, num2):
    counter = num1
    if counter % 2 == 0:
        counter += 1
    while counter <= num2:
        print(counter)
        counter += 2


print_numbers(2, 15)
print("==================\n")
print_numbers2(2, 15)
print("====================\n")

# Напишите программу, которая выводит на экран числа от 15 до 1.

number = 15
# while number > 0 :
while number >= 1 :
    print(number)
    number -= 1 # number = number - 1













