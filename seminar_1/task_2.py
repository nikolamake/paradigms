# Дан список целых чисел numbers.
# Необходимо написать в декларативном стиле процедуру для сортировки числа
# в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

import random

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

numbers = [random.randint(1, 100) for _ in range(10)]
print("Исходный список чисел:", numbers)
numbers = sort_list_declarative(numbers)
print("Отсортированный список чисел по убыванию:", numbers)