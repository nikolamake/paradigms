# Написать программу на любом языке в любой парадигме для бинарного поиска.
# На вход подаётся целочисленный массив и число.
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Пример использования функции
arr = [11, 22, 33, 40, 53, 67, 78, 888, 9888, 100000]
target = 53
result = binary_search(arr, target)

if result != -1:
    print(f"Индекс числа {target} равняется", result)
else:
    print(f"Число {target} в массиве отсутствует")
