class UniquePaths(object):
    def uniquePaths(self, m, n):
        # initial value for m=0 or n =0 is 1
        # since the robot cannot
        dp = [[1 for i in range(n)] for j in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    def uniquePathsII(self, m, n):
        # initial value for m=0 or n =0 is 1
        # since the robot cannot
        dp = [0 for i in range(n)]

        # from row 0 to column i only one possible path
        for i in range(n):
            dp[i] = 1
        # from row 1 to m-1
        # from column 1 to n-1
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[n - 1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        dp = obstacleGrid
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1 - dp[i][j]
                elif i == 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print dp
        return dp[-1][-1]


if __name__ == '__main__':
    uniquePath = UniquePaths()
    print uniquePath.uniquePaths(3, 7)
    print uniquePath.uniquePathsII(3, 7)

    print uniquePath.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
