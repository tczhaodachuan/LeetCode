def maxSlidingWindow(nums, k):
    result = []
    # this queue only maintains the window max or min in the first
    index_queue = []
    for i in range(len(nums)):
        # remove the one outside window, so it doesn't disturb the result
        if len(index_queue) > 0 and index_queue[0] == i - k:
            index_queue.pop(0)
        # remove the one which is less than the current one
        while len(index_queue) > 0 and nums[index_queue[-1]] < nums[i]:
            index_queue.pop(-1)
        index_queue.append(i)

        if i >= k - 1:
            result.append(nums[index_queue[0]])
    return result


def maxTradeInFiveMins(trades):
    maxTradeVolum = 0
    result = {}
    for i in range(len(trades)):
        label, time, price, volum = trades[i]
        if result.has_key(label):
            price_queue = result[label]
            while len(price_queue) > 0 and time - price_queue[0][1] > 5:
                price_queue.pop(0)

            result[label].append(trades[i])

            total = 0
            for v in result[label]:
                total += v[3]
            maxTradeVolum = max(maxTradeVolum, total)
        else:
            result[label] = [trades[i]]

    return maxTradeVolum


if __name__ == '__main__':
    print maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print maxSlidingWindow([1, -1], 1)
    print maxSlidingWindow([1, 3, 1, 2, 0, 5], 3)

    tradelist = []
    tradelist.append(('GOOGLE', 900, 130.1, 120))
    tradelist.append(('GOOGLE', 901, 130.1, 100))
    tradelist.append(('APPLE', 901, 798.4, 400))
    tradelist.append(('GOOGLE', 902, 130.1, 90))
    tradelist.append(('GOOGLE', 904, 130.1, 150))
    tradelist.append(('GOOGLE', 1310, 130.1, 300))
    print maxTradeInFiveMins(tradelist)