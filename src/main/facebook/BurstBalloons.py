def maxCoins(nums):
	return search(nums, 0)


def search(nums, temp):
	if len(nums) == 0:
		return temp

	max_result = 0
	for i in range(len(nums)):
		left = 1
		right = 1
		if i - 1 >= 0:
			left = nums[i - 1]
		if i + 1 < len(nums):
			right = nums[i + 1]

		mid = left * nums[i] * right
		max_result = max(max_result, search(nums[:i] + nums[i + 1:], temp + mid))

	return max_result


def maxCoinsDP(nums):
	m = len(nums)

	dp = [[0 for _ in range(m + 2)] for _ in range(m + 2)]
	visited = [[False for _ in range(m + 2)] for _ in range(m + 2)]
	ext_nums = [1] + nums + [1]
	for i in range(1, len(ext_nums) - 1):
		mid = ext_nums[i - 1] * ext_nums[i] * ext_nums[i + 1]
		dp[i][i] = mid
	result = search_dp(ext_nums, dp, visited, 1, len(nums))
	return result


def search_dp(nums, dp, visited, l, r):
	if visited[l][r]:
		return dp[l][r]
	for k in range(l, r + 1):
		# k is the last balloon, thus its left and right is beyond the boundary
		k_value = nums[l - 1] * nums[k] * nums[r + 1]
		dp[l][r] = max(dp[l][r],
		               search_dp(nums, dp, visited, l, k - 1) + search_dp(nums, dp, visited, k + 1, r) + k_value)

	visited[l][r] = True
	return dp[l][r]


if __name__ == '__main__':
	print maxCoins([4, 1, 5, 10])
	print maxCoins([3, 1, 5])
	print maxCoinsDP([4, 1, 5, 10])
	print maxCoinsDP([3, 1, 5])
