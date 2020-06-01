import collections

'''
Two pointers have 3 types of questions
1. quick and slow pointers
2. binary search pointers
3. sliding window pointers
'''

'''
quick and slow pointers
'''


def longestSubstring(s, k):
    """
    longest sub string with all character repeat at least k times
    :type s: str
    :type k: int
    :rtype: int
    """

    c_count = {}
    for i in range(len(s)):
        c = s[i]
        c_count[c] = c_count.get(c, 0) + 1

    all_more_than_k = True
    for cnt in c_count.values():
        if cnt < k:
            all_more_than_k = False
            break

    if all_more_than_k:
        # maximum result
        return len(s)

    left, right = 0, 0
    result = 0
    while right < len(s):
        ch = s[right]
        if c_count[ch] < k:
            # cannot include the current ch
            # [left,right)
            result = max(result, longestSubstring(s[left:right], k))
            # move the left pass the current char
            left = right + 1
        right += 1
    # it could be that the left pointer never moved, such as aaaabbb situation
    return max(result, longestSubstring(s[left:], k))


def findMidPoint(node):
    slow, fast = node, node

    while slow and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def detectCycle(node):
    # assume the first time fast and slow meet needs k steps, then fast already travelled 2k steps
    # assume the meeting point to the start point is m steps, then from head to start point is k-m
    # since the cycle is k, k-m also goes back to the start point.
    slow, fast = node, node

    while slow and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    slow = node

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def findLastKthElement(node, k):
    i = 0
    fast = node
    while i < k:
        fast = fast.next
        i += 1

    slow = node
    while fast:
        slow = slow.next
        fast = fast.next

    return slow


'''
binary search pointers
'''


def twoSum(nums, sum):
    pass


def findDuplicateTime(nums, k):
    # sorted nums
    i = 0
    j = len(nums) - 1
    mid = i + (j - i) / 2
    while i <= j:
        mid = i + (j - i) / 2
        if nums[mid] == k:
            break
        elif nums[mid] > k:
            j = mid - 1
        else:
            i = mid + 1
    if i > j:
        return 0

    result = 1
    left = mid - 1
    right = mid + 1
    while left >= 0 and nums[left] == nums[mid]:
        result += 1
        left -= 1
    while right < len(nums) and nums[right] == nums[mid]:
        result += 1
        right += 1
    return result


'''
sliding window pointers
'''


def findAllAnagrams(s, p):
    pass


def longestSubStringKDistinct(s, k):
    pass


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree or len(tree) == 0:
            return 0

        ans = 1
        counter = collections.Counter()
        # starting tree
        starting_tree = 0
        for j, fruit in enumerate(tree):
            counter[fruit] += 1
            # when the 3rd fruit appeared as the current tree
            while len(counter) >= 3:
                counter[tree[starting_tree]] -= 1
                if counter[tree[starting_tree]] == 0:
                    del counter[tree[starting_tree]]
                starting_tree += 1
            # updated ans because we can perform step 1 and step 2
            ans = max(ans, j - starting_tree + 1)

        return ans


def intersection(nums1, nums2):
    i, j = 0, 0

    intersec = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            intersec.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1

    return intersec


import sys


def cloestTwoSum(nums, target):
    delta = sys.maxint
    num1 = None
    num2 = None

    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] + nums[j] > target:
            if abs(target - nums[i] - nums[j]) < delta:
                delta = abs(target - nums[i] - nums[j])
                num1 = nums[i]
                num2 = nums[j]

            j -= 1
        elif nums[i] + nums[j] < target:
            if abs(target - nums[i] - nums[j]) < delta:
                delta = abs(target - nums[i] - nums[j])
                num1 = nums[i]
                num2 = nums[j]
            i += 1
        else:
            delta = 0
            num1 = nums[i]
            num2 = nums[j]
            break
    return num1, num2


if __name__ == '__main__':
    s = Solution()
    print s.totalFruit([1, 2, 1, 2, 2, 3])

    print findDuplicateTime([1, 2, 3, 3, 3, 5, 5], 5)

    print intersection([1, 2, 3, 3, 4, 5], [3, 3, 5, 7, 8])

    print cloestTwoSum([1, 2, 3, 5, 6, 7, 8], 12)
