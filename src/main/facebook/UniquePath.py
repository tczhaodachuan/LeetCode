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
