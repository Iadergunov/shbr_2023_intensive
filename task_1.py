"""Сортировка пузырьком"""


def bubble_sort(arr: list):
    for _ in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
