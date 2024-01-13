# Дан список целых чисел numbers.
# Необходимо написать в императивном стиле процедуру для сортировки числа
# в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

import random

def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

numbers = [random.randint(1, 100) for _ in range(10)]
print("Исходный список чисел:", numbers)
sort_list_imperative(numbers)
print("Отсортированный список чисел по убыванию:", numbers)