"""
Task 1.
Вам нужно перетащить тяжёлую мебель, помочь Вам может один из Ваших друзей - Петя или Вася.

Напишите функцию, которая позволяет определить, сможете ли Вы перетащить мебель.
Функция должна иметь два параметра – is_petya_free и is_vasya_free. Мебель можно перетащить, если хотя бы один из друзей свободен.
Функция должна возвращать True, если мебель перетащить можно или False – если нет.

Создайте две переменные для каждого из друзей, содержащие значение, свободен ли Ваш друг.

Вызовите функцию и выведите результат её работы на экран таким образом –

Получится ли перетащить мебель? – True/False
"""



def can_move_furniture(is_petya_free, is_vasya_free ):
    friend_help = is_petya_free or is_vasya_free
    return friend_help

petya_can = True
vasya_can = False

result = can_move_furniture(petya_can, vasya_can)
print("Получиться ли перетащить мебель ?", result)