def findPairWithGivenSum(nums, target):
    sorted_nums = sorted(nums)
    start = 0
    end = len(sorted_nums) - 1

    while start < end:
        if sorted_nums[start] + sorted_nums[end] == target:
            return nums.index(sorted_nums[start]), nums.index(sorted_nums[end])
        elif sorted_nums[start] + sorted_nums[end] > target:
            end -= 1
        else:
            start += 1
    return None
if __name__ == '__main__':
    nums = [1, 10, 25, 35, 60]
    target = 60

    print findPairWithGivenSum(nums, target)

    nums = [20, 50, 40, 25, 30, 10]
    print findPairWithGivenSum(nums, target)