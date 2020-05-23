def backtracking_backpack(items, ret, max_weight):
    if ret['currentWeight'] <= max_weight:
        ret['maxPrice'] = max(ret['maxPrice'], ret['currentPrice'])
    else:
        # over weight
        return True

    for i in range(len(items)):
        # with current item
        [price, weight] = items[i]
        ret['currentWeight'] += weight
        ret['currentPrice'] += price
        overWeight = backtracking_backpack(items[i + 1:], ret, max_weight)
        # without current item
        ret['currentWeight'] -= weight
        ret['currentPrice'] -= price
        if overWeight:
            break
    return False


def dp_one_backpack(items, max_weight):
    # max value for the first i items put into j weight
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + c)
    dp = [[0 for i in range(max_weight + 1)] for j in range(len(items))]

    for i in range(0, len(items)):
        [price, weight] = items[i]
        for j in range(weight, max_weight + 1):
            if i - 1 < 0:
                dp[i][j] = price
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + price)
    return dp[-1][-1]


def dp_two_backpack(items, max_weight):
    f = [0 for i in range(max_weight + 1)]

    for i in range(len(items)):
        [price, weight] = items[i]
        # reverse it so it doesn't overwrite what we have calculated from last loop
        for j in range(max_weight, weight - 1, -1):
            f[j] = max(f[j], f[j - weight] + price)
    return f[-1]


def divide_nums(nums):
    pass


if __name__ == '__main__':
    items = [[3, 2], [4, 3], [2, 4], [4, 6], [4, 8]]
    ret = {}
    ret['maxPrice'] = 0
    ret['currentPrice'] = 0
    ret['currentWeight'] = 0
    backtracking_backpack(items, ret, 10)

    print ret

    print dp_two_backpack(items, 10)

    print dp_one_backpack(items, 10)
