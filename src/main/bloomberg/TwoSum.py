def twoSum(nums):
    sorted_nums = sorted(nums)
    i = 0
    j = len(nums) - 1
    while i < j:
        if sorted_nums[i] + sorted_nums[j] > 0:
            j -= 1
        elif sorted_nums[i] + sorted_nums[j] < 0:
            i += 1
        else:
            return [sorted_nums[i], sorted_nums[j]]

    return False


def twoSum2(nums):
    if len(nums) < 2:
        return []
    num_dict = {}
    for num in nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    for num in nums:
        if num == 0 and num_dict[0] > 1:
            return [num, -1 * num]
        if -1 * num in num_dict:
            return [num, -1 * num]
    return []


def threeSum(nums):
    nums.sort()
    for i in range(0, len(nums) - 2):
        if nums[i] == nums[i + 1]:
            continue

        if nums[i] > 0:
            break
        if nums[len(nums) - 1] < 0:
            break

        j = i + 1
        k = len(nums) - 1
        target = -1 * nums[i]
        while j < k:
            if j > i + 1 and nums[j] == nums[j - 1]:
                j += 1
                continue
            if nums[j] + nums[k] == target:
                return True
            elif nums[j] + nums[k] < target:
                j += 1
            else:
                k -= 1

    return False


if __name__ == '__main__':
    nums = [6, 7, 8, 2, -8, 34, 5, 10]
    print twoSum(nums)
    print twoSum2(nums)

    print threeSum([8, 9, 9, 2, 10, 43, 10, -2, -9, -7])
