class NSum(object):
    def twoSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort arrays
        answers = []
        nums.sort()
        i = 0
        j = nums.__len__() - 1
        while i < j:
            left = nums[i]
            right = nums[j]
            sum = left + right
            if sum > 0:
                j = j - 1
            elif sum < 0:
                i = i + 1
            else:
                answers.append([left, right])
                i = i + 1
                j = j - 1
        return answers

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answers = []
        # sort the nums is the key to KSum questions, O(nlog(n))
        nums.sort()
        # binarySearch O(log(n)) * loop O(n) = O(nlog(n))
        for i in range(len(nums) - 2):
            # avoid duplicates answers
            if nums[i] == nums[i - 1] and i > 0:
                continue
            if nums[i] > 0:
                # if the minimal number is more than 0, it won't have 3 positive numbers sum is 0
                break
            if nums[len(nums) - 1] < 0:
                # if the maximal number is less then 0, it won't have 3 negative numbers sum is 0
                break

            j = i + 1
            k = len(nums) - 1
            while j < k:
                if (j > i + 1 and nums[j] == nums[j - 1]):
                    # avoid duplicates answers
                    j = j + 1
                    continue
                # change the 3sum problem to a binary search problem
                target = -1 * nums[i]
                sum = nums[j] + nums[k]
                if target == sum:
                    answers.append([nums[i], nums[j], nums[k]])
                    # keeps searching until j>=k
                    j = j + 1
                    k = k - 1
                elif sum > target:
                    k = k - 1
                else:
                    j = j + 1
        # 3Sum is O(nlog(n)) complexity
        return answers


# https://leetcode.com/problems/target-sum/
def targetSum(nums, s):
    # dfs
    maximum = sum(nums)
    minimum = sum(nums) * (-1)
    if s > maximum and s < minimum:
        return 0

    return targetSumWays(nums, 0, s)


def targetSumWays(nums, i, s):
    if i == len(nums) - 1:
        # stop condition
        if s == nums[i] or s == nums[i] * (-1):
            print i, s
            return 1
        else:
            return 0

    return targetSumWays(nums, i + 1, s - nums[i]) + targetSumWays(nums, i + 1, s + nums[i])


def targetSumII(nums, s):
    # dp solution
    summation = sum(nums)
    if s > summation or s < (-1) * summation:
        return 0

    dp = [[0 for _ in range(2 * summation + 1)] for _ in range(len(nums) + 1)]
    # dp[i][j] stands the number of ways to use the first i elements to get sum of j
    # dp[len(nums) - 1][s] is the result
    # dp[0][summation] = 1 initial value to say, summation result only has 1 way
    # dp[i-1][j-nums[i]] + dp[i-1][j+nums[i]] = dp[i][j]
    print dp
    dp[0][summation] = 1
    for i in range(len(nums)):
        j = nums[i]
        while j < 2 * summation + 1 - nums[i]:
            if dp[i][j]:
                dp[i + 1][j + nums[i]] += dp[i][j]
                dp[i + 1][j - nums[i]] += dp[i][j]
            j += 1
    # s + summation meaning we shifted the possible value with summaion number, since array cannot store negative index
    # otherwise, the array should be in [-summation, summation]
    return dp[-1][s + summation]


def findTargetSumWaysII(nums, S):
    # NP-complete problem, easy to find answer
    # hard to find all solutions in polynomial time
    summation = sum(nums)
    if summation < S:
        # no solution available
        return 0
    if summation + S % 2 == 1:
        # because all of the num in nums are even number
        # after each num * 2, however, the target number is an odd number
        return 0
    # convert the problem to a subset sum problem
    # (S+sum)/2 is the target number, then only consider the summation
    # numbers in subset is "+", others are using "-"
    # dp[i] meaning the number of ways to get target number i
    target = (S + summation) / 2
    dp = [0 for i in range(target + 1)]
    # get 0 is the empty subset
    dp[0] = 1
    for i in range(len(nums)):
        j = target
        while j >= nums[i]:
            dp[j] += dp[j - nums[i]]
            j -= 1
    return dp[target]


def findTargetSumWays(nums, S):
    res = []
    doFind(0, 0, nums, S, res)
    return len(res)


def doFind(value, index, nums, S, res):
    if index == len(nums):
        if value == S:
            res.append(1)
        return res

    doFind(value + nums[index], index + 1, nums, S, res)
    doFind(value - nums[index], index + 1, nums, S, res)


def addOperators(num, target):
    nums = []
    for n in num:
        nums.append(int(n))
    res = []
    expression = ''
    helper(res, expression, nums, target, 0, 0, 0)
    return res


def helper(res, expression, nums, target, pos, eval, multed):
    if pos == len(nums):
        if target == eval:
            print target, pos, eval, multed, expression
            res.append(expression)
        return

    for i in range(pos, len(nums)):
        curr = nums[i]
        if pos == 0:
            helper(res, expression + '{0}'.format(curr), nums, target, i + 1, curr, curr)
        else:
            helper(res, expression + '+{0}'.format(curr), nums, target, i + 1, eval + curr, curr)
            helper(res, expression + '-{0}'.format(curr), nums, target, i + 1, eval - curr, -curr)
            # because multiply gets executed first
            helper(res, expression + '*{0}'.format(curr), nums, target, i + 1, eval - multed + multed * curr,
                   multed * curr)


# https://leetcode.com/problems/subarray-sum-equals-k/
def subArrayEqual(nums, k):

    if len(nums) == 0:
        return 0

    presum_dict = {0: 1}
    # dp[i] meaning the sum of array from 0 to i,
    presum = 0
    count = 0
    for num in nums:
        presum += num
        # e.g. sum of the sub string i -> j equals k
        # dp[j]-k=dp[i], j>i, means i has been stored before reaches to j
        count += presum_dict.get(presum - k, 0)
        presum_dict[presum] = presum_dict.get(presum, 0) + 1

    return count


if __name__ == '__main__':
    n_sum = NSum()
    nums = [-12, -1, 4, -14, 0, 10, 7, -7, -6, 9, 6, -2, 7, 13, 9, -1, 4, 12, 9, 4, 14, 0, -4, 0, 0, 10, 2, -7, 7, -4,
            -11, 10, 2, 8, 4, -12, -4, -12, -4, -3, 12, 9, 11, 4, -1, -3, 10, -12, -6, -4, -1, -14, 3, 2, -7, -11, -3,
            10, -11, -10, 13, -15, 7, 0, 0, -4, -5, 11, 0, -2, -14, -11, -8, 12, 1, -1, -14, -12, -6, -5, 0, 9, -4, -12,
            -4, 4, 14, 9, -9, 10, 14, -11, 10, 6, -3, -4, 10, -1, 14, -13, 13, 7, -9, 12, 4, -1, -4, 5, 3, 6, 8, 10, 0,
            11, 13, 11, -7, 5, -3, -1, 0, -4, -4, -4, 10, 0]
    answers = n_sum.twoSum(nums)
    print answers

    answers = n_sum.threeSum(nums)
    print answers

    print 'findTargetSumWays'
    print findTargetSumWays([1, 1, 1, 1, 1], 3)
    print targetSum([1, 1, 1, 1, 1], 3)
    print targetSumII([1, 1, 1, 1, 1], 3)
    # print findTargetSumWays([10, 9, 6, 4, 19, 0, 41, 30, 27, 15, 14, 39, 33, 7, 34, 17, 24, 46, 2, 46], 45)

    print 'findTargetSumWaysII'
    print findTargetSumWaysII([1, 1, 1, 1, 1], 3)
    print findTargetSumWaysII([10, 9, 6, 4, 19, 0, 41, 30, 27, 15, 14, 39, 33, 7, 34, 17, 24, 46, 2, 46], 45)

    print 'addOperators'
    print addOperators('123', 6)

    print 'subArrayEqualsK'

    print subArrayEqual([1, 1, 1], 2)
