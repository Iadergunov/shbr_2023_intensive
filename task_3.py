"""
Сортировка вставками
"""


def insert_sort(arr: list) -> list:
    for i in range(len(arr)):
        curr_el = arr[i]
        for j in range(i):
            if curr_el < arr[j]:
                arr[j], curr_el = curr_el, arr[j]

        arr[i] = curr_el

    return arr


assert insert_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
assert insert_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
