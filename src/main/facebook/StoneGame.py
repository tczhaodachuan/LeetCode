import sys


def stoneGame(stones):
    import sys
    result = {'min_cost': sys.maxint}
    _stoneGame(stones, 0, result)
    return result['min_cost']


def _stoneGame(stones, temp, result):
    if len(stones) == 0:
        return
    if len(stones) == 2:
        current_result = temp + sum(stones)
        if current_result < result['min_cost']:
            result['min_cost'] = current_result
            return
    for i in range(0, len(stones) - 1):
        j = i + 1
        _stoneGame(stones[:i] + [stones[i] + stones[i + 1]] + stones[j + 1:], temp + stones[i] + stones[i + 1], result)


def search(l, r, visited, sums, dp):
    print l, r
    if visited[l][r]:
        return dp[l][r]

    if l == r:
        visited[l][r] = True
        return dp[l][r]

    # all divide possibles
    dp[l][r] = sys.maxint
    for k in range(l, r):
        dp[l][r] = min(dp[l][r], search(l, k, visited, sums, dp) + search(k + 1, r, visited, sums, dp) + sums[l][r])
    visited[l][r] = True
    return dp[l][r]


def stoneGameDPSolution(stones):
    m = len(stones)

    max_int = sum(stones) + 1
    sums = [[0 for _ in range(m)] for _ in range(m)]
    visited = [[False for _ in range(m)] for _ in range(m)]
    # from dp[i][i] stands for no adjacent piles together.
    dp = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        sums[i][i] = stones[i]
        for j in range(i + 1, m):
            sums[i][j] = sums[i][j - 1] + stones[j]

    # dp[i][j] = min(dp[i][k-1] + dp[k+1][j] + sums[i][j])
    result = search(0, m - 1, visited, sums, dp)
    return result


if __name__ == '__main__':
    print stoneGame([3, 4, 3])
    print stoneGame([4, 1, 1, 4])
    print stoneGameDPSolution([4, 1, 1, 4])
