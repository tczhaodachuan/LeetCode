def diagonalTraverse(matrix):
    if len(matrix) == 0:
        return []
    result = list()
    m = len(matrix)
    n = len(matrix[0])

    row = 0
    col = 0
    # go up, go down
    directions = [(-1, 1), (1, -1)]
    d = 0
    for i in range(n * m):
        result.append(matrix[row][col])
        row += directions[d][0]
        col += directions[d][1]

        if row >= m:
            row = m - 1
            col += 2
            d = 1 - d
        if col >= n:
            col = n - 1
            row += 2
            d = 1 - d
        if row < 0:
            row = 0
            d = 1 - d
        if col < 0:
            col = 0
            d = 1 - d
    return result


if __name__ == '__main__':
    print diagonalTraverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
