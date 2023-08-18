"""
Перестановки от 1 до N
"""


def permutations(n: int):
    answer = []

    def permute(curr_el, left, right):
        if left == right:
            answer.append(curr_el)
            return

        for i in range(left, right + 1):
            new_el = curr_el.copy()
            new_el[left], new_el[i] = new_el[i], new_el[left]
            permute(new_el, left + 1, right)

    permute([i + 1 for i in range(n)], 0, n - 1)
    return answer


assert permutations(3) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
assert permutations(2) == [[1, 2], [2, 1]]
assert permutations(1) == [[1]]
