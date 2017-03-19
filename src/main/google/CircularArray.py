def circularArrayLoop(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 0:
        return False
    i = 0
    currentPos = (i + nums[i] + len(nums)) % len(nums)
    while i < len(nums):
        i += 1
        if currentPos == 0 and i < len(nums):
            return True
        currentPos = (currentPos + nums[currentPos] + len(nums)) % len(nums)
        print currentPos
    currentPos = (currentPos + nums[currentPos] + len(nums)) % len(nums)
    return currentPos == 0


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    for i in range(len(nums)):
        pos = (i + nums[i]) % 5
        if pos < 0:
            pos = pos + 5
            # print pos
    print circularArrayLoop(nums)
