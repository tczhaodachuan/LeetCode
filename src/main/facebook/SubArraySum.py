# continuous subarray sum
def subarraySum(nums, k):
    # nums[i:j] = if sum(nums[:j]) - sum(nums[:i]) == k else 0
    prefix_sum = 0
    # if need 0
    prefix_sum_dict  = {0 : 1}
    result = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]
        result += prefix_sum_dict.get(prefix_sum - k, 0)
        prefix_sum_dict[prefix_sum] = prefix_sum_dict.get(prefix_sum, 0) + 1

    return result