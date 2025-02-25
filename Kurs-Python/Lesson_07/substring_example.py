# В Python можно проверить содержит ли строку определенный символ или последовательность символов

# substring in string
# substring - искомый символ или последовательность символов
# string - строка, в которой выполняется поиск
# результат типа boolean ->
# True если substring найден в string
# False - если нет

# Проверка наличия символа
text = "Hello, world!"
print("H" in text) # True
print("z" in text) # False

# Проверка наличия последовательности символов
# Порядок символов имеет значение
print("worl" in text) # True
print("wolr" in text) # False
bol = "World" in text  # False
# Регистр имеет значение: w != W
print(f"World in {text} -> {bol}")
word = "Python"
print(word in text) # False

print("=============\n\n")

# Отрицательная проверка (оператор not in)
# Можно проверить, что строка не содержит подстроку
text = "Hello, world!"
print("Python" not in text) # True
print("Hel" not in text) # False

# len - определение длины строки
# len(string) -> вернет кол-во символов в строке (длину строки)
print(len(text))
l = len("Hello !")
print(l)

str = "" # пустой строка
print(len(str))

