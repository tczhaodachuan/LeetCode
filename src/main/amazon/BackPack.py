def maximumShopping(items, ret, maxWeight):
    if ret['currentWeight'] <= maxWeight:
        ret['maxPrice'] = max(ret['maxPrice'], ret['currentPrice'])
    else:
        # over weight
        return True

    for i in range(len(items)):
        # with current item
        [price, weight] = items[i]
        ret['currentWeight'] += weight
        ret['currentPrice'] += price
        overWeight = maximumShopping(items[i+1:], ret, maxWeight)
        # without current item
        ret['currentWeight'] -= weight
        ret['currentPrice'] -= price
        if overWeight:
            break
    return False


def maximumShooping_backpack(items, maxWeight):
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
    maximumShopping(items, ret, 10)

    print ret

    print maximumShooping_backpack(items, 10)
