"""
Task 1.
Напишите программу, которая запрашивает у пользователя число.
Если введённое число делится нацело на три без остатка, вывести на экран – «Ваше число делится на три».
Если нет – вывести на экран – «Ваше число не делится на три».
"""


number = int(input("Введите ваше число: "))

if number % 3 == 0 :
    print("Ваше число делиться на 3")

else:
    print("Ваше число не делиться на три")