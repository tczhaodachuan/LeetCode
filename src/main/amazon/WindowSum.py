
def getWindowSum(array, k):
    ret = []
    if len(array) < k or len(array) < 1:
        return None

    windowSum = 0
    for i in range(len(array)):
        windowSum += array[i]
        if i - k + 1 >= 0:
            ret.append(windowSum)
            windowSum -= array[i - k + 1]
    return ret

if __name__ == '__main__':

    print getWindowSum([1, 2, 3, 4, 5], 3)