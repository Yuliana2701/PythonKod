"""
Task 2.
Напишите программу, которая запрашивает у пользователя имя, название улицы и номер дома, а затем выводит на экран строку по образцу:
"Вас зовут Аркадий, и Вы живёте по адресу: ул. Гоголя, д. 7."

"""


name = input("Как Вас зовут ?: ")
street =input("Название вашей улицы: ")
number = 7
home_number = "дом " + str(number)


print("Вас зовут", name, "и Вы живете по адресу", street, home_number )