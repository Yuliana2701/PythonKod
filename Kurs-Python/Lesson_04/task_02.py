"""
Задание
Напишите программу, которая запрашивает у пользователя его имя и возраст,
а затем выводит сообщение с приветствием и через сколько лет ему исполнится 100 лет.
"""

user_name = input("Enter your name:")
user_age1 = input(" Enter your age:")

to_100 = 100 - int(user_age1)

print(f"Hi {user_name}, you have left {to_100} years to 100")
