"""
Task 2.
Автобус в другой город отправляется в 18 часов. Стоимость проезда - 150 у.е.

Напишите функцию, которая определяет, сможете ли Вы уехать на автобусе,
и возвращает True, если сможете,
и False – если нет.

Для того чтобы уехать, у Вас должно быть достаточно денег, и времени должно быть не больше 18 ч.
Функция имеет два параметра - сколько сейчас часов и сколько у Вас денег.

Вызовите функцию несколько раз, передав ей различные аргументы, и выведите результаты в консоль.

"""
def function1(hours, money):
    return hours <= 18 and money >= 150

print("Вариант 1 : 18 150 у.е ", function1(18, 150))
print("Вариант 2 : 20 120 у.е ", function1(20, 120))
print("Вариант 3 : 10 150 у.е ", function1(10, 150))
print("Вариант 4 : 12 130 у.е ", function1(12, 130))