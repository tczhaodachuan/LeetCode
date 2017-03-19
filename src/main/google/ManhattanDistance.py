def minTotalDistance(grid):
    iPos = []
    jPos = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                iPos.append(i)
                jPos.append(j)

    minTotalDistance = 0
    for i in iPos:
        minTotalDistance += abs(i - iPos[len(iPos) / 2])

    jPos = sorted(jPos)
    for j in jPos:
        minTotalDistance += abs(j - jPos[len(jPos) / 2])
    return minTotalDistance


def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])

    dp = [[0 for i in range(n)] for j in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + grid[0][i]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]


if __name__ == '__main__':
    grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    print minTotalDistance(grid)
