class Solution(object):
    def minDistance(self, word1, word2):

        m = len(word1) + 1
        n = len(word2) + 1

        # dp[i][j] stands for from word1[:i] to word[:j] minimal distance

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0
        for i in range(1, m):
            # remove i character
            dp[i][0] = 1

        for i in range(1, n):
            # remove i character
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    print s.minDistance("horse", "ros")
