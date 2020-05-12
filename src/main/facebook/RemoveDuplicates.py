def removeDuplicates(nums):
    if len(nums) == 0 or not nums:
        return 0
    # sorted nums
    i = 0
    j = i + 1
    while i < len(nums) - 1 and j < len(nums):
        if nums[i] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1
        j += 1
    return i + 1


def countDistinctNumbers(nums):
    i = 1
    result = 1
    while i < len(nums):
        while nums[i - 1] == nums[i]:
            i += 1
        i += 1
        result += 1
    return result


def removeElements(nums, val):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


def removeDuplicatesFromSortedArray(nums):
    # duplicates appeared at most twice
    if len(nums) == 0 or not nums:
        return 0

    i = 1
    j = 1
    cnt = 1
    k = 2
    while j < len(nums):
        if nums[j] != nums[j - 1]:
            cnt = 1
            nums[i] = nums[j]
            i += 1
        else:
            if cnt < k:
                nums[i] = nums[j]
                i += 1
                cnt += 1
        j += 1
    return i


if __name__ == '__main__':
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print removeDuplicates(a)

    print removeDuplicates([1, 1, 1, 1])

    print removeDuplicates([1, 1, 2])

    print removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

    print removeElements([3, 2, 2, 3], 3)
    print removeElements([0, 1, 2, 2, 3, 0, 4, 2], 2)
    print removeElements([0, 1, 2, 2, 3, 0, 4, 2], 9)
    print removeElements([1], 1)
    print removeElements([4, 5], 4)
    print 'removeDuplicatesFromSortedArray'
    print removeDuplicatesFromSortedArray([1, 1, 1, 2, 2, 3])
    print removeDuplicatesFromSortedArray([0, 0, 1, 1, 1, 1, 2, 3, 3])

    print countDistinctNumbers([1, 1, 1, 1, 1, 2])
    print countDistinctNumbers([1, 1, 1, 1, 1, 2, 2, 2, 3])
