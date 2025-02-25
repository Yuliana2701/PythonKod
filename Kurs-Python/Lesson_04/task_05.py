"""

Task 4. Самостоятельная работа.
Вы отправляетесь в путешествие по Европе, и у Вас есть 1000 у.е.
Напишите программу, которая должна выполнять следующие действия:
задает два вопроса, сколько денег Вы потратили в Париже на шоппинг и экскурсии
выводит на экран информацию, сколько денег осталось после Парижа
задает два вопроса, сколько денег Вы потратили в Мадриде на экскурсии и рестораны
выводит на экран информацию, сколько денег осталось после Мадрида
задает два вопроса, сколько денег Вы потратили в Афинах на музеи и отель
выводит на экран информацию, сколько денег осталось после Афин
"""
money_left = float(input("Сколько денег вы взяли в путешествие? "))

paris_shopping = float(input("Сколько Вы потратили на шоппинг в Париже? "))
paris_excursions = float(input("Сколько Вы потратили на экскурсии в Париже? "))
paris_expenses = paris_shopping + paris_excursions
money_left = money_left - paris_expenses
print("После Парижа осталось", money_left, "у.е.")

madrid_excursions = float(input("Сколько Вы потратили на экскурсии в Мадриде? "))
madrid_restaurants = float(input("Сколько Вы потратили на рестораны в Мадриде? "))
madrid_expenses = madrid_excursions + madrid_restaurants
money_left = money_left - madrid_expenses
print("После Мадрида осталось", money_left, "у.е.")

athens_museums = float(input("Сколько Вы потратили на музеи в Афинах? "))
athens_hotel = float(input("Сколько Вы потратили на отель в Афинах? "))
athens_expenses = athens_museums + athens_hotel
money_left -= athens_expenses

print("После Афин осталось", round(money_left, 2), "у.е.")
print(f"После Афин осталось {money_left:.2f} у.е.")
