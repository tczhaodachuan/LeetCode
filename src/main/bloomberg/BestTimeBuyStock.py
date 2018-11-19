def bestTimeBuyStock(prices):
    # profit = current price - previous price
    # currentMin has to be previous price
    maxProfit = 0
    currentMin = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < currentMin:
            currentMin = prices[i]

        currentProfit = prices[i] - currentMin
        if currentProfit > maxProfit:
            maxProfit = currentProfit
    return maxProfit


def bestTimeBuyStocks(prices):
    # multiple buy and sell decisions could add up all the positive profit

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            print 'Buy at time {0} [{1}], Selling at time {2} [{3}]'.format(i - 1, prices[i - 1], i, prices[i])
            dp[i] = dp[i - 1] + prices[i] - prices[i - 1]
        else:
            dp[i] = dp[i - 1]
    return dp[-1]


if __name__ == '__main__':
    print bestTimeBuyStocks([7, 2, 5, 3, 6, 1])
