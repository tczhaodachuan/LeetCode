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


if __name__ == '__main__':
    s = Solution()
    print s.totalFruit([1, 2, 1, 2, 2, 3])

    print findDuplicateTime([1, 2, 3, 3, 3, 5, 5], 5)
