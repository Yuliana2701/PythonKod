"""
Напишите функцию, которая определяет, сдал ли студент экзамен, и возвращает True, если сдал, и False – если не сдал.

Для успешной сдачи экзамена студенту необходимо:
 иметь два зачёта, а также получить балл не ниже 80 на самом экзамене.

Функция имеет три параметра – сдан ли первый зачёт, сдан ли второй зачёт, полученный балл на экзамене.

Вызовите функцию несколько раз, передав ей различные аргументы, и выведите результаты в консоль.

"""

def is_exam_passed(first_test_passed, second_test_passed, exam_rate):
    all_tests_passed = first_test_passed and second_test_passed
    is_exam_rate_positive = exam_rate >= 80
    exam_passed = all_tests_passed and is_exam_rate_positive
    return exam_passed


print(is_exam_passed(True, True, 90))
print(is_exam_passed(False, True, 85))
print(is_exam_passed(True, False, 95))
print(is_exam_passed(True, True, 78))
print(is_exam_passed(True, False, 76))
