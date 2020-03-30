def maximumShopping_backtrack(i, items, ret, maxWeight):
    if ret['currentWeight'] <= maxWeight:
        # update max price based on the current shopping cart pricing
        ret['maxPrice'] = max(ret['maxPrice'], ret['currentPrice'])
    else:
        # over weight
        return True

    for j in range(i, len(items)):
        # with current item
        [price, weight] = items[j]
        ret['currentWeight'] += weight
        ret['currentPrice'] += price
        overWeight = maximumShopping_backtrack(j + 1, items, ret, maxWeight)
        # without current item
        ret['currentWeight'] -= weight
        ret['currentPrice'] -= price
        if overWeight:
            break
    return False


def maximumShopping_backpack(items, maxWeight):
    f = [0 for i in range(maxWeight + 1)]

    for i in range(len(items)):
        [price, weight] = items[i]
        for j in range(maxWeight, weight - 1, -1):
            f[j] = max(f[j], f[j - weight] + price)
    return f[-1]


if __name__ == '__main__':
    items = [[3, 2], [4, 3], [2, 4], [4, 6], [4, 8]]
    ret = {}
    ret['maxPrice'] = 0
    ret['currentPrice'] = 0
    ret['currentWeight'] = 0
    maximumShopping_backtrack(0, items, ret, 10)

    print(ret)

    print(maximumShopping_backpack(items, 10))
