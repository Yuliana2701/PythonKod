"""
Task 3: Возраст и 100 лет
Условие:
Напишите программу, которая хранит имя и возраст человека в переменных,
затем выводит сообщение с приветствием и сообщает, через сколько лет этому человеку исполнится 100 лет.
"""

"""
1. Сохранить имя пользователя в переменную.
2. Сохранить возраст пользователя в переменную.
3. Вычислить, через сколько лет пользователю исполнится 100 лет.
4. Вывести результат.
"""

# Ввод данных
name = "Анна"
age = 25

# Вычисление
years_left = 100 - age

# Вывод результата
print("Привет,", name, "! Через", years_left, "лет тебе исполнится 100 лет.")

print(f"Привет, {name}! Через {years_left} лет тебе исполнится 100 лет.")
