class Solution(object):
    def uniquePathsOneDp(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for i in range(n)] for j in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    def uniquePathsOneRecursive(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        results = {}
        return self.uniquePathsOneRecursiveMemory(m, n, results)

    def uniquePathsOneRecursiveMemory(self, m, n, results):

        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        if (m, n) in results:
            return results[(m, n)]
        result = self.uniquePathsOneRecursiveMemory(m - 1, n, results) + self.uniquePathsOneRecursiveMemory(m, n - 1,
                                                                                                            results)
        results[(m, n)] = result
        return result

    def uniquePathsTwo(self, obstacleGrid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if m == 1:
            if 1 in obstacleGrid[0]:
                return 0
            else:
                return 1
        if n == 1:
            if [1] in obstacleGrid:
                return 0
            else:
                return 1

        # dp[i][j] stands for i,j as the end point, how many ways from top to the i,j
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for i in range(1, m):
            dp[i][0] = int(obstacleGrid[i][0] == 0 and dp[i - 1][0] == 1)
        for i in range(1, n):
            dp[0][i] = int(obstacleGrid[0][i] == 0 and dp[0][i - 1] == 1)

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        return dp[m - 1][n - 1]

    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        # dp[i][j] stands for to position i, j the min path sum
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min((dp[i - 1][j] + grid[i][j]), (dp[i][j - 1] + grid[i][j]))
        return dp[m - 1][n - 1]

    def climbStairs(self, n):
        if n == 1:
            return 1

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n <= 1:
            return 0
        dp = [0 for _ in range(n + 1)]
        # dp[i] stands for minimal cost of ith step
        dp[0] = 0
        dp[1] = 0
        dp[2] = min(dp[0] + cost[0], dp[1] + cost[1])
        for i in range(3, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print s.uniquePathsOneDp(3, 2)
    print s.uniquePathsOneDp(3, 3)
    print s.uniquePathsOneRecursive(3, 2)
    print s.uniquePathsOneRecursive(3, 3)

    print s.uniquePathsTwo([[0]])
    print s.uniquePathsTwo([[0], [1]])
    print s.uniquePathsTwo([[0, 1]])
    print s.uniquePathsTwo([[0], [0]])
    print s.uniquePathsTwo([[0, 0], [1, 0]])
    print s.uniquePathsTwo([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

    print s.minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ])

    print s.climbStairs(3)
    print s.climbStairs(4)

    print s.minCostClimbingStairs([10, 15, 20])
