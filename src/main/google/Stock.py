def best_time_buy_stock(prices):
    dp = [0 for i in range(len(prices))]
    dp[0] = 0
    # dp[i] stores until i, the max profit possible
    # dp[i] = max(dp[i-1], curretMax-currentMin)
    currentMax = prices[0]
    currentMin = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < currentMin:
            currentMin = prices[i]
            currentMax = currentMin
        elif prices[i] > currentMax:
            currentMax = prices[i]
        dp[i] = max(dp[i - 1], currentMax - currentMin)

    return dp[-1]


def best_time_buy_stock_ii(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0:
        return 0
    dp = [0 for i in range(len(prices))]
    # dp[i] meaning until ith day, the max profit for dp[i] = dp[i-1] + p[i]-p[i-1]>0?p[i]-p[i-1]:0
    # because assume i-2 has the lowest value, ith day has higher value than i-1 day, the profit would accumulate
    # if i day is lower then i-1 day, i-1 - i-2 day already make profits, so compare one day difference is enough
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            dp[i] = dp[i - 1] + prices[i] - prices[i - 1]
        else:
            dp[i] = dp[i - 1]

    return dp[-1]


if __name__ == '__main__':
    print best_time_buy_stock([7, 1, 5, 3, 6, 4])
    print best_time_buy_stock([7, 6, 4, 3, 1])

    print best_time_buy_stock_ii([1, 4, 2])
    print best_time_buy_stock_ii([3, 3, 5, 0, 0, 3, 1, 4])
