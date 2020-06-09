# binary tree, numbers integers, path includes path, traverse all nodes, longest path,

#     1
#   2 3
# -2
# 6

#  1
# -2 -3

# not necessary with root?
# negative numbers?
# tree is completed? random tree
# tree node value is 0 possible?
import sys


def maximumPath(root):
    result = {'max': -sys.maxint}
    findMax(root, result)

    return result['max']


def findMax(root, result):
    if not root:
        return -sys.maxint

    left_max = findMax(root.left, result)
    right_max = findMax(root.right, result)

    # if left side is negative, do not include
    left_max = max(0, left_max)

    right_max = max(0, right_max)

    if left_max + right_max + root.val > result['max']:
        result['max'] = left_max + right_max + root.val

    return max(left_max, right_max) + root.val


# array, positive integers, size is k, maximum summation, 3 subarrays, no overlapping elements
# return list[list1, list2, list3], subarray is the continues connected

# 2,3,6,3,6,7   k = 2
# sum(nums[i:j]) = sum(nums[j:]) - sum(nums[i:])

from collections import deque



