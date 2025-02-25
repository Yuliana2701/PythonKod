# Логический тип данных
# bool -> Boolean

# True (истина) / False (ложь)

is_sunny = True
is_raining = False
print(is_sunny)  # Вывод: True

print("=============\n")

# Логическое (условное) выражение - это выражение, которое возвращает значение типа Boolean (True / False)

# 5 больше 3 -> это логическое выражение, результат которого True (правда)
# 2 меньше 1 -> это логическое выражение, результат которого False (ложь)

# К условным выражениям относятся операторы сравнения и логические операции

# Операторы сравнения (есть 6 оператор)
# В операциях сравнения сравниваются два операнда и возвращается значение типа boolean.
# Если выражение верно - true; если неверно - false

# Сравнение на равенство ==
print(5 == 3)  # 5 равно 3 -> False

x = 10
y = 5
print(f"{x} == {y} -> {x == y}") # -> print (10 == 5) -> 10 равно 5 -> false

# Сравнение на неравенство (!=)
is_not_equals = x != y # x не равен y -> 10 не равно 5 -> true
print(f"{x} != {y} -> {is_not_equals}")

# Больше чем (>)
bol = x > y # Х больше чем У -> 10 больше чем 5 -> true
print(f"{x} > {y} -> {bol}")

# Меньше чем (<)
bol = x < y # Х меньше чем У -> 10 меньше чем 5 -> false
print(f"{x} < {y} -> {bol}")

# Больше или равно (>=)
print(10 > 10) # 10 больше чем 10 -> false

bol = 10 >= 10 # 10 больше или равно 10 -> true
print(f"{10} >= {10} -> {bol}")
print(f"{9} >= {10} -> {9 >= 10}")

# Меньше или равно (<=)
bol = x <= 10 # 10 меньше или равно 10 -> true
print(f"{x} <= {10} -> {bol}")


# Мат. операции (не относится к boolean)

digit = 10
# digit = digit + 5 # короткая форма записи digit += 5

digit += 5
digit -= 10 # -> digit = digit - 10
# digit *= 2
print(digit)

# =========

# Логические операторы используются для объединения нескольких логических выражений
"""

(лог.выражение) and (лог.выражение) -> boolean and boolean

and -> Логическое И -> оба выражения истины
or -> Логическое ИЛИ -> хотя бы одно из выражений вернуло истину
not -> Логическое НЕ -> инверсия значения (отрицание) - меняет значение на противоположное

"""

print("=============\n")

x = 10
y = 5
z = 8
# Логическое "И"
print((x > y) and (z > y)) # -> 10 > 5 и 8 > 5 ->  true and true -> true
print("True and True:", True and True) # True
print("True and False:", True and False) # False
print("False and True:", False and True) # False
print("False and False:", False and False) # False

# Если мы просим пользователя ввести число от 0 до 100?

num = int(input("Введите число от 0 до 100: "))
b = num >= 0 and num <= 100
print("Число в диапазоне от 0 до 100:", b)

# Вы идете на прогулку, если на улице тепло и не идет дождь
# Вы идете на прогулку если на улице солнечно или у вас есть зонт
# Вы остаетесь дома если НЕ солнечно

print("True or True:", True or True) # True
print("True or False:", True or False) # True
print("False or True:", False or True) # True
print("False or False:", False or False) # False

# Логическое YT
print("not (10 > 5):", not (10 > 5)) # not True -> False
# not False = True










