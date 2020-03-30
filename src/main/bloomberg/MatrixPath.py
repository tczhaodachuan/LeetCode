def longestPath(matrix, i, j, dp, directions):
    # any star point, 4 directions, can only go to the lower level,
    if dp[i][j] > 0:
        return dp[i][j]
    m = len(matrix)
    n = len(matrix[0])

    for dir in directions:
        ni = i + dir[0]
        nj = j + dir[1]

        if 0 <= ni < m and 0 <= nj < n and matrix[i][j] > matrix[ni][nj] and dp[i][j] < 1 + longestPath(
                matrix, ni, nj, dp, directions):
            dp[i][j] = dp[ni][nj] + 1

    return dp[i][j]


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
    ]
    m = len(matrix)
    n = len(matrix[0])
    dp = [[1 for i in range(n)] for i in range(m)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            path = longestPath(matrix, i, j, dp, directions)
            dp[i][j] = path


    print dp
