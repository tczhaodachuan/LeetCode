import string


def decodeWays(expression):
    encodings = {str(i): string.ascii_uppercase[i - 1] for i in range(1, 27)}
    dp = [0 for i in range(len(expression) + 1)]
    dp[0] = 1
    dp[1] = 1 if expression[0] != '0' else 0
    for i in range(2, len(expression) + 1):
        one_digit = expression[i - 1]
        two_digit = expression[i - 2:i]
        if one_digit in encodings:
            dp[i] += dp[i - 1]
        if two_digit in encodings:
            dp[i] += dp[i - 2]
    return dp[len(expression)]


print decodeWays('110')
