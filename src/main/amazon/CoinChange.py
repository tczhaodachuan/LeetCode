def coinChange(coins, amount):
    if amount < 0 or len(coins) == 0:
        return -1
    # dp question dp[amount] = min(dp[amount - N] + 1), N is from the coins
    coins = sorted(coins)
    if coins[0] >  amount:
        # impossible to combine with other coins
        return -1


    dp = [amount + 1 for _ in range(amount + 1)]
    # amount 0 needs 0 coins
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == amount + 1:
        # it's impossible to find a combine for the amount
        return -1
    return dp[amount]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print coinChange(coins, amount)