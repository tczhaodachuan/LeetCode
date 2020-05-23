def min_coins(coins, amount):
    if amount == 0:
        return 0

    # dp[i] stands for minimal coins for amount i
    # dp[0] = 0, no coins for amount 0
    # dp[i] = min(dp[i], dp[i - coin] + 1) for coin in coins
    dp = [amount + 1 for i in range(amount + 1)]
    dp[0] = 0

    for i in range(min(coins), amount + 1):
        for coin in coins:
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1]


def min_coins_dfs(coins, amount, count):
    if amount == 0:
        return count
    if len(coins) == 0:
        return amount + 1
    i = amount / coins[0]
    min_count = amount + 1
    while i >= 0 and i + count < amount + 1:
        min_count = min(min_count, min_coins_dfs(coins[1:], amount - i * coins[0], count + i))
        i -= 1
    return min_count


if __name__ == '__main__':
    coins = [1, 2, 5, 10]
    print min_coins(coins, 10)
    print min_coins_dfs(sorted(coins, reverse=True), 10, 0)
