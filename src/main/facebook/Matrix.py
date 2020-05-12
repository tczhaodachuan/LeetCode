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


if __name__ == '__main__':
    input = [[0, 0, 0, 1],
             [0, 1, 1, 1],
             [0, 0, 1, 1]]

    print findColumn(input)

    input = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    print findColumn(input)
