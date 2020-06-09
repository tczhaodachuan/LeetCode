# continuous subarray sum
def subarraySum(nums, k):
    # nums[i:j] = if sum(nums[:j]) - sum(nums[:i]) == k else 0
    prefix_sum = 0
    # if need 0
    prefix_sum_dict = {0: 1}
    result = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]
        result += prefix_sum_dict.get(prefix_sum - k, 0)
        prefix_sum_dict[prefix_sum] = prefix_sum_dict.get(prefix_sum, 0) + 1

    return result


def longestSubArray(nums):
    # find the longest subarray contains equal 0 and 1s, the nums only contains 1 or 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = -1

    presum = {0: [0]}
    total = 0
    length = 0
    for i in range(len(nums)):
        num = nums[i]
        total += num
        if total in presum:
            long = i - presum[total][0] + 1
            if long > length:
                length = long
        else:
            presum[total] = []
        presum[total].append(i)

    return length


def subarraySquareSum(nums, k):
    square_sum = 0
    presum = {0: 1}
    result = 0
    for i in range(len(nums)):
        square_sum += nums[i] * nums[i]
        result += presum.get(square_sum - k, 0)
        presum[square_sum] = presum.get(square_sum, 0) + 1
    return result


if __name__ == '__main__':
    print longestSubArray([0, 0, 1, 0, 1, 1, 1, 1, 1, 1])

    print subarraySquareSum([1, -3, 4, 6], 26)
