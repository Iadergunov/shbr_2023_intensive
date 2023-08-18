"""
Простые числа
"""


def prime_numbers(n: int) -> list[int]:
    board = [0 for _ in range(n + 1)]
    answer = []
    for i in range(2, n + 1):
        if board[i]:
            continue

        answer.append(i)
        curr_el = i
        while curr_el <= n:
            board[curr_el] = 1
            curr_el += answer[-1]

    return answer


assert prime_numbers(2) == [2]
assert prime_numbers(1) == []
assert prime_numbers(3) == [2, 3]
assert prime_numbers(7) == [2, 3, 5, 7]
assert prime_numbers(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                              89, 97]
