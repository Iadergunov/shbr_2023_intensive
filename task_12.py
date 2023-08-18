"""
Сортировка слиянием
"""


def merge_sort(arr: list) -> list:
    def sort_step(sub_arr):
        if len(sub_arr) == 1:
            return sub_arr

        mid = (len(sub_arr) + 1) // 2
        left = sort_step(sub_arr[:mid])
        right = sort_step(sub_arr[mid:])
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    return sort_step(arr)


assert merge_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
