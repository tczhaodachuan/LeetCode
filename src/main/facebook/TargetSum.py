# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
def findTargetSumWays(nums, S):
    visited = set()
    result = {'ways': 0}
    _findSumWays(nums, S, 0, '', visited, result)
    return result['ways']


def _findSumWays(nums, S, start, temp, visited, result):
    if temp in visited:
        return
    visited.add(temp)

    if start == len(nums):
        if S == 0:
            result['ways'] += 1
        return
    num = nums[start]
    _findSumWays(nums, S - num, start + 1, '{}-{}'.format(temp, num), visited, result)
    _findSumWays(nums, S + num, start + 1, '{}+{}'.format(temp, num), visited, result)


import sys


def findTargetSumWaysMemory(nums, S):
    total = sum(nums)
    if total > 0 and (S > total or S < -1 * total):
        return 0
    if total < 0 and (S < total or S > -1 * total):
        return 0
    memo = [[-sys.maxint for _ in range(2001)] for _ in range(len(nums))]
    return _findTargetSumWays(nums, 0, S, 0, memo)


def _findTargetSumWays(nums, sum, S, index, memo):
    if index == len(nums):
        if sum == S:
            return 1
        else:
            return 0
    else:
        if memo[index][sum + 1000] != -sys.maxint:
            # memory the result for index and sum result
            # as different combination could reach to the same result
            return memo[index][sum + 1000]

        num = nums[index]
        add = _findTargetSumWays(nums, sum + num, S, index + 1, memo)
        minus = _findTargetSumWays(nums, sum - num, S, index + 1, memo)
        memo[index][sum + 1000] = add + minus
        return add + minus


def findTargetSumWaysDP(nums, S):
    total = sum(nums)
    if S > total or S < -1 * total:
        return 0

    dp = [[0 for _ in range(2 * total + 1)] for _ in range(len(nums) + 1)]
    # dp[i][j] stands for number of ways of using first ith (exclusive) nums to get summation of j
    # because total could be a negative value
    # dp[len(nums) - 1][S + total] is the final result
    # initial value
    dp[0][total + nums[0]] = 1
    dp[0][total - nums[0]] = 1
    for i in range(1, (len(nums))):
        j = nums[i]
        while j < 2 * total + 1 - nums[i]:
            if dp[i][j]:
                dp[i + 1][j + nums[i]] += dp[i][j]
                dp[i + 1][j - nums[i]] += dp[i][j]
            j += 1

    return dp[-1][S + total]


if __name__ == '__main__':
    print findTargetSumWays([1, 1, 1, 1, 1], 3)
    print findTargetSumWaysMemory([1, 1, 1, 1, 1], 3)

    print findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1)
    print findTargetSumWaysMemory([0, 0, 0, 0, 0, 0, 0, 0, 1], 1)
    print findTargetSumWaysMemory([2, 20, 24, 38, 44, 21, 45, 48, 30, 48, 14, 9, 21, 10, 46, 46, 12, 48, 12, 38], 48)
    print findTargetSumWaysMemory([2, 107, 109, 113, 127, 131, 137, 3, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 47, 53],899)
    #print findTargetSumWaysDP([2, 20, 24, 38, 44, 21, 45, 48, 30, 48, 14, 9, 21, 10, 46, 46, 12, 48, 12, 38], 48)
