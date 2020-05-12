# 674, Longest continuous increasing subsequence
import sys


def longestContinuousIncreasingSubsequence(nums):
    if len(nums) <= 1:
        return len(nums)
    result = -sys.maxint
    i = 0
    j = 1
    while j < len(nums):
        if nums[j] <= nums[j - 1]:
            i = j
        result = max(result, j - i + 1)

        j += 1

    return result


def longestSubStringWithoutRepeatingChars(s):
    # two pointers
    pass

def minimumSizeSubAarraySum(nums):
    pass

if __name__ == '__main__':
    print longestContinuousIncreasingSubsequence([1, 2, 3, 2, 3, 4, 5, 4, 7, 9, 4, 10])

    print longestContinuousIncreasingSubsequence([1, 3, 5, 4, 2, 3, 4, 5])
