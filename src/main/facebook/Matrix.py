# a matrix, for one row, from left to right if one column is 1, all of the remaining columns are 1.
# find the first column which contains the 1


def findColumn(matrix):
    m = len(matrix)
    n = len(matrix[0])

    i = 0
    j = n - 1

    result = -1
    while i < m and j >= 0:
        if matrix[i][j] == 1:
            result = j
            j -= 1
        else:
            i += 1
    return result


def antiDiagonal(matrix):
    m = len(matrix)
    n = len(matrix[0])
    result = []

    queue = [(0, 0)]
    seen = set()
    directions = [(0, 1), (1, 0)]
    while len(queue) > 0:
        size = len(queue)
        diagonal = []
        for i in range(size):
            x, y = queue.pop()
            diagonal.append(matrix[x][y])
            for dx, dy in directions:
                _x = x + dx
                _y = y + dy
                if (_x, _y) in seen or _x >= m or _y >= n:
                    continue
                seen.add((_x, _y))
                queue.append((_x, _y))
        result.append(diagonal)
    return result


if __name__ == '__main__':
    input = [[0, 0, 0, 1],
             [0, 1, 1, 1],
             [0, 0, 1, 1]]

    print findColumn(input)

    input = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    print findColumn(input)

    print antiDiagonal([[12, 7, 21, 31, 11],
                        [45, -2, 14, 27, 19],
                        [-3, 15, 36, 71, 26],
                        [4, -13, 55, 34, 15]])
