def getWindowSum(array, k):
    if len(array) < k or len(array) < 1:
        return None

    result = []
    window_sum = 0
    for i in range(len(array)):
        window_sum += array[i]
        if i - k + 1 >= 0:
            result.append(window_sum)
            window_sum -= array[i - k + 1]
    return result


def getSlidingWindowMax(array, k):
    if len(array) < k or len(array) < 1:
        return None

    sliding_window = []
    result = []
    for i in range(len(array)):
        sliding_window.append(array[i])
        if i - k + 1 >= 0:
            result.append(max(sliding_window))
            sliding_window = sliding_window[1:]
    return result


if __name__ == '__main__':
    print(getWindowSum([1, 2, 3, 4, 5], 3))

    print(getSlidingWindowMax([1, 3, -1, -3, 5, 3, 6, 7], 3))
