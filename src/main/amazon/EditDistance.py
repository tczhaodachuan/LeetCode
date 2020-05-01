def oneEditDistance(s, t):
    if not s and not t:
        return False

    if len(s) == len(t):
        for i in range(len(s)):
            if s[i] != t[i]:
                _s = s[:i] + t[i] + s[i + 1:]
                if _s == t:
                    return True
        return False

    if len(s) > len(t):
        for i in range(len(s)):
            _s = s[:i] + s[i + 1:]
            if _s == t:
                return True
        return False

    return oneEditDistance(t, s)


def editDistance(s, t):
    # min steps from s to t
    # dp[m][n] to represent the min distance from s[:m] to t[:n]
    m = len(s)
    n = len(t)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for i in range(n + 1):
        dp[0][i] = i

    for i in range(m + 1):
        for j in range(n + 1):
            if s[i] == t[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    return dp[m][n]


if __name__ == '__main__':
    s = "aDb"
    t = "adb"
    print oneEditDistance(s, t)

    s = "ab"
    t = "ab"
    print oneEditDistance(s, t)

    s = "ab"
    t = "abc"
    print oneEditDistance(s, t)

    s = "abc"
    t = "ab"
    print oneEditDistance(s, t)
