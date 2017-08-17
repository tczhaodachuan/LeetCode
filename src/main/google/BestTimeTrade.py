def bestTimeBuyAndSellStock(prices):
    currentMin = prices[0]
    maxProfits = 0

    for i in range(1, len(prices)):
        if prices[i] < currentMin:
            currentMin = prices[i]
        currentProfits = prices[i] - currentMin
        if currentProfits > maxProfits:
            maxProfits = currentProfits

    return maxProfits


def bestTimeBuyAndSellStockII(prices):
    # dp[i] meaning at ith price max profits, if prices[i] > prices[i-1], the profits could add together
    # given the assumption dp[i-1] already make the max profits decision
    dp = [0 for i in range(len(prices))]
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            dp[i] = dp[i - 1] + prices[i] - prices[i - 1]
        else:
            # no operation today
            dp[i] = dp[i - 1]
    return dp[-1]


def bestTimeBuyAndSellStockIII(prices):
    # profits table got updated from two ways, one way is from left side, buy and sell before i with max profit
    # also got updated from right side, but after i but sell after i with max profit
    # max profits of two transactions would be within this table when before i + after i maximum
    leftProfits = [0 for i in range(len(prices))]
    rightProfits = [0 for i in range(len(prices))]

    currentMin = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < currentMin:
            currentMin = prices[i]

        currentProfits = prices[i] - currentMin
        if currentProfits > leftProfits[i]:
            leftProfits[i] = currentProfits

    currentMax = prices[-1]
    i = len(prices) - 2
    while i >= 0:
        if prices[i] > currentMax:
            currentMax = prices[i]
        currentProfits = currentMax - prices[i]
        if currentProfits > rightProfits[i]:
            rightProfits[i] = currentProfits
        i -= 1

    profits = leftProfits + rightProfits

    return max(profits)


if __name__ == '__main__':
    print 'bestTimeBuyAndSellStock'
    print bestTimeBuyAndSellStock([7, 1, 5, 3, 6, 4])
    print bestTimeBuyAndSellStock([7, 6, 4, 3, 1])

    print 'bestTimeBuyAndSellStockII'
    print bestTimeBuyAndSellStockII([7, 1, 5, 3, 6, 4])

    print 'bestTimeBuyAndSellStockIII'
    print bestTimeBuyAndSellStockIII([1, 4, 5, 7, 6, 3, 2, 9])
    print bestTimeBuyAndSellStockIII([1, 2])
