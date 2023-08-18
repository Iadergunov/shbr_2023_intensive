"""
Спираль
"""


def spiral(n: int):
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    matrix = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(n + 2):
            if i == 0 or j == 0 or i == n + 1 or j == n + 1:
                matrix[i][j] = -1

    x, y = 1, 1
    direction = 0
    for i in range(n * n):
        matrix[y][x] = i + 1
        d_x, d_y = deltas[direction % 4]
        if matrix[y + d_y][x + d_x] != 0:
            direction += 1
            d_x, d_y = deltas[direction % 4]

        x, y = x + d_x, y + d_y

    final_matrix = []
    for i in range(1, n + 1):
        row = matrix[i][1:n + 1]
        final_matrix.append(row)

    print(*final_matrix, sep='\n')
    return final_matrix


assert spiral(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
assert spiral(2) == [[1, 2], [4, 3]]
assert spiral(1) == [[1]]
assert spiral(4) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
