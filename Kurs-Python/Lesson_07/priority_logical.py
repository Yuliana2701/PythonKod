print(True or False and False) # True
# Предположение: True or False and False -> True and False -> False # # НЕ ВЕРНО!!!
# True or False and False -> True or False -> True

# Приоритет логических операций

"""
0. () - скобки
1. not 
2. and
3. or
"""

# Скобки могут изменять порядок выполнения операций, т.к. скобки имеют наивысший приоритет
print((True or False) and False) # False -> ((True or False) and False) -> True and False -> False
print(True or False and not True) # True -> True or False and False -> True or False -> Trie

number = 5
print(number % 2)
