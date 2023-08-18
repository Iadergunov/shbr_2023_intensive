"""
Сортировка выбором
"""


def choice_sort(arr: list) -> list:
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if arr[i] != arr[min_index]:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


assert choice_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
assert choice_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
