def replaceTwoAdjentDigits(num):
    if num == 0:
        return 0
    nums = []
    while num > 0:
        digit = num % 10
        nums.insert(0, digit)
        num = num / 10
    end = len(nums) - 1
    mid = end - 1
    start = end - 2

    replaceStart = False
    while start > 0:
        if nums[start] >= nums[mid] > nums[end]:
            start -= 1
            mid -= 1
            end -= 1
        else:
            break
        if start == 0:
            replaceStart = True
            break
    if replaceStart:
        larger = max(nums[start], nums[mid])
        nums[start] = larger
        nums[mid] = larger
        nums.pop(start)
    else:
        larger = max(nums[end], nums[mid])
        nums[end] = larger
        nums[mid] = larger
        nums.pop(mid)

    minNum = 0
    for num in nums:
        minNum = minNum * 10 + num
    return minNum


if __name__ == '__main__':
    print replaceTwoAdjentDigits(0)
    print replaceTwoAdjentDigits(12)
    print replaceTwoAdjentDigits(233614)
    print replaceTwoAdjentDigits(234)

    print replaceTwoAdjentDigits(177763)
    print replaceTwoAdjentDigits(52231)
