def searchRotatedArrayII(array, target):
    # each time, it cannot exclude the other half of range, it becomes worst case O(n)
    # e.g. [3,1,2,3,3,3,3] target = 2, you cannot exlcude the other half of 3, because the array could be
    # [3,3,3,3,2,1,3]
    if len(array) == 0:
        return False

    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) / 2
        if array[mid] == target:
            return True
        elif array[mid] < array[end]:  # right half is sorted
            if array[mid] < target and target <= array[end]:
                start = mid + 1
            else:
                end = mid - 1
        elif array[mid] > array[end]:  # left half is sorted
            if array[start] <= target and target < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            # array[mid] == array[end], it could be undermined, so can only exclude the last one
            # e.g. 3,3,3,3,2,1,3] or [3,1,2,3,3,3,3], end -1 will try to find a sorted half
            end -= 1
    return False


def searchRotatedArray(array, target):
    if len(array) == 0:
        return -1

    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) / 2
        if array[mid] == target:
            return mid
        elif array[mid] < array[end]:
            if array[mid] < target and target <= array[end]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if array[start] <= target and target < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
    if start < len(array) and array[start] == target:
        return start

    if end >= 0 and array[end] == target:
        return end
    return -1


def findMinInRotatedArray(nums):
    # since nums has no duplicates, the min number happens at
    # either nums[0], nums[i] where nums[i] < nums[i-1] and nums[i] < nums[i+1], or nums[len(nums)-1]
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return min(nums)
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) / 2
        if mid == 0 or mid == len(nums) - 1:
            return min(nums[start], nums[end])
        elif nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
            return nums[mid]
        elif nums[mid] > nums[end]:
            # minimal number is in right half
            start = mid + 1
        elif nums[mid] < nums[start]:
            # minimal number is in left half
            end = mid - 1
        else:
            # the array is in order
            return nums[start]

    return min(nums[end], nums[start])


def findMinInRotatedArrayII(nums):
    '''
    [1,2,3,4,5]
    [3,3,3,1,2,3]
    [3,1,2,3,3,3]
    [4,1,2,3,3,3]
    '''
    if len(nums) == 1:
        return nums[0]
    start = 0
    end = len(nums) - 1
    # 1st case
    if nums[start] < nums[end]:
        return nums[start]
    while start <= end:
        while nums[start] == nums[end] and start != end:
            # find until start != end
            start += 1
        if nums[start] <= nums[end]:
            # case 2 or case 3
            return nums[start]
        mid = (start + end) / 2
        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid
    return -1


def rotateArray(nums, k):
    if k == 0:
        return
    k = k % len(nums)
    k = len(nums) - k
    for i in range(gcd(k, len(nums))):
        temp = nums[i]
        j = i
        while True:
            fromPosition = j + k
            if fromPosition >= len(nums):
                fromPosition -= len(nums)
            if fromPosition == i:
                break
            nums[j] = nums[fromPosition]
            j = fromPosition
        nums[j] = temp
    print nums


def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


def rotateArrayReverse(nums, k):
    # [1,2,3,4,5,6] flip over the array
    # [6,5,4,3,2,1]
    # [5,6,1,2,3,4] reverse digits in sub array will get the correct answer
    if k == 0:
        return
    k = k % len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
    print nums


def reverse(nums, start, end):
    mid = (start + end) / 2
    i = start
    while i <= mid:
        temp = nums[i]
        nums[i] = nums[end - i + start]
        nums[end - i + start] = temp
        i += 1


if __name__ == '__main__':
    print 'searchRotatedArray'
    rotatedArray = [5, 6, 7, 8, 1, 2, 3]
    print searchRotatedArray(rotatedArray, 8)
    print searchRotatedArray(rotatedArray, 0)
    print searchRotatedArray(rotatedArray, 3)

    print 'searchRotatedArrayII'
    rotatedArray = [5, 2, 3, 4, 5, 5, 5]
    print searchRotatedArrayII(rotatedArray, 3)

    print 'findMinInRotatedArray'
    rotatedArray = [5, 6, 7, 8, 1]
    print findMinInRotatedArray(rotatedArray)
    rotatedArray = [1, 5, 6, 7, 8]
    print findMinInRotatedArray(rotatedArray)
    rotatedArray = [5, 6, 7, 8, 1, 2, 3, 4]
    print findMinInRotatedArray(rotatedArray)
    print findMinInRotatedArray([5, 1, 2, 3, 4])

    print 'findMinInRotatedArrayII'
    print findMinInRotatedArrayII([1, 2, 3, 4, 5])
    print findMinInRotatedArrayII([3, 3, 3, 1, 2, 3])
    print findMinInRotatedArrayII([3, 1, 2, 3, 3, 3])
    print findMinInRotatedArrayII([4, 1, 2, 3, 3, 3])
    print findMinInRotatedArrayII([3, 1, 3])
    print findMinInRotatedArrayII([5, 1, 3])

    print 'rotateArray'
    rotateArray([1, 2, 3, 4, 5, 6], 2)
    rotateArray([1, 2], 3)
    rotateArray([1, 2, 3], 2)

    print 'rotateArrayReverse'
    rotateArrayReverse([1, 2, 3, 4, 5, 6], 2)
    rotateArrayReverse([1, 2], 3)
    rotateArrayReverse([1, 2, 3], 2)