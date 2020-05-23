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


def longestSubStringAtLeastKRepeatingChars(s, k):
    char_count = {}

    for i in range(len(s)):
        c = s[i]
        char_count[c] = char_count.get(c, 0) + 1

    flag = True
    for ch, count in char_count.iteritems():
        if count < k:
            flag = False

    if flag:
        # all char repeat more than or equal k times
        return len(s)

    left, right = 0, 0
    result = 0
    while right < len(s):
        c = s[right]
        if char_count[c] < k:
            result = max(result, longestSubStringAtLeastKRepeatingChars(s[left:right], k))
            left = right + 1
        right += 1

    return max(result, longestSubStringAtLeastKRepeatingChars(s[left:], k))


def longestSubStringKDistinct(s, k):
    left, right = 0, 0
    sliding_window = {}
    result = 0

    while right < len(s):
        c = s[right]
        sliding_window[c] = sliding_window.get(c, 0) + 1
        if len(sliding_window.keys()) <= k:
            result = max(result, right - left + 1)

        while len(sliding_window.keys()) > k:
            d = s[left]
            sliding_window[d] -= 1
            if sliding_window[d] == 0:
                sliding_window.pop(d)
            left += 1
        right += 1

    return result


def longestSubStringWithoutRepeatingChars(s):
    # two pointers
    pass


def minimumSizeSubAarraySum(nums):
    pass


if __name__ == '__main__':
    print longestContinuousIncreasingSubsequence([1, 2, 3, 2, 3, 4, 5, 4, 7, 9, 4, 10])

    print longestContinuousIncreasingSubsequence([1, 3, 5, 4, 2, 3, 4, 5])
