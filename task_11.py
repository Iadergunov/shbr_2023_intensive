"""
Максимальная сумма подмассива
"""


def sub_array_sums(arr: list[int]):
    max_arr = max(arr)
    if max_arr <= 0:
        return [max_arr], max_arr

    dp = [0 for _ in range(len(arr))]
    dp[0] = max(arr[0], 0)
    for i in range(1, len(arr)):
        dp[i] = max(0, dp[i - 1] + arr[i])

    max_ind = 0
    for i in range(len(arr)):
        if dp[max_ind] < dp[i]:
            max_ind = i

    max_sum = dp[max_ind]
    current_sum = arr[max_ind]
    left_index = max_ind
    while current_sum != max_sum:
        left_index -= 1
        current_sum += arr[left_index]

    return arr[left_index:max_ind + 1], max_sum


assert sub_array_sums([-2, 1, -3, 4, -1, 2, 1, -5, -4]) == ([4, -1, 2, 1], 6)
assert sub_array_sums([-1, -2, -3]) == ([-1], -1)
assert sub_array_sums([-1, -2, 0, -4]) == ([0], 0)
