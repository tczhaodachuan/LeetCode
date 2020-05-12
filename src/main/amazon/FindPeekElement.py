def findPeak(A):
    if len(A) == 1:
        return 0

    l = 0
    r = len(A)

    while l < r:
        mid = (l + r) / 2
        if (mid == 0 and A[mid] > A[mid + 1]) or (mid == len(A) - 1 and A[mid] > A[mid - 1]) or (
                A[mid] > A[mid - 1] and A[mid] > A[mid + 1]):
            return mid
        elif mid > 0 and A[mid - 1] > A[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return l


def checkBadVersion(mid):
    pass


def firstBadVersion(n):
    i = 0
    j = n
    result = -1
    # i <=j to cover all of the possible points, otherwise we will miss the j
    while i <= j:
        mid = i + (j - i) / 2  # avoid overflow
        if checkBadVersion(mid):
            result = mid
            j = mid - 1
        else:
            i = mid + 1
    return result


import sys


def findRadius(houses, heaters):
    houses = sorted(houses)
    heaters = sorted(heaters)

    # adding two fake heaters so any given house will be between two heaters
    heaters = [-sys.maxint] + heaters + [sys.maxint]

    result = 0
    pos = 0

    for house in houses:
        while house >= heaters[pos]:
            # for the first house, this condition will be met for sure
            # find the first position where house < heaters[pos], the house
            # must between heaters[pos-1] and heaters[pos]
            pos += 1

        r = min(house - heaters[pos - 1], heaters[pos] - house)
        result = max(result, r)

    return result


def binarySearch(nums, l, r, target):
    # binary search has to return the index in the nums
    # the boundary has to be set, thus has to be l <= r, because we only search mid value
    # if l<r, we possible will miss one element which could be the answer
    while l <= r:
        mid = l + (r - l) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def searchInsertPos(nums, target):
    # sorted nums, the complexity should be O(logN) better then O(N)
    i = 0
    j = len(nums) - 1

    while i <= j:
        mid = i + (j - i) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return i


if __name__ == '__main__':
    print findPeak([1, 2, 1, 3, 4, 5, 7, 6])
    print findPeak([1, 2, 3, 4, 1])
    print findPeak([1, 2, 1, 3, 5, 6, 4])

    nums = [2, 3, 4, 10, 40]
    print binarySearch(nums, 0, len(nums) - 1, 10)

    nums = [2, 3, 4, 10, 40, 80]
    print binarySearch(nums, 0, len(nums) - 1, 2)

    nums = [2, 3, 4, 10, 40, 80]
    print searchInsertPos(nums, 5)
    print searchInsertPos(nums, 85)
    print searchInsertPos(nums, 1)
